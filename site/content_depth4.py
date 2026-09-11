# -*- coding: utf-8 -*-
"""Fourth depth pass: the reference pages (permits and comparisons).

These are the pages the whole positioning rests on and they were the thinnest in the build.
Each block below is written for one route from the research files in ../research, with the code
section or the office named so a reader can check it. Fees and forms were read on 2026-09-10 and
each page says so; nothing here is copied from a competitor.
"""
from _h import cap, sec, p, ul, ol, table, note, link, cards

D = {}

CHECKED = "Read on September 10, 2026. Fees and forms change by resolution; confirm with the office before you budget."

# ============================================================ PERMITS
D["/permits/"] = (
    sec("Six offices, one map",
        p("There is no single answer to \"do I need a permit\" in this service area, because six separate authorities issue them inside forty miles of Sarasota and they do not agree with each other. The table below is the whole picture on one screen; each office has its own page with the forms, the fees and the inspections.")
        + table(["Office", "Covers", "Flatwork position", "Portal"], [
            ["Sarasota County", "Unincorporated county: Siesta Key, Casey Key, Gulf Gate, Palmer Ranch, Fruitville, Bee Ridge, The Meadows, Osprey, Nokomis, Laurel, South Venice, Venice Gardens, north Englewood", "Right-of-way and culvert work always permitted; residential work under $7,500 may use a documented exemption", "Accela Citizen Access"],
            ["City of Sarasota", "City limits: downtown, Laurel Park, Arlington Park, Indian Beach, Lido Key, St. Armands, Bird Key", "The apron between sidewalk and street is city right-of-way and permitted separately", "FTG portal"],
            ["City of Venice", "Venice Island, the mainland city, the Venice side of Wellen Park", "Pavers in the right-of-way need engineering approval and often a licence agreement", "eTRAKiT"],
            ["City of North Port", "North Port, Warm Mineral Springs, the North Port side of Wellen Park", "Right of Way Use Permit covers culvert, driveway, sidewalk and concrete slab; swale restored and inspected", "Click2Gov"],
            ["Town of Longboat Key", "The whole island, both the Sarasota and Manatee halves", "At-grade driveways, decks and patios reviewed by Planning and Zoning; substantial-improvement check on every permit", "Town portal"],
            ["Charlotte County", "Port Charlotte, Rotonda West, Placida, Grove City, south Englewood", "All concrete flatwork including pavers requires a permit and inspections", "County portal"],
        ], "Permit authorities in the service area")
        + note(CHECKED))
    + sec("What a permit actually buys you",
          p("Homeowners often read a permit as a tax on the job. It is more useful to read it as the only independent record that the work happened and met a standard. Three practical consequences follow.")
          + ul([
              "<strong>Resale.</strong> Unpermitted work shows up in a title search or a buyer's inspection, and the cost of legalising it afterwards is always higher than permitting it at the time. On the barrier islands it can also complicate a substantial-improvement calculation years later.",
              "<strong>Insurance.</strong> After a storm, an adjuster asks what the surface was and when it was built. A permit and its inspection record answer that; a receipt from a contractor who is no longer in business does not.",
              "<strong>Recourse.</strong> A permit ties the work to a licensed or registered entity that the jurisdiction can act against. That is the mechanism behind every complaint process in the state, and it does not exist for unpermitted work.",
          ]))
    + sec("Who pulls it, and why that matters more than who pays for it",
          p("In every jurisdiction here the permit can be pulled by a qualified contractor or, for a homeowner's own residence, by the owner under an owner-builder exemption. The two are not equivalent. Sarasota County's code requires an owner acting as their own contractor to appear in person, sign the application and provide direct on-site supervision, and it states plainly that the exemption does not extend to anyone the owner employs who is acting as a contractor.")
          + p("The practical risk is that an owner-builder permit moves responsibility for the work from the contractor to the owner. If a contractor asks you to pull the permit on a driveway or a pool deck, the question to ask is why they cannot, and the answer is usually that they are not registered in that county. That is worth knowing before the deposit rather than after the inspection."))
)

