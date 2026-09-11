# -*- coding: utf-8 -*-
"""Fifth depth pass: the coastal hub, the HOA guides and the individual guides.

Sources are named inline. Where a figure comes from a vendor page rather than a measurement it is
attributed as such. Where a rule comes from a code section the section is cited. Nothing here is
reused from another route: the blocks are keyed to one URL each.
"""
from _h import cap, sec, p, ul, ol, table, note, link, cards

D = {}

# ============================================================ COASTAL
D["/coastal/"] = (
    sec("Four mechanisms, and the pages that cover each",
        p("Everything that shortens the life of hardscape on this coast reduces to four processes. Separating them matters, because the remedy for one is useless against another.")
        + table(["Mechanism", "What it does", "Where it bites hardest", "Page"], [
            ["Chloride ingress", "Salt moves into concrete and porous stone, weakening the surface paste and, over years, corroding steel", "Within about a mile of open water; at the splash line of a salt-chlorinated pool", link("/coastal/salt-and-concrete/", "Salt and concrete")],
            ["Base loss", "Water carries fines out of a sand base, leaving voids that the surface follows", "Everywhere on Myakka and Immokalee sands; catastrophically after surge", link("/coastal/post-storm-restoration/", "Post-storm restoration")],
            ["Surge displacement", "Moving water lifts unrestrained pavers and edge restraint and deposits sand and salt", "Barrier islands and canal lots", link("/coastal/storm-season-playbook/", "Storm season playbook")],
            ["Ultraviolet and thermal cycling", "Sun breaks down sealer films and drives daily expansion and contraction", "Every unshaded surface; worst on dark colours", link("/coastal/maintenance-calendar/", "Maintenance calendar")],
        ], "The four coastal mechanisms"))
    + sec("The numbers that define this coast",
          table(["Fact", "Figure", "Source"], [
              ["Helene storm surge measured on Longboat Key", "6.68 feet, September 2024", "Reported measurement"],
              ["Milton landfall", "Near Siesta Key, October 9, 2024", "National Hurricane Center reporting"],
              ["Surge inundation, Venice south to Boca Grande, 2024", "6 to 9 feet above ground level", "Storm reporting"],
              ["August rainfall, Sarasota-Bradenton", "9.11 inches", "NOAA 1991-2020 normals"],
              ["August average high", "91.5 °F", "NOAA 1991-2020 normals"],
              ["Wet-season water table, Myakka fine sand", "Within 10 inches of the surface for 2 to 6 months", "USDA Official Series Description"],
              ["Paver sealer life within a mile of open water", "18 to 24 months against 2 to 3 years inland", "Florida sealing-contractor guidance"],
              ["Turtle nesting season", "May 1 to October 31", "Sarasota County Code Ch. 54 Art. XXIII"],
              ["Maximum impervious coverage, RSF lot", "50 percent, pool decks and pavers counted", "Zoning Appendix A § 6.5"],
          ], "Reference figures used across the coastal pages"))
)

