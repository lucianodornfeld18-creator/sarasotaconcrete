# -*- coding: utf-8 -*-
"""Photo library. Source of truth: ../images/photos.json (written by images/process_photos.py)."""
import json
import pathlib

from _h import esc

_JSON = pathlib.Path(__file__).resolve().parent.parent / "images" / "photos.json"
PHOTOS = json.loads(_JSON.read_text(encoding="utf-8")) if _JSON.exists() else []


def photos_for(service_key, include_secondary=True, real_first=True):
    out = [p for p in PHOTOS if (p["services"][0] == service_key or (include_secondary and service_key in p["services"]))]
    if real_first:
        out.sort(key=lambda p: (p["kind"] != "real", p["services"][0] != service_key))
    return out


FEATURED = [
    "marble-paver-lanai-pool-deck", "travertine-look-paver-pool-deck-square-pool", "gray-paver-driveway-charcoal-grid-border",
    "marble-pool-coping-and-deck-detail", "raised-paver-terrace-stone-wall-pergola", "tan-paver-driveway-meeting-concrete-apron",
]


def featured(limit=6):
    by = {p["slug"]: p for p in PHOTOS}
    picked = [by[s] for s in FEATURED if s in by]
    for p in PHOTOS:
        if len(picked) >= limit:
            break
        if p["kind"] == "real" and p not in picked:
            picked.append(p)
    return picked[:limit]


def figure_html(p, sizes="(max-width:600px) 100vw, (max-width:1100px) 50vw, 380px", eager=False):
    slug = p["slug"]
    srcset = ", ".join(f"/static/images/{slug}-{w}.webp {w}w" for w in (480, 960, 1600))
    badge = '<span class="badge">Concept rendering</span>' if p["kind"] == "rendering" else ""
    lazy = "" if eager else 'loading="lazy" '
    prio = 'fetchpriority="high" ' if eager else ""
    return (f'<figure class="photo"><img src="/static/images/{slug}-960.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{p["w"]}" height="{p["h"]}" alt="{esc(p["alt"])}" {lazy}{prio}decoding="async">{badge}'
            f'<figcaption>{esc(p["alt"])}</figcaption></figure>')


def gallery(service_key, heading, limit=6, intro=""):
    items = photos_for(service_key)[:limit]
    if not items:
        return ""
    has_render = any(p["kind"] == "rendering" for p in items)
    note = " Renderings are labeled; they aren't job photos." if has_render else ""
    figs = "".join(figure_html(p) for p in items)
    return (f'<section class="gallery-sec" id="photos"><h2>{esc(heading)}</h2><p class="src-note">{intro} Provider photos; Suncoast jobs added as documented.{note}</p>'
            f'<div class="gallery">{figs}</div><p><a href="/gallery/">See the full gallery</a></p></section>')


def image_schema(items, base_url):
    return [{"@context": "https://schema.org", "@type": "ImageObject", "contentUrl": f"{base_url}/static/images/{p['slug']}-1600.webp",
             "name": p["alt"], "description": p["alt"] + (" (concept rendering)" if p["kind"] == "rendering" else ""),
             "width": p["w"], "height": p["h"]} for p in items]
