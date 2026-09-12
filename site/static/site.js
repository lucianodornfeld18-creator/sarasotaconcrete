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
  document.querySelectorAll("form.lead").forEach(function (form) {
    var q = new URLSearchParams(window.location.search);
    var set = function (n, v) { var el = form.querySelector('[name="' + n + '"]'); if (el && !el.value) el.value = v || ""; };
    set("page_url", window.location.href.split("#")[0].slice(0, 300));
    set("referrer", document.referrer.slice(0, 300));
    set("utm_source", q.get("utm_source")); set("utm_medium", q.get("utm_medium")); set("utm_campaign", q.get("utm_campaign"));
    set("client_ts", new Date().toISOString());
    var started = false;
    form.addEventListener("focusin", function () { if (!started) { started = true; track("form_start", { variant: form.classList.contains("short") ? "hero_short" : "full" }); } });
    if (window.fetch) {
      form.addEventListener("submit", function (evt) {
        evt.preventDefault();
        var msg = form.querySelector(".form-msg");
        var btn = form.querySelector('button[type="submit"]');
        var consent = form.querySelector('[name="consent"]');
        if (consent && consent.type === "checkbox" && !consent.checked) {
          if (msg) { msg.textContent = "Please check the consent box so we can contact you."; msg.className = "form-msg error"; }
          return;
        }
        if (msg) { msg.textContent = ""; msg.className = "form-msg"; }
        // A disabled button with unchanged text reads as a dead button. Say what is happening.
        var label = btn ? btn.textContent : "";
        if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
        track("form_submit", { variant: form.classList.contains("short") ? "hero_short" : "full" });
        fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
          .then(function (res) {
            if (res.redirected || res.ok) { window.location.href = "/thank-you/"; return; }
            return res.text().then(function (t) { throw new Error(t || "We could not send your request."); });
          })
          .catch(function (err) {
            track("form_error", { message: String(err.message).slice(0, 120) });
            if (msg) { msg.textContent = err.message || "We could not send your request. Please call instead."; msg.className = "form-msg error"; }
          })
          .finally(function () { if (btn) { btn.disabled = false; btn.textContent = label; } });
      });
    }
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
