// Cloudflare Pages Function — POST /api/contact (sarasotaconcrete.com)
// Server-side validation, honeypot, Turnstile (when TURNSTILE_SECRET_KEY is set), KV rate limit,
// optional photo attachment (<= 8 MB JPG/PNG), then hands the payload to the contact-email Worker
// via a service binding. No PII is logged.

const MAX_FORM_BYTES = 9_500_000; // 8 MB photo + fields
const MAX_PHOTO_BYTES = 8_000_000;
const HUB_ID = "sarasota";
const LIMITS = { name: 100, phone: 40, email: 254, service: 120, city: 120, property_type: 60, flood_zone: 20, timeline: 60,
  presence: 60, message: 3000, page_url: 300, referrer: 300, utm: 120 };

function isAllowedOrigin(origin) {
  if (!origin) return true;
  try {
    const { hostname, protocol } = new URL(origin);
    if (protocol !== "https:" && hostname !== "localhost" && hostname !== "127.0.0.1") return false;
    return hostname === "sarasotaconcrete.com" || hostname === "www.sarasotaconcrete.com" ||
      hostname === "sarasotaconcrete.pages.dev" || hostname.endsWith(".sarasotaconcrete.pages.dev") ||
      hostname === "localhost" || hostname === "127.0.0.1";
  } catch { return false; }
}
const field = (form, n) => { const v = form.get(n); return typeof v === "string" ? v.trim() : ""; };
const text = (m, s) => new Response(m, { status: s, headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" } });

function validate(p) {
  if (!p.name || p.name.length > LIMITS.name) return "Please enter your name.";
  if (!p.phone || p.phone.length > LIMITS.phone || !/[0-9]{7,}/.test(p.phone.replace(/\D/g, ""))) return "Please enter a valid phone number.";
  if (!p.email || p.email.length > LIMITS.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(p.email)) return "Please enter a valid email address.";
  if (p.service.length > LIMITS.service || p.city.length > LIMITS.city) return "Please choose a valid service and location.";
  if (p.message.length > LIMITS.message) return "The project description is too long.";
  if (p.consent !== "yes") return "Please check the consent box so we can contact you.";
  return null;
}
async function verifyTurnstile(token, secret, ip) {
  if (!secret) return { ok: true, skipped: true };
  if (!token) return { ok: false };
  const body = new URLSearchParams({ secret, response: token });
  if (ip) body.set("remoteip", ip);
  try {
    const r = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" }, body });
    const d = await r.json();
    return { ok: !!d.success };
  } catch { return { ok: false }; }
}
async function rateLimit(env, ip) {
  if (!env.RATE_LIMIT_KV || !ip) return true;
  const key = `rl:${ip}`;
  const n = Number((await env.RATE_LIMIT_KV.get(key)) || "0");
  if (n >= 5) return false; // 5 submissions per rolling 10 minutes per IP
  await env.RATE_LIMIT_KV.put(key, String(n + 1), { expirationTtl: 600 });
  return true;
}

export async function onRequestPost({ request, env }) {
  if (Number(request.headers.get("content-length") || "0") > MAX_FORM_BYTES) return text("This request is too large.", 413);
  if (!isAllowedOrigin(request.headers.get("origin"))) return text("This form submission is not allowed.", 403);
  const ct = request.headers.get("content-type") || "";
  if (!ct.startsWith("multipart/form-data") && !ct.startsWith("application/x-www-form-urlencoded")) return text("Unsupported form format.", 415);
  let form;
  try { form = await request.formData(); } catch { return text("The form could not be read.", 400); }
  if (field(form, "company")) return Response.redirect(new URL("/thank-you/", request.url), 303); // honeypot
  const ip = request.headers.get("cf-connecting-ip") || "";
  if (!(await rateLimit(env, ip))) return text("Too many requests. Please call us instead.", 429);
  const ts = await verifyTurnstile(field(form, "cf-turnstile-response"), env.TURNSTILE_SECRET_KEY, ip);
  if (!ts.ok) return text("We could not verify this submission was made by a person. Please try again.", 403);

  const payload = {
    hub_id: HUB_ID, name: field(form, "name"), phone: field(form, "phone"), email: field(form, "email"),
    service: field(form, "service"), city: field(form, "city"), property_type: field(form, "property_type").slice(0, LIMITS.property_type),
    flood_zone: field(form, "flood_zone").slice(0, LIMITS.flood_zone), timeline: field(form, "timeline").slice(0, LIMITS.timeline),
    presence: field(form, "presence").slice(0, LIMITS.presence), message: field(form, "message"), consent: field(form, "consent"),
    page_url: field(form, "page_url").slice(0, LIMITS.page_url), referrer: field(form, "referrer").slice(0, LIMITS.referrer),
    utm_source: field(form, "utm_source").slice(0, LIMITS.utm), utm_medium: field(form, "utm_medium").slice(0, LIMITS.utm),
    utm_campaign: field(form, "utm_campaign").slice(0, LIMITS.utm), client_ts: field(form, "client_ts").slice(0, 40),
    submittedAt: new Date().toISOString(),
  };
  const err = validate(payload);
  if (err) return text(err, 400);

  const photo = form.get("photo");
  if (photo && typeof photo === "object" && photo.size) {
    if (photo.size > MAX_PHOTO_BYTES) return text("The photo is larger than 8 MB.", 413);
    if (!["image/jpeg", "image/png"].includes(photo.type)) return text("Please attach a JPG or PNG photo.", 415);
    const buf = new Uint8Array(await photo.arrayBuffer());
    let bin = ""; for (let i = 0; i < buf.length; i += 0x8000) bin += String.fromCharCode.apply(null, buf.subarray(i, i + 0x8000));
    payload.photo = { name: (photo.name || "photo").replace(/[^\w.\-]/g, "_").slice(0, 80), type: photo.type, base64: btoa(bin) };
  }
  try {
    const r = await env.CONTACT_EMAIL.fetch("https://contact-email.internal/send", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
    if (!r.ok) { console.error("contact-email rejected", { status: r.status }); return text("We could not send your request right now. Please email hello@sarasotaconcrete.com.", 502); }
  } catch (e) {
    console.error("contact-email unavailable", { name: e instanceof Error ? e.name : "Error" });
    return text("We could not send your request right now. Please email hello@sarasotaconcrete.com.", 502);
  }
  return Response.redirect(new URL("/thank-you/", request.url), 303);
}
