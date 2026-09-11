# -*- coding: utf-8 -*-
"""Depth blocks for the highest-value singleton pages (home, pillars, pricing, county hubs, FAQ hub).

Every block here is page-specific: no block is reused on two routes, and nothing is filler.
The content is the material that a homeowner comparing three estimates actually needs and that
no audited Sarasota competitor publishes: line-item anatomy of a quote, Florida deposit and lien
law, seasonal scheduling economics, per-jurisdiction fee tables, soil series behaviour, and the
storm timeline that set the current condition of half the hardscape on the coast.
"""
from _h import cap, sec, p, ul, ol, table, note, link, cards, facts

DEPTH = {}


# ---------------------------------------------------------------------------- /pricing/
DEPTH["/pricing/"] = (
    sec("What a complete estimate has on it, line by line",
        p("Three estimates for the same driveway can differ by thousands and all three can be honest, because they are not describing the same job. The cheapest one usually leaves out the base, the joints, the demolition or the permit. This is the line list to compare across quotes; anything missing is a question, not a discount.")
        + table(["Line", "What it should say", "Why it moves the price"], [
            ["Square footage", "Measured, not estimated from the plat", "A 10 percent measuring error is 10 percent of the job"],
            ["Demolition and haul-off", "Included or excluded, with a per-square-foot figure", "$2 to $4 per sq ft; pavers over concrete cost more to remove"],
            ["Subgrade preparation", "Excavate to firm material, proof-roll, geotextile where the sand pumps", "The line most often missing; it decides whether the slab settles"],
            ["Base", "Material, depth, number of lifts, compaction method", "4 in. vs 6 in. of limerock in lifts is a real cost and a real difference"],
            ["Thickness", "4 in., 5 in. or 6 in., and where each applies", "About $1.50 to $2.50 per sq ft between 4 and 6 inches"],
            ["Mix", "PSI and whether fiber is included", "4,000 PSI over 3,000 is a few dollars a yard and years of surface life"],
            ["Reinforcement", "Fiber, wire mesh or #3/#4 bar on chairs, with spacing", "Mesh laid on the ground costs the same as mesh done right and does nothing"],
            ["Joints", "Spacing and whether they are cut the same day", "Same-day saw cutting is a scheduling commitment, not a material cost"],
            ["Drainage", "Slope in inches per foot, deck drains, where water goes", "A deck without a drain is cheaper today and re-poured in five years"],
            ["Permit", "Which office, who applies, whether the fee is included", "County culvert and line-and-grade fees run $90 to $310 before review"],
            ["Restoration", "Swale regrading, sod, irrigation repair", "Commonly excluded and commonly needed"],
            ["Schedule", "Start window and working days on site", "A firm window is worth money in season"],
            ["Payment terms", "Deposit, progress payments, final", "See the Florida deposit rules below"],
            ["Warranty", "Written, with the period and the exclusions", "A verbal warranty is not a warranty"],
            ["Legal name and contact", "The entity that signs the contract", "You cannot check a license or a lien history against a trade name alone"],
        ], "Estimate comparison checklist"))
    + sec("Deposits, progress payments and liens under Florida law",
          p("Florida Statute 489.126 limits what a contractor may take up front on residential work: when a contractor collects more than 10 percent of the contract price as a deposit, work must begin or materials must be ordered within 30 days (90 days where a permit is required and applied for), and payments must be applied to the job. The practical reading for a driveway or a pool deck is that a request for half the money before anything arrives on site is outside the norm for this trade.")
          + p("Florida's Construction Lien Law (Chapter 713) is the other half. On contracts over $2,500 the contract must carry the statutory lien warning, and a Notice of Commencement is recorded before the first inspection on permitted work above $5,000 in Charlotte County. Ask for lien releases from the contractor and from any material supplier at final payment. This protects you even when nothing goes wrong, because a supplier who was not paid can lien the property regardless of what you paid the contractor.")
          + note("None of this is legal advice. It is the paperwork a careful homeowner asks for, and a contractor who is uncomfortable producing it has told you something useful."))
    + sec("Why the same job costs more in January than in July",
          p("Sarasota County's population rises past 570,000 in the winter, and the people who arrive are the ones who notice the driveway. From January through April the calendar fills, crews are booked out, and the price of a fast start goes up. From June through September owners are away, the rain arrives every afternoon, and the schedule loosens.")
          + table(["Window", "Demand", "Weather", "What it means for price and schedule"], [
              ["January to April", "Peak; seasonal owners in residence", "Dry, 62 to 73 degrees average", "Longest lead times; least flexibility on start dates"],
              ["May", "Falling", "Drying out, turtle season opens May 1", "Good window; island lighting rules begin"],
              ["June to September", "Lowest", "7 to 9 inches of rain a month, highs near 91", "Best availability; morning pours; rain days built into the schedule"],
              ["October to November", "Rising; storm repairs compete", "Drying, hurricane season to November 30", "Post-storm demand can outrun capacity in a bad year"],
              ["December", "Rising", "Dry, mild", "Owners want work finished before the holidays"],
          ], "Seasonality in the Sarasota hardscape market, from NOAA 1991-2020 normals and county population data")
          + p("The practical move for a seasonal owner is to price the job in March, sign it in April and let it run in June while the house is empty. That sequence buys the best availability and puts the finished surface in front of you when you come back in November."))
)


