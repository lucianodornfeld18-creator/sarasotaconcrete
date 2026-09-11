# -*- coding: utf-8 -*-
"""One-off: shorten the titles the build flagged as > 65 characters (keyword first, city kept)."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent
FIX = {
    "content_pillars.py": [("Concrete Contractor in Sarasota, FL – Pool Decks, Driveways, Slabs", "Concrete Contractor in Sarasota, FL – Pool Decks & Driveways"),
                           ("Paver Installation in Sarasota, FL – Pool Decks, Travertine, Driveways", "Paver Installation in Sarasota, FL – Pool Decks & Driveways")],
    "content_areas.py": [("Concrete & Pavers in Venice, FL – City Permits, Island, Wellen Park", "Concrete & Pavers in Venice, FL – City Permits & Wellen Park")],
    "content_city_service_b.py": [("Concrete Driveways in Osprey, FL – Rivendell, Park Trace, Bay Street", "Concrete Driveways in Osprey, FL – Rivendell & Park Trace"),
                                  ("Paver Driveways in Nokomis, FL – Toscana Isles, Bellacina, Calusa Lakes", "Paver Driveways in Nokomis, FL – Toscana Isles & Bellacina"),
                                  ("Concrete Driveways in Nokomis & Laurel, FL – Sorrento East, Calusa Lakes", "Concrete Driveways in Nokomis & Laurel, FL – Sorrento East"),
                                  ("Concrete Slabs & Pads in North Port, FL – Boat, RV, Shed, Generator", "Concrete Slabs & Pads in North Port, FL – Boat, RV & Shed"),
                                  ("Concrete Driveways in Englewood, FL – Sarasota or Charlotte Permit", "Concrete Driveways in Englewood, FL – Which County Permits")],
    "content_pricing.py": [("Pool Deck Cost in Sarasota, FL (2026): Concrete, Pavers, Travertine", "Pool Deck Cost in Sarasota, FL (2026): Concrete vs Pavers")],
    "content_coastal.py": [("Salt and Concrete on the Sarasota Coast: Scaling, Spalling, Defense", "Salt and Concrete on the Sarasota Coast: Scaling & Spalling")],
    "content_guides.py": [("Snowbird Guide: Running a Sarasota Hardscape Job From Out of State", "Snowbird Guide: Sarasota Hardscape Jobs From Out of State")],
}
for fn, pairs in FIX.items():
    p = ROOT / fn
    s = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in s, (fn, a)
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8")
print("titles fixed")
