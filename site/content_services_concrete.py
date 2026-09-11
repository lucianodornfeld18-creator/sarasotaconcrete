# -*- coding: utf-8 -*-
"""Concrete service pages. Structure per prompt 9.3: capsule (what / cost here / how long), scope, process,
price factors table, local spec, permits/flood/HOA, what goes wrong here, maintenance, comparisons, FAQ, cases, CTA, reviewed."""
from _data import SERVICES, CITIES, CITY_SERVICE, cs_route
from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, svc_link, city_link, cs_link, link, ext, facts, cards, service_schema
from _photos import gallery
from content_services_extra import extra

SRC = "Published Sarasota-area pricing read on September 10, 2026 (see data and methods). Planning ranges, not quotes."


def city_links(key):
    xs = [cs_link(c, key, CITIES[c]["name"]) for c, s in CITY_SERVICE if s == key]
    return p("City pages for this service: " + ", ".join(xs) + ".") if xs else ""


def page(key, title, meta, h1, kicker, lede, body, faq, title_full=False):
    s = SERVICES[key]
    return {"route": s["route"], "title": title, "title_full": title_full, "meta_description": meta, "h1": h1, "kicker": kicker, "lede": lede,
            "breadcrumbs": [("Home", "/"), ("Concrete", "/concrete/"), (s["name"], None)], "body_html": body, "faq": faq,
            "schema": [service_schema(key, s["route"])]}


# ---------------------------------------------------------------- POOL DECKS
def pool_decks():
    key = "concrete-pool-decks"
    faq = [
        ("Can a concrete deck be poured right against the pool shell?", "No. An isolation joint with a compressible filler separates the deck from the pool beam so the two can move independently; the coping bridges the gap. Decks poured tight to the shell crack along the coping within a couple of summers."),
        ("How wide should the deck be around a residential pool?", "Four feet is the minimum for walking and cleaning; six to eight feet on the side you'll furnish. Under a screen cage the deck runs to the cage base so the anchors sit in concrete, not in a paver joint."),
        ("Does the deck need a deck drain?", "Any deck over about 400 square feet or any lanai where the cage traps water should have one. Without it the slope has to carry water off the edge, and the edge is where the lanai screen and the house are."),
        ("Will a new deck match the color of the existing one?", "Not exactly. Cement and finishing time shift the gray, so the practical answers are a full pour, a decorative overlay across both, or a color break at a joint. The resurfacing page covers overlays."),
        ("Is a textured concrete deck slippery when wet?", "A broom or knockdown texture tested to a wet dynamic coefficient of friction of 0.42 or higher (ANSI A326.3) is not. A smooth troweled deck or a glossy film sealer is. The comparison page has the slip figures by finish."),
        ("How long before the pool can be used after the deck is poured?", "Foot traffic after 24 hours, furniture after 3 days, and the pool itself the same day the deck is protected from splash for the first 24 hours. Cure protection matters more than waiting."),
    ]
    body = facts([("Typical size", "500 to 1,000 sq ft"), ("Spec", "4 in., 4,000 PSI, fiber plus #3 bar at the cage line"), ("Time on site", "5 to 10 working days"), ("Planning range", "$9 to $14 per sq ft new; $10 to $15 overlay")])
    body += cap("What is a concrete pool deck and what does it cost in Sarasota?",
                "A poured-in-place slab, 4 inches thick, around the pool shell and inside the screen cage, with an isolation joint at the coping, deck drains and a textured finish. On September 10, 2026, published Sarasota-area pricing put a new textured deck at roughly $9 to $14 per square foot and a decorative overlay on a sound slab at $10 to $15. A 700-square-foot deck lands near $7,000 to $10,000 new.",
                p(SRC + " Demolition of an old deck adds $2 to $4 per square foot; deck drains, cage re-anchoring and coping replacement are separate lines."))
    body += cap("How long does a pool deck take?",
                "Five to ten working days from demolition to the day you can put furniture back. Day one is tear-out and haul-off, days two and three are base, drains and forms, the pour is a single morning, joints are cut that afternoon, and the rest is cure protection, texture sealing and cage re-anchoring. Permit review adds one to three weeks before day one.",
                p("The pour is scheduled for the morning in summer because NOAA's normals give Sarasota-Bradenton 7 to 9 inches of rain in each of June through September, almost all of it after 2 p.m."))
    body += sec("What the work includes",
                ul(["Removal of the old deck, or of the failed sections when a partial replacement is honest, with the cage screens protected.",
                    "Subgrade compaction, 4 inches of compacted crushed base, and a slope of 1/8 inch per foot to the drains or the edge.",
                    "Deck drains (linear or point) where the cage traps water, tied into the yard drainage or a dry well.",
                    "Isolation joint at the pool beam and at the house slab; control joints at 8 to 10 feet, cut the same day.",
                    "Fiber-reinforced 4,000 PSI concrete with #3 rebar along the cage line where the anchors go.",
                    "Broom, knockdown or stamped texture; integral color or a light topcoat where heat is the priority.",
                    "Re-anchoring of the screen cage, reset of the coping if it was disturbed, and a care sheet with the sealing schedule."]))
    body += sec("Price factors and ranges",
                table(["Factor", "Effect", "Notes"], [
                    ["Deck size", "Under 400 sq ft costs more per foot", "Mobilization and the pump truck don't shrink with the deck"],
                    ["Demolition", "+$2 to $4 per sq ft", "Old decks with pavers over concrete cost more to remove"],
                    ["Texture", "Broom lowest; knockdown +$1 to $2; stamped +$4 to $8", "Stamped needs sealing every 2 to 3 years"],
                    ["Drains", "$300 to $900 per run", "Cheaper than re-pouring a deck that ponds"],
                    ["Cage anchors", "$15 to $40 per anchor", "Aluminum cages need new tapcons or wedge anchors after a pour"],
                    ["Barrier island access", "+5 to 15%", "Bridge timing, staging on a small lot, salt-resistant mix"]],
                    "Concrete pool deck price factors, Sarasota County, 2026 (planning ranges)") +
                p(f'Full size bands and the resurfacing alternative are in the {link("/pricing/pool-decks/", "pool deck cost guide")}.'))
    body += sec("The spec for a Sarasota pool deck",
                p("Four inches of 4,000 PSI concrete with fiber is the working standard; the base under it is what varies. On Myakka and EauGallie sands with a wet-season water table under 10 inches, the subgrade is compacted after any old base is removed, then 4 inches of crushed limerock goes down in two lifts. Where the cage columns land, #3 rebar runs along the perimeter so the anchors have steel to hold against uplift.") +
                p("Slope is set to the drains, not to the pool. A deck that pitches toward the water dumps every rain into the pool and every leaf with it. Control joints go in at 8 to 10 feet on center, cut to one quarter of the slab depth the same afternoon, because in a 91-degree July the slab starts shrinking before dinner. The isolation joint at the coping gets a closed-cell filler and a flexible sealant, not mortar."))
    body += sec("Permits, flood zones and HOAs",
                p(f'Replacing a deck on the same footprint inside a cage is treated differently by each office. Unincorporated Sarasota County and the City of Sarasota generally review it as a slab; the Town of Longboat Key runs every permit through substantial-improvement review; Charlotte County requires a permit for any slab. Details are on the {link("/permits/", "permit hub")}.') +
                p(f'On the keys the deck itself is a site improvement outside the NFIP 50 percent calculation, but a deck seaward of the Gulf Beach Setback Line needs a coastal setback variance, and any deck lighting must follow the {link("/permits/sea-turtle-lighting/", "turtle lighting rules")} from May 1 to October 31. Condo associations on Siesta Key and Longboat Key approve deck work through the board; the {link("/hoa/barrier-island-condos/", "condo guide")} covers phasing and reserves.'))
    body += sec("What goes wrong with pool decks on this coast",
                ul(["<strong>Spalling at the coping.</strong> Salt-chlorinated pool water and Gulf spray move chloride into the top inch; the surface flakes at the waterline first. Low water-cement ratio, cure protection and a breathable sealer slow it down.",
                    "<strong>Ponding under the cage.</strong> Decks poured flat to save on drains hold water against the screen base and rot the aluminum. A 1/8-inch-per-foot slope to a deck drain fixes it for the life of the deck.",
                    "<strong>Cracks that cross the deck.</strong> Joints cut the next morning are joints cut too late. Same-day cuts and an isolation joint at the shell keep cracks where they belong.",
                    "<strong>A deck too hot to cross.</strong> Dark integral color and smooth troweled finishes store heat. Light color and open texture help; the temperature study will put numbers on how much.",
                    "<strong>Surge.</strong> A slab that sat under salt water needs the base checked for voids before anyone resurfaces it. The post-storm page has the sequence."]))
    body += sec("Maintenance", p(f'Rinse salt splash weekly if the pool is salt-chlorinated, reseal a textured deck every 2 to 3 years inland and every 18 to 24 months within a mile of open water, and keep sprinklers off the deck if you\'re on well water (rust). The {link("/coastal/maintenance-calendar/", "maintenance calendar")} sets the dates by distance from the coast.'))
    body += sec("Comparisons", cards([("/compare/resurface-vs-replace-pool-deck/", "Resurface or replace?", "The tests that decide, and the price gap."), ("/compare/cool-deck-vs-pavers/", "Cool deck vs pavers", "Lifespan, heat and repairability."), ("/compare/pool-deck-surfaces-heat/", "Surfaces and heat", "What color, mass and texture do at 2 p.m."), ("/pavers/pool-decks/", "Paver pool decks", "The other pillar's answer to the same deck.")]))
    body += gallery("pavers-pool-decks", "Pool decks from the provider's crews", 3)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a pool deck estimate", "/contact/", "Send a photo of the deck and the cage; a site visit follows.")
    body += reviewed("September 10, 2026")
    return page(key, "Concrete Pool Decks in Sarasota, FL – Cost, Heat & Permits", "Concrete pool decks in Sarasota County: $9 to $14 per sq ft planning range, 4,000 PSI spec, deck drains, cage anchors, permits by jurisdiction, and what fails near salt water.",
                "Concrete pool decks for Sarasota County, poured for salt, splash and barefoot afternoons", "Concrete · pool decks", "New decks, deck extensions and condo decks on a real slope to real drains, with the isolation joint at the coping that keeps the cracks away.", body, faq)


