# -*- coding: utf-8 -*-
"""8-gram similarity QA: internal (every pair of pages on this site) and network (this site vs sibling hubs).
Boilerplate (header, footer, forms, CTA bands, 'last reviewed' lines, legal pages) is excluded before hashing.
A pair is flagged when shared 8-grams exceed 15% of the smaller page's 8-grams, or when any 8-gram longer
sentence fragment repeats between pages (listed for rewrite)."""
import html
import json
import pathlib
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent
DIST = ROOT / "dist"
SIBLINGS = {
    "lakewoodranch": pathlib.Path(r"C:\Users\luana\Documents\Codex\Projects\lakewoodranchconcretefl"),
    "windermere": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\Projetos\windermereconcrete"),
    "ocoee": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\Projetos\ocoeeconcrete"),
    "groveland": pathlib.Path(r"C:\Users\luana\Documents\Codex\2026-09-07\groveland-concrete\site\dist"),
    "gcm": pathlib.Path(r"C:\Users\luana\SSD-Antigo-Lucia\gcm-site"),
}
LEGAL_ROUTES = {"/privacy/", "/terms/", "/accessibility/", "/thank-you/", "/404/"}


def clean(h, ours=True):
    if ours:
        m = re.search(r"<main.*?</main>", h, re.S)
        t = m.group(0) if m else h
        t = re.sub(r'<form.*?</form>', " ", t, flags=re.S)
        t = re.sub(r'<div class="cta-band">.*?</div>', " ", t, flags=re.S)
        t = re.sub(r'<p class="reviewed">.*?</p>', " ", t, flags=re.S)
        t = re.sub(r'<nav class="crumbs".*?</nav>', " ", t, flags=re.S)
        t = re.sub(r'<dl class="facts">.*?</dl>', " ", t, flags=re.S)
        t = re.sub(r'<figure.*?</figure>', " ", t, flags=re.S)
        t = re.sub(r'<p class="src-note">.*?</p>', " ", t, flags=re.S)
    else:
        t = h
        t = re.sub(r"<(header|nav|footer|form)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).lower()
    return re.findall(r"[a-z0-9][a-z0-9'\-]*", t)


def grams(words, n=8):
    return {" ".join(words[i:i + n]) for i in range(max(0, len(words) - n + 1))}


def main():
    pages = {}
    for f in sorted(DIST.rglob("index.html")):
        route = "/" + f.parent.relative_to(DIST).as_posix().strip(".") + "/"
        route = route.replace("//", "/")
        if route in LEGAL_ROUTES:
            continue
        pages[route] = grams(clean(f.read_text(encoding="utf-8")))
    routes = list(pages)
    internal = []
    for i in range(len(routes)):
        for j in range(i + 1, len(routes)):
            a, b = pages[routes[i]], pages[routes[j]]
            if not a or not b:
                continue
            shared = a & b
            ratio = len(shared) / min(len(a), len(b))
            if shared:
                internal.append((routes[i], routes[j], len(shared), round(ratio * 100, 1), sorted(shared)[:3]))
    internal.sort(key=lambda x: -x[3])
    print(f"INTERNAL: {len(routes)} pages, {len(internal)} pairs share at least one 8-gram")
    over = [x for x in internal if x[3] > 15]
    print(f"  pairs over 15%: {len(over)}")
    for x in internal[:25]:
        print("  ", x[3], "%", x[2], "shared", x[0], "|", x[1], "|", x[4][0][:80] if x[4] else "")
    # network
    network = []
    for name, base in SIBLINGS.items():
        if not base.exists():
            print("SIBLING MISSING", name); continue
        sib = {}
        for f in base.rglob("index.html"):
            if any(x in f.parts for x in (".git", "node_modules", "__pycache__", "es", "pt", "images")):
                continue
            try:
                sib[f] = grams(clean(f.read_text(encoding="utf-8", errors="ignore"), ours=False))
            except Exception:
                pass
        hits = []
        for r, g in pages.items():
            for f, sg in sib.items():
                shared = g & sg
                if shared:
                    hits.append((round(len(shared) / max(1, min(len(g), len(sg))) * 100, 1), len(shared), r, str(f.relative_to(base)), sorted(shared)[:2]))
        hits.sort(key=lambda x: -x[0])
        print(f"NETWORK vs {name}: {len(sib)} sibling pages; {len(hits)} page pairs share an 8-gram; max {hits[0][0] if hits else 0}%")
        for h in hits[:8]:
            print("  ", h[0], "%", h[1], h[2], "|", h[3], "|", h[4][0][:90] if h[4] else "")
        network.append({"sibling": name, "pairs": len(hits), "top": hits[:20]})
    (ROOT / "qa-similarity-report.json").write_text(json.dumps({"internal_top": internal[:100], "internal_over_15": over, "network": network}, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