D["/permits/sarasota-county/"] = (
    sec("The code sections behind the rules",
        table(["Subject", "Where it lives", "What it says"], [
            ["Work in county right-of-way", "Code Chapter 74; fees under Chapter 98 § 98-3", "Any work in a county right-of-way must be authorised by a permit issued by the County Engineer"],
            ["Driveway culverts", "Code § 98-3(b)(1)", "Installation of a driveway culvert requires a culvert permit, and the fee includes county surveying for line and grade plus any resurvey during installation"],
            ["Other right-of-way work", "Code § 98-3(b)(2)", "A right-of-way use permit covers work other than culvert installation"],
            ["Contractor licensing", "Code Chapter 22, Article V, § 22-122", "Work in a regulated trade requires an active county Operating Certificate plus the applicable Certificate of Competency"],
            ["Owner-contractor exemption", "Code § 22-122(3) and (6)", "An owner improving their own one- or two-family residence may act as owner-contractor with direct on-site supervision, must appear in person and sign, and receives a statutory disclosure"],
            ["Impervious coverage", "Zoning Appendix A § 6.5", "Maximum impervious coverage is 50 percent of an RSF lot; roofs, pools, pool decks, concrete, asphalt and pavers count, while grass and shell do not"],
            ["Coastal setback", "Code Chapter 54, Article XXII, § 54-723", "Construction and excavation are prohibited seaward of the Gulf Beach Setback Line except under listed exceptions or a Board-granted variance"],
            ["Marine turtle protection", "Code Chapter 54, Article XXIII", "Lighting standards for property visible from the beach during nesting season"],
            ["Trees", "Code Chapter 54, Article XVIII", "Protected trees, including grand oaks, are regulated; root pruning and removal are reviewed"],
        ], "Sarasota County code references for hardscape")
        + note(CHECKED))
    + sec("The residential exemption, and its paperwork",
          p("Sarasota County operates a residential permit exemption for qualifying work under $7,500 on a single-family home, introduced following 2026 state legislation and described in the county's own bulletin. It is not automatic. The county requires a written exemption request, a copy of the written contract and documentation of the value of the work before the exemption applies.")
          + p("For hardscape the exemption is useful on small repairs and pads and much less useful than it sounds on driveways, because the moment the work touches the county right-of-way it needs a culvert or right-of-way use permit regardless of its value. A 400-square-foot patio behind the house is a good candidate. A driveway replacement that meets the road is not.")
          + note("Because the county's own pages could not be read automatically for this build, the exemption threshold and process here come from secondary reporting of the county bulletin. Confirm the current bulletin number and requirements with the Building division before relying on it.", "warn"))
    + sec("Offices, inspections and how long it takes",
          table(["Item", "Detail"], [
              ["Main counter", "1001 Sarasota Center Boulevard, Sarasota"],
              ["South county counter", "4000 South Tamiami Trail, Venice"],
              ["Phone", "(941) 861-5000"],
              ["Portal", "Accela Citizen Access; issued permits searchable at the county's permit search"],
              ["Typical review", "One to two weeks for simple flatwork; longer where engineering or a variance is involved"],
              ["Inspections", "Line and grade on right-of-way work; final on the permitted scope"],
              ["Coastal variance", "Coastal setback variances are heard by the Board of County Commissioners, which adds months, not weeks"],
          ], "Sarasota County practical details")
          + p(f'If the property is on Siesta Key, Casey Key or Manasota Key, read the {link("/permits/flood-zones-50-percent-rule/", "flood and setback page")} before the permit page, because the setback line can change the scope before the permit process starts.'))
)