# ---------------------------------------------------------------- DRIVEWAYS
def driveways():
    key = "concrete-driveways"
    faq = [
        ("Why is my new driveway a different shade in patches?", "Uneven moisture in the base, a finishing pass that ran late on one section, or curing compound applied unevenly. It usually evens out over months of sun; it isn't structural. Ask for a uniform cure method in the scope."),
        ("What happens to my irrigation lines?", "Lines under the old driveway are located before demolition, capped during the work and re-run in sleeves under the new slab so heads can be serviced without cutting concrete. Add the sleeves to the scope; they cost little now and a lot later."),
        ("Do you haul away the old driveway?", "Yes, demolition and haul-off are part of a replacement scope. Broken concrete goes to a recycler, not a landfill, and some of it comes back as base for another job."),
        ("How are control joints spaced?", "Every 8 to 10 feet in both directions for a 4-inch slab, in panels as close to square as the layout allows, cut to a quarter of the depth the same day. Joints that make long rectangles crack across the middle."),
        ("Does a new concrete driveway need sealing?", "Not for strength. A penetrating siloxane sealer after 28 days slows chloride and oil staining and is worth it within a mile of the water; a film sealer on a driveway is a maintenance commitment you probably don't want."),
        ("How long does a concrete driveway last near the Gulf?", "Thirty years is realistic for a 4-inch, 4,000 PSI slab on a compacted base with sealed edges and drains that work. The 1960s Gulf Gate driveways that are failing now were 3.5 inches on raw sand with no joints."),
    ]
    body = facts([("Typical size", "400 to 900 sq ft (two-car)"), ("Spec", "4 in., 4,000 PSI, fiber + #3 bar; 6 in. aprons where required"), ("Time on site", "3 to 6 working days plus 7-day cure"), ("Planning range", "$7 to $12 per sq ft")])
    body += cap("What does a concrete driveway cost in Sarasota County in 2026?",
                "Published Sarasota-area pricing on September 10, 2026 puts a plain broom-finished driveway at roughly $7 to $12 per square foot installed, with demolition of the old slab adding $2 to $4. A two-car driveway of 600 square feet therefore runs about $5,500 to $9,500 as a planning range; widening, aprons in the right-of-way and culvert work are separate lines.",
                '<p class="src-note">' + SRC + '</p>' + p(f' The {link("/pricing/concrete/", "concrete cost guide")} shows the size bands.'))
    body += cap("How long does a driveway replacement take?",
                "Three to six working days on site: one for demolition and haul-off, one or two for base and forms, a morning for the pour, and the rest for joint cutting and cure protection. You park on the street for 7 days after the pour; delivery trucks and boat trailers wait 28. Permit review, where required, comes before day one and takes one to three weeks.")
    body += sec("Scope options",
                ul(["Full replacement of the existing driveway, including the apron where the jurisdiction allows it under the same permit.",
                    "Widening by 2 to 4 feet on one side, with a dowelled joint to the existing slab so the two don't step.",
                    "Extensions and turnouts for a third car, a boat trailer or a golf cart, subject to the community's width rules.",
                    "New driveways on infill lots, with the culvert or swale crossing designed to the county or city detail.",
                    "Golf-cart paths where the community allows them (Venice-area and Wellen Park communities set their own rules)."]))
    body += sec("Price factors",
                table(["Factor", "Effect", "Why"], [
                    ["Demolition", "+$2 to $4 per sq ft", "Thickness and rebar in the old slab; access for the skid steer"],
                    ["Apron in the right-of-way", "+$500 to $2,500", "City of Sarasota and Venice details call for 6 in. and their own permit"],
                    ["Culvert or swale crossing", "+$1,500 to $5,000", "North Port and the county size the pipe; the crossing is inspected"],
                    ["Thickness", "6 in. adds about $1.50 to $2.50 per sq ft", "Heavy vehicles, RV and boat-trailer parking"],
                    ["Finish", "Broom base; exposed aggregate +$3 to $5; stamped +$5 to $8", "Labor and sealing"],
                    ["Irrigation sleeves", "$150 to $400", "Avoids cutting concrete later"]],
                    "Concrete driveway price factors, Sarasota County, 2026 (planning ranges)"))
    body += sec("The spec for a driveway on Sarasota sand",
                p("The Florida Building Code, Residential sets 4 inches as the floor, and that's the working thickness for cars and SUVs. The base is where local driveways are won or lost: 4 inches of compacted crushed limerock over a proof-rolled subgrade, 6 inches where the wet-season water table sits within a foot of the surface, and a geotextile separation layer where the sand pumps under the plate compactor.") +
                p("The mix is 4,000 PSI with a water-cement ratio at or below 0.45, fiber for plastic shrinkage and #3 rebar on chairs at 18 to 24 inches for load. Control joints go in at 8 to 10 feet, cut the same afternoon. Slope is a minimum of 1/8 inch per foot away from the garage, and where the driveway meets a swale the last few feet are formed to the jurisdiction's crossing detail so the swale keeps draining."))
    body += sec("Permits by jurisdiction",
                table(["Office", "What usually applies to a driveway", "Page"], [
                    ["Sarasota County (unincorporated)", "Culvert permit if the crossing is touched; right-of-way use permit for any work in the county road frontage; residential exemption up to $7,500 with documentation", link("/permits/sarasota-county/", "Sarasota County")],
                    ["City of Sarasota", "The apron between the sidewalk and the street is city property and needs a permit; the rest is reviewed through the FTG portal", link("/permits/city-of-sarasota/", "City of Sarasota")],
                    ["City of Venice", "Pavers or non-standard work in the right-of-way need a license agreement and the city detail", link("/permits/venice/", "Venice")],
                    ["City of North Port", "Right of Way Use Permit (Culvert/Driveway/Sidewalk/Concrete Slab); swale restoration inspected", link("/permits/north-port/", "North Port")],
                    ["Town of Longboat Key", "At-grade driveways reviewed by Planning & Zoning; substantial-improvement check", link("/permits/longboat-key/", "Longboat Key")],
                    ["Charlotte County", "Residential driveway permit, or ROW permit if only in the right-of-way; NOC over $5,000", link("/permits/charlotte-county/", "Charlotte County")]],
                    "Driveway permitting summary, checked September 10, 2026; confirm fees with the office"))
    body += sec("What goes wrong with driveways here",
                ul(["<strong>Settlement at the garage.</strong> Backfill against the garage footing was never compacted; the slab drops half an inch and cracks at the threshold. The fix is compacting that strip and dowelling the slab to the apron.",
                    "<strong>Cracks across long panels.</strong> Joints at 15 feet or cut the next day. Cut at 8 to 10 feet, same day.",
                    "<strong>Rust bleeding from well-water sprinklers.</strong> Iron in the irrigation water stains the driveway orange. Heads get redirected, or the water gets filtered; the guide on rust stains has the chemistry.",
                    "<strong>Scaling within a mile of the water.</strong> Salt spray on a slab finished with too much water at the surface. Low water-cement ratio, no water added at the truck, and a proper cure.",
                    "<strong>A crossing that blocks the swale.</strong> North Port and Port Charlotte lots depend on roadside swales; a driveway poured flat across one floods the neighbor. The crossing is formed to the city or county detail with the culvert they size."]))
    body += sec("Maintenance", p("Keep sprinklers off the slab, rinse salt splash if you're on the water, seal with a penetrating product after 28 days on coastal lots, and keep the joint at the garage sealed. Cracks under a sixteenth of an inch are cosmetic; wider ones, or a panel that rocks, are a repair call."))
    body += sec("Comparisons", cards([("/compare/concrete-vs-pavers-driveway/", "Concrete vs paver driveway", "Cost over 20 years, flood zones, repairability."), ("/compare/4-inch-vs-6-inch/", "4 inches or 6?", "Loads, cost, and where 6 is required."), ("/compare/rebar-vs-fiber/", "Rebar, mesh or fiber", "What each does on Myakka sand."), ("/pavers/driveways/", "Paver driveways", "The other pillar's driveway.")]))
    body += gallery("concrete-driveways", "Driveways from the provider's crews", 3)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a driveway estimate", "/contact/", "Send the width and length, a photo, and whether the driveway crosses a swale.")
    body += reviewed("September 10, 2026")
    return page(key, "Concrete Driveways in Sarasota, FL – Cost, Spec & Permits", "Concrete driveway replacement and widening in Sarasota County: $7 to $12 per sq ft planning range, 4-inch 4,000 PSI spec on compacted base, permits by office, swale crossings.",
                "Concrete driveways for Sarasota County, from the base to the apron", "Concrete · driveways", "Replacement, widening and new driveways specified for a shallow water table, with the apron and culvert rules of six different permit offices.", body, faq)


