# -*- coding: utf-8 -*-
"""Rasterises the brand assets the site references, from the owner's logo.

Priority: if ../brand/owner-logo/logo-full.png exists (the original artwork the owner supplied),
it is used for the social card and the 512 icon. Otherwise the flat SVG derivative is used, so the
build never depends on a binary that may not be on disk.
"""
import pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
BRAND = ROOT / "static" / "brand"
BRAND.mkdir(parents=True, exist_ok=True)
OWNER = ROOT.parent / "brand" / "owner-logo"

GOLD, GOLD_LT, GRAPHITE, INK, PAPER = "#C1922E", "#E0BC63", "#2E2E30", "#1F1F1F", "#FFFFFF"
HEX_OUTER = "M32.00,4.00 L56.25,18.00 L56.25,46.00 L32.00,60.00 L7.75,46.00 L7.75,18.00 Z"
HEX_INNER = "M32.00,13.50 L48.02,22.75 L48.02,41.25 L32.00,50.50 L15.98,41.25 L15.98,22.75 Z"
S_RIBBON = "M41.5,20.5 H26.5 a5.5,5.5 0 0 0 0,11 H37.5 a5.5,5.5 0 0 1 0,11 H22.5"


def mark(size=512, gold=GOLD, dark=GRAPHITE):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 64 64">'
            f'<defs><clipPath id="u"><path d="M0,0 H64 V32 H0 Z"/></clipPath>'
            f'<clipPath id="l"><path d="M0,32 H64 V64 H0 Z"/></clipPath></defs>'
            f'<path d="{HEX_OUTER} {HEX_INNER}" fill="{dark}" fill-rule="evenodd" clip-path="url(#l)"/>'
            f'<path d="{HEX_OUTER} {HEX_INNER}" fill="{gold}" fill-rule="evenodd" clip-path="url(#u)"/>'
            f'<path d="{S_RIBBON}" fill="none" stroke="{gold}" stroke-width="6.5" stroke-linecap="square"/></svg>')


FAVICON = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           f'<path d="M32,2 L58,17 L58,47 L32,62 L6,47 L6,17 Z" fill="{GRAPHITE}"/>'
           f'<path d="M42,20 H26 a6,6 0 0 0 0,12 H38 a6,6 0 0 1 0,12 H22" fill="none" stroke="{GOLD}" '
           f'stroke-width="8" stroke-linecap="square"/></svg>')


def social():
    lattice = "".join(
        f'<path d="M{x},{y} l30,-17 l30,17 l0,34 l-30,17 l-30,-17 Z" fill="none" stroke="{GOLD}" '
        f'stroke-width="1.4" opacity="{max(0.05, 0.30 - row * 0.055):.2f}"/>'
        for row, y in enumerate(range(-20, 660, 51))
        for x in range(-30 + (30 if row % 2 else 0), 1240, 60))
    m = mark(180).split(">", 1)[1].rsplit("</svg>", 1)[0]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">'
            f'<rect width="1200" height="630" fill="{PAPER}"/>{lattice}'
            f'<g transform="translate(510,64) scale(2.8)">{m}</g>'
            f'<text x="600" y="404" text-anchor="middle" font-family="Archivo, Arial Black, sans-serif" '
            f'font-weight="900" font-size="86" fill="{INK}">SARASOTA</text>'
            f'<text x="600" y="452" text-anchor="middle" font-family="Archivo, Arial, sans-serif" '
            f'font-weight="600" font-size="34" letter-spacing="19" fill="{GOLD}">CONCRETE</text>'
            f'<text x="600" y="512" text-anchor="middle" font-family="Instrument Sans, Arial, sans-serif" '
            f'font-size="25" letter-spacing="3" fill="#4A4842">SOLID FOUNDATIONS. BEAUTIFUL SPACES.</text>'
            f'<text x="600" y="566" text-anchor="middle" font-family="Instrument Sans, Arial, sans-serif" '
            f'font-size="22" fill="#63615C">Sarasota County and the Charlotte County coast</text></svg>')


def main():
    (BRAND / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (BRAND / "icon.svg").write_text(mark(512), encoding="utf-8")
    (BRAND / "social.svg").write_text(social(), encoding="utf-8")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for name, svg, w, h in [("icon-512", mark(512), 512, 512), ("icon-192", mark(192), 192, 192),
                                ("social-1200", social(), 1200, 630)]:
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            pg.set_content(f"<style>body{{margin:0;background:transparent}}</style>{svg}")
            pg.wait_for_timeout(250)
            pg.screenshot(path=str(BRAND / f"{name}.png"), omit_background=(name != "social-1200"))
            pg.close()
        b.close()
    original = OWNER / "logo-full.png"
    if original.exists():
        im = Image.open(original).convert("RGBA")
        sq = im.copy(); sq.thumbnail((512, 512), Image.LANCZOS)
        canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
        canvas.paste(sq, ((512 - sq.width) // 2, (512 - sq.height) // 2), sq)
        canvas.save(BRAND / "icon-512.png")
        card = Image.new("RGB", (1200, 630), (255, 255, 255))
        art = im.copy(); art.thumbnail((980, 470), Image.LANCZOS)
        card.paste(art, ((1200 - art.width) // 2, (630 - art.height) // 2), art)
        card.save(BRAND / "social-1200.png", quality=92)
        print("used the owner's original artwork for icon-512 and social-1200")
    else:
        print("owner original not found at", original, "- using the flat SVG derivative")
    Image.open(BRAND / "icon-512.png").save(ROOT / "static" / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("brand assets written to", BRAND)


if __name__ == "__main__":
    main()