# ---------------------------------------------------------------------------- /pricing/concrete/
DEPTH["/pricing/concrete/"] = (
    sec("Worked examples with the arithmetic shown",
        p("Ranges are easier to trust when you can see how the number is built. These are planning calculations from the September 10, 2026 ranges, not quotes, and they assume normal access and no surprises under the old slab.")
        + table(["Project", "Size", "Calculation", "Planning total"], [
            ["Two-car driveway replacement, Gulf Gate", "24 × 25 = 600 sq ft", "600 × $9 (mid range, 4 in. on 4 in. base) = $5,400, plus demolition 600 × $3 = $1,800", "$7,200"],
            ["Driveway widening, Palmer Ranch", "4 × 60 = 240 sq ft", "240 × $11 (small area, dowelled to existing) = $2,640, no demolition", "$2,640"],
            ["Pool deck replacement, 1970s ranch", "700 sq ft", "700 × $11 = $7,700, demolition 700 × $3 = $2,100, two drains $1,200, cage anchors $600", "$11,600"],
            ["Lanai extension, Nokomis", "12 × 20 = 240 sq ft", "240 × $10 = $2,400, floor drain $500", "$2,900"],
            ["Generator pad", "5 × 8 = 40 sq ft", "40 × $14 (mobilization on a small pad) = $560, anchor template and conduit sleeve $150", "$710"],
            ["Front walk replacement", "4 × 40 = 160 sq ft", "160 × $11 = $1,760, demolition $400", "$2,160"],
        ], "Planning calculations, September 10, 2026"))
    + sec("Ready-mix, labor and the floor under every price",
        p("Concrete is one of the few trades where a homeowner can sanity-check the floor. Ready-mix in the Sarasota market ran roughly $150 to $190 per cubic yard delivered in 2026. A 4-inch slab uses one cubic yard per 81 square feet, so the concrete alone in a 600-square-foot driveway is about 7.4 yards, or $1,100 to $1,400. Add 20 tons of base at delivered cost, forms, fiber and steel, a crew of three for two to three days, the pump or buggy, demolition, haul-off and disposal fees, insurance, and the margin that keeps a crew available next year.")
        + p("That arithmetic is why a $4 per square foot driveway quote in this market is not a bargain. It is either 3 inches on raw sand, or it is missing the demolition, or the number will change once the crew is on site. The useful comparison is not the total but the per-square-foot rate with the base depth and the thickness attached to it."))
    + sec("Where concrete beats pavers on cost, and where it does not",
          table(["Situation", "Cheaper choice", "Why"], [
              ["Large plain driveway, inland lot, Zone X", "Concrete", "Lower installed rate per square foot and no joint-sand maintenance"],
              ["Deck that has to match an existing slab", "Concrete overlay", "Color and texture can run across both; pavers create a height step"],
              ["Lot that floods or has a history of surge", "Pavers", "A surge-damaged paver field is lifted and reset; a slab is demolished"],
              ["Utility access under the surface", "Pavers", "Units lift and go back; concrete is cut and patched forever"],
              ["Tight budget, small patio", "Concrete", "Mobilization dominates either way, and the slab is cheaper per foot"],
              ["Lot at the 50 percent impervious cap", "Permeable pavers", "The only option that adds surface without adding counted impervious area"],
          ], "Cost-driven material choice"))
)


