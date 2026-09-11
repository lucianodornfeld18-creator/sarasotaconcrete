# -*- coding: utf-8 -*-
"""Photo pipeline for sarasotaconcrete.com (same discipline as the Groveland pipeline):
EXIF transpose, optional crop (signage/overlays), strip metadata, master JPEG <= 2400px,
WebP 480/960/1600 into site/static/images, photos.json manifest.

Alt text never claims a city the photo is not from (the provider photos come from
Central Florida jobs and are described by what is visible, not by location).
Renderings are labelled kind="rendering" and shown with a visible badge on the site.
"""
import json
import pathlib

from PIL import Image, ImageOps
from alts import ALTS

ROOT = pathlib.Path(__file__).resolve().parent
SRC = pathlib.Path(r"C:\Users\luana\Projetos\Concreto Fotos")
OUT = ROOT.parent / "site" / "static" / "images"
OUT.mkdir(parents=True, exist_ok=True)

# slug, source file, services, kind, alt, crop (left, top, right, bottom as fractions) or None
PHOTOS = [
    ("charcoal-slate-texture-pavers-detail", "IMG_1966.jpeg", ["pavers-driveways", "pavers-patios-lanais"], "real",
     "Close-up of charcoal slate-texture concrete pavers with a soldier-course border, showing joint alignment and surface relief", None),
    ("gray-paver-driveway-charcoal-grid-border", "IMG_2877.jpeg", ["pavers-driveways"], "real",
     "Wide gray paver driveway with a charcoal grid and border pattern running from the street to a two-car garage", None),
    ("paver-clad-entry-pillar-with-light", "IMG_2879.jpeg", ["pavers-driveways", "pavers-outdoor-lighting"], "real",
     "Paver-clad driveway entry pillar with a wall-mounted light, matching the gray and charcoal paver driveway behind it", None),
    ("gray-charcoal-paver-driveway-garage-approach", "IMG_2882.jpeg", ["pavers-driveways", "pavers-walkways-steps"], "real",
     "Gray paver driveway with charcoal banding leading to a dark two-car garage, with a matching paver walkway alongside", None),
    ("marble-pool-coping-and-deck-detail", "IMG_4183.jpeg", ["pavers-marble-porcelain", "pavers-pool-decks"], "real",
     "Bullnose marble pool coping and matching marble deck pavers around a curved pool edge", None),
    ("marble-paver-lanai-pool-deck", "IMG_4204.jpeg", ["pavers-pool-decks", "pavers-marble-porcelain"], "real",
     "Screened lanai with a full marble paver pool deck, a deck drain channel, and a freeform pool with a rock waterfall", None),
    ("paver-driveway-installation-in-progress", "IMG_4455.jpeg", ["pavers-driveways", "pavers-repair-storm-restoration"], "real",
     "Paver driveway installation in progress with stacked pavers staged on the screeded bedding layer and the crew setting the field", None),
    ("paver-driveway-bedding-and-edge-line", "IMG_4457.jpeg", ["pavers-driveways"], "real",
     "Stacked pavers staged along a driveway during installation, showing the leveled bedding layer and the edge line against the lawn", None),
    ("travertine-look-paver-pool-deck-square-pool", "IMG_5036.jpeg", ["pavers-pool-decks", "pavers-travertine-shellstone"], "real",
     "Tumbled travertine-look paver pool deck with a deck drain around a rectangular pool under mature oaks", None),
    ("large-format-paver-patio-gravel-joints", "CONCRETE PATIO DAVENPORT.jpeg", ["pavers-patios-lanais"], "real",
     "Backyard patio built from large square concrete pavers set on a compacted base with gravel-filled joints", None),
    ("raised-paver-terrace-stone-wall-pergola", "CONCRETE SERVICE IN KISSIMMEE.png", ["pavers-patios-lanais", "pavers-retaining-walls-outdoor-living"], "real",
     "Raised curved terrace with large-format pavers, a stone-veneer seat wall face, and a cedar pergola on a lakefront home", None),
    ("multi-level-paver-patio-pool-terrace-under-construction", "PAVER PATIO DAVENPORT.jpeg", ["pavers-patios-lanais", "pavers-retaining-walls-outdoor-living"], "real",
     "Multi-level paver patio under construction with a raised pool terrace, paver-faced step risers and a wet-cut saw on site", None),
    ("paver-patio-under-pergola", "PAVER DECK WINDERMERE.jpeg", ["pavers-patios-lanais"], "real",
     "Large paver patio in a tumbled tan blend under a dark-stained wood pergola behind a single-story home", None),
    ("mixed-tone-paver-driveway-two-car-garage", "PAVER DRIVEWAY OCOEE.jpeg", ["pavers-driveways"], "real",
     "Mixed gray, tan and terracotta paver driveway in a random-ashlar pattern in front of a two-car garage", None),
    ("tan-paver-driveway-meeting-concrete-apron", "PAVER DRIVEWAY WINTER GARDEN.jpeg", ["pavers-driveways", "concrete-driveways"], "real",
     "Tan blend paver driveway meeting a poured concrete apron at the street, in front of a two-car garage", None),
    ("tan-gray-paver-driveway-random-pattern", "WhatsApp Image 2026-04-09 at 2.41.37 PM (1).jpeg", ["pavers-driveways"], "real",
     "Tan and gray blend paver driveway in a random pattern, with solar path lights along the lawn edge", None),
    ("concrete-paver-side-yard-patio", "73e2a25b-5b8e-46ff-bde0-1d8f71df2bb7.jpeg", ["pavers-patios-lanais", "concrete-patios-lanais"], "real",
     "Side-yard patio of large square concrete pavers on a gravel bed with open joints beside a single-story home", None),
    ("poured-concrete-entry-steps-porcelain-treads", "6BAF8FC5-7847-4205-9DB7-6987FBE91485.png", ["concrete-sidewalks-walkways", "pavers-marble-porcelain"], "real",
     "Poured concrete front entry steps finished with large-format porcelain paver treads and stucco cheek walls", None),
    ("tan-paver-front-walkway-concept", "PAVER CONCRETE OCOEE.jpeg", ["pavers-walkways-steps"], "rendering",
     "Concept rendering of a tan paver front walkway with a soldier-course border leading to a covered entry", None),
    ("curved-paver-driveway-charcoal-border-concept", "PAVER DRIVEWAY FOUR CORNERS.jpeg", ["pavers-driveways"], "rendering",
     "Concept rendering of a curved tan paver driveway with a charcoal border in front of a tile-roof home", None),
    ("curved-paver-driveway-aerial-concept", "PAVER DRIVEWAY KISSIMMEE.jpeg", ["pavers-driveways"], "rendering",
     "Aerial concept rendering of a curved paver driveway with a dark border between two oak trees", None),
    ("brick-tone-paver-walkway-running-bond-concept", "PAVER DRIVEWAY WINTER GARDEN (2).jpeg", ["pavers-walkways-steps"], "rendering",
     "Concept rendering of a brick-tone paver walkway in running bond with a border course leading to a front door", None),
    ("small-paver-patio-bistro-concept", "PAVER IN APOPKA.jpeg", ["pavers-patios-lanais"], "rendering",
     "Concept rendering of a small tan paver patio with a bistro set beside a wood privacy fence", None),
    ("paver-entry-courtyard-planting-beds-concept", "PAVER RENOVATION OCOEE.jpeg", ["pavers-walkways-steps", "pavers-patios-lanais"], "rendering",
     "Concept rendering of a paver entry courtyard and walkway with planting beds cut into the field", None),
    ("paver-walkway-recessed-step-lights-dusk-concept", "PAVERS WALKWAY WINTER GARDEN.jpeg", ["pavers-walkways-steps", "pavers-outdoor-lighting"], "rendering",
     "Concept rendering of a gray paver walkway and entry step with recessed lights at dusk", None),
    ("curved-paver-steps-riser-lighting-concept", "PAVERS WITH LIGHT WINDERMERE.jpeg", ["pavers-walkways-steps", "pavers-outdoor-lighting"], "rendering",
     "Concept rendering of curved paver entry steps with integrated riser lighting and a winding walkway", None),
]


