# -*- coding: utf-8 -*-
"""Browser QA with Playwright against a local server of dist/: console errors, horizontal overflow at
360/390/768/1440 widths, tool scripts producing output, nav toggle working, screenshots for the report."""
import pathlib
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent
DIST = ROOT / "dist"
SHOTS = ROOT / "qa-screenshots"
SHOTS.mkdir(exist_ok=True)
PORT = 8765
PAGES = ["/", "/concrete/pool-decks/", "/pavers/pool-decks/siesta-key/", "/areas/longboat-key/", "/permits/flood-zones-50-percent-rule/",
         "/pricing/pool-decks/", "/tools/coastal-surface-selector/", "/tools/permit-flood-setback-finder/", "/tools/concrete-paver-calculator/",
         "/tools/pour-calendar/", "/coastal/pool-deck-surface-temperature-study/", "/contact/", "/guides/ask-the-estimator/"]
VIEWPORTS = [(360, 800), (390, 844), (768, 1024), (1440, 900)]


def main():
    server = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1", "--directory", str(DIST)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1.5)
    problems = []
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            for w, h in VIEWPORTS:
                ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
                page = ctx.new_page()
                errors = []
                page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e: errors.append(str(e)))
                for route in PAGES:
                    errors.clear()
                    page.goto(f"http://127.0.0.1:{PORT}{route}", wait_until="load")
                    page.wait_for_timeout(250)
                    sw = page.evaluate("document.documentElement.scrollWidth")
                    if sw > w + 1:
                        problems.append(f"{w}px {route}: horizontal overflow scrollWidth={sw}")
                    if errors:
                        problems.append(f"{w}px {route}: console {errors[:2]}")
                    if "/tools/" in route and route != "/tools/":
                        out = page.locator(".out").first.inner_text()
                        if len(out) < 40 or "Choose" in out and "updates" in out:
                            problems.append(f"{w}px {route}: tool produced no output ({out[:40]!r})")
                    if w == 360 and route == "/":
                        page.click("#navToggle")
                        page.wait_for_timeout(150)
                        if not page.locator("#primaryNav.open").count():
                            problems.append("360px nav toggle did not open")
                    if w in (390, 1440):
                        page.screenshot(path=str(SHOTS / f"{w}{route.strip('/').replace('/', '_') or 'home'}.png"), full_page=(route == "/"))
                ctx.close()
            b.close()
    finally:
        server.terminate()
    print(f"{len(PAGES)} pages x {len(VIEWPORTS)} viewports; {len(problems)} problems")
    for p in problems:
        print("  -", p)
    (ROOT / "qa-browser-report.txt").write_text("\n".join(problems) or "no problems", encoding="utf-8")


if __name__ == "__main__":
    main()