# ---------------------------------------------------------------------------- /pricing/pavers/
DEPTH["/pricing/pavers/"] = (
    sec("Worked examples with the arithmetic shown",
        p("Planning calculations from the September 10, 2026 ranges. They assume a normal lot, standard access and an existing surface that comes out without surprises.")
        + table(["Project", "Size", "Calculation", "Planning total"], [
            ["Paver driveway, two-car, Nokomis", "600 sq ft", "600 × $17 (6 in. base, vehicular units, herringbone) = $10,200, demolition 600 × $3 = $1,800, curb 60 lin ft × $15 = $900", "$12,900"],
            ["Paver pool deck, concrete units", "700 sq ft", "700 × $14.50 = $10,150, demolition $2,100, coping 90 lin ft × $35 = $3,150, drain $600", "$16,000"],
            ["Travertine pool deck", "700 sq ft", "700 × $23 = $16,100, demolition $2,100, coping 90 × $45 = $4,050", "$22,250"],
            ["Paver patio, no demolition", "400 sq ft", "400 × $14.50 = $5,800", "$5,800"],
            ["Front walkway", "4 × 40 = 160 sq ft", "160 × $17 (cutting-heavy, narrow) = $2,720", "$2,720"],
            ["Clean, re-sand and seal a driveway", "600 sq ft", "600 × $2 = $1,200", "$1,200"],
        ], "Planning calculations, September 10, 2026"))
    + sec("The maintenance column nobody puts in the quote",
          p("Pavers are quoted as an installation and owned as a maintenance cycle. Over twenty years on a coastal lot the cycle is a real number, and it belongs next to the install price when you compare pavers with concrete.")
          + table(["Item", "Interval within a mile of open water", "Interval inland", "Cost per cycle, 600 sq ft"], [
              ["Clean, re-sand and seal", "18 to 24 months", "2 to 3 years", "$600 to $1,800"],
              ["Top up joint sand only", "As joints drop a quarter inch", "Same", "$200 to $500"],
              ["Reset a settled area", "As it appears", "As it appears", "$8 to $15 per sq ft of the affected area"],
              ["Reseal travertine coping on a salt pool", "Annually", "Every 2 years", "$150 to $400"],
          ], "Paver maintenance cycle, Sarasota County")
          + p("Twenty years of that on a 600-square-foot driveway is roughly $7,000 to $15,000 in today's money, against a concrete driveway that wants a penetrating sealer every few years and nothing else. What you buy for the difference is a surface that can be lifted, reset and repaired unit by unit, which is worth more on a lot that floods than it is on a dry lot east of I-75."))
    + sec("Material cost at the yard versus installed cost",
          p("The spread between what a paver costs on a pallet and what it costs finished on your lot is labor, base and cutting, and it is the part most estimates do not break out. Knowing the yard price tells you how much of a quote is material and how much is work.")
          + table(["Material", "Approximate yard price per sq ft, 2026", "Typical installed", "Material share"], [
              ["Concrete paver, standard", "$3 to $6", "$13 to $16", "About 25 to 35 percent"],
              ["Travertine, tumbled", "$6 to $12", "$20 to $26", "About 30 to 45 percent"],
              ["Shellstone", "$6 to $12", "$20 to $26", "Similar to travertine"],
              ["Porcelain, 2 cm", "$8 to $15", "$22 to $32", "About 35 to 50 percent"],
              ["Marble, honed", "$10 to $20", "$24 to $34", "About 40 to 55 percent"],
          ], "Regional 2026 material pricing against installed ranges")
          + p("The pattern to notice: on concrete pavers you are mostly buying labor and base, so the quality of the crew decides the outcome. On marble and porcelain you are mostly buying the material, and the crew's job is to not waste it and to build a base flat enough that a rigid unit does not rock."))
)