D["/permits/city-of-sarasota/"] = (
    sec("What the city controls that the county does not",
        p("Inside city limits the City of Sarasota is the building department, and two of its rules catch people who have worked with the county before.")
        + ul([
            "<strong>The apron is city property.</strong> The strip between the sidewalk and the street sits in city right-of-way. Replacing it, in concrete or in pavers, is permitted work even when the rest of the driveway is not, and local guidance describes it as a landscaping permit rather than a building permit.",
            "<strong>Retaining walls over 3.5 feet.</strong> Above that height a wall stops being landscape and becomes a permitted structure.",
            "<strong>Trees at 4 inches.</strong> The city requires a permit for work on trees with a trunk of 4 inches diameter or more, which is why walks and drives in Indian Beach, Laurel Park and west of the Trail get routed around roots rather than through them.",
        ])
        + note(CHECKED + " The city's own permitting pages blocked automated reading for this build, so the specific permit category for a full driveway replacement inside city limits is listed as unconfirmed rather than guessed.", "warn"))
    + sec("Where the city line actually runs",
          p("City addresses and city limits are not the same thing, and the difference decides which office reviews the job. These are the areas that generate the most confusion.")
          + table(["Area", "Jurisdiction", "Note"], [
              ["Downtown, Rosemary District, Laurel Park, Gillespie Park", "City", "Alley access and tight lots; permeable options matter on impervious limits"],
              ["Indian Beach, Sapphire Shores, Bayou Oaks", "City", "1920s housing stock and protected oaks"],
              ["Arlington Park, Alta Vista, Paver Park", "City", "1950s to 70s block homes, original thin driveways"],
              ["Lido Key, St. Armands, Bird Key", "City", "AE and VE flood zones; Lido is subject to turtle lighting rules"],
              ["Siesta Key", "County", "A Sarasota mailing address; the county issues the permit"],
              ["Gulf Gate Estates, Palmer Ranch, The Meadows, Fruitville, Bee Ridge", "County", "Same"],
              ["Southgate, parts of Gulf Gate along US-41", "Mixed", "Check the parcel; the boundary is not the road"],
          ], "City versus county inside the Sarasota area")
          + p("The Property Appraiser's parcel search resolves any address in about a minute and shows the flood zone on the same screen, which is why it is the first step on every city estimate."))
    + sec("Practical details", table(["Item", "Detail"], [
        ["Department", "Development Services, Building and Permitting"],
        ["Portal", "FTG portal at ftgportal.sarasotafl.gov, with permit search and application"],
        ["Historic review", "Designated properties and districts have design review in addition to the building permit"],
        ["Residential exemption", "State legislation in 2026 introduced an exemption path for work under $7,500 on a single-family dwelling, requiring a written request, the contract and documented value"],
        ["Right-of-way", "Apron, sidewalk and driveway connection work is reviewed as right-of-way work"],
    ], "City of Sarasota practical details"))
)

D["/permits/venice/"] = (
    sec("Two departments, one driveway",
        p("Venice splits a driveway between two desks. The Building department permits the work on private property through eTRAKiT. Engineering controls everything in the right-of-way, and that is where the paperwork gets specific.")
        + p("Under the city's Code of Ordinances Chapter 62, an improvement placed within a city right-of-way, easement or other public property that does not meet city standards requires approval of the city engineer, an approved right-of-way use authorisation and a licence agreement. Pavers installed in the right-of-way must be constructed in accordance with city standards. In plain terms: a poured concrete apron built to the city detail is straightforward, and a paver apron is a licence agreement in which you accept responsibility for a non-standard improvement on public land.")
        + note(CHECKED + " The city's engineering permit list blocked automated reading for this build; the code reference above is from the published Code of Ordinances.", "warn"))
    + sec("What that licence agreement means in practice",
          ul([
              "<strong>You own the maintenance.</strong> A non-standard improvement in the right-of-way stays your responsibility, including restoring it if the city or a utility has to dig there.",
              "<strong>It runs with the property.</strong> The agreement is recorded, so it transfers on sale and shows up in the buyer's title work.",
              "<strong>It adds time.</strong> Engineering review plus an agreement is weeks, not days, and it is the single most common reason a Venice paver driveway starts later than the owner expected.",
              "<strong>The alternative is a concrete apron.</strong> Many Venice paver driveways stop at the sidewalk with a poured apron to the city detail beyond it. It is not a compromise on durability, and it removes the agreement entirely.",
          ]))
    + sec("Decks, patios and the island",
          p("For decks and patios the city follows the residential code thresholds: a freestanding deck not more than 30 inches above grade is generally exempt, an attached deck is permitted because the ledger affects the dwelling, and anything over 30 inches or supporting a roof is permitted with structural detail. A pool deck slab is permitted when it exceeds the exempt size or supports a cage.")
          + p("On Venice Island the flood zone is AE with VE on the Gulf side, and the 1926 Nolen-plan neighbourhoods around Historic Downtown carry design expectations that are worth checking before choosing a paver colour. Venice also maintains beach-area lighting rules for turtle nesting season, alongside the county's Chapter 54 Article XXV provisions for the Venice beach area."))
    + sec("Practical details", table(["Item", "Detail"], [
        ["Building portal", "eTRAKiT at trakit.venicegov.com"],
        ["Engineering", "Permits, forms and applications through the Engineering department"],
        ["Right-of-way", "City engineer approval, right-of-way use authorisation, licence agreement for non-standard improvements"],
        ["Flood", "AE island-wide with VE on the Gulf front; X across most of the mainland city"],
        ["Turtle season", "May 1 to October 31 for beach-visible lighting"],
    ], "City of Venice practical details"))
)