# ---------------------------------------------------------------- PATIOS & LANAIS
def patios():
    key = "concrete-patios-lanais"
    faq = [
        ("Does exposed aggregate stay cooler than a broom finish?", "Slightly, when the aggregate is light and the matrix is light; the texture also feels cooler underfoot because less skin touches the surface. It isn't a substitute for a light color. The temperature study will measure it against broom concrete."),
        ("Can a lanai extension be poured over the old screened floor?", "If the old slab is sound and the new floor can stay below the door threshold, an overlay works; otherwise the extension is poured beside it with a dowelled joint, and the finish is matched with an overlay across both."),
        ("How thick is a patio slab?", "Four inches, on 4 inches of compacted base. A hot tub, an outdoor kitchen or a heavy grill island gets a thickened section or a separate pad sized for the load."),
        ("Do I need a permit for a patio?", "Often not for an uncovered at-grade slab in unincorporated Sarasota County, yes in Charlotte County, and yes anywhere the slab supports a roof, a cage or a structure. The permit hub has the offices."),
        ("What slope does a lanai floor need?", "1/8 inch per foot away from the house is the minimum; under a screen cage a floor drain lets the floor stay flatter. A lanai that drains toward the sliders is a lanai that floods the living room in a September storm."),
    ]
    body = facts([("Typical size", "12×20 to 20×30 ft"), ("Spec", "4 in., 4,000 PSI, fiber; thickened sections for kitchens and spas"), ("Time on site", "2 to 5 working days"), ("Planning range", "$8 to $13 per sq ft broom; $11 to $17 exposed aggregate or colored")])
    body += cap("What does a concrete patio or lanai slab cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts a broom-finished patio slab at roughly $8 to $13 per square foot installed, exposed aggregate or integrally colored slabs at $11 to $17, and a 12-by-20-foot lanai extension at about $2,000 to $4,000 before any cage work. Adding a screen cage, a roof or an outdoor kitchen base is priced separately.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a patio slab take?",
                "Two to five working days: base and forms the first day or two, a morning pour, joints cut the same afternoon, then cure. Furniture goes back after 3 days, a screen cage after 7. Rain in the first two hours after the pour is the one weather risk, which is why summer pours start at 7 a.m.")
    body += sec("Scope options",
                ul(["New backyard patios, from a 10-by-12 pad to a 600-square-foot entertaining slab.",
                    "Lanai floor extensions beyond the existing cage, with a new cage base line.",
                    "Screened-room and under-roof slabs that carry a future cage or roof, with the anchor line reinforced.",
                    "Finishes: broom, smooth trowel (shaded areas only), exposed aggregate, integral color, or a light-reflective topcoat.",
                    "Thickened pads for hot tubs, outdoor kitchens, grill islands and generator-adjacent equipment."]))
    body += sec("Price factors", table(["Factor", "Effect"], [["Finish", "Broom lowest; exposed aggregate and color add $3 to $5 per sq ft"], ["Access", "Wheelbarrow-only backyards add labor; pump truck adds $600 to $1,200"], ["Drains", "Lanai floor drain $300 to $700"], ["Thickened sections", "$150 to $400 each"], ["Tying to existing slab", "Dowels and matched finish, $200 to $600"]], "Patio and lanai slab price factors, 2026 (planning ranges)"))
    body += sec("The spec for a Sarasota patio slab",
                p("Four inches of fiber-reinforced 4,000 PSI concrete on 4 inches of compacted crushed base, control joints at 8 to 10 feet, an isolation joint at the house slab, and a slope of 1/8 inch per foot away from the sliders or toward a floor drain. Where the slab will carry a cage, the perimeter gets #3 bar so the anchors hold in wind. On lots east of I-75 where the wet-season water table is under 10 inches, the base goes to 6 inches and the subgrade is proof-rolled first.") +
                p("Finish choice is a heat and slip decision as much as a look. Broom is the safest wet-slip finish and the cheapest; exposed aggregate with light stone stays visually cool and hides stains; smooth trowel belongs under a roof, never around water; integral color in light tones keeps the surface temperature down compared with charcoal."))
    body += sec("Permits and HOAs", p(f'An uncovered at-grade patio in unincorporated Sarasota County is often below the permit threshold, but a slab that carries a cage, a roof or an outdoor kitchen isn\'t. Charlotte County permits every slab. Communities from Palmer Ranch to Wellen Park treat a patio extension as an exterior modification that needs ARC approval before anyone digs. See {link("/permits/", "permits")} and {link("/hoa/", "HOA guides")}.'))
    body += sec("What goes wrong", ul(["Lanai floors pitched toward the house.", "Joints cut a day late across a 20-foot panel.", "A grill island set on a 4-inch slab that wasn't thickened.", "Smooth trowel around a pool or spa.", "A cage anchored into a slab edge with no steel."]))
    body += sec("Maintenance", p("Reseal colored and exposed-aggregate slabs every 2 to 3 years; broom slabs need only a penetrating sealer on coastal lots. Keep the house-slab joint sealed and keep irrigation heads off the surface."))
    body += sec("Comparisons", cards([("/pavers/patios-lanais/", "Paver patios and lanais", "When pavers beat a pour, and the overlay tests."), ("/concrete/stamped/", "Stamped concrete", "Patterned patios and their sealing cycle."), ("/compare/pool-deck-surfaces-heat/", "Surfaces and heat", "Color and texture at 2 p.m.")]))
    body += gallery("concrete-patios-lanais", "Patios from the provider's crews", 3)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a patio estimate", "/contact/", "Send the dimensions and whether a cage or roof is planned.")
    body += reviewed("September 10, 2026")
    return page(key, "Concrete Patios & Lanai Slabs in Sarasota, FL – Cost", "Concrete patios and lanai slab extensions in Sarasota County: $8 to $13 per sq ft planning range, finishes by heat and slip, cage anchor reinforcement, drains, permits and HOA approvals.",
                "Concrete patios and lanai slabs for Sarasota County homes", "Concrete · patios and lanais", "Broom, exposed-aggregate and colored slabs sized for the cage you have or the one you're planning, sloped to a drain instead of to the sliders.", body, faq)