def main():
    manifest = []
    for slug, src, services, kind, alt, crop in PHOTOS:
        p = SRC / src
        if not p.exists():
            print("MISSING", src)
            continue
        im = ImageOps.exif_transpose(Image.open(p))
        if im.mode in ("RGBA", "LA", "P"):
            rgba = im.convert("RGBA")
            bg = Image.new("RGB", rgba.size, (255, 255, 255))
            bg.paste(rgba, mask=rgba.split()[-1])
            im = bg
        elif im.mode != "RGB":
            im = im.convert("RGB")
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        master = im.copy()
        master.thumbnail((2400, 2400), Image.LANCZOS)
        # Saving without exif= drops every metadata block (GPS, device, timestamps).
        master.save(ROOT / f"{slug}-sarasota-concrete.jpg", "JPEG", quality=88, optimize=True)
        sizes = {}
        for w in (1600, 960, 480):
            v = im.copy()
            v.thumbnail((w, w), Image.LANCZOS)
            v.save(OUT / f"{slug}-{w}.webp", "WEBP", quality=80, method=6)
            sizes[w] = v.size
        manifest.append({"slug": slug, "services": services, "kind": kind, "alt": ALTS.get(slug, alt),
                         "source": src, "w": sizes[1600][0], "h": sizes[1600][1]})
        print("OK", slug, sizes[1600])
    (ROOT / "photos.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(len(manifest), "photos")


if __name__ == "__main__":
    main()
