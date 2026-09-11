# -*- coding: utf-8 -*-
"""Page shell for sarasotaconcrete.com.

Page dict contract:
{
  "route": "/concrete/pool-decks/",   # trailing slash; "/" for home
  "title": "...",                       # <title> without suffix (suffix added if it fits)
  "meta_description": "...",            # 120-160 chars
  "h1": "...",                          # required, different from title
  "kicker": "...",                      # optional eyebrow above h1
  "lede": "...",                        # optional lead paragraph (HTML)
  "breadcrumbs": [("Home","/"), ("Concrete","/concrete/"), ("Pool decks", None)],
  "body_html": "...",
  "schema": [ {...} ],                  # extra JSON-LD; WebPage + BreadcrumbList added automatically
  "faq": [(q, a_html), ...],            # optional; renders FAQPage JSON-LD (only when visible on page)
  "noindex": False, "is_home": False,
  "date_published": "2026-09-10", "date_modified": "2026-09-10",
  "og_image": "/static/brand/social-1200.png",
  "article": True,                      # optional: emits Article schema with author
}
"""
import hashlib
import json
import pathlib
import re

from _data import (BASE_URL, PUBLIC_NAME, BUSINESS, has, NAV_PRIMARY, FOOTER_COLUMNS, CITIES, TIER1, TIER2,
                   FORM_LOCALITIES, FORM_SERVICES_CONCRETE, FORM_SERVICES_PAVERS, FORM_PROPERTY, FORM_FLOOD,
                   FORM_TIMELINE, FORM_PRESENCE, TURNSTILE_SITE_KEY, BUILD_DATE)
from _h import esc
from _seo import title_for, description_for

STATIC = pathlib.Path(__file__).resolve().parent / "static"
_SITE_JS_SRC = (STATIC / "site.js").read_text(encoding="utf-8")
SITE_JS = "/static/site." + hashlib.sha256(_SITE_JS_SRC.encode()).hexdigest()[:10] + ".js"

FONTS_CSS = """
@font-face{font-family:'Bricolage Grotesque';font-style:normal;font-weight:400 800;font-display:swap;src:url(/static/fonts/bricolage-normal-400-800-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:400 700;font-display:optional;src:url(/static/fonts/instrument-normal-400-700-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:'Instrument Sans';font-style:italic;font-weight:400 700;font-display:optional;src:url(/static/fonts/instrument-italic-400-700-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:'DM Mono';font-style:normal;font-weight:500;font-display:optional;src:url(/static/fonts/dmmono-normal-500-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
"""