# ---------------------------------------------------------------- STAMPED
def stamped():
    key = "concrete-stamped"
    faq = [
        ("Is stamped concrete slippery around a pool in Sarasota?", "It can be. Stamped surfaces sealed with a glossy film get slick when wet; a matte sealer with a grit additive and a pattern with texture keeps the wet slip rating acceptable. Ask for the additive in writing."),
        ("Can hairline cracks in stamped concrete be repaired?", "Cosmetically, yes: cracks are routed, filled with a color-matched polymer and re-sealed. They'll still be visible up close. Structural cracks that offset mean the base moved, and that's a different job."),
        ("How often does stamped concrete need resealing here?", "Every 2 to 3 years inland and closer to every 18 to 24 months near the Gulf, because UV and salt break the film. Skipping it fades the color and lets water in under the release agent."),
        ("Does stamped concrete cost less than pavers?", "Usually a little less to install and more to maintain. The planning ranges are $12 to $20 per square foot for stamped versus $13 to $16 for concrete pavers; pavers can be lifted and reset, stamped concrete can't."),
        ("Can an existing patio be stamped?", "Not directly. A stamped overlay of 3/8 to 1/2 inch can go over a sound slab; a slab that's cracked, hollow or pitched wrong comes out first."),
    ]
    body = facts([("Uses", "Patios, walkways, pool decks, driveway borders"), ("Spec", "4 in., 4,000 PSI, fiber; color hardener or integral color; matte sealer with grit"), ("Time on site", "3 to 6 working days"), ("Planning range", "$12 to $20 per sq ft")])
    body += cap("What does stamped concrete cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts stamped and decorative concrete at roughly $12 to $20 per square foot installed, depending on pattern, one or two colors, and whether a border or a second pattern is cut in. A 400-square-foot stamped patio therefore lands near $5,000 to $8,000, plus demolition of anything it replaces.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a stamped pour take?",
                "Three to six working days. The pour itself is a morning, but stamping happens in a window of about two hours while the concrete is plastic, so the crew size and the sequence matter more than for a broom slab. Release agent is washed the next day, the surface is sealed at 3 to 7 days, and furniture goes back after the sealer cures.")
    body += sec("Patterns, colors and what they do in the sun",
                p("Ashlar slate, random flagstone, wood plank and cobble patterns all stamp well here. Color is the decision that matters: a charcoal or dark slate pool deck can run far hotter than a light sand tone in July because the surface absorbs more of the sun's energy, and the temperature study will put local numbers on it. For pool decks the recommendation is a light base color, a light-to-medium release for depth, and a matte sealer with a slip additive."))
    body += sec("Price factors", table(["Factor", "Effect"], [["Pattern complexity", "Borders, two patterns or hand-tooled joints add $2 to $4 per sq ft"], ["Colors", "Second color or antiquing adds $1 to $2"], ["Overlay vs new slab", "Stamped overlay on a sound slab $10 to $15"], ["Sealer type", "Matte with grit costs a little more and slips less"], ["Coastal reseal cycle", "Every 18 to 24 months near the water"]], "Stamped concrete price factors, 2026 (planning ranges)"))
    body += sec("The spec", p("Same slab as any Sarasota flatwork, 4 inches of 4,000 PSI fiber concrete on compacted base with same-day control joints, plus a color hardener or integral color, a release agent, the stamp, and a sealer chosen for the coast. Joints are laid out so they fall in pattern lines. Around pools the sealer is matte with a polymer grit; glossy film sealers are refused on decks because they're the reason stamped pool decks have a slippery reputation."))
    body += sec("Permits and HOAs", p(f'Permits follow the underlying slab (see {link("/concrete/patios-lanais/", "patios")} and {link("/concrete/pool-decks/", "pool decks")}). Associations care about the color and pattern: submit a sample chip and a photo of the pattern with the ARC packet. Sarasota-area HOAs tend to reject dark colors and busy patterns on driveways more than on rear patios.'))
    body += sec("What goes wrong", ul(["Stamping too late: the pattern is shallow on one end of the slab because the concrete set before the crew reached it.", "Glossy sealer around water.", "Reseal skipped for five years; the color goes chalky and water gets under the release.", "Dark colors on a pool deck.", "Joints ignored in the pattern, so the crack shows up through a flagstone."]))
    body += sec("Maintenance", p("Rinse, don't pressure-wash at close range. Reseal on the coastal cycle. Repair cracks early with color-matched filler so water doesn't work under the surface."))
    body += sec("Comparisons", cards([("/pavers/patios-lanais/", "Paver patios", "Repairable, no resealing schedule to keep the look."), ("/pavers/travertine-shellstone/", "Travertine", "The stone stamped concrete imitates."), ("/compare/pool-deck-surfaces-heat/", "Heat by surface", "Why color matters more than pattern.")]))
    body += extra(key)
    body += faq_block(faq)
    body += cta("Get a stamped concrete estimate", "/contact/", "Send the area, the pattern you like and whether it's around a pool.")
    body += reviewed("September 10, 2026")
    return page(key, "Stamped & Decorative Concrete in Sarasota, FL – Cost", "Stamped and decorative concrete for Sarasota County patios, walks and pool decks: $12 to $20 per sq ft planning range, patterns, light colors for heat, matte sealers for slip, reseal cycle.",
                "Stamped and decorative concrete for Sarasota County", "Concrete · stamped", "Patterned and colored concrete with a light color for heat, a matte sealer with grit for slip, and a resealing cycle that respects salt air.", body, faq)


