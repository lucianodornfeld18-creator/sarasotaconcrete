# -*- coding: utf-8 -*-
"""Rasterize the provisional Bayline mark into the PNG/ICO assets the site references.
Uses Playwright (headless Chromium) for SVG -> PNG and Pillow for favicon.ico."""
import pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
BRAND = ROOT / "static" / "brand"
BRAND.mkdir(parents=True, exist_ok=True)

ICON = ('<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0F4C81"/>'
        '<g fill="none" stroke="#F7F4EE" stroke-width="4" stroke-linecap="round"><path d="M12 22c7-6 13-6 20 0s13 6 20 0"/>'
        '<path d="M12 33c7-6 13-6 20 0s13 6 20 0"/><path d="M12 44c7-6 13-6 20 0s13 6 20 0"/></g></svg>')
FAV = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0F4C81"/>'
       '<g fill="none" stroke="#F7F4EE" stroke-width="7" stroke-linecap="round"><path d="M12 26c7-6 13-6 20 0s13 6 20 0"/><path d="M12 44c7-6 13-6 20 0s13 6 20 0"/></g></svg>')
SOCIAL = ('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#F7F4EE"/>'
          + "".join(f'<path d="M0 {y}c140-40 280-40 420 0s280 40 420 0 280-40 420 0" fill="none" stroke="#0F4C81" stroke-width="2" opacity="{0.9 - i*0.08:.2f}"/>' for i, y in enumerate(range(80, 630, 60)))
          + '<rect x="90" y="220" width="120" height="120" rx="24" fill="#0F4C81"/><g fill="none" stroke="#F7F4EE" stroke-width="8" stroke-linecap="round" transform="translate(90 220) scale(1.875)">'
          '<path d="M12 22c7-6 13-6 20 0s13 6 20 0"/><path d="M12 33c7-6 13-6 20 0s13 6 20 0"/><path d="M12 44c7-6 13-6 20 0s13 6 20 0"/></g>'
          '<text x="240" y="290" font-family="Bricolage Grotesque, Arial, sans-serif" font-weight="800" font-size="84" fill="#14202B">Sarasota Concrete</text>'
          '<text x="244" y="345" font-family="Bricolage Grotesque, Arial, sans-serif" font-weight="600" font-size="28" letter-spacing="8" fill="#0F4C81">CONCRETE · PAVERS · POOL DECKS</text>'
          '<text x="244" y="400" font-family="Instrument Sans, Arial, sans-serif" font-size="26" fill="#3B4854">Sarasota County and the Charlotte County coast</text></svg>')


def main():
    (BRAND / "favicon.svg").write_text(FAV, encoding="utf-8")
    (BRAND / "icon.svg").write_text(ICON.format(s=512), encoding="utf-8")
    (BRAND / "social.svg").write_text(SOCIAL, encoding="utf-8")
    from playwright.sync_api import sync_playwright
    fonts = (ROOT / "static" / "fonts").resolve().as_uri()
    css = (f"@font-face{{font-family:'Bricolage Grotesque';src:url({fonts}/bricolage-normal-400-800-latin.woff2) format('woff2');font-weight:400 800}}"
           f"@font-face{{font-family:'Instrument Sans';src:url({fonts}/instrument-normal-400-700-latin.woff2) format('woff2');font-weight:400 700}}"
           "body{margin:0;background:transparent}")
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for name, svg, w, h in [("icon-512", ICON.format(s=512), 512, 512), ("icon-192", ICON.format(s=192), 192, 192), ("social-1200", SOCIAL, 1200, 630)]:
            page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            page.set_content(f"<style>{css}</style>{svg}")
            page.wait_for_timeout(300)
            page.screenshot(path=str(BRAND / f"{name}.png"), omit_background=(name != "social-1200"))
            page.close()
        b.close()
    im = Image.open(BRAND / "icon-512.png")
    im.save(ROOT / "static" / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print("brand assets written")


if __name__ == "__main__":
    main()