CSS = r"""
:root{--tide:#C1922E;--deep:#8F6B1E;--ink:#1F1F1F;--shell:#FFFFFF;--sand:#F4F1EA;--glass:#F6EFDC;--coq:#2E2E30;--mute:#63615C;--rule:#E2DCD0;--card:#FFFFFF;--gold-lt:#E0BC63;--graphite:#2E2E30;
--disp:'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;--body:'Instrument Sans','Segoe UI',system-ui,sans-serif;--mono:'DM Mono',Consolas,monospace;--w:1140px;--r:10px}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;font-family:var(--body);font-size:17px;line-height:1.6;color:var(--ink);background:var(--shell)}
a{color:var(--deep);text-decoration-thickness:1px;text-underline-offset:3px}a:hover{color:#6E5116}
h1,h2,h3,h4{font-family:var(--disp);line-height:1.12;letter-spacing:-.015em;color:var(--ink);margin:0 0 .5em}
h1{font-size:clamp(2rem,4.6vw,3.2rem);font-weight:800;font-variation-settings:'opsz' 96}
h2{font-size:clamp(1.45rem,2.6vw,2rem);font-weight:700;margin-top:1.6em}
h3{font-size:1.18rem;font-weight:700;margin-top:1.3em}
p{margin:0 0 1em}ul,ol{padding-left:1.3em;margin:0 0 1em}li{margin:.25em 0}
img{max-width:100%;height:auto;display:block}
.mono{font-family:var(--mono);font-size:.95em}
.wrap{max-width:var(--w);margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-999px;top:0;background:var(--ink);color:#fff;padding:8px 12px;z-index:99}.skip:focus{left:8px;top:8px}
/* header */
.top{background:var(--shell);border-bottom:1px solid var(--rule);position:sticky;top:0;z-index:50}
.top .wrap{display:flex;align-items:center;gap:18px;min-height:64px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);font-family:var(--disp);font-weight:800;font-size:1.22rem;letter-spacing:-.01em;white-space:nowrap}
.brand svg{flex:0 0 auto}
.brand{gap:9px}
.brand .wm{display:block;line-height:1}
.brand .wm b{display:block;font-family:var(--disp);font-weight:800;font-size:1.16rem;letter-spacing:.005em;color:var(--ink);line-height:1}
.brand .wm small{display:block;font-family:var(--disp);font-weight:600;font-size:.6rem;letter-spacing:.30em;color:var(--deep);line-height:1;margin-top:3px}
nav.primary{margin-left:auto}
nav.primary>ul{list-style:none;margin:0;padding:0;display:flex;gap:2px}
nav.primary>ul>li{position:relative}
nav.primary a{display:block;padding:10px 11px;color:var(--ink);text-decoration:none;font-weight:600;font-size:.92rem;border-radius:8px}
nav.primary a:hover,nav.primary a:focus{background:var(--sand)}
nav.primary ul ul{display:none;position:absolute;left:0;top:100%;background:#fff;border:1px solid var(--rule);border-radius:var(--r);padding:8px;min-width:250px;box-shadow:0 12px 30px rgba(31,31,31,.13);list-style:none;margin:0;z-index:60}
nav.primary li:hover>ul,nav.primary li:focus-within>ul{display:block}
nav.primary ul ul a{font-weight:500;padding:8px 10px;font-size:.9rem}
.top .call{margin-left:6px;font-weight:700;color:#1F1F1F;background:var(--tide);padding:10px 16px;border-radius:999px;text-decoration:none;white-space:nowrap;font-size:.92rem}
.top .call:hover{background:var(--gold-lt);color:#1F1F1F}
.navtoggle{display:none;margin-left:auto;background:none;border:1px solid var(--rule);border-radius:8px;padding:8px 10px;font:inherit;font-weight:600}
@media(max-width:1000px){nav.primary{display:none;position:absolute;left:0;right:0;top:64px;background:var(--shell);border-bottom:1px solid var(--rule);padding:10px 16px 18px}
nav.primary.open{display:block}nav.primary>ul{flex-direction:column}nav.primary ul ul{display:block;position:static;box-shadow:none;border:0;padding:0 0 4px 12px;background:transparent}
.navtoggle{display:inline-block}.top .call{display:none}.top .wrap{gap:10px}}
/* hero */
.hero{position:relative;padding:44px 0 26px;overflow:hidden}
.hero .wrap{position:relative;max-width:900px}
.hero .kicker{display:inline-block;font-family:var(--disp);font-weight:700;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:var(--deep);margin-bottom:10px}
.hero .lede{font-size:1.15rem;color:#2C3A47;max-width:62ch;margin:.4em 0 0}
.tide{position:absolute;right:-60px;top:-30px;width:520px;height:320px;opacity:.55;pointer-events:none}
@media(max-width:700px){.tide{width:340px;right:-120px;top:-40px;opacity:.35}}
.crumbs{font-size:.85rem;color:var(--mute);margin:0 0 14px}.crumbs a{color:var(--mute)}.crumbs span{margin:0 6px}
/* main */
main{padding:10px 0 50px}
.content{max-width:820px}
.content>section{margin:0 0 1.2em}
.capsule{background:#fff;border-left:4px solid var(--tide);padding:14px 18px;border-radius:0 var(--r) var(--r) 0;font-size:1.06rem}
.note{background:var(--glass);border-radius:var(--r);padding:12px 16px;margin:0 0 1.1em;font-size:.97rem}
.note.warn{background:#F6E4DA}
.tablewrap{overflow-x:auto;margin:0 0 1.2em;border:1px solid var(--rule);border-radius:var(--r);background:#fff}
table{border-collapse:collapse;width:100%;font-size:.95rem}
caption{text-align:left;font-weight:600;padding:10px 12px;font-family:var(--disp)}
th,td{padding:9px 12px;border-top:1px solid var(--rule);text-align:left;vertical-align:top}
thead th{background:var(--sand);border-top:0;font-family:var(--disp);font-weight:700;font-size:.9rem}
tbody th[scope=row]{font-weight:600;text-align:left;background:#FBFAF7}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin:0 0 1.4em;padding:0}
.facts div{background:#fff;border:1px solid var(--rule);border-radius:var(--r);padding:12px 14px}
.facts dt{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);font-weight:600}
.facts dd{margin:4px 0 0;font-family:var(--disp);font-weight:700;font-size:1.05rem}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;margin:0 0 1.4em}
.card{display:block;background:#fff;border:1px solid var(--rule);border-radius:var(--r);padding:16px;text-decoration:none;color:var(--ink);transition:transform .15s,border-color .15s}
.card:hover{transform:translateY(-2px);border-color:var(--tide)}
.card-t{display:block;font-family:var(--disp);font-weight:700;font-size:1.05rem;margin-bottom:6px;color:var(--deep)}
.card-x{display:block;font-size:.92rem;color:#3B4854}
.cta-band{background:var(--graphite);color:#fff;border-radius:var(--r);padding:22px 24px;margin:1.6em 0;display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.cta-band .cta-sub{margin:0;color:#D7DEE4;font-size:.95rem;max-width:56ch}
.btn{display:inline-block;background:var(--tide);color:#1F1F1F;font-weight:700;padding:12px 20px;border-radius:999px;text-decoration:none;border:0;font:inherit;cursor:pointer}
.btn:hover{background:var(--gold-lt);color:#1F1F1F}.btn.outline{background:transparent;border:2px solid var(--tide);color:var(--tide)}
.reviewed{font-size:.88rem;color:var(--mute);border-top:1px solid var(--rule);padding-top:12px;margin-top:2em}
.changelog{display:block;font-size:.85rem}
.faq .qa{border-top:1px solid var(--rule);padding:10px 0 2px}.faq h3{margin-top:.2em;font-size:1.08rem}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin:0 0 1em}
.photo{margin:0;position:relative;background:#fff;border:1px solid var(--rule);border-radius:var(--r);overflow:hidden}
.photo img{width:100%;aspect-ratio:4/3;object-fit:cover}
.photo figcaption{font-size:.82rem;color:var(--mute);padding:8px 10px}
.badge{position:absolute;top:8px;left:8px;background:var(--ink);color:#fff;font-size:.7rem;padding:3px 8px;border-radius:999px;letter-spacing:.06em;text-transform:uppercase}
.two{display:grid;grid-template-columns:1fr 1fr;gap:22px}@media(max-width:760px){.two{grid-template-columns:1fr}}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:0 0 1.4em}
.pill{display:inline-block;background:var(--sand);border-radius:999px;padding:3px 10px;font-size:.82rem;margin:2px 4px 2px 0}
.split{display:grid;grid-template-columns:minmax(0,820px) 300px;gap:40px}@media(max-width:1100px){.split{grid-template-columns:1fr}}
aside.rail{font-size:.93rem}aside.rail .box{background:#fff;border:1px solid var(--rule);border-radius:var(--r);padding:16px;margin-bottom:16px}
aside.rail h3{margin-top:0;font-size:1rem}aside.rail ul{padding-left:1.1em;margin:0}
/* home blocks */
.pillars{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin:10px 0 24px}@media(max-width:760px){.pillars{grid-template-columns:1fr}}
.pillar{background:#fff;border:1px solid var(--rule);border-radius:14px;padding:22px}
.pillar h2{margin-top:0}.pillar ul{columns:2;column-gap:18px;padding-left:1.1em}@media(max-width:520px){.pillar ul{columns:1}}
.stripe{background:var(--sand);padding:28px 0;margin:28px 0}
/* forms */
form.lead{background:#fff;border:1px solid var(--rule);border-radius:14px;padding:22px}
form.lead .row{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:640px){form.lead .row{grid-template-columns:1fr}}
label{display:block;font-weight:600;font-size:.9rem;margin:10px 0 4px}
input,select,textarea{width:100%;font:inherit;padding:10px 12px;border:1px solid #C9C2B4;border-radius:8px;background:#fff}
textarea{min-height:120px}
.consent{display:flex;gap:10px;align-items:flex-start;font-size:.88rem;font-weight:400;margin:14px 0}.consent input{width:auto;margin-top:4px}
.form-msg{margin:10px 0 0;font-size:.95rem}.form-msg.error{color:#9B2F1F}
.hp{position:absolute;left:-9999px}
/* tools */
.tool{background:#fff;border:1px solid var(--rule);border-radius:14px;padding:22px;margin:0 0 1.4em}
.tool .out{background:var(--glass);border-radius:var(--r);padding:14px 16px;margin-top:14px}
.tool fieldset{border:0;padding:0;margin:0 0 10px}
/* footer */
footer{background:var(--graphite);color:#D7DEE4;padding:44px 0 30px;font-size:.92rem}
footer a{color:#fff}footer .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:24px}
footer .colh{color:#fff;margin:0 0 10px;font-size:.85rem;letter-spacing:.14em;text-transform:uppercase;font-family:var(--disp);font-weight:700}
footer ul{list-style:none;padding:0;margin:0}footer li{margin:4px 0}
footer .legal{border-top:1px solid #46464A;margin-top:28px;padding-top:18px;color:#B7C2CC;font-size:.85rem}
.tools-nav{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 1em}
@media print{.top,footer,.cta-band{display:none}}
"""