# ---------------------------------------------------------------- SLABS & PADS
def slabs():
    key = "concrete-slabs"
    faq = [
        ("Is a permit required for a shed pad under 100 square feet in Sarasota County?", "A detached, single-story shed of 100 square feet or less with no electricity or plumbing is generally exempt from a building permit in unincorporated Sarasota County, and the pad follows the shed. Anything larger, or any pad in Charlotte County, is permitted. Confirm with the office on the permit page."),
        ("How thick should a generator pad be?", "Four inches is enough for a residential standby generator; the manufacturer's footprint plus 6 inches of margin, level within 1/8 inch, with anchor bolts set to the unit's template. Whole-house units over 20 kW get 5 inches."),
        ("What does an AC pad need?", "A 4-inch pad 3 inches wider than the condenser on each side, elevated above the finished grade to stay dry, on compacted base. Precast pads sink on sand; poured pads don't."),
        ("Can you pour a pad for a boat lift or a dock approach?", "Dock approaches and lift-motor pads on the upland side, yes. Anything over the water or tied to the seawall is marine construction and needs its own contractor and permit."),
        ("What does a hot tub pad cost?", "A 6-inch reinforced pad of about 80 square feet lands around $1,200 to $2,200 as a planning range, depending on access and whether an electrical conduit is sleeved in."),
    ]
    body = facts([("Uses", "Shed, AC, generator, hot tub, boat-lift motor, dumpster, dock approach"), ("Spec", "4 in. standard; 5 to 6 in. for hot tubs, RVs and dumpsters; #4 bar where loaded"), ("Time on site", "1 to 3 working days"), ("Planning range", "$9 to $15 per sq ft small pads; $8 to $12 large")])
    body += cap("What does a concrete pad cost in Sarasota?",
                "Small pads cost more per square foot than driveways because mobilization is the same for 40 square feet as for 600. Published Sarasota-area pricing on September 10, 2026 supports a planning range of $9 to $15 per square foot for pads under 150 square feet and $8 to $12 for larger slabs; an AC pad runs about $350 to $700 and a 10-by-12 shed pad about $1,200 to $2,000.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a pad take?",
                "One to three working days. Base and forms in the morning, pour the same day for small pads, joints if the slab is over 10 feet in either direction, then cure. A shed can go on after 7 days, a hot tub after 28 because of the concentrated water weight.")
    body += sec("Pads sized for the load", table(["Pad", "Thickness", "Reinforcement", "Notes"], [
        ["AC condenser", "4 in.", "Fiber", "3 in. margin each side, raised 2 to 4 in. above grade"],
        ["Standby generator", "4 to 5 in.", "Fiber + #3 bar", "Anchor bolts to the manufacturer's template; conduit sleeved"],
        ["Shed (up to 12×16)", "4 in.", "Fiber", "Thickened edge if the shed has no floor"],
        ["Hot tub / swim spa", "6 in.", "#4 bar at 12 in.", "A filled 8-ft spa can exceed 5,000 lb"],
        ["Boat-trailer / RV pad", "6 in.", "#4 bar at 18 in.", "Tongue jack point on a plate, not bare concrete"],
        ["Dumpster / equipment pad", "6 in.", "#4 bar at 12 in.", "Turning wheels and drop loads"],
        ["Dock approach (upland)", "4 in.", "Fiber + #3 bar", "Salt-resistant mix; marine work beyond the seawall excluded"]],
        "Pad specifications used by Sarasota Concrete, 2026"))
    body += sec("The base matters more on a pad than anywhere", p("A pad is small enough that one soft spot tilts the whole thing, and on Myakka fine sand with a shallow water table that soft spot is common. The subgrade is dug to firm material, compacted, and topped with 4 inches of crushed base compacted in two lifts. Pads for equipment are set 2 to 4 inches above finished grade so irrigation and rain don't sit against the unit."))
    body += sec("Permits", p(f'Unincorporated Sarasota County generally exempts a detached shed of 100 square feet or less; the pad follows the shed. Generator and AC pads are usually reviewed with the electrical or mechanical permit for the equipment, not as slabs. Charlotte County permits every slab, structural or not, and requires a Notice of Commencement over $5,000. See {link("/permits/", "permits")}.'))
    body += sec("What goes wrong", ul(["Precast AC pads sinking into sand and tilting the condenser.", "Generator pads poured without the anchor template, so the bolts miss.", "Shed pads level with the lawn that hold water at the door.", "Hot tub pads at 4 inches that crack under a filled spa.", "Pads poured at the seawall as if they were marine work."]))
    body += sec("Comparisons", cards([("/concrete/driveways/", "Driveways", "Same base logic at a larger scale."), ("/concrete/patios-lanais/", "Patios and lanais", "Thickened sections for outdoor kitchens."), ("/tools/concrete-paver-calculator/", "Calculator", "Cubic yards and a dated cost range for any pad size.")]))
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a slab or pad estimate", "/contact/", "Tell us what's going on the pad and where the lot drains.")
    body += reviewed("September 10, 2026")
    return page(key, "Concrete Slabs & Pads in Sarasota, FL – Shed, AC, Generator", "Concrete pads in Sarasota County for sheds, AC units, generators, hot tubs, boat lifts and dumpsters: thickness and rebar by load, base for sandy soil, permit thresholds, dated planning ranges.",
                "Concrete slabs and pads for Sarasota County, sized for the load", "Concrete · slabs and pads", "Shed, AC, generator, hot-tub, boat-lift and dumpster pads poured thick enough for what sits on them and high enough to stay dry.", body, faq)