D["/coastal/salt-and-concrete/"] = (
    sec("Three sources of chloride, and why the pool is usually the worst of them",
        table(["Source", "How it arrives", "Concentration", "What it attacks first"], [
            ["Gulf spray", "Airborne aerosol carried inland on the prevailing wind", "Diluted, but continuous and everywhere on the seaward rows", "Sealer films, then surface paste on unsealed concrete"],
            ["Bay and canal water", "Direct contact at seawalls, and splash", "Brackish", "Slab edges, seawall caps, the base under a paver field"],
            ["Salt-chlorinated pool water", "Splash-out and swimmer carry-off onto the deck", "Highest of the three at the point of contact", "Coping and the first course of deck, at the waterline"],
        ], "Chloride sources on the Suncoast")
        + p("A salt-chlorinated pool generates sodium hypochlorite by electrolysis and leaves residual salt on every surface the water touches. Over years that salt crystallises inside porous stone and pushes the surface off in flakes, which is why limestone-family materials degrade noticeably faster around salt pools than around chlorine pools. The deck ten feet from the water may be fine while the coping is failing."))
    + sec("What it does to concrete, in order",
          ol([
              "<strong>Surface paste weakens.</strong> A slab finished with too much water at the surface has a weak, porous top layer. Chloride and moisture cycle through it and it dusts, then scales.",
              "<strong>Scaling becomes spalling.</strong> Flakes lift in sheets. On a pool deck this shows first at the coping and at any edge that gets splash.",
              "<strong>Steel corrodes.</strong> Once chloride reaches reinforcement, the steel expands as it rusts and cracks the concrete from inside. Rust staining bleeding through a surface is the visible sign, and at that point a surface repair is cosmetic.",
          ])
          + p("The defences are all specified before the pour, not after. A water-cement ratio at or below 0.45, no water added at the chute, adequate cover over steel, a full seven-day cure and a breathable penetrating sealer. None of them is expensive. All of them are invisible in a photograph, which is why they are the lines that get cut from a cheap quote."))
    + sec("What it does to stone and pavers",
          table(["Material", "Behaviour in salt", "Practical rule"], [
              ["Travertine, shellstone and other limestones", "Calcium carbonate; salt crystallises in the pores and fractures the surface", "Seal coping annually on a salt pool, rinse weekly with fresh water, pH-neutral cleaners only"],
              ["Dense concrete pavers", "Largely unaffected in the body; colour fades without sealer", "Seal on the coastal cycle for appearance rather than survival"],
              ["Marble", "Denser than travertine; etches from acid rather than flaking from salt", "Neutral cleaners; penetrating sealer"],
              ["Porcelain", "Non-porous and chemically inert", "No sealing needed; salt is a non-issue"],
              ["Clay brick", "Durable; efflorescence possible", "Normal maintenance"],
          ], "Salt behaviour by material")
          + p("The single most useful habit on a coastal deck costs nothing: run a hose over the coping and the first course after heavy pool use. It removes the salt before it has time to crystallise, and it is the difference between coping that lasts twenty years and coping that flakes in three."))
)

D["/coastal/storm-season-playbook/"] = (
    sec("Before June 1",
        ol([
            "<strong>Check the joint sand.</strong> Joints that have dropped more than a quarter inch let water into the base. Top them up with polymeric sand and let them cure dry before the season starts.",
            "<strong>Check the edge restraint.</strong> Walk the perimeter and push. Anything that moves is the line a surge will open first. Spiked restraint at a seawall or a street edge should be replaced with a poured curb.",
            "<strong>Clear the drainage.</strong> Deck drains, yard drains and the roadside swale all have to be flowing before the first storm, not after it.",
            "<strong>Photograph everything.</strong> Dated wide shots and close-ups of every hardscape surface, stored off the property. This is the single highest-value hour of preparation, because it is the before picture an adjuster will ask for.",
            "<strong>Seal if it is due.</strong> A sealed surface sheds silt and salt more easily. If the cycle is due in the summer, do it in May rather than September.",
            "<strong>Move loose items.</strong> Furniture, planters and grills become projectiles and gouge a deck on the way past.",
        ]))
    + sec("The first week after a surge, in order",
        table(["Day", "Action", "Why the order matters"], [
            ["0 to 1", "Photograph before touching anything; note water lines on walls and fences", "The adjuster's file is built from this; cleaning first destroys the evidence"],
            ["1 to 3", "Clear debris by hand, not by pressure washer", "High pressure drives salt and silt into the joints and strips the remaining sand"],
            ["3 to 7", "Let the base drain; walk it and mark low or hollow areas with chalk", "A saturated base cannot be assessed or compacted"],
            ["7 to 21", "Sound the surface and survey for voids; get the restoration scope written", "Voids are invisible from above and decide repair against rebuild"],
            ["After drying", "Lift, flush the base with fresh water, rebuild in lifts, reset units, new polymeric sand on a dry day", "Resetting on wet salty base means doing it twice"],
            ["+30 days", "Clean and seal", "Sealing traps salt and moisture if it is done early"],
        ], "Post-surge sequence"))
    + sec("What is a repair and what is a rebuild",
          p("The test is the base, not the surface. A paver field where the units shifted but the base sounds solid is a lift-and-reset, typically $8 to $15 per square foot of the affected area. A field over voids, or a slab that was undermined, is a rebuild regardless of how the surface looks.")
          + p("Concrete behaves worse than pavers here for a structural reason: a slab spans its voids until it cracks, so the damage is hidden until it fails, and the remedy is demolition. A paver field telegraphs the void as a dip you can see and fix in sections with the original units. That asymmetry is the strongest argument for pavers on a barrier island or a canal lot, and it is worth more than any appearance argument.")
          + p(f'The documentation side is on the {link("/guides/hurricane-insurance-documentation/", "insurance documentation guide")}; the mechanics are on {link("/pavers/repair-storm-restoration/", "paver repair and storm restoration")}.'))
)