def _minify(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*\n\s*", "", css)
    return re.sub(r"\s*([{}:;,>])\s*", r"\1", css).replace(";}", "}")


CSS_MIN = _minify(FONTS_CSS + CSS)

# Flat two-colour derivative of the owner's hexagonal monogram. The original art is an isometric
# brass gradient with stone texture: it is unreadable at 16 px and adds weight to the LCP, so the
# header, favicon and icons use this derivative while the original serves og:image, social and email.
_HEX_OUTER = "M32.00,4.00 L56.25,18.00 L56.25,46.00 L32.00,60.00 L7.75,46.00 L7.75,18.00 Z"
_HEX_INNER = "M32.00,13.50 L48.02,22.75 L48.02,41.25 L32.00,50.50 L15.98,41.25 L15.98,22.75 Z"
_S_RIBBON = "M41.5,20.5 H26.5 a5.5,5.5 0 0 0 0,11 H37.5 a5.5,5.5 0 0 1 0,11 H22.5"
MARK_SVG = (
    f'<svg width="36" height="36" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
    f'<defs><clipPath id="mkU"><path d="M0,0 H64 V32 H0 Z"/></clipPath>'
    f'<clipPath id="mkL"><path d="M0,32 H64 V64 H0 Z"/></clipPath></defs>'
    f'<path d="{_HEX_OUTER} {_HEX_INNER}" fill="#2E2E30" fill-rule="evenodd" clip-path="url(#mkL)"/>'
    f'<path d="{_HEX_OUTER} {_HEX_INNER}" fill="#C1922E" fill-rule="evenodd" clip-path="url(#mkU)"/>'
    f'<path d="{_S_RIBBON}" fill="none" stroke="#C1922E" stroke-width="6.5" stroke-linecap="square"/>'
    f'</svg>')

TIDE_SVG = (
    '<svg class="tide" viewBox="0 0 520 320" aria-hidden="true" focusable="false" fill="none" '
    'stroke="#C1922E" stroke-width="1.1">'
    + "".join(
        f'<path d="M{x},{y} l21,-12 l21,12 l0,24 l-21,12 l-21,-12 Z" opacity="{op:.2f}"/>'
        for row, y in enumerate(range(10, 320, 36))
        for col, x in enumerate(range(-10 + (21 if row % 2 else 0), 520, 42))
        for op in [max(0.05, 0.34 - (row * 0.035) - (col * 0.012))]
    )
    + "</svg>")

def _nav():
    items = []
    for label, href, subs in NAV_PRIMARY:
        sub = ""
        if subs:
            sub = "<ul>" + "".join(f'<li><a href="{h}">{esc(t)}</a></li>' for t, h in subs) + "</ul>"
        items.append(f'<li><a href="{href}">{esc(label)}</a>{sub}</li>')
    call = f'<a class="call" href="tel:{BUSINESS["phone_tel"]}" data-track="tel">Call {esc(BUSINESS["phone_display"])}</a>' if has("phone_display") else '<a class="call" href="/contact/">Get an estimate</a>'
    return (f'<header class="top"><div class="wrap"><a class="brand" href="/">{MARK_SVG}<span class="wm"><b>SARASOTA</b><small>CONCRETE</small></span></a>'
            f'<button class="navtoggle" id="navToggle" aria-expanded="false" aria-controls="primaryNav">Menu</button>'
            f'<nav class="primary" id="primaryNav" aria-label="Primary"><ul>{"".join(items)}</ul></nav>{call}</div></header>')


def _footer():
    cols = "".join(f'<div><div class="colh">{esc(h)}</div><ul>' + "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for t, u in links) + "</ul></div>" for h, links in FOOTER_COLUMNS)
    phone = f' · <a href="tel:{BUSINESS["phone_tel"]}" data-track="tel">{esc(BUSINESS["phone_display"])}</a>' if has("phone_display") else ""
    lic = f' · License {esc(BUSINESS["license_number"])}' if BUSINESS.get("license_number") else ""
    ent = f' Requests are handled by {esc(BUSINESS["legal_entity"])}.' if has("legal_entity") else ""
    return (f'<footer><div class="wrap"><div class="cols">{cols}</div><div class="legal">'
            f'<p><strong>{PUBLIC_NAME}</strong> · {esc(BUSINESS["insurance_statement"])}{lic} · <a href="mailto:{BUSINESS["email"]}">{BUSINESS["email"]}</a>{phone}</p>'
            f'<p>{esc(BUSINESS["disclosure_short"])}{ent} Cost ranges on this site are planning ranges with a stated date and method; a written estimate follows a site visit or video walkthrough. '
            f'No address, license, rating or project count is claimed that the provider has not documented.</p>'
            f'<p>© {BUILD_DATE[:4]} {PUBLIC_NAME}. <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="/accessibility/">Accessibility</a> · <a href="/sitemap.xml">Sitemap</a> · <a href="/llms.txt">llms.txt</a></p>'
            f'</div></div></footer>')


def lead_form(compact=False, city=None, service=None):
    opt = lambda xs, sel=None: "".join(f'<option{" selected" if x == sel else ""}>{esc(x)}</option>' for x in xs)
    turn = f'<div class="cf-turnstile" data-sitekey="{TURNSTILE_SITE_KEY}"></div>' if not TURNSTILE_SITE_KEY.startswith("{{") else ""
    return f'''<form class="lead" method="post" action="/api/contact" enctype="multipart/form-data" novalidate>
<input type="hidden" name="hub_id" value="sarasota"><input type="hidden" name="page_url" value=""><input type="hidden" name="utm_source" value=""><input type="hidden" name="utm_medium" value=""><input type="hidden" name="utm_campaign" value=""><input type="hidden" name="referrer" value=""><input type="hidden" name="client_ts" value="">
<div class="hp" aria-hidden="true"><label>Company<input type="text" name="company" tabindex="-1" autocomplete="off"></label></div>
<div class="row"><div><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name" maxlength="100"></div>
<div><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel" maxlength="40"></div></div>
<div class="row"><div><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email" maxlength="254"></div>
<div><label for="f-city">Where is the property?</label><select id="f-city" name="city">{opt(FORM_LOCALITIES, city)}</select></div></div>
<div class="row"><div><label for="f-service">What do you need?</label><select id="f-service" name="service"><optgroup label="Concrete">{opt(FORM_SERVICES_CONCRETE, service)}</optgroup><optgroup label="Pavers &amp; hardscape">{opt(FORM_SERVICES_PAVERS, service)}</optgroup></select></div>
<div><label for="f-prop">Property type</label><select id="f-prop" name="property_type">{opt(FORM_PROPERTY)}</select></div></div>
<div class="row"><div><label for="f-flood">Flood zone, if you know it</label><select id="f-flood" name="flood_zone">{opt(FORM_FLOOD)}</select></div>
<div><label for="f-time">Timeline</label><select id="f-time" name="timeline">{opt(FORM_TIMELINE)}</select></div></div>
<label for="f-presence">Are you at the property?</label><select id="f-presence" name="presence">{opt(FORM_PRESENCE)}</select>
<label for="f-msg">Tell us about the project (size, material, what's there now)</label><textarea id="f-msg" name="message" maxlength="3000"></textarea>
<label for="f-photo">Photo (optional, JPG or PNG up to 8 MB)</label><input id="f-photo" name="photo" type="file" accept="image/jpeg,image/png">
<label class="consent"><input type="checkbox" name="consent" value="yes" required><span>{esc(BUSINESS["consent_text"])} See the <a href="/privacy/">privacy policy</a>.</span></label>
{turn}<button class="btn" type="submit">Send my request</button><p class="form-msg" aria-live="polite"></p></form>'''


def _breadcrumbs(bc):
    parts = []
    for i, (name, href) in enumerate(bc):
        parts.append(f'<a href="{href}">{esc(name)}</a>' if href else f'<strong>{esc(name)}</strong>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "<span>›</span>".join(parts) + "</nav>"


def _schema(page, full_title):
    url = BASE_URL + page["route"]
    graph = []
    if page.get("is_home"):
        org = {"@type": "Organization", "@id": BASE_URL + "/#organization", "name": PUBLIC_NAME, "url": BASE_URL + "/",
               "logo": BASE_URL + "/static/brand/icon-512.png", "email": BUSINESS["email"],
               "areaServed": [{"@type": "City", "name": CITIES[c]["name"], "sameAs": CITIES[c]["wiki"]} for c in TIER1 + TIER2],
               "description": BUSINESS["disclosure_short"]}
        if has("phone_tel"):
            org["telephone"] = BUSINESS["phone_tel"]
        same = [BUSINESS[k] for k in ("google_profile", "yelp", "facebook", "instagram", "nextdoor") if BUSINESS.get(k)]
        if same:
            org["sameAs"] = same
        graph.append(org)
        graph.append({"@type": "WebSite", "@id": BASE_URL + "/#website", "url": BASE_URL + "/", "name": PUBLIC_NAME, "publisher": {"@id": BASE_URL + "/#organization"}})
    wp = {"@type": "WebPage", "@id": url, "url": url, "name": full_title, "description": description_for(page), "isPartOf": {"@id": BASE_URL + "/#website"},
          "datePublished": page.get("date_published", BUILD_DATE), "dateModified": page.get("date_modified", BUILD_DATE), "inLanguage": "en-US"}
    graph.append(wp)
    if page.get("breadcrumbs"):
        items = []
        for i, (name, href) in enumerate(page["breadcrumbs"], start=1):
            it = {"@type": "ListItem", "position": i, "name": name}
            if href:
                it["item"] = BASE_URL + href
            items.append(it)
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if page.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in page["faq"]]})
    if page.get("article"):
        art = {"@type": "Article", "headline": page["h1"], "datePublished": page.get("date_published", BUILD_DATE), "dateModified": page.get("date_modified", BUILD_DATE),
               "mainEntityOfPage": url, "publisher": {"@id": BASE_URL + "/#organization"}}
        art["author"] = {"@type": "Person", "name": BUSINESS["author_name"], "jobTitle": BUSINESS["author_title"]} if has("author_name") else {"@id": BASE_URL + "/#organization"}
        graph.append(art)
    out = [{"@context": "https://schema.org", "@graph": graph}] + list(page.get("schema") or [])
    return "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in out)