# ---------------------------------------------------------------------------- /pricing/pool-decks/
DEPTH["/pricing/pool-decks/"] = (
    sec("Twenty-year cost of ownership by surface",
        p("A pool deck is bought once and paid for over two decades. This table projects a 700-square-foot deck on a coastal Sarasota lot using the September 10, 2026 installed ranges and the maintenance intervals from the coastal maintenance calendar. It assumes the base stays sound and no storm resets the clock.")
        + table(["Surface", "Install", "Maintenance to year 20", "Replacement before year 20?", "Twenty-year total"], [
            ["Cool-deck or textured overlay", "$3,000 to $7,000", "Reseal every 2 to 3 years, $400 to $900 each", "Likely once, at 8 to 15 years", "$11,000 to $22,000"],
            ["New textured concrete deck", "$7,000 to $10,000", "Penetrating sealer every 3 years, $400 to $800", "No", "$10,000 to $15,000"],
            ["Concrete pavers", "$9,000 to $11,000", "Clean, re-sand, seal every 18 to 24 months, $700 to $2,100", "No", "$17,000 to $28,000"],
            ["Travertine", "$14,000 to $18,000", "Same cycle plus annual coping seal", "No", "$23,000 to $36,000"],
            ["Porcelain, 2 cm", "$15,000 to $22,000", "Rinse and joint sand only", "No", "$16,000 to $25,000"],
        ], "Twenty-year projection, 700 sq ft coastal deck, September 10, 2026 ranges")
        + p("Two things fall out of the arithmetic. Overlays are the cheapest entry and the most expensive decade, because the resealing never stops and the surface has a life. Porcelain has the highest install and one of the lowest carrying costs, which is why it keeps winning on condo decks where the association is budgeting a reserve rather than a purchase."))
    + sec("What a deck estimate should tell you before you sign",
          ul([
              "<strong>The condition of the slab underneath, in writing.</strong> Hollow areas found by sounding, cracks with an offset, and the slope measured with a level, not estimated by eye.",
              "<strong>Where the water goes.</strong> The number of drains, where they discharge, and the slope in inches per foot. A deck under a cage without a drain is a decision, and it should be a stated one.",
              "<strong>What happens at the pool edge.</strong> Coping material, whether it is being replaced, and the joint detail between coping and field.",
              "<strong>What happens at the cage.</strong> Anchor count, whether a new curb or edge beam is being poured, and who re-screens if a panel is damaged.",
              "<strong>Salt.</strong> Whether the pool is salt-chlorinated, and what that changes in the sealer and the maintenance schedule.",
              "<strong>The cure and the reopening date.</strong> When furniture goes back, when the pool can be used, and what happens if it rains on day one.",
          ]))
    + sec("Condo and HOA decks price differently",
        p("A common-area deck is not a bigger residential deck. It is bid against a reserve study, phased so the amenity stays partly open, scheduled around occupancy, and governed by accessibility and pool-code requirements that do not apply to a private deck. Florida Statute 718.112 requires condominium associations to fund reserves for deferred-maintenance items over $10,000, and pool decking with a 20 to 30 year life sits squarely in that list.")
        + p("Practically, that changes three numbers. Phasing adds mobilizations, typically 10 to 20 percent. Off-season scheduling from May through September lowers the per-foot rate because it is the contractor's quiet window. And the specification is usually tighter, because a board is buying a surface that has to survive a thousand feet a week rather than a family's.")
        + p(f'The {link("/guides/condo-pool-deck-boards/", "guide for boards and property managers")} covers the bid package, the phasing plan and the reserve conversation in detail.'))
)


# ---------------------------------------------------------------------------- /pricing/sarasota-concrete-cost-index/
DEPTH["/pricing/sarasota-concrete-cost-index/"] = (
    sec("Why a local index exists at all",
        p("Search for what a pool deck costs in Sarasota and you will find national aggregators quoting a range built from Ohio and Arizona jobs, contractor pages quoting a number with no date, and marketplace estimates derived from lead volume rather than invoices. None of them tell you the sample, the period or the geography, so none of them can be checked.")
        + p("An index that names its sample size, its quarter and its limitations can be checked, and can be wrong in public. That is the point. It also gives every other page on this site a source to cite that is not a competitor's marketing copy, and it gives other people something to cite too, which is why it carries a CC BY 4.0 licence and a stable JSON endpoint."))
    + sec("What the quarterly release will contain",
        table(["Field", "Definition", "Example"], [
            ["quarter", "Calendar quarter of job completion", "2027-Q1"],
            ["service", "Service slug from this site", "pavers-pool-decks"],
            ["material", "Material where it changes the rate", "travertine"],
            ["locality", "Tier 1 locality or county rollup", "siesta-key"],
            ["n", "Number of completed jobs in the cell", "4"],
            ["median_psf", "Median installed price per square foot", "23.40"],
            ["p25_psf, p75_psf", "Quartiles, reported only when n is 4 or more", "21.80, 25.10"],
            ["excludes", "What is not in the per-foot figure", "demolition, permit fees, coping, drains"],
            ["notes", "Anything that moved the cell", "two jobs included bridge staging"],
        ], "Cost Index record schema, v0.1")
        + p("Cells with fewer than three jobs are reported at county level only, so a single unusual project cannot move a locality number. Releases are dated and never overwritten; when a figure is corrected, the correction is a new release with a note, and the prior release stays available at its own URL."))
    + sec("How to cite it, and what it cannot tell you",
          p("Cite it as: Sarasota Concrete, Sarasota Concrete Cost Index, version and date, retrieved from the JSON endpoint. The licence allows reuse with attribution, including by other contractors, journalists and property managers.")
          + p("What it cannot tell you: what the whole Sarasota market charges. It is one provider's completed work. A provider that declines the cheapest jobs will show a higher median than the market, and a quarter with three island decks in it will show island logistics baked into the number. Those limitations are printed on every release rather than hidden in a methodology page, because an index that pretends to be a market survey is worse than no index at all."))
)