# ---------------------------------------------------------------- SIDEWALKS
def sidewalks():
    key = "concrete-sidewalks-walkways"
    faq = [
        ("Is a trip hazard on the public sidewalk in front of my house my responsibility?", "In unincorporated Sarasota County the county maintains public sidewalks in its right-of-way; in the City of Sarasota and Venice, report it to the city. A walkway on your own lot is yours. Roots from your tree lifting the public sidewalk can become your problem, so call the office before you cut anything."),
        ("How wide should a front walk be?", "Three feet is the minimum that feels right; four feet lets two people pass and matches most entries. Side-yard paths can be 30 inches."),
        ("How thick is a walkway?", "Four inches, fiber-reinforced, on compacted base, with joints at 5 feet on a 3-foot walk so the panels stay near square."),
        ("Can a walkway be poured around an oak?", "Not through the root zone without a plan. Either the walk bends around the critical root zone or it's built as a floating slab on a pier system; cutting roots on a protected oak in Sarasota County needs a permit."),
        ("What does a walkway cost?", "About $9 to $14 per square foot as a planning range, so a 4-by-40-foot front walk lands near $1,500 to $2,300 before demolition."),
    ]
    body = facts([("Uses", "Front walks, side-yard paths, sidewalk replacement, trip-hazard fixes"), ("Spec", "4 in., fiber, joints at 5 ft on a 3-ft walk"), ("Time on site", "1 to 3 working days"), ("Planning range", "$9 to $14 per sq ft")])
    body += cap("What does a concrete walkway cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 supports a planning range of $9 to $14 per square foot for a broom-finished walkway, with demolition of an old walk adding $2 to $3. A 4-by-40-foot front walk lands near $1,500 to $2,300 new; a trip-hazard panel replacement in a public sidewalk is usually $400 to $900 per panel where the county allows a private contractor to do it.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a walkway take?",
                "One to three working days. Small enough to pour with a buggy from the street, which means no pump truck and no damage to the lawn. Foot traffic after 24 hours.")
    body += sec("Scope", ul(["Front entry walks and stoops, with a landing at the door that meets the threshold correctly.", "Side-yard paths to the pool equipment or the trash enclosure, 30 to 36 inches wide.", "Replacement of lifted panels in a private sidewalk; coordination with the county or city for public ones.", "ADA-style slopes and landings for accessible entries.", "Exposed-aggregate or stamped borders on an entry walk."]))
    body += sec("Spec", p("Four inches of fiber-reinforced concrete on 4 inches of compacted base, control joints at 5 feet on a 3-foot walk and 4 feet on a narrower one, cross slope of 1/4 inch per foot away from the house, and an isolation joint at the stoop. Walks near the bay or the Gulf get the same low water-cement ratio as everything else so they don't scale."))
    body += sec("Permits and trees", p(f'A private walk on your lot is usually below the permit threshold in unincorporated Sarasota County and permitted in Charlotte County. Work in the public sidewalk is a right-of-way matter. Grand oaks are protected under Sarasota County\'s tree ordinance (Chapter 54, Article XVIII) and the City of Sarasota requires a permit for trunks 4 inches and up; a walk that would cut roots is routed instead. See {link("/permits/", "permits")}.'))
    body += sec("What goes wrong", ul(["Walks poured without joints that crack every 6 feet anyway.", "Stoops that hold water against the door.", "Roots cut on a protected tree.", "Panels replaced without matching the grade of the neighbors, creating the next trip hazard."]))
    body += sec("Comparisons", cards([("/pavers/walkways-steps/", "Paver walkways and steps", "When a path should be pavers."), ("/concrete/repair/", "Repair and leveling", "Lifting a settled panel instead of replacing it."), ("/concrete/architectural/", "Architectural concrete", "Honed and board-formed entries.")]))
    body += extra(key)
    body += faq_block(faq)
    body += cta("Get a walkway estimate", "/contact/", "Send the length and width, and a photo of any tree it passes.")
    body += reviewed("September 10, 2026")
    return page(key, "Concrete Sidewalks & Walkways in Sarasota, FL", "Concrete sidewalks and walkways in Sarasota County: $9 to $14 per sq ft planning range, 4-inch fiber spec with joints at 5 feet, tree-root rules, right-of-way responsibilities and trip-hazard fixes.",
                "Concrete sidewalks and walkways for Sarasota County", "Concrete · sidewalks and walkways", "Front walks, side paths and sidewalk panel replacements built to the county's grade, around the oaks, with joints where the cracks would have been.", body, faq)


