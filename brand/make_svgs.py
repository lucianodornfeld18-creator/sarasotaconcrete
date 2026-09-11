# -*- coding: utf-8 -*-
"""Writes the individual SVG files for the ten logo directions shown in logos.html,
plus the provisional Bayline (direction 1) assets used by the site until the owner chooses."""
import pathlib, re, html
ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "svg"; OUT.mkdir(exist_ok=True)
src = (ROOT / "logos.html").read_text(encoding="utf-8")
cards = re.findall(r'<div class="card">(.*?)</div>\s*<div class="meta">', src, flags=re.S)
names = ["bayline", "terrazzo", "coquina", "seawall-grid", "pool-edge", "mangrove", "benchmark", "ringling", "horizon", "conch"]
FONTS = {"f-bric": "Bricolage Grotesque, Archivo, sans-serif", "f-serif": "Newsreader, Georgia, serif", "f-mono": "DM Mono, Consolas, monospace",
         "f-geo": "Sora, sans-serif", "f-cond": "Barlow Condensed, Arial Narrow, sans-serif", "f-hum": "Instrument Sans, sans-serif",
         "f-slab": "Zilla Slab, Rockwell, serif", "f-disp": "Bricolage Grotesque, sans-serif"}
def fix(svg):
    for k, v in FONTS.items():
        svg = svg.replace(f'class="{k}"', f'font-family="{v}"')
    return svg.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
n = 0
for i, (card, name) in enumerate(zip(cards, names), start=1):
    svgs = re.findall(r"<svg.*?</svg>", card, flags=re.S)
    labels = ["horizontal-light", "horizontal-dark", "square", "favicon-32", "favicon-16"]
    for svg, label in zip(svgs, labels):
        (OUT / f"{i:02d}-{name}-{label}.svg").write_text(fix(svg), encoding="utf-8"); n += 1
print(n, "svg files written to", OUT)