# ---------------------------------------------------------------------------- /areas/sarasota-county/
DEPTH["/areas/sarasota-county/"] = (
    sec("Permit fees and what they are for",
        p("Fees change by resolution and should be confirmed with the office before you budget. These were the published figures on September 10, 2026 and are listed so a homeowner can tell a permit line on an estimate from a markup.")
        + table(["Jurisdiction", "Item", "Published figure", "Notes"], [
            ["Sarasota County", "Driveway culvert permit", "Set by separate resolution under Code § 98-3", "Includes county survey for line and grade, and resurvey during installation"],
            ["Sarasota County", "Right-of-way use permit", "Set by separate resolution under Code § 98-3", "Any work in county right-of-way other than a culvert"],
            ["Sarasota County", "Residential exemption", "Work under $7,500 on a single-family home", "Requires a written exemption request, the contract and documented value"],
            ["Charlotte County", "Zoning review", "$22", "Every residential permit"],
            ["Charlotte County", "Non-structural slab review", "$22", "Includes pavers"],
            ["Charlotte County", "Structural slab review", "$90", ""],
            ["Charlotte County", "Line and grade at issuance", "$310", "Or $90 for a right-of-way permit"],
            ["Charlotte County", "Building fee", "0.004 × ICC valuation", "Applies at $50,000 and above"],
            ["Charlotte County", "Surcharge", "0.025 × building fee", "State surcharge"],
        ], "Published permit figures, read September 10, 2026"))
    + sec("The soil series under your lot, and what each one does",
        p("The USDA Natural Resources Conservation Service maps Sarasota County's flatwoods into a handful of sandy, poorly drained series. They behave differently enough to change a base spec, and the Web Soil Survey will name the one under a specific parcel in about two minutes.")
        + table(["Series", "Where it dominates", "Drainage", "What it means for a base"], [
            ["Myakka fine sand", "Most of the county's flatwoods; Florida's state soil", "Poorly drained; water table within 10 in. for 2 to 6 months", "Compact in lifts, proof-roll, geotextile where it pumps"],
            ["EauGallie fine sand", "East of the city, Fruitville and Bee Ridge", "Poorly drained with a spodic horizon", "Water perches on the hardpan; drainage off the lot matters more than depth"],
            ["Immokalee fine sand", "North Port, inland south county", "Poorly drained, deep sand", "Drains on the surface, soft when saturated; over-compact the subgrade"],
            ["Oldsmar fine sand", "Palmer Ranch and graded developments", "Poorly drained", "Usually covered by developer fill; test what is actually there"],
            ["Wabasso fine sand", "Scattered flatwoods", "Poorly drained", "Similar handling to EauGallie"],
            ["Beach sand and fill", "Siesta, Lido, Longboat, Casey, Manasota keys", "Excessively drained", "Drains fast, carries salt, loses fines to surge; concrete edge restraint"],
        ], "Soil series in Sarasota County, USDA Official Series Descriptions")
        + p("The practical rule that comes out of the table is the same one every failed driveway on this coast could have used: the sand under your lot has bearing capacity when it is dry and compacted, and much less of it when it is saturated. A base built in thin lifts and compacted to refusal is the difference between a surface that lasts thirty years and one that settles in five."))
    + sec("Storm timeline and why it still shapes the work",
        table(["Date", "Event", "What it did to hardscape here"], [
            ["September 28, 2022", "Hurricane Ian, landfall in Lee County", "Surge and wind reached Charlotte Harbor and the Englewood coast; south-county paver fields lost joint sand"],
            ["September 26, 2024", "Hurricane Helene, offshore passage", "Measured 6.68-foot surge on Longboat Key; ground-floor flooding on the keys; salt into bases"],
            ["October 9, 2024", "Hurricane Milton, landfall near Siesta Key", "Pushed Helene's debris inland, sand into first floors within 150 yards of the beach, muddy waterlines about 2.5 feet up walls"],
        ], "Recent storm events affecting Sarasota County hardscape")
        + p("Two storms two weeks apart in 2024 is why so much of the island work today is restoration rather than new construction, and why the standard detail on this coast is now a concrete curb at every exposed edge instead of spiked plastic restraint. It is also why any estimate on a barrier island starts by sounding the base rather than by pricing the surface."))
)


