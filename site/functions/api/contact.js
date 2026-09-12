// Cloudflare Pages Function — POST /api/contact (sarasotaconcrete.com)
// Server-side validation, honeypot, Turnstile (when TURNSTILE_SECRET_KEY is set), KV rate limit,
// optional photo attachment (<= 8 MB JPG/PNG), then hands the payload to the contact-email Worker
// via a service binding. No PII is logged.

const MAX_FORM_BYTES = 9_500_000; // 8 MB photo + fields
const MAX_PHOTO_BYTES = 8_000_000;
const HUB_ID = "sarasota";
const LIMITS = { name: 100, phone: 40, email: 254, service: 120, city: 120, zip: 10, property_type: 60, flood_zone: 20,
  timeline: 60, presence: 60, message: 3000, page_url: 300, referrer: 300, utm: 120 };

function isAllowedOrigin(origin) {
  if (!origin) return true;
  try {
    const { hostname, protocol } = new URL(origin);
    if (protocol !== "https:" && hostname !== "localhost" && hostname !== "127.0.0.1") return false;
    if (hostname === "sarasotaconcrete.com" || hostname === "www.sarasotaconcrete.com") return true;
    if (hostname === "localhost" || hostname === "127.0.0.1") return true;
    // Pages hosts for this project: sarasotaconcrete.pages.dev, the preview project
    // sarasotaconcrete-preview.pages.dev, and per-deployment subdomains like
    // <hash>.sarasotaconcrete-preview.pages.dev. Without this the form 403s on every preview,
    // which is exactly where it gets tested before the domain is attached.
    if (hostname.endsWith(".pages.dev")) {
      const project = hostname.slice(0, -".pages.dev".length).split(".").pop();
      return project === "sarasotaconcrete" || project === "sarasotaconcrete-preview";
    }
    return false;
  } catch { return false; }
}
const field = (form, n) => { const v = form.get(n); return typeof v === "string" ? v.trim() : ""; };
const text = (m, s) => new Response(m, { status: s, headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" } });

function validate(p) {
  if (!p.name || p.name.length > LIMITS.name) return "Please enter your name.";
  if (!p.phone || p.phone.length > LIMITS.phone || !/[0-9]{7,}/.test(p.phone.replace(/\D/g, ""))) return "Please enter a valid phone number.";
  if (!p.email || p.email.length > LIMITS.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(p.email)) return "Please enter a valid email address.";
  if (p.service.length > LIMITS.service || p.city.length > LIMITS.city) return "Please choose a valid service and location.";
  // ZIP is what the form now asks for instead of a locality dropdown. Five digits, optionally
  // ZIP+4, and only US shapes: everything served is in Florida. Kept required-on-the-server rather
  // than trusting the browser's pattern attribute.
  if (!p.zip || !/^[0-9]{5}(-[0-9]{4})?$/.test(p.zip)) return "Please enter a 5-digit ZIP code.";
  if (p.message.length > LIMITS.message) return "The project description is too long.";
  // "yes" = explicit checkbox on the long form. "submit" = the short hero form, where the
  // disclosure sits directly above the button and submitting is the affirmative act.
  if (p.consent !== "yes" && p.consent !== "submit") return "Please agree to be contacted so we can reply.";
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

// Keeps the lead even if the email fails. Cloudflare's outbound email path takes several seconds,
// and it is the one part of this chain that can fail after the visitor is gone, so the payload is
// written to KV first under a key that sorts by time. Nothing reads these automatically; they exist
// so a delivery failure is recoverable rather than a lost customer.
async function archive(env, payload) {
  if (!env.RATE_LIMIT_KV) return;
  const key = `lead:${payload.submittedAt}:${Math.random().toString(36).slice(2, 8)}`;
  const { photo, ...rest } = payload;           // the photo would blow past KV's value limit
  try {
    await env.RATE_LIMIT_KV.put(key, JSON.stringify({ ...rest, had_photo: !!photo }),
      { expirationTtl: 60 * 60 * 24 * 90 });    // 90 days is long enough to notice and recover
  } catch (e) {
    console.error("lead archive failed", { name: e instanceof Error ? e.name : "Error" });
  }
}

export async function onRequestPost({ request, env, waitUntil }) {
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
    service: field(form, "service"), city: field(form, "city"), zip: field(form, "zip").slice(0, LIMITS.zip),
    property_type: field(form, "property_type").slice(0, LIMITS.property_type),
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
  // Handing the payload to the email Worker used to be awaited here, and Cloudflare's send_email
  // path takes four to eight seconds. That was four to eight seconds of a visitor staring at a
  // disabled button after they had already done everything asked of them, which is where forms lose
  // people. The submission is archived first, then the response goes out immediately and delivery
  // finishes in the background under waitUntil, which keeps the request alive after the response.
  //
  // The cost of the change is honest: a delivery failure can no longer be reported to the visitor.
  // That is the right trade. A failure is rare, the visitor could not act on it anyway, and the
  // lead is in KV either way -- whereas the delay hit every single submission.
  await archive(env, payload);

  const deliver = (async () => {
    try {
      const r = await env.CONTACT_EMAIL.fetch("https://contact-email.internal/send",
        { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
      if (!r.ok) console.error("contact-email rejected", { status: r.status });
    } catch (e) {
      console.error("contact-email unavailable", { name: e instanceof Error ? e.name : "Error" });
    }
  })();
  if (typeof waitUntil === "function") waitUntil(deliver); else await deliver;

  return Response.redirect(new URL("/thank-you/", request.url), 303);
}