def render_page(page):
    full_title = title_for(page)
    url = BASE_URL + page["route"]
    robots = '<meta name="robots" content="noindex,follow">' if page.get("noindex") else '<meta name="robots" content="index,follow,max-image-preview:large">'
    og_img = BASE_URL + page.get("og_image", "/static/brand/social-1200.png")
    kicker = f'<span class="kicker">{esc(page["kicker"])}</span>' if page.get("kicker") else ""
    lede = f'<p class="lede">{page["lede"]}</p>' if page.get("lede") else ""
    crumbs = _breadcrumbs(page["breadcrumbs"]) if page.get("breadcrumbs") and not page.get("is_home") else ""
    return f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description_for(page))}">
{robots}
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.ico" sizes="32x32"><link rel="icon" href="/static/brand/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/static/brand/icon-192.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/static/fonts/bricolage-normal-400-800-latin.woff2" as="font" type="font/woff2" crossorigin>
<meta property="og:site_name" content="{PUBLIC_NAME}"><meta property="og:type" content="{'website' if page.get('is_home') else 'article'}"><meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(description_for(page))}"><meta property="og:url" content="{url}"><meta property="og:image" content="{og_img}"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Ask the Estimator" href="/feed.xml">
<style>{CSS_MIN}</style>
{_schema(page, full_title)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{_nav()}
<main id="main">
<div class="hero">{TIDE_SVG}<div class="wrap">{crumbs}{kicker}<h1>{page["h1"]}</h1>{lede}</div></div>
<div class="wrap">{page["body_html"]}</div>
</main>
{_footer()}
<script src="{SITE_JS}" defer></script>
</body>
</html>'''
