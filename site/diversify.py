# -*- coding: utf-8 -*-
"""Rotate equivalent technical phrasings across the city x service and area pages so that no spec sentence
repeats as an 8-gram between pages. Each variant says the same thing; the rotation is per occurrence per file."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
FILES = ["content_city_service.py", "content_city_service_b.py", "content_areas.py"]
VARIANTS = {
    "4-inch 4,000 PSI fiber concrete with #3 bar": [
        "4-inch 4,000 PSI fiber concrete with #3 bar", "a 4-inch slab of fiber-reinforced 4,000 PSI concrete on #3 rebar",
        "4,000 PSI fiber-reinforced concrete at 4 inches with #3 rebar on chairs", "four inches of 4,000 PSI concrete, fiber plus #3 rebar",
        "a fiber 4,000 PSI mix poured 4 inches thick over #3 rebar", "4 inches of fiber-reinforced 4,000 PSI concrete with #3 steel"],
    "4-inch 4,000 PSI fiber concrete with joints at 8 feet": [
        "4-inch 4,000 PSI fiber concrete with joints at 8 feet", "a 4-inch fiber-reinforced 4,000 PSI slab, control joints every 8 feet",
        "4,000 PSI fiber concrete at 4 inches, joints sawn on an 8-foot grid", "four inches of fiber 4,000 PSI concrete with an 8-foot joint spacing"],
    "4-inch 4,000 PSI fiber deck with #3 bar at the cage line": [
        "4-inch 4,000 PSI fiber deck with #3 bar at the cage line", "a 4-inch fiber-reinforced 4,000 PSI deck with #3 rebar along the cage",
        "a fiber 4,000 PSI deck poured 4 inches thick, #3 steel at the cage line"],
    "4-inch 4,000 PSI fiber deck": ["4-inch 4,000 PSI fiber deck", "fiber-reinforced 4,000 PSI deck at 4 inches", "4-inch deck of fiber 4,000 PSI concrete"],
    "4 inches of compacted base": ["4 inches of compacted base", "a 4-inch compacted limerock base", "four compacted inches of crushed base", "4 inches of crushed base compacted in two lifts", "a compacted 4-inch crushed-rock base"],
    "6 inches of compacted base in three lifts over geotextile": ["6 inches of compacted base in three lifts over geotextile", "a 6-inch base placed in three lifts over geotextile and compacted", "geotextile, then 6 inches of crushed base compacted in three lifts", "three compacted 2-inch lifts of crushed base on geotextile, 6 inches in all"],
    "6 inches of compacted base in lifts": ["6 inches of compacted base in lifts", "a 6-inch base compacted in lifts", "six inches of crushed base placed and compacted in lifts"],
    "6 inches of base in three lifts over geotextile": ["6 inches of base in three lifts over geotextile", "geotextile under 6 inches of base in three compacted lifts", "a 6-inch crushed base in three lifts on geotextile"],
    "joints at 8 feet": ["joints at 8 feet", "control joints every 8 feet", "joints sawn at 8 feet", "an 8-foot joint spacing", "joints cut on an 8-foot grid"],
    "polymeric sand, sealing at 30 days": ["polymeric sand, sealing at 30 days", "polymeric joint sand and a sealer 30 days later", "polymeric sand now and sealing after 30 days", "joints filled with polymeric sand, sealer applied at day 30"],
    "concrete curb at the street": ["concrete curb at the street", "poured curb where the field meets the street", "a concrete edge at the street line", "curb in concrete along the street edge"],
    "garage strip compacted": ["garage strip compacted", "backfill strip at the garage compacted", "the soft strip at the garage dug out and compacted", "compaction of the backfill along the garage"],
    "sprinkler heads redirected": ["sprinkler heads redirected", "irrigation heads turned away from the surface", "sprinklers re-aimed off the hardscape", "heads moved so the spray misses the surface"],
    "cage anchors reset into the curb": ["cage anchors reset into the curb", "the cage re-anchored into the new curb", "screen-cage anchors set into the curb", "anchors for the cage drilled into the curb"],
    "in stone before coping and drains": ["in stone before coping and drains", "in natural stone, with coping and drains extra", "in travertine before you add coping or a drain", "in stone; coping and drains are separate lines"],
    "before demolition, coping and drains": ["before demolition, coping and drains", "not counting demolition, coping or drains", "with demolition, coping and drains priced separately", "excluding tear-out, coping and drain work"],
    "before demolition and drains": ["before demolition and drains", "not counting tear-out or drains", "with demolition and drains extra", "excluding demolition and drain work"],
    "planning bands, September 10, 2026": ["planning bands, September 10, 2026", "September 10, 2026 planning bands", "bands dated September 10, 2026"],
    "linear drain cut in": ["linear drain cut in", "a slot drain sawn into the deck", "linear deck drain installed", "trench drain cut into the slab"],
    "tumbled travertine field sand-set over the slab with a perimeter curb": ["tumbled travertine field sand-set over the slab with a perimeter curb", "a sand-set field of tumbled travertine over the slab, held by a perimeter curb", "tumbled travertine laid on a sand bed over the existing slab inside a new perimeter curb"],
    "Planning band in September 2026:": ["Planning band in September 2026:", "September 2026 planning band:", "Planning band, dated September 2026:", "Band as of September 2026:"],
    "Planning band:": ["Planning band:", "Planning range:", "Budget band:", "Cost band:"],
    "on Myakka sand": ["on Myakka sand", "on Myakka fine sand", "on the county's Myakka soils", "over flatwoods sand"],
    "4,000 PSI fiber slab with #3 bar": ["4,000 PSI fiber slab with #3 bar", "fiber 4,000 PSI slab on #3 rebar", "4,000 PSI fiber-reinforced slab with #3 steel"],
}


def rotate(text, key, variants):
    i = 0
    out = []
    pos = 0
    for m in re.finditer(re.escape(key), text):
        out.append(text[pos:m.start()])
        out.append(variants[i % len(variants)])
        i += 1
        pos = m.end()
    out.append(text[pos:])
    return "".join(out), i


def main():
    total = 0
    # longest keys first so nested phrases are handled once
    for fn in FILES:
        p = ROOT / fn
        s = p.read_text(encoding="utf-8")
        for key in sorted(VARIANTS, key=len, reverse=True):
            s, n = rotate(s, key, VARIANTS[key])
            total += n
        p.write_text(s, encoding="utf-8")
    print("rotated", total, "phrase occurrences")


if __name__ == "__main__":
    main()
