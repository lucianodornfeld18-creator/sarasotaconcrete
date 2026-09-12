# -*- coding: utf-8 -*-
"""Static site builder for sarasotaconcrete.com: site/build.py -> site/dist/."""
import base64
import datetime
import hashlib
import importlib
import json
import pathlib
import re
import shutil
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _data import BASE_URL, PUBLIC_NAME, BUSINESS, SERVICES, SERVICE_ORDER, CITIES, CITY_ORDER, BUILD_DATE, has
from _seo import title_for, description_for, check as seo_check
from templates import render_page, SITE_JS

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"
CONTENT_MODULES = ["content_home", "content_pillars", "content_services_concrete", "content_services_pavers", "content_areas",
                   "content_city_service", "content_city_service_b", "content_pricing", "content_permits", "content_hoa", "content_compare", "content_tools",
                   "content_coastal", "content_faq", "content_guides", "content_company", "content_legal"]


def load_pages():
    pages, seen = [], {}
    for name in CONTENT_MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            print(f"[build] SKIP  {name} (not written yet)"); continue
        importlib.reload(mod)
        ps = mod.get_pages()
        for p in ps:
            if p["route"] in seen:
                raise SystemExit(f"[build] DUPLICATE ROUTE {p['route']} in {seen[p['route']]} and {name}")
            seen[p["route"]] = name
            p["_module"] = name
            p.setdefault("date_published", BUILD_DATE)
            p.setdefault("date_modified", BUILD_DATE)
            pages.append(p)
        print(f"[build] OK    {name} -> {len(ps)} page(s)")
    return pages


def write_page(page):
    out = DIST if page["route"] == "/" else DIST / page["route"].strip("/")
    out.mkdir(parents=True, exist_ok=True)
    html = render_page(page)
    (out / "index.html").write_text(html, encoding="utf-8")
    return len(html.encode("utf-8"))