# ---------------------------------------------------------------- REPAIR
def repair():
    key = "concrete-repair"
    faq = [
        ("Can a cracked driveway be repaired or does it have to be replaced?", "Cracks under a sixteenth of an inch with no offset are sealed and watched. Cracks with a step, panels that rock, or more than a couple of cracks per panel mean the base failed, and a repair is paint over rust. The diagnosis on site is a level, a hammer and a hose."),
        ("Does slab lifting work on sandy soil?", "Polyurethane foam injection lifts and fills voids well in sand as long as the void isn't being fed by water; if the base washed out because of a drainage problem, the drainage gets fixed first or the slab settles again. Mudjacking is heavier and less precise and isn't used here."),
        ("What is spalling and why does it show up on coastal pool decks first?", "Spalling is the surface flaking off in scales. Chloride from salt pools and Gulf spray reaches the reinforcement or simply weakens the top paste; freeze isn't the cause here, salt and a wet finish are. A spalled deck is resurfaced if the slab underneath is sound."),
        ("Can a trip hazard in a walkway be ground down?", "Up to about half an inch, yes, with a grinder and a bevel. More than that, the panel is lifted or replaced."),
        ("What does concrete repair cost?", "Crack sealing runs $8 to $20 per linear foot, slab lifting $500 to $2,500 per area as a planning range, and panel replacement $400 to $900 per panel. The estimate says which one your slab needs and why."),
    ]
    body = facts([("Problems", "Cracks, spalling, settlement, trip hazards, storm damage"), ("Methods", "Seal, lift, grind, patch, resurface, replace"), ("Time on site", "Half a day to 3 days"), ("Planning range", "$8 to $20 per lin ft cracks; $500 to $2,500 lifting")])
    body += cap("What does concrete repair cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 supports these planning ranges: crack routing and sealing $8 to $20 per linear foot, polyurethane slab lifting $500 to $2,500 per settled area, trip-hazard grinding $150 to $400 per joint, spall patching $10 to $18 per square foot, and panel replacement $400 to $900 per panel. The estimate names the cause before the method.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a repair take?",
                "Most repairs are a half day to three days. Slab lifting is done in hours and usable the same day; spall patching needs a day to cure; a panel replacement is a small pour with a 7-day cure. Storm-damage assessments are scheduled first and documented for the insurer before any work starts.")
    body += sec("Diagnosis first", p("Every repair call starts with three tools: a 4-foot level across the slab to find the settlement, a hammer to sound for hollow base, and a hose to see where the water goes. In Sarasota County the answer is usually water. A downspout dumping onto the base, a swale that stopped draining, or a sprinkler line leaking under the slab washes fines out of the sand and the slab follows them down. Fixing the crack without fixing the water is a job you'll pay for twice."))
    body += sec("Repair methods", table(["Problem", "Method", "When it's the wrong call"], [
        ["Hairline shrinkage cracks", "Route and seal with a flexible polyurethane", "When the crack has a step: the base moved"],
        ["Settled panel, no crack", "Polyurethane foam lifting through 5/8-inch holes", "When water is still washing out the base"],
        ["Trip hazard at a joint", "Grind and bevel up to 1/2 in.; lift beyond that", "When the panel is cracked in pieces"],
        ["Spalling / scaling", "Remove loose paste, bond coat, polymer-modified patch or full overlay", "When chloride has reached the rebar and it's rusting"],
        ["Broken panel", "Saw-cut and replace with dowels", "When most panels are failing: replace the slab"],
        ["Post-surge damage", "Void survey, lift or replace, salt rinse of the base", "Never resurface over a base you haven't sounded"]],
        "Concrete repair methods used by Sarasota Concrete"))
    body += sec("Salt and spalling on this coast", p(f'Concrete within a mile of the Gulf, on the bays, or around a salt-chlorinated pool sees chloride every week. The first sign is scaling at the waterline of the pool deck or at the driveway edge where spray lands. The {link("/coastal/salt-and-concrete/", "salt and concrete guide")} explains the mechanism; the repair is a polymer-modified patch or an overlay if the slab is sound, and replacement with a low water-cement mix if it isn\'t.'))
    body += sec("Permits", p(f'Repairs that don\'t change the footprint are usually below permit thresholds in Sarasota County and the cities; Charlotte County permits slab work broadly. Replacement of a full driveway or pool deck follows those pages. Storm-damage repairs on the islands are documented against the {link("/permits/flood-zones-50-percent-rule/", "50% rule")} even though site work is excluded, because the Town of Longboat Key tracks it.'))
    body += sec("Comparisons", cards([("/concrete/resurfacing/", "Resurfacing and overlays", "When a spalled deck gets a new surface instead of a patch."), ("/compare/resurface-vs-replace-pool-deck/", "Resurface or replace", "The decision tests."), ("/coastal/post-storm-restoration/", "Post-storm restoration", "What to check after surge before repairing anything.")]))
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a repair assessment", "/contact/", "Send close-up photos of the cracks and a wider shot showing where water goes.")
    body += reviewed("September 10, 2026")
    return page(key, "Concrete Repair in Sarasota, FL – Cracks, Spalling, Leveling", "Concrete repair in Sarasota County: crack sealing, polyurethane slab lifting, trip-hazard grinding, spall patching and panel replacement, with dated planning ranges and the water-first diagnosis.",
                "Concrete repair and leveling for Sarasota County, cause first", "Concrete · repair", "Cracks, spalling, settled slabs and storm damage diagnosed with a level, a hammer and a hose before anyone chooses a method.", body, faq)


# ---------------------------------------------------------------- RESURFACING
def resurfacing():
    key = "concrete-resurfacing"
    faq = [
        ("Does a pool deck overlay need a permit?", "Usually not in unincorporated Sarasota County or the City of Sarasota when the footprint and height don't change; Charlotte County may treat it as slab work. Condo boards on the islands need to approve it. Check the office on the permit page."),
        ("How long after resurfacing can I use the pool deck?", "Foot traffic after 24 hours, furniture after 48 to 72, and the sealer needs 24 hours dry. Plan on three days of no splash on a salt pool."),
        ("Can an overlay fix a spalled deck?", "If the spalling is surface scaling and the slab sounds solid, yes: loose paste is removed, a bond coat goes on, and a polymer-modified overlay of 1/8 to 3/8 inch is textured. If the slab is hollow, cracked through or has rusting steel, an overlay buys a year or two and then fails."),
        ("What is cool deck?", "A brand name that became generic for a textured, light-colored cementitious overlay on pool decks. It stays cooler than bare concrete mostly because it's light and porous; the porosity is also why it absorbs water and needs resealing. The comparison page covers its lifespan."),
        ("How long does an overlay last?", "Eight to fifteen years on a sound slab with resealing every 2 to 3 years, less near salt water. A poured deck lasts 30."),
    ]
    body = facts([("Uses", "Pool deck resurfacing, cool-deck renewal, textured overlays, lanai floors"), ("Spec", "1/8 to 3/8 in. polymer-modified overlay on a sound, profiled slab"), ("Time on site", "3 to 5 working days"), ("Planning range", "$4 to $8 basic; $10 to $15 decorative")])
    body += cap("What does pool deck resurfacing cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts a basic textured overlay at roughly $4 to $8 per square foot and a decorative overlay (stamped travertine, flagstone or tile pattern) at $10 to $15, on a slab that's sound. A 700-square-foot deck therefore runs about $3,000 to $10,000 depending on the finish, compared with $6,000 to $10,000 for a new pour.",
                '<p class="src-note">' + SRC + '</p>' + p(f' The {link("/compare/resurface-vs-replace-pool-deck/", "resurface or replace comparison")} has the decision tests.'))
    body += cap("How long does resurfacing take?",
                "Three to five working days: pressure-wash and profile the slab, repair cracks and spalls, bond coat, overlay, texture, and seal, with a dry day between coats. Summer schedules work around the afternoon rain by starting early and stopping by 1 p.m.")
    body += sec("When an overlay is the right answer, and when it isn't", table(["Test", "Overlay works", "Replace instead"], [
        ["Hammer sounding", "Solid ring everywhere", "Hollow patches larger than a dinner plate"],
        ["Cracks", "Hairline, no offset", "Offset, or more than a few per panel"],
        ["Slope", "Drains away from the house and pool", "Ponds or pitches toward the house"],
        ["Steel", "No rust staining", "Rust bleeding through the surface"],
        ["Height", "Overlay keeps the deck below the door threshold", "Threshold already tight"],
        ["Age of surface", "Original concrete or one prior overlay", "Two or more failed overlays stacked"]],
        "Resurfacing decision tests used on every deck"))
    body += sec("Finishes", p("Knockdown texture in a light color is the pool-deck default because it's cool underfoot and slip-resistant wet. Stamped overlays in a stone pattern give the travertine look at a lower price with a shorter life. Smooth-troweled and polished overlays belong under roofs. Sealers are matte with a grit additive around water."))
    body += sec("Permits and boards", p(f'Overlays that don\'t change footprint or height are usually below permit thresholds in Sarasota County and the City of Sarasota; Charlotte County can treat them as slab work. Condo pool decks on Siesta Key, Longboat Key and Venice Island go through the board, and the {link("/hoa/barrier-island-condos/", "condo deck guide")} covers phasing so half the deck stays open.'))
    body += sec("What goes wrong", ul(["Overlays on a hollow slab that delaminate in one summer.", "Sealer applied before the overlay is dry, trapping moisture and turning white.", "Glossy sealer around water.", "Overlay stacked on a failed overlay.", "Deck resurfaced before anyone fixed the drain it was ponding around."]))
    body += sec("Comparisons", cards([("/compare/cool-deck-vs-pavers/", "Cool deck vs pavers", "Lifespan and heat."), ("/pavers/pool-decks/", "Paver pool decks", "The alternative that can be lifted and reset."), ("/concrete/repair/", "Repair", "When the problem is the slab, not the surface.")]))
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a resurfacing assessment", "/contact/", "Send photos of the worst spots and tell us how old the deck is.")
    body += reviewed("September 10, 2026")
    return page(key, "Pool Deck Resurfacing in Sarasota, FL – Overlays & Cost", "Pool deck resurfacing and concrete overlays in Sarasota County: $4 to $15 per sq ft planning range, the six tests that decide overlay vs replace, finishes for heat and slip, permits and condo boards.",
                "Concrete resurfacing and overlays for Sarasota County pool decks and lanais", "Concrete · resurfacing", "A new surface on a sound slab, with the six tests that say when a slab is sound and when an overlay is just a delay.", body, faq)


