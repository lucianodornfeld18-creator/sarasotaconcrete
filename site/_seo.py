# -*- coding: utf-8 -*-
"""Title/description policy. Pages set their own title and meta_description; this module enforces the
length rules at build time: brand suffix only when it fits, descriptions cut at a clause boundary to <= 160."""
import re

SUFFIX = " | Sarasota Concrete"
MAX_DESC = 160


def title_for(page):
    t = page["title"].strip()
    if page.get("is_home") or page.get("title_full"):
        return t
    if len(t) + len(SUFFIX) <= 60:
        return t + SUFFIX
    return t


def fit_description(d):
    d = " ".join(d.split())
    if len(d) <= MAX_DESC:
        return d
    head = d[:MAX_DESC - 1]
    best = -1
    for sep in (". ", "; ", ": ", ", ", " "):
        i = head.rfind(sep)
        if i >= 118 and i > best:
            best = i
            if sep in (". ", "; ", ": "):
                break
    if best < 118:
        best = head.rfind(" ")
    out = head[:best].rstrip(" ,;:")
    return out if out.endswith((".", "!", "?")) else out + "."


def description_for(page):
    return fit_description(page["meta_description"])


def check(page, full_title):
    problems = []
    if len(full_title) > 65:
        problems.append(f"title too long ({len(full_title)}): {full_title}")
    d = description_for(page)
    if not (110 <= len(d) <= MAX_DESC):
        problems.append(f"meta description length {len(d)}: {page['route']}")
    return problems