# ---------------------------------------------------------------------------- /areas/charlotte-county/
DEPTH["/areas/charlotte-county/"] = (
    sec("The Charlotte County permit packet, item by item",
        p("Charlotte County publishes what it wants, which makes it the easiest jurisdiction in the region to prepare for and the least forgiving if something is missing. This is the residential driveway and slab packet as published on September 10, 2026.")
        + table(["Item", "When it applies", "Detail"], [
            ["Application for Construction Permit", "Always", "Two original signed and sealed sets in person, one online"],
            ["Site plan", "Always", "May be hand drawn if legible; must show easements, property lines and be drawn to scale"],
            ["Notice of Commencement", "Direct contract price over $5,000", "Signed and recorded, submitted before the first inspection"],
            ["Affidavit for Accessory Structures", "Where the slab serves an accessory structure", "Shed, detached garage and similar"],
            ["Owner-Builder Disclosure Statement", "Owner pulls the permit", "Owner provides direct on-site supervision"],
            ["Tree Permit Application Package", "Tree removal or lot clearing", "Separate review"],
            ["Signed and sealed drawings", "Structural work", "Digitally signed for online applications"],
        ], "Charlotte County residential flatwork packet, published figures read September 10, 2026")
        + p("Two rules catch people out. Flatwork within one foot of an existing structure requires termite treatment, which is a scheduled inspection rather than a line item to skip. And pavers crossing a recorded easement may need an occupation-of-easement approval from Real Estate Services, which is a separate department and a separate timeline."))
    + sec("The GDC grid, the swales, and why driveways flood the neighbour",
        p("General Development Corporation platted Port Charlotte, North Port and parts of the Englewood area from the 1950s through the 1980s: tens of thousands of quarter-acre lots on a grid, drained not by storm sewers but by shallow roadside swales that carry water to the canal system. The swale in front of your house is infrastructure, and the driveway crosses it.")
        + p("When a driveway is poured flat across a swale, or over a culvert that is too small or has collapsed, the swale stops conveying water and it backs up onto the lot upstream. That is why Charlotte County and the City of North Port size the culvert themselves, inspect the crossing, and require the swale restored to grade before final approval. It is also why a driveway on a GDC lot is a drainage project with a slab on top, and why a quote that does not mention the culvert is not a quote for the job you have."))
    + sec("Canal lots, brackish water and what it does to a deck",
        p("Gulf Cove, South Gulf Cove, Grassy Point, Rotonda's canal ring and the Cape Haze waterfront all sit on filled lots beside brackish water with a water table close to the surface. Three things follow. Bases stay wetter, so compaction in thin lifts matters more. Salt reaches the surface from the water as well as from a salt-chlorinated pool, so the sealing cycle runs on the coastal schedule of 18 to 24 months rather than the inland two to three years. And a seawall edge is the first place a surge lifts an unrestrained paver field, so the detail there is a poured curb rather than spiked restraint.")
        + p("The upside of a canal lot is the same as the upside of any island lot: a paver surface that has been built to be rebuilt is repairable after a storm in days rather than demolished in weeks."))
)


