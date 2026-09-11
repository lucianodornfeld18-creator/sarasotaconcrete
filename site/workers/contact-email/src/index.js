// contact-email Worker for sarasotaconcrete.com — receives the validated payload from the
// Pages Function over a service binding and sends it with Cloudflare Email Workers (send_email binding).
// Sender: hello@sarasotaconcrete.com (Email Routing must be verified on the zone).
// Destination: env.DESTINATION_EMAIL ({{MAIN_DESTINATION_EMAIL}} in OWNER-INPUTS.md).

function esc(s) { return String(s || "").replace(/[<>&]/g, c => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c])); }

function buildMime({ from, to, subject, textBody, htmlBody, attachment }) {
  const boundary = "sc-" + crypto.randomUUID();
  const alt = "alt-" + crypto.randomUUID();
  const head = [`From: Sarasota Concrete <${from}>`, `To: ${to}`, `Subject: ${subject}`, "MIME-Version: 1.0"];
  const body = [];
  if (attachment) {
    head.push(`Content-Type: multipart/mixed; boundary="${boundary}"`);
    body.push(`--${boundary}`, `Content-Type: multipart/alternative; boundary="${alt}"`, "");
  } else {
    head.push(`Content-Type: multipart/alternative; boundary="${alt}"`);
  }
  body.push(`--${alt}`, "Content-Type: text/plain; charset=utf-8", "Content-Transfer-Encoding: 8bit", "", textBody, "",
    `--${alt}`, "Content-Type: text/html; charset=utf-8", "Content-Transfer-Encoding: 8bit", "", htmlBody, "", `--${alt}--`);
  if (attachment) {
    body.push("", `--${boundary}`, `Content-Type: ${attachment.type}; name="${attachment.name}"`, "Content-Transfer-Encoding: base64",
      `Content-Disposition: attachment; filename="${attachment.name}"`, "", attachment.base64.replace(/(.{76})/g, "$1\r\n"), "", `--${boundary}--`);
  }
  return head.join("\r\n") + "\r\n\r\n" + body.join("\r\n");
}

export default {
  async fetch(request, env) {
    if (request.method !== "POST") return new Response("Method not allowed", { status: 405 });
    let p;
    try { p = await request.json(); } catch { return new Response("Bad JSON", { status: 400 }); }
    if (p.hub_id !== "sarasota") return new Response("Wrong hub", { status: 400 });
    const to = env.DESTINATION_EMAIL;
    if (!to) return new Response("DESTINATION_EMAIL not configured", { status: 500 });
    const from = env.FROM_EMAIL || "hello@sarasotaconcrete.com";
    const rows = [["Name", p.name], ["Phone", p.phone], ["Email", p.email], ["Location", p.city], ["Service", p.service],
      ["Property", p.property_type], ["Flood zone", p.flood_zone], ["Timeline", p.timeline], ["Presence", p.presence],
      ["Message", p.message], ["Consent", p.consent], ["Page", p.page_url], ["Referrer", p.referrer],
      ["UTM", [p.utm_source, p.utm_medium, p.utm_campaign].filter(Boolean).join(" / ")], ["Submitted", p.submittedAt]];
    const subject = `[Sarasota Concrete] ${p.service || "Estimate"} — ${p.city || "Sarasota area"} — ${p.name}`;
    const textBody = rows.map(([k, v]) => `${k}: ${v || "-"}`).join("\n");
    const htmlBody = `<h2 style="font-family:sans-serif">New estimate request (sarasotaconcrete.com)</h2><table style="font-family:sans-serif;border-collapse:collapse">` +
      rows.map(([k, v]) => `<tr><td style="padding:4px 10px 4px 0;color:#555"><b>${esc(k)}</b></td><td style="padding:4px 0">${esc(v || "-").replace(/\n/g, "<br>")}</td></tr>`).join("") + "</table>";
    const raw = buildMime({ from, to, subject, textBody, htmlBody, attachment: p.photo || null });
    const { EmailMessage } = await import("cloudflare:email");
    const msg = new EmailMessage(from, to, raw);
    try {
      await env.EMAIL.send(msg);
    } catch (e) {
      console.error("send failed", { name: e instanceof Error ? e.name : "Error" });
      return new Response("Send failed", { status: 502 });
    }
    return new Response("ok", { status: 200 });
  },
};
