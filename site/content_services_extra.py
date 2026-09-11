# -*- coding: utf-8 -*-
"""Per-service 'scenarios we see most' and 'day by day' blocks, injected into the service pages before the FAQ.
Written per service; no shared sentences."""
from _h import sec, ul, ol, p

SCENARIOS = {
    "concrete-pool-decks": ("Three Sarasota decks and what each one needed", [
        "<strong>A 1968 Gulf Gate deck poured tight to the shell.</strong> No isolation joint, a 1990s cool-deck overlay lifting in sheets, hollow across a third of the field. Replacement, with a compressible joint at the coping and two drains, because an overlay would have followed the slab down.",
        "<strong>A 2004 Palmer Ranch deck with a good slab and a bad slope.</strong> Solid under the hammer, ponding at the far corner under the cage. One drain cut in and a light knockdown overlay; the slab stayed.",
        "<strong>A Siesta Key canal deck after Milton.</strong> Sounded hollow along 30 feet of seawall where surge had washed the base out. Even with a sound surface, that deck came out and went back as pavers on a rebuildable base.",
    ]),
    "concrete-driveways": ("Three Sarasota driveways and what each one needed", [
        "<strong>A 1959 west-of-Trail ribbon drive under a live oak.</strong> Roots had lifted the apron; the city protects the trunk. The root was bridged with a thickened section on compacted stone instead of cut, and the apron went in under the city's right-of-way permit.",
        "<strong>A 1996 Turtle Rock builder slab settled at the garage.</strong> The backfill strip against the footing had never been compacted. Eighteen inches dug out and compacted before the new base went down; the new slab was dowelled to the apron so it can't step.",
        "<strong>A 1986 North Port crossing over a crushed culvert.</strong> The driveway was the smaller job; the city sized a new pipe, the swale was regraded and inspected, and the slab followed.",
    ]),
    "concrete-patios-lanais": ("Three lanai jobs and what each one needed", [
        "<strong>A Talon Preserve extension beyond the builder cage.</strong> New slab poured beside the old on its own base, dowelled, pitched to a new floor drain, finish matched across both with a thin overlay so the joint reads as a line.",
        "<strong>A 1978 Meadows lanai pitched at the sliders.</strong> Sound slab, wrong slope. It came out anyway, because you can't tilt a slab, and went back with a drain at the cage edge.",
        "<strong>A downtown courtyard behind a Rosemary District townhouse.</strong> Fourteen by sixteen feet, wheelbarrow access only through the house, poured from a buggy in the alley at 7 a.m.",
    ]),
    "concrete-stamped": ("Three stamped jobs and what each one needed", [
        "<strong>A Bee Ridge patio in ashlar slate, light sand color.</strong> The owner wanted charcoal; the sample sat in the July sun for an hour and changed her mind. Matte sealer with grit because the patio wraps a spa.",
        "<strong>A Venice pool deck overlay stamped in a travertine pattern.</strong> Slab passed the six tests; a 3/8-inch stamped overlay gave the stone look at a third of the stone price, with the reseal date on the care sheet.",
        "<strong>A Palmer Ranch driveway border.</strong> Broom field, 18-inch stamped border in a cobble pattern; the sub-association approved the border color faster than it would have approved a full stamped driveway.",
    ]),
    "concrete-slabs": ("Three pads and what each one needed", [
        "<strong>A generator pad in South Venice after the 2024 outages.</strong> Poured to the manufacturer's template with the anchor bolts set in the wet concrete and a conduit sleeved through; the electrician's permit covered the pad.",
        "<strong>A boat-trailer pad on an acre off Lorraine Road.</strong> Six inches, #4 bar at 18 inches, a steel plate cast in at the tongue-jack point, raised 3 inches and sloped to the swale.",
        "<strong>An AC pad in Gulf Gate that had sunk on a precast block.</strong> Twenty minutes of demolition, a compacted subgrade, a 4-inch poured pad 3 inches above grade. The condenser stopped rattling.",
    ]),
    "concrete-sidewalks-walkways": ("Three walks and what each one needed", [
        "<strong>A Cherokee Park front walk lifted by an oak.</strong> Routed around the critical root zone with a gentle curve instead of cutting the root; the city's tree rule made the decision.",
        "<strong>A Venice Gardens side path to the pool equipment.</strong> Thirty inches wide, 4 inches thick, joints every 4 feet, cross-sloped so the pump pad stays dry.",
        "<strong>A Longboat Key entry with a landing at the door.</strong> Salt-mix concrete, penetrating sealer, and amber step lights because the beach can see the front of the house.",
    ]),
    "concrete-repair": ("Three repair calls and what each one needed", [
        "<strong>A Fruitville driveway settled at the garage.</strong> The gutter dumped onto the slab edge. Downspout extended, slab lifted with foam through eight holes, joints sealed. Not a new driveway.",
        "<strong>A Bird Key seawall-side slab scaling white.</strong> Salt spray on a wet-finished surface. Loose paste ground off, polymer-modified patch, penetrating sealer; the steel wasn't rusting yet, so the slab stayed.",
        "<strong>A 1966 Gulf Gate driveway in seven pieces.</strong> The owner asked for a lift. The honest answer was replacement, because there was no base to lift it onto.",
    ]),
    "concrete-resurfacing": ("Three resurfacing calls and what each one needed", [
        "<strong>A Stoneybrook deck with a peeling 2008 overlay.</strong> Solid, drained, threshold fine. Stripped, cracks routed, bond coat, light knockdown, matte sealer with grit. Two days of drying between coats.",
        "<strong>A Jacaranda West deck hollow at the coping.</strong> Failed the hammer test along 40 feet. No overlay; replacement with an isolation joint the original never had.",
        "<strong>A Wellen Park builder deck that ponded at the screen.</strong> The slab was fine; the water wasn't. A drain first, then the overlay.",
    ]),
    "concrete-architectural": ("Three architectural jobs and what each one needed", [
        "<strong>A Sapphire Shores entry with cantilevered steps.</strong> Board-formed cheek walls in cedar liners, honed treads, 2 inches of cover over the steel because the bay is a block away.",
        "<strong>A honed lanai floor that continues the living room.</strong> Integral light pigment, tight joints laid out in the design, ground to a matte 400 grit and sealed with a penetrating product.",
        "<strong>Cast planters along a Lido Key motor court.</strong> Poured in place with the driveway base, salt-mix, and a drainage weep at the bottom of each.",
    ]),
    "pavers-pool-decks": ("Three paver decks and what each one needed", [
        "<strong>A Country Club Shores travertine deck that stood in surge.</strong> Lifted, base rebuilt and flushed, concrete curb at the seawall, the owner switched the field to porcelain to end the annual coping seal.",
        "<strong>A Prestancia builder deck under a big cage.</strong> Passed the overlay tests; travertine sand-set over it with a perimeter curb, drain cut in at the low side, anchors reset into the curb.",
        "<strong>A Siesta condo common deck, phased.</strong> Half open while the other half was rebuilt, temporary edge at the phase line, May to August, board file updated with the sealing date.",
    ]),
    "pavers-travertine-shellstone": ("Three stone jobs and what each one needed", [
        "<strong>Travertine coping flaking on a Placida salt pool.</strong> Nobody had sealed it in five years. The worst pieces replaced, the rest sealed annually from then on, the field rinsed weekly.",
        "<strong>Shellstone on a Casey Key bay-side deck.</strong> Chosen for the fossil look and the wet grip; delivered over the swing bridge in four trips.",
        "<strong>Honed travertine lanai in Bay Isles.</strong> Filled and honed for a clean floor, neutral cleaners only on the care sheet.",
    ]),
    "pavers-marble-porcelain": ("Three marble and porcelain jobs and what each one needed", [
        "<strong>A Bird Key lanai in honed marble.</strong> Base re-screeded to an eighth of an inch, bullnose coping in the same stone, penetrating sealer.",
        "<strong>Porcelain over an engineered slab on an elevated Siesta rebuild.</strong> Mortar-set on the engineer's slab, R11 face, no sealer line on the care sheet.",
        "<strong>A Longboat Key owner who left travertine for porcelain.</strong> Salt pool, seasonal owner, no property manager. Porcelain needs nothing between visits.",
    ]),
    "pavers-driveways": ("Three paver driveways and what each one needed", [
        "<strong>A Toscana Isles builder driveway on developer fill.</strong> Six inches of base in three lifts over geotextile on top of the fill, because fill keeps settling and a driveway laid on it follows.",
        "<strong>A Sapphire Shores bungalow in clay brick.</strong> Running bond suited the 1948 house and passed historic review; the apron went in concrete to the city's detail.",
        "<strong>A Longboat Key motor court after Helene.</strong> Spiked restraint had floated. Concrete curbs on every edge the bay can reach, herringbone in a light coral blend.",
    ]),
    "pavers-patios-lanais": ("Three patio jobs and what each one needed", [
        "<strong>A Meadows villa lanai, sound but ponding.</strong> Linear drain first, then travertine sand-set with a perimeter curb and a bullnose step at the slider.",
        "<strong>A South Venice side yard beside the septic tank.</strong> Ten by fourteen feet of pavers on 4 inches of base, drawn around the drain field from the county's septic record.",
        "<strong>A Rosemary District courtyard with a tight threshold.</strong> Porcelain thin-set over the existing slab to keep the floor an inch below the door.",
    ]),
    "pavers-walkways-steps": ("Three walks and what each one needed", [
        "<strong>A Sarasota Springs front walk around a 1960s oak.</strong> Pavers bend where concrete can't; the path curved around the root zone and can be lifted later if a root heaves it.",
        "<strong>Entry steps in Osprey on a block core.</strong> Seven-inch risers, 11-inch treads, 1-inch overhang, riser lights wired in conduit before the treads went on.",
        "<strong>A Manasota Key beach path with amber lights.</strong> Fully shielded fixtures set low; Code Enforcement's night survey passed.",
    ]),
    "pavers-sealing": ("Three sealing calls and what each one needed", [
        "<strong>A Harbor Acres deck blushed white on the shaded side.</strong> A wet-look sealer over a damp base. Stripped, cleaned, re-sanded, resealed two weeks later with a breathable product.",
        "<strong>A Gulf of Mexico Drive condo after Milton.</strong> Fresh-water flush, a dry month, then re-sand and seal; the board wanted it done in July when the building was empty.",
        "<strong>A Fruitville driveway orange from the well.</strong> Oxalic cleaning, heads redirected, then a penetrating sealer so the next stains sit on top.",
    ]),
    "pavers-repair-storm-restoration": ("Three repair calls and what each one needed", [
        "<strong>A Sabal Drive deck that floated its restraint in Milton.</strong> Three weeks of drying, 260 square feet lifted, two voids rebuilt, concrete curb along 38 feet of seawall, original pavers reset.",
        "<strong>A Nokomis driveway sinking at one corner.</strong> A leaking irrigation line had emptied the base. Line fixed, 40 square feet lifted, base rebuilt, same pavers back.",
        "<strong>Weeds along one line of a Palmer Ranch patio.</strong> The line was a drainage path with no joint sand left. Cleaned, polymeric re-sand, and the downspout that fed it extended.",
    ]),
    "pavers-retaining-walls-outdoor-living": ("Three outdoor-living jobs and what each one needed", [
        "<strong>A seat wall around a Bee Ridge patio.</strong> Twenty inches high in segmental block, first course buried, cap adhered, drainage stone behind it where it held a grade change.",
        "<strong>A kitchen base on an Osprey lanai.</strong> Six-inch reinforced pad with gas and electric sleeves set before the pour, block frame, stone veneer, poured cap.",
        "<strong>A fire pit surround in Wellen Park.</strong> Gas, on a non-combustible base, with the cage clearance the manufacturer specifies and the ARC's approval for the height.",
    ]),
    "pavers-artificial-turf": ("Three turf jobs and what each one needed", [
        "<strong>A side yard in Palmer Ranch that never saw sun.</strong> Sod died twice; turf on 3 inches of compacted stone with a weed barrier, pitched to the swale, brushed twice a year.",
        "<strong>Turf bands between paver strips on a modern driveway.</strong> Permeable backing, nailer edge, silica infill; the pavers carry the cars, the turf carries the look.",
        "<strong>A pet run in North Port on well water.</strong> Rinsed weekly; the sprinklers were moved so iron didn't stain the fibers.",
    ]),
    "pavers-outdoor-lighting": ("Three lighting jobs and what each one needed", [
        "<strong>A Longboat Key motor court within sight of the beach.</strong> FWC-certified amber column lights, full cut-off, tested by Code Enforcement from the sand.",
        "<strong>Riser lights in Osprey entry steps.</strong> Conduit under the treads before the pavers went down; no cutting later.",
        "<strong>A Palmer Ranch path with brass fixtures.</strong> Powder-coated aluminum had pitted in three years; brass replaced it on the same transformer.",
    ]),
}