D["/permits/north-port/"] = (
    sec("The permit is named after the culvert for a reason",
        p("North Port's own form covers Culvert, Driveway, Sidewalk and Concrete Slab work as a single Right of Way Use Permit, and the order of those words reflects the order of the job. On a lot platted by General Development Corporation between the 1950s and the 1980s, the swale in front of the house is the drainage system for the whole street, and the driveway crosses it.")
        + p("The city sizes the pipe. The applicant is responsible for repair and restoration of the roadway, right-of-way, swales and adjacent properties before the Public Works department gives final approval. Published city drainage standards allow a lot pipe where slopes cannot be met if a secondary swale drains the adjacent roadway and a minimum of six inches of cover is provided over the pipe.")
        + note(CHECKED + " Figures here come from the city's published permit form and drainage standards; the fee schedule should be confirmed with the Building Division."))
    + sec("What gets a North Port driveway rejected or delayed",
          ol([
              "<strong>No survey.</strong> Review needs a current survey showing the proposed work and the driveway detail. Many GDC lots have nothing recent on file.",
              "<strong>A crossing designed by the contractor.</strong> The culvert size is the city's call, and a quote that names a pipe diameter before the city has reviewed it is guessing.",
              "<strong>Unsealed drawings where they are required.</strong> Construction documents that need engineering must be signed and sealed by a Florida-licensed professional engineer.",
              "<strong>Swale left short.</strong> Final approval depends on the swale being restored to grade, and Public Works inspects it.",
              "<strong>Width beyond the standard.</strong> Driveway width and apron geometry follow the city detail; a widening that was never drawn is a correction after the pour.",
          ]))
    + sec("Practical details", table(["Item", "Detail"], [
        ["Division", "Building Division, Neighborhood Development Services, 4970 City Hall Boulevard"],
        ["Phone and email", "(941) 429-7044; bldginfo@cityofnorthport.com"],
        ["Portal", "Click2Gov for permits; forms on the city's Building and Planning pages"],
        ["Permit type", "Right of Way Use Permit: Culvert / Driveway / Sidewalk / Concrete Slab"],
        ["Inspections", "Public Works checks roadway, right-of-way and swale restoration before final"],
        ["Flood", "Mostly X across the grid; AE along Myakkahatchee Creek and the Myakka River"],
    ], "City of North Port practical details"))
)