D["/coastal/post-storm-restoration/"] = (
    sec("Why the base, not the pavers, is the damage",
        p("Concrete pavers and natural stone are not harmed by immersion. Twenty-four hours under salt water changes nothing structural about a paver. What changes is everything underneath it: the bedding sand migrates, the joint sand washes out, fines leave the base, and salt stays behind in what remains.")
        + p("That is why the restoration cost on a storm-damaged paver deck tracks the base area rather than the number of pavers, and why the first honest question after a surge is how much of the base survived. Sounding with a hammer and probing with a rod answers it in an hour. Reporting it in writing, with the marked areas on a sketch, is what turns a guess into a scope.")
        + table(["Finding", "Typical extent", "Remedy", "Planning cost"], [
            ["Joint sand washed out, units in place", "Whole field", "Clean joints, polymeric re-sand", "$1 to $3 per sq ft"],
            ["Units shifted, base sound", "Local", "Lift, re-screed bedding, reset", "$8 to $15 per sq ft of the area"],
            ["Voids under the field", "Local to extensive", "Lift, rebuild base in lifts, flush salt, reset", "$8 to $15 per sq ft plus base material"],
            ["Edge restraint lifted", "Perimeter runs", "Replace with poured concrete curb", "$12 to $20 per linear foot"],
            ["Slab undermined", "Local to whole slab", "Demolish and replace, or lift where the void can be filled", "Replacement rates apply"],
            ["Sand deposited over the surface", "Whole field", "Remove by hand and shovel before any washing", "Labour only"],
        ], "Post-surge findings and remedies"))
    + sec("Salt in the base, and what to do about it",
          p("Seawater in a limerock base leaves chloride behind as it drains. It will not dissolve the base, but it keeps the material damp longer, it accelerates corrosion of anything steel in contact with it, and it migrates upward into porous stone during dry spells, where it crystallises and damages the surface from below.")
          + p("The remedy is unglamorous: flush the exposed base with fresh water before the units go back, let it drain, then compact. On a small deck that is an hour with a hose. Skipping it is the most common reason a professionally reset travertine deck starts flaking at the surface a year later, with nobody able to explain why."))
    + sec("Dealing with a contractor after a storm",
          ul([
              "<strong>Get the assessment in writing before the work is scoped.</strong> A sketch with the sounded areas marked is the difference between a scope and an invoice.",
              "<strong>Refuse same-day starts.</strong> Anyone offering to reset a field three days after a surge has not let the base drain and is producing a repeat job.",
              "<strong>Keep the insurer in the loop before demolition.</strong> Once the old surface is in a dumpster the claim rests entirely on your photographs.",
              "<strong>Ask about the edge detail.</strong> A reset that puts the same spiked restraint back in the same sand is the same failure scheduled for the next storm.",
              "<strong>Expect a queue.</strong> After Helene and Milton the restoration queue on the keys ran for months. The owners who were scheduled early were the ones with documentation ready in the first week.",
          ]))
)

