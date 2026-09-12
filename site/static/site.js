(function () {
  "use strict";
  function track(name, data) {
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: name }, data || {}));
      if (typeof window.gtag === "function") window.gtag("event", name, data || {});
    } catch (e) {}
  }
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("primaryNav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  document.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.addEventListener("click", function () { track("tel_click", { href: a.getAttribute("href") }); }); });
  document.querySelectorAll('a[href^="sms:"]').forEach(function (a) { a.addEventListener("click", function () { track("sms_click", { href: a.getAttribute("href") }); }); });

  // Lead forms: progressive enhancement over a plain HTML POST to /api/contact.
  // querySelectorAll, not querySelector: the home page carries two forms (the short one in the hero
  // and the long one further down) and binding only the first would leave the other unenhanced.
  // Lead forms post natively to Web3Forms. There is no fetch() here on purpose.
  //
  // Web3Forms sits behind Cloudflare Bot Management, which can answer a submission with an
  // interstitial verification page instead of the API response. A navigation survives that - the
  // visitor sees the check, then Web3Forms' own `redirect` field carries them to /thank-you/. A
  // fetch cannot survive it: the challenge response carries no CORS headers, so the request dies as
  // "Failed to fetch" and the visitor is told nothing useful. Verified against the live domain:
  // fetch with JSON, FormData and urlencoded bodies all failed that way, while the native POST
  // reached Web3Forms.
  //
  // Because the post is native, the browser's own required/pattern validation is what guards the
  // fields, which is why the forms no longer carry `novalidate`.
  document.querySelectorAll("form.lead").forEach(function (form) {
    var q = new URLSearchParams(window.location.search);
    var set = function (n, v) { var el = form.querySelector('[name="' + n + '"]'); if (el && !el.value) el.value = v || ""; };
    set("page_url", window.location.href.split("#")[0].slice(0, 300));
    set("referrer", document.referrer.slice(0, 300));
    set("utm_source", q.get("utm_source")); set("utm_medium", q.get("utm_medium")); set("utm_campaign", q.get("utm_campaign"));
    set("client_ts", new Date().toISOString());
    var started = false;
    var variant = form.classList.contains("short") ? "hero_short" : "full";
    form.addEventListener("focusin", function () { if (!started) { started = true; track("form_start", { variant: variant }); } });
    // Fires before the navigation begins, so the event is recorded; the submit is not intercepted.
    form.addEventListener("submit", function () {
      track("form_submit", { variant: variant });
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
    });
  });

  // Tools: each tool page defines window.SCTools[name](rootEl); site.js wires the common submit/input events.
  document.querySelectorAll("[data-tool]").forEach(function (root) {
    var name = root.getAttribute("data-tool");
    var fn = window.SCTools && window.SCTools[name];
    if (!fn) return;
    var run = function () { try { fn(root); } catch (e) { var o = root.querySelector(".out"); if (o) o.textContent = "Something went wrong with this calculation."; } };
    root.addEventListener("input", run);
    root.addEventListener("change", run);
    root.addEventListener("submit", function (e) { e.preventDefault(); run(); });
    run();
  });
})();