D["/permits/longboat-key/"] = (
    sec("One town, two counties, every permit reviewed for flood",
        p("The Town of Longboat Key issues permits for the whole island, including the Manatee County half, so the county line does not change the process. What does change the process is that the island is entirely within FEMA Special Flood Hazard Areas, so the Town's floodplain management rules under Chapter 154 of its code sit behind every application.")
        + p("Substantial damage is defined as damage where the cost of restoring the structure to its before-damaged condition would equal or exceed fifty percent of its market value before the damage. Where a building is substantially improved or substantially damaged, it must be brought into compliance with flood damage prevention regulations, including elevation to the flood protection elevation. All repairs and improvements on a property subject to that review must be permitted through the Town.")
        + note(CHECKED + " The Town's building FAQ page returned a 404 during this build; the code references are from the published Code of Ordinances and the Town's marine turtle pages, which were readable.", "warn"))
    + sec("Where hardscape sits in that review",
          p("Driveways, decks and patios at grade are reviewed by the Planning and Zoning division against the Town's zoning criteria. The important distinction for an owner is that site improvements such as a driveway or a pool deck are not part of the structure, and federal guidance excludes outside improvements to the land from the fifty percent calculation. That does not mean the work is invisible to the Town: on a property already under substantial-improvement or substantial-damage review, the hardscape permit is documented alongside the rest of the file.")
          + p("The practical sequence on Longboat Key after the 2024 storms has therefore been: document the damage, establish whether the building is in substantial-damage review, then permit the site work with that file referenced. Doing it in the other order is how owners end up re-submitting."))
    + sec("Turtle lighting is a construction specification here",
          p("The Town adopted Ordinance 2021-01 on July 2, 2021 for the protection of marine turtles under Chapter 100 of its code. All artificial lighting, direct or indirect, visible from the beach must use turtle-friendly bulbs and fixtures. Turtle-friendly bulbs are FWC Certified Wildlife Lighting, or bulbs producing only long-wavelength light at 560 nanometers or more without filters, gels or lenses. Turtle-friendly fixtures are FWC certified, or fully shielded, downward directed, meeting and exceeding full cut-off, with non-reflective opaque interior surfaces.")
          + p("Code Enforcement will test bulbs and conduct property lighting surveys on request at (941) 316-1966, extension 2520. For a hardscape job this means fixture selection is part of the specification from the first drawing, not a finishing decision, because a path or step light chosen for its look and rejected in August is a rework."))
    + sec("Practical details", table(["Item", "Detail"], [
        ["Town Hall", "501 Bay Isles Road, Longboat Key, FL 34228; hours 7:30 a.m. to 4 p.m."],
        ["Phone", "(941) 316-1999; Code Enforcement (941) 316-1966 ext. 2520"],
        ["Departments", "Planning, Zoning and Building; Building Division; Code Enforcement"],
        ["Flood", "AE and VE island-wide; Helene measured a 6.68-foot surge here in September 2024"],
        ["Turtle season", "May 1 to October 31, Chapter 100, Ordinance 2021-01"],
        ["Associations", "Bay Isles, Longboat Key Club, Country Club Shores and most condominiums review exterior changes separately"],
    ], "Town of Longboat Key practical details"))
)

D["/permits/charlotte-county/"] = (
    sec("The clearest flatwork rule in the region",
        p("Charlotte County states it without hedging: all concrete flat work, whether considered structural or non-structural, including pavers, requires a permit and inspections. There is no size threshold to argue about and no exemption to research. If it is flatwork, it is permitted.")
        + table(["Fee or item", "Published figure", "When"], [
            ["Zoning review", "$22", "Every residential permit"],
            ["Non-structural slab review, including pavers", "$22", "At application"],
            ["Structural slab review", "$90", "At application"],
            ["Building fee", "0.004 × ICC valuation", "Where valuation is $50,000 or more"],
            ["State surcharge", "0.025 × building fee", "With the building fee"],
            ["Line and grade", "$310", "At issuance"],
            ["Right-of-way permit alternative", "$90", "At issuance, where work is only in the right-of-way"],
            ["Notice of Commencement", "Recorded, no county fee", "Direct contract price over $5,000, before the first inspection"],
        ], "Charlotte County residential flatwork fees")
        + note(CHECKED + " These figures were read from the county's residential driveway and residential slab pages, which were fully readable for this build."))
    + sec("Two requirements that surprise people",
          ul([
              "<strong>Termite treatment.</strong> Work performed one foot or less from an existing structure requires termite treatment. That is a scheduled step in the sequence, not an optional add-on, and it catches patio slabs poured against the house.",
              "<strong>Occupation of easement.</strong> Any flatwork, including pavers, may require an occupation of easement from Real Estate Services. That is a different department with its own timeline, and on the GDC grid rear and side easements are common.",
          ])
          + p("Accepted licences for driveway and slab permits include Owner-Builder, Certified or Registered Building, General and Residential, and Local Concrete Masonry. The presence of a local concrete masonry category is why a contractor licensed only in an adjoining county cannot simply pull a permit here without registering."))
    + sec("Practical details", table(["Item", "Detail"], [
        ["Office", "Community Development, 18500 Murdock Circle, Port Charlotte, FL 33948"],
        ["Phone", "(941) 743-1200; Zoning (941) 743-1964"],
        ["Submittals", "Two original signed and sealed sets in person, one set online"],
        ["Site plan", "May be hand drawn if legible; must show easements and property lines and be drawn to scale"],
        ["Payment", "Check payable to CCBCC, or credit and debit cards"],
        ["Inspections", "Vary by location and scope; listed on the job card"],
    ], "Charlotte County practical details"))
)