# ---------------------------------------------------------------- ARCHITECTURAL
def architectural():
    key = "concrete-architectural"
    faq = [
        ("What is architectural concrete?", "Concrete where the surface is the finish: honed and polished slabs, board-formed walls and planters that show the wood grain, cast steps and benches, and integrally colored flatwork with tight joints. It's the concrete you see in Sarasota School houses and their modern descendants."),
        ("Is honed concrete slippery?", "Honed to a matte 200 to 400 grit with a penetrating sealer it is not; polished to a gloss it is, and doesn't belong outdoors. Entries get the matte finish."),
        ("Does board-formed concrete work in salt air?", "Yes, with the same low water-cement mix and cover over steel as any coastal concrete. The form liner leaves a texture that hides minor surface change better than a smooth wall."),
        ("What does architectural concrete cost?", "More than flatwork and less than stone: honed slabs run roughly $18 to $30 per square foot and board-formed walls $90 to $180 per square foot of face as planning ranges, because forming and finishing take longer."),
        ("Is this available in Sarasota County?", "It's in the provider's catalog through its Orlando work. Capacity for Suncoast projects is confirmed at estimate time, and the page says so rather than promising a crew that isn't scheduled."),
    ]
    body = facts([("Uses", "Entries, steps, benches, planters, board-formed walls, honed patios"), ("Spec", "Low water-cement mix, tight joints, form liners, penetrating sealer"), ("Time on site", "1 to 3 weeks"), ("Planning range", "$18 to $30 per sq ft honed; $90 to $180 per sq ft board-formed face")])
    body += cap("What does architectural concrete cost in Sarasota?",
                "Planning ranges compiled on September 10, 2026 from regional decorative-concrete pricing put honed or integrally colored flatwork at roughly $18 to $30 per square foot and board-formed walls at $90 to $180 per square foot of wall face, with cast steps and benches priced per piece. These are wider ranges than flatwork because forms, liners and finishing vary with the design.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does it take?",
                "One to three weeks. Forms and liners take days to build, pours are staged so each element cures before the next is formed against it, and honing happens after 7 days. The design conversation before the estimate is longer than for any other concrete service.")
    body += sec("What it's used for here", p("Sarasota's modern houses, from the Sarasota School of the 1950s through today's infill on the keys and west of the Trail, use concrete as a visible material: cantilevered entry steps, board-formed garden walls, planters cast in place, honed slabs that run from the lanai into the living room. Architectural concrete is that work: the surface is the finish, so the mix, the forms and the finishing are specified for how they'll look, not just how they'll hold."))
    body += sec("Finishes", ul(["<strong>Honed</strong>: the slab is ground to a matte grit that reveals a little aggregate and takes a penetrating sealer.", "<strong>Board-formed</strong>: cedar or fir form liners leave the wood grain in a wall or a step riser.", "<strong>Integrally colored</strong> with mineral pigments, in light tones that keep surface temperature down.", "<strong>Cast elements</strong>: benches, planters, steps and caps poured in place or precast on site."]))
    body += sec("Spec and salt", p("Same coastal rules: a low water-cement ratio, 2 inches of cover over steel in walls that face the water, cure protection, and a penetrating rather than film sealer. Joints are laid out in the design so they read as lines, not cracks."))
    body += note("Owner input pending: confirmation of architectural-concrete capacity for Sarasota County projects. This page describes the service in the provider's catalog; scheduling is confirmed at estimate time.", "warn")
    body += sec("Comparisons", cards([("/concrete/sidewalks-walkways/", "Entry walks and stoops", "The plain version of the same entries."), ("/pavers/marble-porcelain/", "Marble and porcelain", "Stone and tile finishes for the same lanai floors."), ("/concrete/stamped/", "Stamped", "Patterned rather than honed.")]))
    body += extra(key)
    body += faq_block(faq)
    body += cta("Ask about an architectural concrete project", "/contact/", "Send a sketch or a photo of what you're after; capacity is confirmed with the estimate.")
    body += reviewed("September 10, 2026")
    return page(key, "Architectural Concrete in Sarasota, FL – Honed & Board-Formed", "Architectural concrete for modern Sarasota homes: honed slabs, board-formed walls, cast steps and planters, with coastal mix rules and dated planning ranges. Capacity confirmed at estimate.",
                "Architectural concrete for Sarasota's modern houses", "Concrete · architectural", "Honed, board-formed and cast finishes where the concrete is the design, specified for salt air and Sarasota light.", body, faq)


def get_pages():
    return [pool_decks(), driveways(), patios(), stamped(), slabs(), sidewalks(), repair(), resurfacing(), architectural()]
