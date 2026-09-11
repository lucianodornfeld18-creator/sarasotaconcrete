# -*- coding: utf-8 -*-
"""One extra, locality-specific section per page for the Tier 1 city hubs that sit close to the
St. Cloud word floor.

These exist because shortening the lead form (four fields in the hero, and four questions dropped
from the long form) removed roughly sixty words of label text from every page that embeds a form,
which pushed the thinnest locality pages under their floor. Rather than pad, each block below is an
operational fact about that one place: how a truck reaches it, what the platting left behind, what
the drainage basin does. Nothing here repeats between pages.
"""
from _h import sec, p, ul, table, link

D = {}

D["/areas/osprey/"] = sec("Getting a truck and a delivery onto Casey Key",
    p("Osprey's mainland streets are ordinary work. Casey Key is not, and the reason is one bridge. "
      "The Blackburn Point Bridge is a single-lane swing bridge, weight restricted and hand-operated "
      "for boat traffic, and it is the only crossing at the north end of the key. The south end "
      "connects through Nokomis at Albee Road. Everything about scheduling a pour or a pallet "
      "delivery on the key follows from that.")
    + ul([
        "<strong>Ready-mix is staged, not queued.</strong> A loaded mixer has a working window before the "
        "concrete is unusable, and that window does not survive a bridge opening plus a single-lane wait. "
        "Pours on the key are booked as the first delivery of the morning.",
        "<strong>Pallets come in smaller loads.</strong> Paver pallets are split across more trips rather "
        "than one heavy truck, which is why island paver work carries the five to fifteen percent logistics "
        "line that shows up on the estimate.",
        "<strong>Staging space is the real constraint.</strong> Key lots are narrow and deep with no verge, "
        "so the base material and the pallets sit where the finished surface will go, and the sequence has "
        "to be planned around that rather than improvised.",
    ])
    + p("None of this makes the work harder to build. It makes it slower to schedule, and an estimate that "
        "has not accounted for it will slip."))

D["/areas/palmer-ranch/"] = sec("Lakes, easements and the district that owns the drainage",
    p("Palmer Ranch was master-planned around a stormwater system, and a large share of its lots back onto "
      "a lake, a pond or a preserve. Two things follow that do not apply to an ordinary infill lot.")
    + p("The first is the drainage easement. The strip between the rear property line and the water is "
        "normally a maintenance and drainage easement, and it belongs to the district or the association "
        "for access even though it sits inside your deed. Hardscape placed in it can be required to come "
        "out at the owner's cost, and no permit protects you from that, because the easement is a private "
        "encumbrance rather than a zoning rule. The survey from your closing shows it. It is the first "
        "document to look at before a patio extension is drawn toward the water.")
    + p("The second is the control elevation. A lot that drains to a lake has a designed flow path across "
        "the rear yard, and a slab or a paver field that interrupts it moves water to a neighbour. That is "
        "the mechanism behind most rear-yard drainage complaints in communities of this vintage, and it is "
        "why a slope arrow and a note on where runoff goes belong on the ARC drawing even when the committee "
        "does not ask for them."))

D["/areas/nokomis/"] = sec("New fill settles, and the first three years tell you how much",
    p("The communities east of Interstate 75 were built on imported fill placed to raise the pads above the "
      "surrounding flatwoods. Fill is better bearing ground than native saturated sand, which is why those "
      "lots build well. What fill also does is consolidate, and the rate depends entirely on how it was "
      "placed and compacted by the developer years before anybody poured a driveway.")
    + table(["Age of the home", "What is usually found", "What it means for hardscape"], [
        ["Under 3 years", "Fill still consolidating; hairline settlement at the garage is common", "Check the builder's warranty before removing anything; a claim may cover it"],
        ["3 to 8 years", "Most consolidation done; any settlement is now localised", "Good window for a paver driveway; the base can be built to final grade"],
        ["Over 8 years", "Stable, except where a downspout or an irrigation leak keeps working on it", "Find the water first, then build"],
    ], "Fill age against hardscape decisions, communities east of I-75")
    + p("The practical point is that a paver driveway laid on developer fill still needs its own six inches "
        "of compacted base. The fill carries the house. It was never placed to the tolerance a finished "
        "surface needs, and treating it as a base is the most common shortcut in new-construction hardscape "
        "in this corridor."))

D["/areas/gulf-gate/"] = sec("What else is buried in a 1960s plat",
    p("Gulf Gate Estates was platted and built before the trenching standards most people assume. Under a "
      "sixty-year-old driveway, the things worth finding before a saw cuts anything are rarely on a drawing.")
    + ul([
        "<strong>Irrigation run shallow.</strong> Original lines and later repairs sit at a few inches rather "
        "than a foot, often directly under the slab, and they are located and re-run in sleeves rather than "
        "discovered by a breaker.",
        "<strong>Cable and phone laid across the front yard.</strong> Utility locates cover the primary "
        "services; the drop from the pedestal to the house is the homeowner's and is not marked.",
        "<strong>An older, smaller apron.</strong> Aprons from this era are narrower than the driveway behind "
        "them, so a replacement that matches the modern driveway width changes the right-of-way footprint and "
        "that is the part the county reviews.",
        "<strong>Tree roots from a canopy that grew up after the pour.</strong> The oaks along these streets "
        "were young in 1968. Their roots are now under the slab, and cutting them is regulated.",
    ])
    + p("A locate request and twenty minutes with a probe before demolition is the difference between a "
        "three-day job and a three-day job plus an irrigation repair and a utility call-out."))