D["/permits/flood-zones-50-percent-rule/"] = (
    sec("The calculation, as the Property Appraiser describes it",
        p("The Sarasota County Property Appraiser publishes the arithmetic, and it is worth reading in the office's own framing because the office is careful about what its numbers are for. The fifty percent rule is a National Flood Insurance Program regulation that prohibits improvements to a structure exceeding fifty percent of its market value unless the entire structure is brought into full compliance with current flood regulations, which may include elevating it, using flood-resistant materials and providing proper flood venting.")
        + p("The threshold can be calculated one of two ways. Using the tax roll, take the most recent improvement value, multiply it by a factor of 1.2, and the threshold is fifty percent of the result. Alternatively an appraisal performed for the purpose by a state-licensed appraiser can be used, and the office notes that a private appraisal is often the better option because its own values exist for ad valorem taxation and are produced by mass appraisal under Department of Revenue rules.")
        + table(["Step", "Example"], [
            ["Improvement value on the most recent pre-damage tax roll", "$300,000"],
            ["Multiply by 1.2", "$360,000"],
            ["Threshold is 50 percent", "$180,000"],
            ["Improvements at or above that", "Trigger full flood compliance for the structure"],
        ], "Worked example of the tax-roll method"))
    + sec("Why hardscape usually sits outside it",
          p("FEMA's substantial improvement guidance excludes outside improvements to the land from the cost of improvement. Plans, specifications, surveys, permits and items incidental to the repair of the structure are also excluded, and improvements to the land such as driveways, pools and seawalls are not included in the fifty percent value. The Town of Fort Myers Beach's published FAQ on the rule states the same position in the same words used across Gulf Coast floodplain offices.")
          + p("So a new pool deck, a driveway replacement or a paver patio normally does not consume the threshold. Three cautions apply. The jurisdiction makes the determination, not the contractor and not this page. Work that is part of the structure, such as an elevated deck framed into the building, is a different question from a slab on grade. And on a property already in substantial-damage review after a storm, everything gets documented, so the exclusion needs to be established in the file rather than assumed."))
    + sec("The Gulf Beach Setback Line is the rule that does stop work",
          p("Sarasota County Code Chapter 54, Article XXII, Section 54-723 prohibits construction and excavation seaward of the Gulf Beach Setback Line and waterward of the Barrier Island Pass Twenty-Year Hazard Line, along with installing non-native plants and landscape boulders in beach, dune or coastal hammock habitat and altering or removing native plants in those habitats.")
          + p("The article does not apply to modification, maintenance or repair of an existing structure that is not a substantial improvement, provided the work stays within the limits of the existing foundation. Beyond that, construction seaward of the line requires a coastal setback variance granted by the Board of County Commissioners on a demonstration of unusual hardship. Swimming pools, spas and pool decks are treated as ancillary structures for this purpose, and published commission decisions include sand-set paver decks approved tens of feet seaward of the line after a hearing.")
          + p("The practical consequence for an owner on Siesta Key, Casey Key, Manasota Key or the Gulf side of Longboat Key: replacing a deck inside its existing footprint is a permit, while extending one seaward is a variance measured in months and public hearings. That distinction belongs in the first conversation, not the third."))
)