# ---------------------------------------------------------------------------- /faq/
DEPTH["/faq/"] = (
    sec("Questions that do not fit a single service page",
        p("These come up on the phone often enough to belong somewhere, and each is answered once here rather than repeated across the site.")
        + "".join(f'<div class="qa"><h3>{q}</h3><p>{a}</p></div>' for q, a in [
            ("Can I do part of the work myself to save money?",
             "You can, and the two places it usually works are demolition and the final landscaping. Breaking out and hauling an old driveway saves $2 to $4 per square foot, and it is unskilled work with a rented saw and a trailer. What rarely works is owner-prepared base: a base that has not been compacted in lifts to refusal is the single most common cause of the failures on this coast, and no contractor will warrant a surface built on ground they did not prepare."),
            ("What happens if the crew finds something under the old slab?",
             "It is the most common change order in this trade. Typical finds are an abandoned irrigation line, a septic drain field closer than the plat suggests, buried debris from the original build, or soft organic soil that has to be dug out and replaced. A good estimate says in advance what the unit rate is for unforeseen excavation, so the change order is arithmetic rather than a negotiation while the crew stands still."),
            ("Do you work with pool builders and landscape designers?",
             "Yes, and on a new pool the sequence matters: the shell and the equipment lines go first, the deck base and the drains follow, and the deck surface goes down after the cage anchors are located. Coming in after a cage is already built means anchoring into a finished surface, which is doable and more expensive."),
            ("How do you handle an HOA that rejects the application?",
             "Most rejections are about a colour that is not on the approved list, a driveway wider than the covenant allows, or a drainage note that was never drawn. All three are fixable before submission, which is why the ARC packet is prepared with the estimate rather than after it. If a board rejects something that the covenant plainly allows, the packet and the covenant reference are what you take back to them."),
            ("Is there a minimum job size?",
             "Not formally, but mobilization dominates small work. A single AC pad or a two-panel sidewalk repair is priced with that in mind, and it is usually cheaper for the homeowner to combine several small items into one visit than to book them separately across a season."),
            ("What is the difference between a service-area business and a contractor with a yard?",
             "A service-area business works at the customer's property and does not keep a public storefront. It is a normal and legitimate structure for this trade, and it is why this site shows no street address. What it does not change is accountability: the legal entity, its insurance and, where one exists, its licence are on the contract before any money changes hands."),
            ("Can you match work done by a previous contractor?",
             "Colour and texture can be approached, rarely matched, because cement source, finishing time and years of weathering all differ. The honest options are the same three every time: replace the visible area entirely, run a decorative overlay across old and new, or place the transition at a control joint so the eye reads it as a designed line."),
            ("How far in advance should I book seasonal work?",
             "For a January through April start, six to ten weeks. For a June through September start, two to four. Storm seasons compress everything: after Helene and Milton in 2024 the restoration queue on the keys ran for months, and the owners who were scheduled first were the ones who had documented their damage in the first week."),
        ]))
)


# ---------------------------------------------------------------------------- /concrete/
DEPTH["/concrete/"] = (
    sec("What happens on a pour day, hour by hour",
        p("Most of what decides whether a slab lasts happens in about six hours, and almost none of it is visible a week later. This is a normal summer pour in Sarasota County.")
        + table(["Time", "Step", "What goes wrong if it slips"], [
            ["6:30 a.m.", "Crew on site, forms checked, reinforcement chaired and tied, base dampened", "Steel lying on the base does nothing; dry base pulls water out of the mix"],
            ["7:00 a.m.", "First truck; slump checked; no water added at the chute", "Water added on site for workability is the classic cause of a surface that dusts and scales"],
            ["7:00 to 9:30 a.m.", "Place, screed, bull float", "Overworking the surface brings fines and water up and weakens the top"],
            ["9:30 to 11:00 a.m.", "Bleed water rises and evaporates; crew waits", "Finishing while bleed water is on the surface traps it and causes delamination"],
            ["11:00 a.m. to 1:00 p.m.", "Float, edge, broom or stamp", "In 91-degree heat this window is short; a late stamp is a shallow pattern"],
            ["1:00 to 3:00 p.m.", "Saw-cut control joints", "Cutting the next morning means the slab has already chosen where to crack"],
            ["3:00 p.m.", "Curing compound or wet cure; protection against afternoon rain", "Rain within the first two hours scars the surface permanently"],
        ], "A summer pour day in Sarasota County")
        + p("The reason morning pours are non-negotiable here from June through September is in the last two rows. NOAA's 1991 to 2020 normals give Sarasota-Bradenton 7.05 inches of rain in June, 7.39 in July and 9.11 in August, and almost all of it falls after 2 p.m. A pour that starts at 10 a.m. is finishing into a thunderstorm."))
    + sec("How to read a crack",
          p("Not every crack is a defect, and treating them all the same is how homeowners either panic or ignore a real problem. These are the four patterns that show up on Sarasota flatwork and what each one is telling you.")
          + table(["Pattern", "Looks like", "Usually means", "What to do"], [
              ["Shrinkage crack", "Hairline, wandering, no height difference", "Normal drying shrinkage that did not find a joint", "Seal it; watch it; it is cosmetic"],
              ["Crack at a joint", "Straight, in the saw cut", "The joint did its job", "Nothing; this is the design working"],
              ["Crack with an offset", "One side sits higher than the other", "The base moved or washed out", "Find the water first; then lift or replace"],
              ["Map cracking or scaling", "Fine web, surface flaking", "Too much water at the surface, or chloride attack near salt", "Resurface if the slab sounds solid; replace if not"],
          ], "Reading cracks in Sarasota flatwork")
          + p("The test that separates the first two from the last two takes a hammer and a straightedge, costs nothing, and is the first thing done on any repair call on this site."))
)