D["/areas/englewood/"] = sec("Telling which county you are in, and why it changes the bill",
    p("Englewood is one community split by a county line, and the line does not follow a landmark anyone uses "
      "for directions. The practical consequence is that two houses on the same street can face different "
      "permit requirements and different fees for identical work.")
    + table(["", "Sarasota County side", "Charlotte County side"], [
        ["Permit for a patio slab", "Often below the threshold for an at-grade uncovered slab", "Required; all flatwork including pavers"],
        ["Permit for pavers", "Depends on the right-of-way and the footprint", "Always required, with inspections"],
        ["Notice of Commencement", "Per Florida lien law on the contract value", "Required above $5,000 before the first inspection"],
        ["Published fee schedule", "Culvert and right-of-way fees set by resolution", "Zoning $22, line and grade $310, slab review $22 or $90"],
        ["Counter", "County offices in Sarasota and Venice", "18500 Murdock Circle, Port Charlotte"],
    ], "The same job, two counties")
    + p(f'The parcel record settles it in a minute, and each side has its own page here: '
        f'{link("/permits/sarasota-county/", "Sarasota County")} and {link("/permits/charlotte-county/", "Charlotte County")}. '
        f'An estimate for an Englewood address should name the county on it. If it does not, the permit line '
        f'is a guess.'))

D["/areas/fruitville-bee-ridge/"] = sec("Phillippi Creek is the basin this whole area drains into",
    p("Everything from Fruitville Road south through Bee Ridge sheds water toward the Phillippi Creek system, "
      "and the creek is the reason inland lots here behave the way they do. The basin is flat, the outfall is "
      "slow, and the wet-season water table sits close to the surface across it.")
    + p("For hardscape that produces a specific failure pattern. A driveway or patio poured to no particular "
        "slope does not flood the lot in an ordinary afternoon storm; it holds a film of water at the low edge "
        "for hours, which keeps the base saturated through the wet season. Saturated sand under a slab loses "
        "bearing, fines migrate to the low point, and four or five years later there is a settled corner with "
        "no obvious cause. The cause was the grade.")
    + p("So the specification on this side of the county is about drainage rather than about salt. A minimum "
        "eighth of an inch per foot away from the structure, a defined path to a swale or a yard drain, and a "
        "base compacted in lifts so it does not pump. The Celery Fields regional stormwater facility at the "
        "north end of the basin handles the volume; getting water off your own lot to reach it is the part "
        "that belongs on the estimate."))

D["/areas/north-port/"] = sec("Two North Ports, one building department",
    p("The city covers more land than any other municipality in Sarasota County, and the work splits cleanly "
      "in two halves that share a single permit counter.")
    + table(["", "The GDC grid", "Wellen Park and the newer communities"], [
        ["Platted", "1950s to 1980s by General Development Corporation", "2010s onward"],
        ["Lots", "Roughly a quarter acre, on a street grid with roadside swales", "Master-planned, piped or lake drainage"],
        ["Typical job", "Driveway replacement with a culvert crossing, repair, pads", "Upgrading builder flatwork to pavers, lanai extensions"],
        ["The constraint", "The swale is the drainage system and the city sizes the culvert", "Architectural review and the builder's warranty period"],
        ["Ground", "Deep Immokalee and Myakka sands", "Imported fill over the same sands"],
    ], "North Port's two markets")
    + p("The same Right of Way Use Permit covers the crossing in both halves, and Public Works inspects the "
        "swale restoration in both. What differs is who else has to say yes: on the grid it is only the city, "
        "and in the newer communities the association reviews the material and the colour before the city ever "
        "sees the application."))

D["/areas/"] = sec("Drive time is part of the specification, not a detail",
    p("Forty miles on a map is not forty miles of scheduling. Three things stretch the distance on this coast, "
      "and each one changes how a job is booked rather than how it is built.")
    + ul([
        "<strong>Drawbridges and a swing bridge.</strong> Siesta Key is reached by the Siesta Drive or Stickney "
        "Point drawbridges, Longboat Key by the Ringling Causeway or the Longboat Pass bridge, Casey Key by the "
        "single-lane Blackburn Point swing bridge. A loaded mixer cannot wait out an opening, so island pours "
        "are the first delivery of the day.",
        "<strong>Season.</strong> From January through April the population of Sarasota County rises past "
        "570,000, and US-41 and the bridges carry it. The same drive is twenty minutes longer at 4 p.m. in "
        "February than in August.",
        "<strong>The southern edge.</strong> Port Charlotte, Rotonda West and Placida are 34 to 37 miles out and "
        "50 to 65 minutes each way, which is why four services are scheduled there rather than the full "
        "catalogue.",
    ])
    + p("This is why each locality page carries a drive time next to the distance, and why the estimate for an "
        "island address names the logistics line instead of burying it in the square-foot rate."))


def apply(pages):
    n = 0
    for pg in pages:
        block = D.get(pg["route"])
        if not block:
            continue
        html = pg["body_html"]
        marker = '<p class="reviewed">'
        i = html.rfind(marker)
        pg["body_html"] = (html[:i] + block + html[i:]) if i != -1 else (html + block)
        n += 1
    return n