def write_static():
    dst = DIST / "static"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT / "static", dst)
    shutil.copy(ROOT / "static" / "site.js", DIST / SITE_JS.lstrip("/"))
    fav = ROOT / "static" / "favicon.ico"
    if fav.exists():
        shutil.copy(fav, DIST / "favicon.ico")
    manifest = {"name": PUBLIC_NAME, "short_name": PUBLIC_NAME, "start_url": "/", "display": "browser", "background_color": "#F7F4EE", "theme_color": "#0F4C81",
                "icons": [{"src": "/static/brand/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/static/brand/icon-512.png", "sizes": "512x512", "type": "image/png"}]}
    (DIST / "site.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def write_robots():
    (DIST / "robots.txt").write_text(f"""User-agent: *
Allow: /
Disallow: /thank-you/
Disallow: /api/contact

# AI search crawlers are welcome (answer-engine citation). Training crawlers are an owner decision — see OWNER-INPUTS.md.
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Applebot
Allow: /
User-agent: DuckDuckBot
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
""", encoding="utf-8")


def write_sitemap(pages):
    urls = "\n".join(f"  <url><loc>{BASE_URL}{p['route']}</loc><lastmod>{p['date_modified']}</lastmod></url>" for p in pages if not p.get("noindex"))
    (DIST / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
    (DIST / "sitemap-index.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <sitemap><loc>{BASE_URL}/sitemap.xml</loc><lastmod>{BUILD_DATE}</lastmod></sitemap>\n</sitemapindex>\n', encoding="utf-8")


def write_llms(pages):
    by_route = {p["route"]: p for p in pages}
    def line(route):
        p = by_route.get(route)
        return f"- [{p['h1'] if p else route}]({BASE_URL}{route}): {description_for(p)}" if p else ""
    phone = BUSINESS["phone_display"] if has("phone_display") else "phone pending (941 area code)"
    lines = [f"# {PUBLIC_NAME}", "", f"> {BUSINESS['disclosure_short']}", "",
             f"Website: {BASE_URL}", f"Email: {BUSINESS['email']}", f"Phone: {phone}",
             f"Service area: {BUSINESS['service_area_short']} (Sarasota, Fruitville and Bee Ridge, Gulf Gate, Siesta Key, Palmer Ranch, Longboat Key, Osprey and Casey Key, Nokomis and Laurel, Venice, South Venice, North Port, Englewood and Manasota Key; Port Charlotte, Rotonda West, Placida).",
             f"Status: {BUSINESS['insurance_statement']}. No license number is claimed. Free written estimates after a site visit or video walkthrough.",
             "Key facts: pool decks are the leading local demand; barrier-island work is governed by FEMA AE/VE zones, the NFIP 50% rule (site improvements excluded), Sarasota County's Gulf Beach Setback Line, and sea-turtle lighting rules from May 1 to October 31; unincorporated Sarasota County caps impervious cover at 50% of an RSF lot; Charlotte County permits all flatwork including pavers.",
             "Data: Sarasota Pool Deck Surface Temperature Study (methodology published, measurements pending) and Sarasota Concrete Cost Index (quarterly, CC BY 4.0) at /api/surface-temperatures.json and /api/cost-index.json.", ""]
    lines += ["## Concrete services", ""] + [line(SERVICES[k]["route"]) for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "concrete"] + [""]
    lines += ["## Paver and hardscape services", ""] + [line(SERVICES[k]["route"]) for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "pavers"] + [""]
    lines += ["## Service areas", ""] + [line(f"/areas/{c}/") for c in CITY_ORDER] + [line("/areas/sarasota-county/"), line("/areas/charlotte-county/"), ""]
    for title, prefix in [("Pricing", "/pricing/"), ("Permits, flood and lighting rules", "/permits/"), ("HOA and ARC guides", "/hoa/"), ("Comparisons", "/compare/"),
                          ("Tools", "/tools/"), ("Coastal guides and data", "/coastal/"), ("FAQ", "/faq/"), ("Guides", "/guides/")]:
        lines += [f"## {title}", ""] + [line(r) for r in sorted(by_route) if r.startswith(prefix)] + [""]
    lines += ["## Company", ""] + [line(r) for r in ("/about/", "/editorial-standards/", "/data-and-methods/", "/warranty/", "/financing/", "/directories/", "/gallery/", "/projects/", "/reviews/", "/contact/")] + [""]
    (DIST / "llms.txt").write_text("\n".join(x for x in lines if x is not None), encoding="utf-8")
    # llms-full.txt: every indexable page's text, in order
    full = [f"# {PUBLIC_NAME} — full text", f"Generated {BUILD_DATE}. Source: {BASE_URL}", ""]
    for p in pages:
        if p.get("noindex"):
            continue
        txt = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", p["body_html"], flags=re.S)
        txt = re.sub(r"<h2[^>]*>", "\n## ", txt); txt = re.sub(r"<h3[^>]*>", "\n### ", txt)
        txt = re.sub(r"</(p|li|h2|h3|tr|div|section)>", "\n", txt); txt = re.sub(r"<[^>]+>", " ", txt)
        txt = re.sub(r"[ \t]+", " ", txt); txt = re.sub(r"\n\s*\n+", "\n\n", txt).strip()
        full += [f"---", f"# {p['h1']}", f"URL: {BASE_URL}{p['route']}", f"Updated: {p['date_modified']}", "", txt, ""]
    (DIST / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")


def write_feed(pages):
    items = [p for p in pages if p.get("feed_item")]
    entries = "".join(f"<item><title>{p['h1']}</title><link>{BASE_URL}{p['route']}</link><guid>{BASE_URL}{p['route']}</guid><pubDate>{p['date_published']}</pubDate><description>{p['meta_description']}</description></item>" for p in items)
    (DIST / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{PUBLIC_NAME} — Ask the Estimator</title><link>{BASE_URL}/guides/ask-the-estimator/</link><description>Real questions from Sarasota-area homeowners, answered weekly.</description>{entries}</channel></rss>', encoding="utf-8")


def write_api():
    (DIST / "api").mkdir(exist_ok=True)
    for name in ("cost-index.json", "surface-temperatures.json"):
        src = ROOT / "data" / name
        if src.exists():
            shutil.copy(src, DIST / "api" / name)


def inline_script_hashes():
    hashes = set()
    for f in DIST.rglob("*.html"):
        for m in re.finditer(r"<script(?P<a>[^>]*)>(?P<b>.*?)</script>", f.read_text(encoding="utf-8"), flags=re.S):
            if "src=" in m.group("a") or "ld+json" in m.group("a"):
                continue
            if m.group("b").strip():
                hashes.add("'sha256-" + base64.b64encode(hashlib.sha256(m.group("b").encode("utf-8")).digest()).decode() + "'")
    return sorted(hashes)


def write_headers_redirects():
    csp = "; ".join(["default-src 'self'", "script-src 'self' " + " ".join(inline_script_hashes()) + " https://challenges.cloudflare.com https://static.cloudflareinsights.com",
                     "style-src 'self' 'unsafe-inline'", "img-src 'self' data:", "font-src 'self'",
                     # api.web3forms.com is where the lead forms post. It has to be in connect-src for the
                     # fetch path and in form-action for the plain-POST fallback when JavaScript is
                     # off; default-src 'self' silently blocks both otherwise, with no console error
                     # the visitor or the owner would ever see.
                     "connect-src 'self' https://cloudflareinsights.com https://challenges.cloudflare.com https://api.web3forms.com",
                     "frame-src https://challenges.cloudflare.com",
                     "form-action 'self' https://api.web3forms.com", "base-uri 'self'", "object-src 'none'", "frame-ancestors 'self'", "upgrade-insecure-requests"])
    (DIST / "_headers").write_text(f"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  Cross-Origin-Opener-Policy: same-origin
  Content-Security-Policy: {csp}

/static/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/static/images/*
  Cache-Control: public, max-age=31536000, immutable
/static/brand/*
  Cache-Control: public, max-age=31536000, immutable
/static/site.*.js
  Cache-Control: public, max-age=31536000, immutable
/api/*.json
  Cache-Control: public, max-age=3600
  Access-Control-Allow-Origin: *
/sitemap.xml
  Cache-Control: public, max-age=3600
/llms.txt
  Cache-Control: public, max-age=3600
/llms-full.txt
  Cache-Control: public, max-age=3600
""", encoding="utf-8")
    # www -> apex is a zone Redirect Rule in the Cloudflare dashboard (hosts cannot be matched in _redirects).
    (DIST / "_redirects").write_text("/index.html / 301\n/services/ /concrete/ 301\n/blog/ /guides/ 301\n/blog/* /guides/:splat 301\n", encoding="utf-8")


def write_404():
    src = DIST / "404" / "index.html"
    if src.exists():
        shutil.copy(src, DIST / "404.html")


def rmtree_retry(path, attempts=5, delay=0.5):
    for i in range(attempts):
        try:
            shutil.rmtree(path); return
        except PermissionError:
            if i == attempts - 1:
                raise
            time.sleep(delay)


def main():
    if DIST.exists():
        rmtree_retry(DIST)
    DIST.mkdir(parents=True)
    pages = load_pages()
    import content_depth
    print(f"[build] DEPTH {content_depth.apply(pages)} page(s) extended")
    import content_depth2
    print(f"[build] DEPTH2 {content_depth2.apply(pages)} page(s) extended")
    import content_depth3
    print(f"[build] DEPTH3 {content_depth3.apply(pages)} page(s) extended")
    import content_depth4
    print(f"[build] DEPTH4 {content_depth4.apply(pages)} page(s) extended")
    import content_depth5
    print(f"[build] DEPTH5 {content_depth5.apply(pages)} page(s) extended")
    import content_depth6
    print(f"[build] DEPTH6 {content_depth6.apply(pages)} page(s) extended")
    import content_areas_extra
    print(f"[build] AREAS+ {content_areas_extra.apply(pages)} locality page(s) extended")
    problems, sizes = [], {}
    for p in pages:
        problems += seo_check(p, title_for(p))
        sizes[p["route"]] = write_page(p)
    write_static(); write_robots(); write_sitemap(pages); write_llms(pages); write_feed(pages); write_api(); write_headers_redirects(); write_404()
    big = {r: s for r, s in sizes.items() if s > 150_000}
    print(f"\n[build] {len(pages)} pages -> {DIST}")
    if problems:
        print("[build] SEO checks:"); [print("   -", x) for x in problems]
    if big:
        print("[build] pages over 150 KB:", big)
    (ROOT / "build-report.json").write_text(json.dumps({"built": datetime.datetime.now().isoformat(), "pages": len(pages), "sizes": sizes, "seo_problems": problems}, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