D["/coastal/maintenance-calendar/"] = (
    sec("The calendar, by distance from open water",
        table(["Task", "Within 1 mile of the Gulf or a bay", "Inland", "Best month here"], [
            ["Clean, re-sand and seal pavers", "Every 18 to 24 months", "Every 2 to 3 years", "April or November; dry, and the sand cures"],
            ["Reseal travertine or shellstone coping on a salt pool", "Annually", "Every 2 years", "April, before peak pool use"],
            ["Reseal stamped or coloured concrete", "18 to 24 months", "2 to 3 years", "November"],
            ["Penetrating sealer on plain concrete", "Every 3 years", "Optional", "November"],
            ["Top up joint sand", "As joints drop a quarter inch", "Same", "Any dry week"],
            ["Fresh-water rinse of pool coping", "Weekly in the swimming season", "Monthly", "Ongoing"],
            ["Clear deck drains and yard drains", "Twice a year", "Annually", "May and October"],
            ["Check edge restraint", "Annually", "Every 2 years", "May, before storm season"],
            ["Photograph everything for the insurance file", "Annually", "Annually", "May"],
        ], "Coastal maintenance intervals")
        + p("The interval column is the part people get wrong. Sealing guidance written for inland Florida quotes three years, and on a Siesta Key or Longboat Key lot that is roughly double what the product survives. Florida sealing contractors put coastal life at 18 to 24 months, and closer to annual for coping in contact with salt-chlorinated water."))
    + sec("Month by month",
          table(["Month", "What to do", "Why now"], [
              ["January to March", "Inspect, plan, get estimates; small repairs", "Dry, mild, and the calendar fills fast for spring work"],
              ["April", "Seal and re-sand; reseal salt-pool coping", "Dry weather, and ahead of both turtle season and the rains"],
              ["May", "Storm prep: joints, restraint, drains, photographs. Turtle lighting rules begin May 1", "Last dry month before the wet season"],
              ["June to August", "Schedule construction, not maintenance. Morning pours only", "7.05, 7.39 and 9.11 inches of rain; highs near 91 °F"],
              ["September", "Watch the forecast; defer sealing", "Peak storm risk and the wettest stretch"],
              ["October", "Post-storm assessment if needed; clear drains", "Season ends November 30 but October is when 2024's damage landed"],
              ["November to December", "Seal and re-sand what April missed; finish work before owners return", "Dry, and the deadline most seasonal owners actually care about"],
          ], "Annual hardscape calendar for Sarasota County, from NOAA 1991-2020 normals"))
)

D["/coastal/pool-deck-surface-temperature-study/"] = (
    sec("The full protocol, published before the data exists",
        p("Publishing a method in advance is a commitment that the results cannot be shaped after the fact. This is the complete protocol.")
        + table(["Element", "Specification"], [
            ["Surfaces, nine", "Gray broom concrete; light broom concrete; cool-deck overlay; gray concrete paver; light concrete paver; tumbled travertine; shellstone; honed marble; 2 cm porcelain"],
            ["Sample preparation", "Each material laid on the same compacted base in the same open location, minimum 24 by 24 inches, fully sun-exposed, dry, no shading from structures or planting"],
            ["Instrument", "Calibrated infrared thermometer, emissivity set for masonry, recorded model and calibration date"],
            ["Readings", "Three per surface per time slot; median reported; ambient air temperature, sky condition and wind noted"],
            ["Time slots", "10:00, 14:00 and 17:00 local time"],
            ["Days", "One clear July day and one clear January day, both recorded with date and conditions"],
            ["Publication", "Table on this page, medians and raw readings, plus JSON at the API endpoint under CC BY 4.0"],
            ["Scheduled", "January 2027 and July 2027"],
        ], "Sarasota Pool Deck Surface Temperature Study, protocol v1"))
    + sec("Why an infrared thermometer and not a probe",
          p("The question a homeowner is asking is what the surface does to the sole of a foot, which is a surface-temperature question, not a bulk-material one. An infrared thermometer reads the surface directly and can sample nine materials in under two minutes, which keeps the readings comparable because the sun has barely moved between them.")
          + p("Its weakness is emissivity: an infrared reading depends on an assumed surface emissivity, and a polished surface reads low. That is why the protocol sets emissivity for masonry, reports the instrument and its calibration date, and takes three readings per surface. It is also why honed marble and porcelain will carry a note in the results: they are the two surfaces where the instrument is least comfortable, and a contact measurement may be added for them.")
          + p("What the study will not claim is how a deck feels. Perceived heat depends on conductivity and contact area as much as on temperature, which is why a porous travertine at 118 degrees can feel better than a dense porcelain at the same reading. The temperature table is one input into that, and the page will say so."))
    + sec("What is published today",
          p("The protocol above, and nothing else. No temperature figure appears on this site attributed to this study until the readings exist, and no vendor figure is adopted as though it were ours.")
          + p(f'The physics of why surfaces differ is on the {link("/compare/pool-deck-surfaces-heat/", "surface heat comparison")}, which also attributes the circulating Florida vendor figures to their source and explains why they are not treated as measurements. The method for every dataset on this site is on {link("/data-and-methods/", "data and methods")}.'))
)