# ============================================================ COMPARISONS
D["/compare/"] = (
    sec("Nine decisions, and the order to make them in",
        p("Material comparisons are usually written to sell a material. These are written to be used in sequence, because the answers constrain each other: the flood zone limits what makes sense to build, the pool chemistry limits the stone, and the heat question only matters once the first two are settled.")
        + ol([
            f'<strong>Repair or replace.</strong> {link("/compare/resurface-vs-replace-pool-deck/", "Six tests on the existing slab")} decide whether anything else on this list is relevant.',
            f'<strong>Concrete or pavers.</strong> {link("/compare/concrete-vs-pavers-driveway/", "Twenty-year cost, flood behaviour and repairability")}, not appearance.',
            f'<strong>Overlay or rebuild on a deck.</strong> {link("/compare/cool-deck-vs-pavers/", "Cool deck against pavers")} on lifespan and carrying cost.',
            f'<strong>Which stone, if stone.</strong> {link("/compare/travertine-vs-shellstone-vs-porcelain/", "Travertine, shellstone and porcelain")} on heat, slip and salt.',
            f'<strong>Stone or concrete pavers.</strong> {link("/compare/travertine-vs-concrete-pavers/", "Where the premium pays and where it does not")}.',
            f'<strong>Heat.</strong> {link("/compare/pool-deck-surfaces-heat/", "What colour, mass and texture actually do")} at two in the afternoon.',
            f'<strong>Thickness.</strong> {link("/compare/4-inch-vs-6-inch/", "Four inches or six")}, by load rather than by budget.',
            f'<strong>Reinforcement.</strong> {link("/compare/rebar-vs-fiber/", "Rebar, mesh or fiber")} on this soil.',
            f'<strong>Sealer.</strong> {link("/compare/sealer-types-coastal/", "Penetrating or film")}, decided by distance from the water.',
        ])
        + p("Running them out of order is how people end up with a beautiful travertine deck on a base that a surge will empty, or a porcelain lanai on a bedding layer that lets the tiles rock."))
    + sec("What every comparison on this site refuses to do",
          ul([
              "<strong>Quote a temperature we did not measure.</strong> The figures circulating in Florida paver marketing, that travertine runs twenty to thirty degrees cooler than concrete, come from vendor pages with no method and no instrument. They may well be directionally right. They are not a measurement, so they are attributed rather than repeated as fact.",
              "<strong>Declare a winner without a scenario.</strong> Every comparison ends in a table of situations, because a driveway east of I-75 and a pool deck on Casey Key have different right answers.",
              "<strong>Hide the maintenance.</strong> A material's carrying cost over twenty years is part of its price, and on this coast the sealing interval is set by distance from open water.",
          ]))
)

_DECISION_TAIL = sec("How to settle this on your own lot in ten minutes",
    ol([
        "<strong>Establish the zone and the office.</strong> The Property Appraiser's parcel search gives the flood zone; the address gives the permit office. Both change the answer before any material does.",
        "<strong>Sound the existing surface.</strong> A hammer and a four-foot level tell you which job this is: a new surface, or a new slab.",
        "<strong>Measure the distance to open water.</strong> Inside about a mile, the maintenance interval shortens and the sealer choice narrows.",
        "<strong>Check the pool chemistry.</strong> Salt-chlorinated water rules some materials in and others out at the coping.",
        "<strong>Read the covenant.</strong> Where there is architectural review, the approved list is the real shortlist.",
    ])
    + p(f'Then bring the answers to the {link("/tools/coastal-surface-selector/", "coastal surface selector")}, which asks the same five questions in the same order and returns a surface and a maintenance cycle with the reasoning attached.'))