DAYS = {
    "concrete-pool-decks": ["Day 1: cage screens protected, old deck cut and hauled, subgrade exposed.", "Day 2: subgrade compacted, base placed and compacted, drains set, forms and isolation joint at the coping.", "Day 3, morning: pour, screed, float, texture; joints cut by afternoon.", "Days 4 to 7: cure protection, sealer once dry, cage re-anchored.", "Day 8 to 10: furniture back, care sheet handed over."],
    "concrete-driveways": ["Day 1: demolition and haul-off; irrigation located and capped.", "Day 2: garage strip compacted, base placed in lifts, forms and rebar on chairs; apron formed to the jurisdiction's detail.", "Day 3, morning: pour and finish; joints cut the same afternoon.", "Days 4 to 9: cure; cars off the slab until day 7.", "Day 10 and on: heavy vehicles after day 28."],
    "concrete-patios-lanais": ["Day 1: layout, excavation or slab prep, base compacted, forms set.", "Day 2, morning: pour, finish, joints cut.", "Days 3 to 4: cure, furniture back after day 3.", "Day 7: cage or roof anchors, if any."],
    "concrete-stamped": ["Day 1: base, forms, color plan confirmed against the sample.", "Day 2, morning: pour, color hardener, release, stamping in the two-hour window.", "Day 3: release washed, joints checked.", "Days 4 to 7: sealer once dry, matte with grit around water.", "Day 8: furniture back."],
    "concrete-slabs": ["Morning: subgrade dug and compacted, base placed, forms and anchor template set.", "Same day: pour and finish; small pads are one-day jobs.", "Day 7: shed or equipment on; day 28 for a spa."],
    "concrete-sidewalks-walkways": ["Day 1: layout around trees, excavation, base, forms.", "Day 2, morning: pour from a buggy, broom finish, joints tooled.", "Day 3: walk on it."],
    "concrete-repair": ["Visit 1: level, hammer and hose; cause named in writing.", "Visit 2: water fixed (downspout, sprinkler, swale) and the repair done, often the same day.", "Follow-up: a photo after the next heavy rain, from you or from us."],
    "concrete-resurfacing": ["Day 1: pressure-wash, profile, crack and spall repairs.", "Day 2: bond coat and overlay, textured while plastic.", "Day 3: dry day.", "Day 4: sealer.", "Day 5 to 6: furniture back, pool splash allowed."],
    "concrete-architectural": ["Week 1: design confirmed, form liners and forms built on site.", "Week 2: staged pours, each element cured before the next is formed against it.", "Week 3: honing after 7 days, sealing, cleanup."],
    "pavers-pool-decks": ["Day 1: demolition and haul-off.", "Day 2: subgrade, geotextile, base in lifts, drain set.", "Day 3: coping mortar-set on the beam; curbs poured at the cage line and exposed edges.", "Days 4 to 5: bedding screeded, field laid and cut, compaction.", "Day 6: polymeric sand on a dry day; cage anchors into the curb.", "Day 30: sealing."],
    "pavers-travertine-shellstone": ["Days 1 to 2: demolition, base in lifts, coping set.", "Days 3 to 5: stone sorted and laid in the pattern, cuts, compaction with a pad.", "Day 6: polymeric sand, holes filled.", "Day 30: penetrating sealer; coping date on the care sheet."],
    "pavers-marble-porcelain": ["Days 1 to 2: base and screed to an eighth of an inch, or slab prep for a mortar bed.", "Days 3 to 6: pieces set with a level on every one; coping.", "Day 7: joints filled; grout if mortar-set.", "Day 30: sealer for marble; nothing for porcelain."],
    "pavers-driveways": ["Day 1: demolition and haul-off; culvert or apron work if the permit includes it.", "Day 2: subgrade proof-rolled, geotextile, base in lifts.", "Days 3 to 5: bedding screeded, herringbone laid and cut, curbs poured.", "Day 6: compaction, polymeric sand, activation.", "Day 7 to 8: drive on it once the sand cures; sealing at day 30."],
    "pavers-patios-lanais": ["Day 1: excavation or slab prep; drain cut in if needed.", "Day 2: base in lifts, bedding, laying begins.", "Day 3: laying and cuts finished, compaction, polymeric sand.", "Day 4: dry day, furniture back.", "Day 30: sealing."],
    "pavers-walkways-steps": ["Day 1: layout around trees, excavation, base; step core poured or built.", "Day 2: conduit for lights, bedding, pavers laid, treads set.", "Day 3: polymeric sand, fixtures connected."],
    "pavers-sealing": ["Day 1: inspection, cleaning, rinse.", "Day 2: dry day.", "Day 3: re-sand, activate.", "Day 5 or later, once dry through: seal.", "Next date written on the care sheet."],
    "pavers-repair-storm-restoration": ["Day 0: photographs before anything moves.", "Weeks 1 to 3: base drains.", "Day 1 of work: lift, sound, dig out voids.", "Day 2: base rebuilt in lifts, flushed, curb poured.", "Day 3: pavers reset, polymeric sand on a dry forecast.", "Weeks later: seal."],
    "pavers-retaining-walls-outdoor-living": ["Day 1: trench, compacted stone base, first course buried.", "Days 2 to 3: courses, drainage stone and pipe behind soil-holding walls, caps adhered.", "Days 4 to 8 for kitchens: pad, frame, veneer, cap; gas and electric between."],
    "pavers-artificial-turf": ["Morning: subgrade pitched, weed barrier, stone base compacted.", "Afternoon: turf laid, seams glued and nailed, infill brushed in.", "Same day: walk on it."],
    "pavers-outdoor-lighting": ["During base work: conduit runs and fixture housings set.", "During laying: fixtures placed in the field or risers.", "Last day: transformer mounted, connections in gel connectors, timer and photocell set."],
}


def extra(key):
    h, items = SCENARIOS[key]
    return sec(h, ul(items)) + sec("Day by day", ol(DAYS[key]))