# ============================================================ HOA
D["/hoa/"] = (
    sec("What an ARC application needs, every time",
        p("Across Sarasota and Charlotte County associations the packet is remarkably consistent, and a complete submission is usually approved in one cycle while an incomplete one loses a month. These are the items that show up on almost every form.")
        + table(["Item", "Detail", "Where to get it"], [
            ["Application form, signed by the owner", "Most boards will not accept a contractor's signature", "The association's management company"],
            ["Survey or approved site plan", "With the proposed work drawn on it to scale and dimensioned", "Your closing documents, or a new survey"],
            ["Dimensions", "Width, length and total square footage, plus any change to the existing footprint", "The estimate"],
            ["Material and colour", "Manufacturer, product name and colour, ideally with a physical sample or chip", "The contractor"],
            ["Drainage note", "Arrows showing slope direction and where runoff goes, especially if levels change", "The contractor"],
            ["Contractor licence and insurance", "Many associations require a licensed and insured installer on file", "The contractor"],
            ["Right-of-way note", "Whether the work touches the apron or a sidewalk, and the permit that covers it", "The permit page for your jurisdiction"],
            ["Neighbour acknowledgement", "Some associations require adjacent owners to sign", "The form will say"],
        ], "Standard ARC packet"))
    + sec("Timelines, and how to lose the least time",
          p("Committees typically meet once or twice a month and many operate a review window of up to thirty days from a complete submission. Three habits save the most time.")
          + ol([
              "<strong>Get the approved materials list before choosing anything.</strong> In communities like Wellen Park and the Palmer Ranch sub-associations the list is short, and choosing outside it guarantees a rejection.",
              "<strong>Submit the packet with the estimate, not after signing.</strong> A contract with a start date that assumes approval is a contract with a delay in it.",
              "<strong>Ask whether master approval is also needed.</strong> Palmer Ranch and Wellen Park both operate a sub-association plus a master, and the two reviews are sequential, not parallel.",
          ])
          + p("Three rejection reasons cover most cases: a colour that is not on the list, a driveway wider than the covenant allows, and a drainage change that was never drawn. All three are avoidable before submission."))
    + sec("Communities in this service area with architectural review",
          p("Not exhaustive, and each community's own documents govern. Palmer Ranch Master Property Owners Association, established October 7, 1986, plus Prestancia, Turtle Rock, Stoneybrook, Deer Creek, Huntington Pointe, Isles of Sarasota, Sandhill Preserve and Esplanade on Palmer Ranch. Wellen Park and the West Villages Improvement District, including Islandwalk, Grand Palm, Gran Paradiso, Renaissance and Sarasota National. Venetian Golf and River Club, Boca Royale, Plantation, Heron Creek, Skye Ranch, Laurel Oak, The Meadows Community Association, Villagewalk, Bay Isles, the Longboat Key Club communities and Country Club Shores. In Charlotte County, the Rotonda West Association's deed restrictions, plus Riverwood, Heritage Oak Park and the South Gulf Cove and Cape Haze associations.")
          + p(f'Two communities have their own page here because their process is unusual enough to be worth detail: {link("/hoa/palmer-ranch/", "Palmer Ranch")} and {link("/hoa/wellen-park/", "Wellen Park")}. Barrier-island condominiums work differently again and are covered on the {link("/hoa/barrier-island-condos/", "condominium page")}.'))
)