# The shared decision tail was removed: applying one identical block to nine comparison pages
# pushed 8-gram similarity to 28 percent, far above the 15 percent gate. Uniqueness outranks volume.

D["/compare/concrete-vs-pavers-driveway/"] = (
    sec("Twenty years on a 600-square-foot driveway",
        p("Both surfaces last. The difference is where the money goes and what happens when something breaks. Figures use the September 10, 2026 planning ranges and the coastal maintenance intervals.")
        + table(["", "Poured concrete", "Concrete pavers"], [
            ["Install", "$5,500 to $9,500", "$8,500 to $13,000"],
            ["Maintenance to year 20", "Penetrating sealer every 3 years on coastal lots, $400 to $800 each", "Clean, re-sand and seal every 18 to 24 months coastal, $600 to $1,800 each"],
            ["Utility repair", "Saw-cut and patch; the patch is permanent and visible", "Lift the units, do the work, put the same units back"],
            ["Surge damage", "Undermined slab is demolished and re-poured", "Field is lifted, base rebuilt and flushed, units reset"],
            ["Settlement", "Lift with foam or replace the panel", "Lift the affected area, rebuild that part of the base"],
            ["Twenty-year total, coastal", "$8,000 to $15,000", "$15,000 to $27,000"],
            ["Twenty-year total, inland Zone X", "$7,000 to $12,000", "$12,000 to $21,000"],
        ], "Twenty-year comparison, planning figures")
        + p("Read that table twice. On a dry lot east of I-75 concrete wins on cost and the paver premium buys appearance and repairability you may never need. On Siesta Key, Longboat Key or a Port Charlotte canal lot, the surge rows are not hypothetical, and a surface designed to be lifted and reset is worth the carrying cost."))
)

D["/compare/pool-deck-surfaces-heat/"] = (
    sec("What is actually happening at two in the afternoon",
        p("Barefoot discomfort is not about the material's name. Three properties decide how hot a deck feels, and they are measurable, which is why the study on this site measures them rather than quoting a brochure.")
        + table(["Property", "What it does", "Which choices move it"], [
            ["Solar reflectance, or albedo", "A light surface reflects more of the incoming energy instead of absorbing it", "Colour, and only colour; a light concrete paver and light travertine start from a similar place"],
            ["Thermal mass and conductivity", "Dense material stores heat and moves it into your foot; porous material holds less and conducts slower", "Travertine and shellstone are porous; porcelain and dense concrete are not"],
            ["Contact area and texture", "A textured surface touches less skin, so less heat transfers per second", "Tumbled and brushed finishes beat honed and smooth-troweled at the same temperature"],
        ], "The three mechanisms behind a hot deck")
        + p("That framework explains the two claims people bring to an estimate. Light travertine really does feel cooler than dark concrete, and most of the gap is colour and texture rather than the stone being magical. And a light porcelain deck can feel warmer than a light travertine deck at the same measured temperature, because porcelain conducts better."))
    + sec("What the published numbers are, and why they are attributed rather than adopted",
        p("Florida paver vendors publish figures that travertine runs twenty to thirty degrees Fahrenheit cooler than poured concrete and fifteen to twenty cooler than porcelain in direct midday sun, with concrete pavers reaching 130 to 140 degrees on a 95-degree day while travertine stays at 110 to 120. Those numbers are plausible and directionally consistent with the mechanisms above.")
        + p("They are also unsourced. No instrument, no time of day, no sky condition, no sample preparation and no location accompanies them, and they are repeated verbatim across competing vendor sites, which is the signature of marketing copy rather than measurement. This site attributes them and does not adopt them.")
        + p(f'What replaces them is the {link("/coastal/pool-deck-surface-temperature-study/", "Sarasota Pool Deck Surface Temperature Study")}: nine surfaces on the same base, read with a calibrated infrared thermometer at 10 a.m., 2 p.m. and 5 p.m. on a clear July day and a clear January day in Sarasota, with air temperature and conditions recorded, medians published as a table and as JSON. The protocol is published now; the readings are scheduled for January and July 2027 and will appear the day they exist.'))
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
