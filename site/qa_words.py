# -*- coding: utf-8 -*-
"""Word counts per page, two ways: <main> only, and full body minus scripts/styles (the St. Cloud benchmark method).
Compares against the floor/target table from the prompt."""
import html
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
DIST = pathlib.Path(__file__).resolve().parent / "dist"
TARGETS = [  # (prefix or exact, type, floor, target_low)
    ("/", "home", 3358, 3800), ("/concrete/", "pillar", 1470, 2200), ("/pavers/", "pillar", 1470, 2200),
    ("/areas/sarasota-county/", "county", 0, 2000), ("/areas/charlotte-county/", "county", 0, 2000),
    ("/pricing/", "cost", 0, 2000), ("/faq/", "faq", 0, 3000), ("/about/", "about", 485, 900), ("/editorial-standards/", "about", 485, 900),
    ("/data-and-methods/", "about", 485, 900), ("/contact/", "contact", 537, 500),
]


def count(t):
    return len(re.findall(r"[A-Za-z][A-Za-z'\-]+", t))


def strip(t):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def classify(route):
    for pre, typ, fl, tg in TARGETS:
        if route == pre:
            return typ, fl, tg
    if re.match(r"^/(concrete|pavers)/[a-z\-]+/[a-z\-]+/$", route):
        return "city_service", 0, 1200
    if re.match(r"^/(concrete|pavers)/[a-z\-]+/$", route):
        return "service", 1000, 1800
    if route.startswith("/areas/"):
        tier2 = any(x in route for x in ("port-charlotte", "rotonda-west", "placida"))
        return ("city_t2", 455, 1000) if tier2 else ("city_t1", 1144, 1800)
    if route.startswith("/pricing/"):
        return "cost", 0, 2000
    if route.startswith("/faq/"):
        return "faq_topic", 0, 1200
    if route.startswith(("/guides/", "/compare/", "/coastal/", "/permits/", "/hoa/")):
        return "guide", 0, 1500
    if route.startswith("/tools/"):
        return "tool", 0, 800
    return "other", 0, 0


def main():
    rows = []
    for f in sorted(DIST.rglob("index.html")):
        route = "/" + f.parent.relative_to(DIST).as_posix().strip(".") + "/"
        route = route.replace("//", "/")
        h = f.read_text(encoding="utf-8")
        m = re.search(r"<main.*?</main>", h, re.S)
        body = re.search(r"<body.*?</body>", h, re.S)
        wm = count(strip(m.group(0))) if m else 0
        wb = count(strip(body.group(0))) if body else 0
        typ, fl, tg = classify(route)
        rows.append({"route": route, "type": typ, "main_words": wm, "body_words": wb, "floor": fl, "target": tg, "meets_floor": wb >= fl, "meets_target": wb >= tg})
    by = {}
    for r in rows:
        by.setdefault(r["type"], []).append(r)
    print(f"{'type':14} {'n':>3} {'min body':>9} {'median':>7} {'max':>6} {'>=floor':>8} {'>=target':>9}")
    for t, rs in sorted(by.items()):
        ws = sorted(x["body_words"] for x in rs)
        print(f"{t:14} {len(rs):3d} {ws[0]:9d} {ws[len(ws)//2]:7d} {ws[-1]:6d} {sum(x['meets_floor'] for x in rs):8d} {sum(x['meets_target'] for x in rs):9d}")
    short = [r for r in rows if not r["meets_floor"]]
    print("\nbelow floor:", len(short))
    for r in short:
        print("  ", r["route"], r["body_words"], "<", r["floor"])
    (DIST.parent / "qa-words-report.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