D["/hoa/palmer-ranch/"] = (
    sec("Two reviews, not one",
        p("Palmer Ranch is a 10,000-acre master-planned community in unincorporated Sarasota County, developed since 1986, and its governance is layered. A homeowner in Turtle Rock or Prestancia belongs to a sub-association with its own architectural review committee and, for many exterior changes, also falls under the Palmer Ranch Master Property Owners Association. Public guidance for the community states that any exterior modification, including painting, landscaping and structural additions, requires approval from the architectural review committee.")
        + p("The practical consequence for a driveway or a pool deck is scheduling. Two reviews that each meet monthly can consume six to eight weeks even when nothing is wrong with the application. Submitting both packets at the same time, rather than waiting for the sub-association before approaching the master, is the single biggest time saving available."))
    + sec("What Palmer Ranch committees consistently care about",
          table(["Element", "What to expect", "How to present it"], [
              ["Paver colour and blend", "Sub-associations maintain short approved lists, generally neutral tans and grays", "Name the manufacturer, product and colour, and attach a chip"],
              ["Driveway width", "Covenants commonly limit width to the garage side walls, often with a stated maximum", "Dimension the existing and proposed width on the survey"],
              ["Border and banding", "Usually accepted; a contrasting soldier course is common in the community", "Show the pattern on the drawing"],
              ["Drainage", "Changes in level or runoff direction attract questions", "Slope arrows and a note on where water goes"],
              ["Pool deck material", "Travertine and light pavers are widely approved", "Sample plus the manufacturer sheet"],
              ["Contractor", "Licensed and insured installer on file", "Certificate of insurance with the association named"],
          ], "Palmer Ranch review, recurring items")
          + note("Each sub-association's recorded documents govern. This page describes the pattern across the community from public guidance read on September 10, 2026; it is not a substitute for your own covenant."))
    + sec("Why so much Palmer Ranch work is happening now",
          p("The housing stock was built largely between 1990 and 2010 on graded fill over Myakka and Oldsmar fine sands. Builder-grade broom driveways from that era are now 15 to 35 years old, and the failure pattern is consistent: settlement at the garage where the footing backfill was never compacted, cracks across panels jointed too far apart, and surface staining from well-water irrigation. Original 1990s cool-deck pool deck overlays are at the end of their service life at the same time.")
          + p("That coincidence is why a Palmer Ranch estimate usually covers a driveway and a pool deck together, and why doing both in one mobilisation is materially cheaper than doing them two seasons apart."))
)

D["/hoa/wellen-park/"] = (
    sec("One community, two cities, one master association",
        p("Wellen Park straddles the City of Venice and the City of North Port boundary, which means two different building departments permit work inside what residents experience as a single community. The master association and the village associations review the work regardless of which city issues the permit.")
        + p("For a homeowner that produces a specific sequence: establish which city your parcel sits in, because the permit path and the right-of-way rules differ, then submit the architectural application to the village association and the master where required. Venice requires engineering approval and often a licence agreement for pavers in the right-of-way; North Port permits the driveway crossing and the culvert under a Right of Way Use Permit and inspects the swale restoration.")
        + note("Village and master documents govern. The items below reflect ARC guidance published for Florida master-planned communities and read on September 10, 2026, not a specific Wellen Park covenant. Request your village's current guidelines before choosing a material.", "warn"))
    + sec("What ARC guidance in communities of this type consistently restricts",
          table(["Element", "Typical restriction"], [
              ["Driveway extension", "Extending, expanding, staining, resurfacing or repaving a walkway, driveway, driveway apron, pool deck, sport court or patio requires ARC approval"],
              ["Driveway width", "Commonly limited so the driveway does not extend beyond the line of the garage side wall, with a stated maximum width"],
              ["Paver colour", "Neutral tones that blend with the architectural style; an approved list is normal"],
              ["Pool and cage", "Pool construction, pavers, fencing and screen enclosures almost always require review"],
              ["Timing", "Submit before work begins; retroactive approval is at the committee's discretion"],
          ], "Recurring ARC restrictions in master-planned Florida communities"))
    + sec("New-construction upgrades, and the order to do them in",
          p("Wellen Park and the surrounding West Villages have delivered thousands of homes since 2018, and the common project is upgrading builder-grade flatwork: a broom driveway to pavers, a bare lanai to a paver or travertine floor, an extension for a fire pit or a spa.")
          + ol([
              "<strong>Check the warranty period on the builder's flatwork first.</strong> Removing a driveway inside the builder's warranty can forfeit a claim on settlement you could have had repaired at no cost.",
              "<strong>Do the lanai before the pool cage is screened if both are planned.</strong> Anchoring into a finished paver field costs more and looks worse than anchoring into a curb poured for the purpose.",
              "<strong>Batch the ARC application.</strong> One packet covering the driveway, the lanai and the extension is one review cycle instead of three.",
              "<strong>Confirm the city.</strong> On the Venice side a paver apron triggers a licence agreement; on the North Port side the culvert is sized by the city. Both belong in the schedule before a start date is promised.",
          ]))
)

