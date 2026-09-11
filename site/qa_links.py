# -*- coding: utf-8 -*-
"""Structural QA over dist/: internal links resolve, orphans, unique titles/H1/meta, JSON-LD parses, one H1,
canonical present, sizes <= 150 KB, noindex pages absent from sitemap, breadcrumbs present, click depth <= 3."""
import html
import json
import pathlib
import re
import sys
from collections import deque

sys.stdout.reconfigure(encoding="utf-8")
DIST = pathlib.Path(__file__).resolve().parent / "dist"


def main():
    pages = {}
    for f in sorted(DIST.rglob("index.html")):
        route = "/" + f.parent.relative_to(DIST).as_posix().strip(".") + "/"
        pages[route.replace("//", "/")] = f.read_text(encoding="utf-8")
    routes = set(pages)
    problems = []
    titles, h1s, metas = {}, {}, {}
    links = {}
    for r, h in pages.items():
        t = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
        h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", h, re.S)
        m = re.search(r'<meta name="description" content="(.*?)"', h)
        if len(h1) != 1:
            problems.append(f"{r}: {len(h1)} H1")
        if not re.search(r'<link rel="canonical"', h):
            problems.append(f"{r}: no canonical")
        if "index,follow" not in h and "noindex" not in h:
            problems.append(f"{r}: no robots meta")
        for lst, key, val in ((titles, "title", t), (h1s, "h1", html.unescape(re.sub("<[^>]+>", "", h1[0])) if h1 else ""), (metas, "meta", m.group(1) if m else "")):
            if val in lst:
                problems.append(f"{r}: duplicate {key} with {lst[val]}")
            lst[val] = r
        for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                json.loads(s)
            except Exception as e:
                problems.append(f"{r}: bad JSON-LD {e}")
        size = len(h.encode("utf-8"))
        if size > 150_000:
            problems.append(f"{r}: {size // 1024} KB")
        hrefs = set(re.findall(r'href="(/[^"#?]*)"', h))
        internal = {x for x in hrefs if not x.startswith("/static/") and not x.startswith("/api/") and x not in ("/sitemap.xml", "/llms.txt", "/feed.xml", "/favicon.ico", "/site.webmanifest", "/llms-full.txt")}
        for x in internal:
            if x not in routes:
                problems.append(f"{r}: broken link {x}")
        links[r] = internal & routes
        if r not in ("/",) and 'class="crumbs"' not in h:
            problems.append(f"{r}: no breadcrumbs")
    # orphans and depth
    depth = {"/": 0}
    q = deque(["/"])
    while q:
        cur = q.popleft()
        for nxt in links.get(cur, ()):
            if nxt not in depth:
                depth[nxt] = depth[cur] + 1
                q.append(nxt)
    orphans = [r for r in routes if r not in depth]
    deep = [(r, d) for r, d in depth.items() if d > 3]
    sm = (DIST / "sitemap.xml").read_text(encoding="utf-8")
    for r, h in pages.items():
        if "noindex" in h and r in sm:
            problems.append(f"{r}: noindex page in sitemap")
        if "noindex" not in h and r not in sm:
            problems.append(f"{r}: indexable page missing from sitemap")
    print(f"{len(pages)} pages; {len(problems)} problems; {len(orphans)} orphans; {len(deep)} deeper than 3 clicks")
    for p in problems[:60]:
        print("  -", p)
    for o in orphans:
        print("  orphan:", o)
    for r, d in deep[:20]:
        print("  depth", d, r)
    (DIST.parent / "qa-links-report.json").write_text(json.dumps({"problems": problems, "orphans": orphans, "deep": deep, "depth": depth}, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
