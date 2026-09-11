# -*- coding: utf-8 -*-
"""HTML helpers shared by every content module. Keep output plain HTML: no tabs,
no closed accordions, no JS-rendered text (answer capsules must be crawlable)."""
import html as _html
import re

from _data import BASE_URL, BUSINESS, has, SERVICES, CITIES, cs_route


def esc(s):
    return _html.escape(str(s), quote=True)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def cap(question, answer, body="", level=2):
    """Answer capsule: question heading + direct 40-70 word answer, then optional detail."""
    hid = slug(question)[:70]
    return (f'<section class="cap" id="{hid}"><h{level}>{esc(question)}</h{level}>'
            f'<p class="capsule">{answer}</p>{body}</section>')


def sec(heading, body, cls="", level=2, id_=None):
    hid = id_ or slug(heading)[:70]
    c = f' class="{cls}"' if cls else ""
    return f'<section{c} id="{hid}"><h{level}>{heading}</h{level}>{body}</section>'


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


def ul(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def ol(items):
    return "<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"


def table(headers, rows, caption="", cls=""):
    """Renders a data table. In tables of three or more columns the first cell of each row becomes
    a <th scope="row">: axe's td-has-header rule (which Lighthouse runs) requires every data cell in
    a table of 3+ columns and 3+ rows to be reachable from a header, and in these tables the
    left-hand column is the row's header in practice."""
    th = "".join(f'<th scope="col">{h}</th>' for h in headers)
    row_header = len(headers) >= 3 and len(rows) >= 3
    trs = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            if i == 0 and row_header:
                cells.append(f'<th scope="row">{c}</th>')
            else:
                cells.append(f"<td>{c}</td>")
        trs.append("<tr>" + "".join(cells) + "</tr>")
    cap_ = f"<caption>{caption}</caption>" if caption else ""
    return f'<div class="tablewrap"><table class="{cls}">{cap_}<thead><tr>{th}</tr></thead><tbody>{"".join(trs)}</tbody></table></div>'


def note(text, kind="note"):
    return f'<div class="note {kind}">{text}</div>'


def faq_block(items, heading="Questions we get about this"):
    """Visible FAQ (h3 + p). Pass the same items as page['faq'] for FAQPage JSON-LD."""
    inner = "".join(f'<div class="qa"><h3>{esc(q)}</h3><p>{a}</p></div>' for q, a in items)
    return f'<section class="faq" id="faq"><h2>{esc(heading)}</h2>{inner}</section>'


def cta(text="Get a written estimate", href="/contact/", sub=""):
    s = f'<p class="cta-sub">{sub}</p>' if sub else ""
    return f'<div class="cta-band"><a class="btn" href="{href}">{esc(text)}</a>{s}</div>'


def phone_line():
    if has("phone_display"):
        return f'Call or text <a href="tel:{BUSINESS["phone_tel"]}" data-track="tel">{BUSINESS["phone_display"]}</a> or '
    return ""


def reviewed(date, changelog=""):
    who = f'{esc(BUSINESS["author_name"])}, {esc(BUSINESS["author_title"])}' if has("author_name") else "the Sarasota Concrete editorial team (author name pending owner input)"
    cl = f'<span class="changelog">{esc(changelog)}</span>' if changelog else ""
    return f'<p class="reviewed">Last reviewed {date} by {who}. {cl}</p>'


def svc_link(key, text=None):
    s = SERVICES[key]
    return f'<a href="{s["route"]}">{esc(text or s["name"])}</a>'


def city_link(slug_, text=None):
    c = CITIES[slug_]
    return f'<a href="/areas/{slug_}/">{esc(text or c["name"])}</a>'


def cs_link(city, service, text):
    return f'<a href="{cs_route(city, service)}">{esc(text)}</a>'


def link(href, text):
    return f'<a href="{href}">{text}</a>'


def ext(href, text):
    return f'<a href="{href}" rel="noopener" target="_blank">{text}</a>'


def range_(lo, hi, unit="per sq ft"):
    return f'<span class="mono">${lo}–${hi}</span> {unit}'


def facts(items):
    """Key-fact strip: list of (label, value)."""
    return '<dl class="facts">' + "".join(f"<div><dt>{esc(k)}</dt><dd>{v}</dd></div>" for k, v in items) + "</dl>"


def cards(items):
    """items: (href, title, text)"""
    return '<div class="cards">' + "".join(f'<a class="card" href="{h}"><span class="card-t">{esc(t)}</span><span class="card-x">{x}</span></a>' for h, t, x in items) + "</div>"


def service_schema(key, route, extra_area=None):
    s = SERVICES[key]
    area = extra_area or [{"@type": "City", "name": CITIES[c]["name"], "sameAs": CITIES[c]["wiki"]} for c in ("sarasota", "venice", "north-port", "longboat-key", "siesta-key")]
    return {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
            "provider": {"@id": BASE_URL + "/#organization"}, "areaServed": area, "url": BASE_URL + route,
            "description": s["short"]}


def dataset_schema(name, description, url, dist_url, date_modified, keywords):
    return {"@context": "https://schema.org", "@type": "Dataset", "name": name, "description": description, "url": BASE_URL + url,
            "license": "https://creativecommons.org/licenses/by/4.0/", "creator": {"@id": BASE_URL + "/#organization"},
            "dateModified": date_modified, "keywords": keywords, "spatialCoverage": {"@type": "Place", "name": "Sarasota County, Florida"},
            "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": BASE_URL + dist_url}]}