D["/hoa/barrier-island-condos/"] = (
    sec("A common-area deck is a reserve item, not a purchase",
        p("Florida Statute 718.112(2)(f) requires condominium associations to maintain reserves for roof replacement, building painting, pavement resurfacing and any other item with a deferred maintenance cost exceeding $10,000. Pool decking, with a service life of roughly 20 to 30 years, sits squarely in that list, and a reserve study should carry it as a line with a remaining-life estimate.")
        + p("That changes the conversation from what a deck costs to when the reserve funds it and what happens if the remaining life was estimated before the 2024 storms. Boards on Siesta Key and Longboat Key are commonly discovering that a deck scheduled for replacement in 2031 has a base that surge emptied in 2024, and the reserve schedule has not caught up.")
        + p("The practical advice for a board: get the deck sounded and surveyed, put the finding in writing, and let the reserve study be updated from a measurement rather than from an age assumption. A stale component list is the most common reason an association is underfunded for the work it actually needs."))
    + sec("Phasing, so the amenity stays open",
        table(["Phase", "Typical duration", "What stays open", "Note"], [
            ["Mobilisation and demolition, section A", "3 to 5 days", "Section B and the pool, with temporary fencing", "Dust and noise control matter more than speed here"],
            ["Base, drains and edge, section A", "3 to 4 days", "Same", "Temporary edge restraint at the phase line"],
            ["Surface, section A", "2 to 4 days", "Same", "Cure or joint-sand window before traffic"],
            ["Repeat for section B", "8 to 13 days", "Section A", "The phase line is re-worked when the sections meet"],
            ["Final joint, seal and handover", "2 to 3 days", "Whole deck", "Sealing waits 30 days on pavers"],
        ], "Two-phase common-area deck, indicative schedule")
        + p("Phasing adds mobilisations, typically 10 to 20 percent on the total, and it is almost always worth it on a building where the pool is the amenity residents actually use. Scheduling the work between May and September lowers the per-foot rate because it is the contractor's quiet window and occupancy is lowest, which partly offsets the phasing premium."))
    + sec("What belongs in a board's bid package",
          ul([
              "<strong>A sounding and void survey</strong> of the existing deck, with the findings marked on a plan, so every bidder prices the same base condition instead of guessing.",
              "<strong>The flood determination.</strong> The building's zone, and whether it is under substantial-improvement or substantial-damage review, because on Longboat Key that file governs the permit.",
              "<strong>Drainage design.</strong> Number and location of deck drains and where they discharge, specified by the association rather than left to each bidder.",
              "<strong>Lighting.</strong> On a beach-visible property, FWC Certified Wildlife Lighting specified from the start, not chosen at handover in August.",
              "<strong>Accessibility.</strong> Slopes and transitions at the pool entry and along the required route, since a common-area deck is not a private patio.",
              "<strong>The phasing plan and firm dates,</strong> written into the contract rather than discussed.",
              "<strong>Material and maintenance cycle.</strong> Porcelain and dense concrete pavers carry the lowest maintenance on a salt pool; a travertine deck commits the association to annual coping sealing in perpetuity.",
          ])
          + p(f'The twenty-year cost comparison by surface is on the {link("/pricing/pool-decks/", "pool deck cost guide")}, and the phasing calendar in detail is on the {link("/guides/condo-pool-deck-boards/", "twelve-month calendar for boards")}.'))
)


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