# ---------------------------------------------------------------------------- /pavers/
DEPTH["/pavers/"] = (
    sec("What happens on an install, day by day",
        p("A paver job is four distinct trades stacked in sequence, and each one can undo the last. This is a typical 600-square-foot driveway in Sarasota County.")
        + table(["Day", "Step", "What decides the outcome"], [
            ["1", "Demolition, haul-off, excavation to firm material", "Digging deep enough; a base placed on soft ground is already failing"],
            ["2", "Geotextile where the sand pumps; base in 3-inch lifts, each compacted to refusal", "Number of lifts; one thick lift stays soft in the middle and shows up in year two"],
            ["3", "Screed 1 inch of concrete sand; lay the field in herringbone; cut the borders", "Bedding depth stays at 1 inch; sand is never used to level a low base"],
            ["4", "Edge restraint or poured curb; plate-compact the field; sweep polymeric sand", "Restraint fixed to the base, not into the bedding; compaction with a protective pad"],
            ["4 to 5", "Activate the polymeric sand; 24 to 48 dry hours", "Rain during the cure washes the joints out and the day is repeated"],
            ["+30 days", "Clean and seal if the owner wants it", "Sealing early traps efflorescence under the film"],
        ], "A paver driveway, day by day")
        + p("The single line in that table that separates a twenty-five-year driveway from a five-year one is the second: lifts. It is also the line that never appears in a cheap quote, because it is two hours of a compactor and nobody can see it once the pavers are down."))
    + sec("Patterns, and why herringbone is not a style choice on a driveway",
          table(["Pattern", "Interlock under load", "Cutting waste", "Where it belongs"], [
              ["Herringbone, 45 or 90 degrees", "Highest; units resist rotation under turning tires", "Higher at the borders", "Driveways, aprons, anything vehicular"],
              ["Running bond", "Low; the field creeps in the direction of travel", "Lowest", "Walkways, patios, pedestrian areas"],
              ["Basketweave", "Low", "Low", "Patios, courtyards, decorative panels"],
              ["Random ashlar or French pattern", "Moderate", "Moderate; needs sorting on site", "Pool decks and patios in travertine and stone"],
              ["Large-format stack bond", "Depends entirely on the base", "Low", "Lanais and modern pool decks in porcelain and marble"],
          ], "Paver patterns and where each one works")
          + p("A driveway laid in running bond because the homeowner preferred the look will creep toward the street over a few years of turning tires, and the joint lines will tell you exactly which way the cars turn. If the look matters more than the mechanics, the compromise is a herringbone field with a running-bond soldier course at the border."))
)


# ---------------------------------------------------------------------------- /  (home)
DEPTH["/"] = (
    sec("How to compare the estimates you are about to collect",
        p("Most people reading this page will get two or three quotes. The useful ones are comparable line by line; the rest are a number on a page. Five questions separate them, and none of them require knowing anything about concrete.")
        + ol([
            "<strong>How deep is the base, and in how many lifts?</strong> On this soil a base compacted in 3-inch lifts is the difference between thirty years and five. A quote that does not name a depth is not describing the job.",
            "<strong>Is demolition and haul-off in the number?</strong> It is $2 to $4 per square foot, and it is the most common reason two quotes look thousands apart.",
            "<strong>Which office issues the permit, and who applies for it?</strong> Six different offices cover this service area and they do not have the same rules. A contractor who cannot name yours has not looked at your address.",
            "<strong>When are the control joints cut, or where does the edge restraint fix?</strong> Same-day joints on concrete, restraint fixed to the base on pavers. Both are invisible in a week and decisive in a decade.",
            "<strong>What is the legal name on the contract?</strong> You cannot check insurance, licensing or lien history against a trade name.",
        ])
        + p(f'The full line-by-line checklist, with Florida\'s deposit and lien rules, is on the {link("/pricing/", "pricing hub")}.'))
)


def apply(pages):
    """Append the depth block for each route that has one. Called by build.py after modules load."""
    n = 0
    for pg in pages:
        block = DEPTH.get(pg["route"])
        if not block:
            continue
        html = pg["body_html"]
        marker = '<p class="reviewed">'
        i = html.rfind(marker)
        pg["body_html"] = (html[:i] + block + html[i:]) if i != -1 else (html + block)
        n += 1
    return n
