# -*- coding: utf-8 -*-
from _data import BUSINESS, has, SERVICES, CONCRETE_ORDER, PAVER_ORDER, CITIES, TIER1, TIER2
from _h import cap, sec, p, ul, table, note, faq_block, cta, reviewed, svc_link, city_link, link, ext, facts, cards
from _photos import featured, figure_html, image_schema
from templates import lead_form
from _data import BASE_URL

FAQ = [
    ("Is Sarasota Concrete a contractor or a referral site?",
     "It's a lead-generation site for one insured provider that pours and paves in Sarasota County and the Charlotte County coast. Your request goes to that crew, not to a list of bidders. The provider's legal name is printed on the estimate and in the contract before any deposit changes hands."),
    ("Do you work on Siesta Key, Longboat Key and Casey Key?",
     "Yes. Barrier-island work is where the flood-zone, setback and sea-turtle lighting rules bite, so every island estimate starts with the FEMA zone and the jurisdiction (Sarasota County for Siesta and Casey Key, the Town of Longboat Key for Longboat) written on the scope."),
    ("How fast can a pool deck or driveway be scheduled?",
     "In season (January through April) the calendar is tightest and lead times stretch; June through September opens up but afternoon rain shapes pour days. Ask for a date range when you request the estimate and we'll say what is realistic for your month, not a generic promise."),
    ("Are the prices on this site quotes?",
     "No. They're planning ranges compiled from published Sarasota-area pricing on a stated date, plus the provider's own completed jobs as they're documented. A written estimate follows a site visit or a video walkthrough, and that number is the one that counts."),
    ("Do you handle the permit and the HOA paperwork?",
     "The provider pulls permits where it holds the required county registration, and prepares the ARC packet (site plan, material sample, color, drainage note) for you to submit, since most associations only accept applications from the owner."),
    ("What if I'm out of state for the summer?",
     "Most of our seasonal clients are. Video estimates, e-signed scope, daily photo reports and a hand-off to your property manager are standard, and the schedule is built so the work is finished before you fly back in November."),
]


def get_pages():
    c_list = [
        (SERVICES["concrete-pool-decks"]["route"], "Concrete pool decks", "New decks, extensions and condo decks poured with a real slope to the drain and a texture your feet can stand in July."),
        (SERVICES["concrete-driveways"]["route"], "Concrete driveways", "Replacement and widening on Myakka sand, with the base, joints and apron detail each jurisdiction expects."),
        (SERVICES["concrete-patios-lanais"]["route"], "Patios and lanai slabs", "Broom, exposed-aggregate and colored slabs sized for the cage you have or the one you're planning."),
        (SERVICES["concrete-stamped"]["route"], "Stamped and decorative", "Patterned and stained concrete sealed for Gulf sun, with honest notes on slip and resealing."),
        (SERVICES["concrete-slabs"]["route"], "Slabs and pads", "Shed, generator, AC, hot-tub and boat-lift pads engineered for the load, not the price sheet."),
        (SERVICES["concrete-sidewalks-walkways"]["route"], "Sidewalks and walkways", "Entry walks, side paths and trip-hazard replacements that meet the county's grade."),
        (SERVICES["concrete-repair"]["route"], "Repair and leveling", "Cracks, spalling and settled slabs diagnosed before anyone sells you a tear-out."),
        (SERVICES["concrete-resurfacing"]["route"], "Resurfacing and overlays", "Pool deck renewal over sound slabs, with a clear line on when an overlay is the wrong answer."),
        (SERVICES["concrete-architectural"]["route"], "Architectural concrete", "Honed, board-formed and cast finishes for modern Sarasota entries and steps."),
    ]
    p_list = [
        (SERVICES["pavers-pool-decks"]["route"], "Paver pool decks", "Concrete pavers, travertine, shellstone and porcelain laid on a base that drains, around residential and condo pools."),
        (SERVICES["pavers-travertine-shellstone"]["route"], "Travertine and shellstone", "Natural stone with the sealing cycle and salt-pool facts stated up front."),
        (SERVICES["pavers-marble-porcelain"]["route"], "Marble and porcelain", "Large-format and luxury lines, including Belgard, for lanais that read as interior floors."),
        (SERVICES["pavers-driveways"]["route"], "Paver driveways", "Vehicular pavers, brick and permeable systems with base depths matched to a high water table."),
        (SERVICES["pavers-patios-lanais"]["route"], "Paver patios and lanais", "New patios, lanai floors and overlays where the slab underneath earns it."),
        (SERVICES["pavers-walkways-steps"]["route"], "Walkways and steps", "Entry paths and steps in pavers and stone, with lighting that passes turtle season on the islands."),
        (SERVICES["pavers-sealing"]["route"], "Sealing and cleaning", "Cleaning, polymeric re-sanding and sealer choice tuned to how far you are from the Gulf."),
        (SERVICES["pavers-repair-storm-restoration"]["route"], "Repair and storm restoration", "Sunken, shifted and surge-damaged pavers reset on a rebuilt base, documented for your insurer."),
        (SERVICES["pavers-retaining-walls-outdoor-living"]["route"], "Walls, fire pits, kitchens", "Seat walls, decorative retaining walls and outdoor-kitchen bases in block and stone."),
        (SERVICES["pavers-artificial-turf"]["route"], "Artificial turf", "Turf inlays and side yards paired with pavers where grass gives up."),
        (SERVICES["pavers-outdoor-lighting"]["route"], "Hardscape lighting", "Path, step and wall lights built into the hardscape, amber and shielded where the ordinance requires."),
    ]
    tier1_rows = [[city_link(c), CITIES[c]["jurisdiction"], CITIES[c]["drive"], CITIES[c]["flood"].split(";")[0]] for c in TIER1]
    tier2_rows = [[city_link(c), CITIES[c]["jurisdiction"], CITIES[c]["drive"], CITIES[c]["flood"].split(";")[0]] for c in TIER2]

    body = ""
    body += facts([
        ("Service area", "Sarasota County and the Charlotte County coast, 40 miles from Sarasota"),
        ("Jurisdictions covered", "Sarasota County, City of Sarasota, Venice, North Port, Longboat Key, Charlotte County"),
        ("Two trades, two pillars", "Poured concrete and pavers, planned and priced separately"),
        ("Status", BUSINESS["insurance_statement"] + ". Written estimates, no license claim until documented"),
    ])
    body += sec("Two pillars, one coast", p(
        "Sarasota homeowners rarely need \"concrete\" or \"pavers\" in the abstract. They need a pool deck that doesn't burn feet in August, a driveway that survives the water table under Palmer Ranch, or a lanai floor on Siesta Key that can be hosed off after the next surge. So this site is organized around those decisions rather than around a company brochure. The concrete pillar covers everything poured in place. The paver pillar covers everything set on a compacted base. Each service page tells you what the work is, what it costs in this market on a stated date, how long it takes, which office issues the permit, and what goes wrong here that doesn't go wrong in Ocala.",
        "Everything below is written for Sarasota County first, then for the Charlotte County coast between Englewood and Port Charlotte. If you live in Lakewood Ranch, Bradenton or Parrish, those communities have their own local resources and this site links you there rather than pretending to cover Manatee County too."))
    body += '<div class="pillars"><div class="pillar"><h2>Poured concrete</h2>' + ul([f'{link(h, t)}: {x}' for h, t, x in c_list]) + f'<p>{link("/concrete/", "Concrete pillar: specs, prices and permits")}</p></div>'
    body += '<div class="pillar"><h2>Pavers and hardscape</h2>' + ul([f'{link(h, t)}: {x}' for h, t, x in p_list]) + f'<p>{link("/pavers/", "Paver pillar: materials, base and sealing")}</p></div></div>'

    body += cap("What does a pool deck cost in Sarasota in 2026?",
                "Published Sarasota-area pricing on September 10, 2026 puts installed concrete pavers around $13 to $16 per square foot, travertine around $20 to $26, and a decorative overlay on an existing slab at $10 to $15. A 700-square-foot deck therefore runs roughly $9,000 to $18,000 depending on material, not counting demolition, drainage fixes or coping. These are planning ranges, not quotes.",
                p(f'The full breakdown by material, deck size and condition is in the {link("/pricing/pool-decks/", "pool deck cost guide")}, and the method behind every number on this site is on the {link("/data-and-methods/", "data and methods page")}. From the first quarter of 2027 the {link("/pricing/sarasota-concrete-cost-index/", "Sarasota Concrete Cost Index")} replaces published third-party ranges with the provider\'s own completed-job data, published quarterly under a CC BY 4.0 license so anyone can cite it.'))
    body += cap("Do I need a permit to replace a driveway or pool deck here?",
                "It depends on the jurisdiction, not the county line alone. Unincorporated Sarasota County requires a culvert permit or right-of-way use permit for anything touching the county road frontage; the City of Sarasota treats the apron between sidewalk and street as city property; Charlotte County permits every slab, pavers included. Details per office are on the permits hub.",
                p(f'Start with the {link("/permits/", "permit hub")} or type your address into the {link("/tools/permit-flood-setback-finder/", "permit, flood-zone and setback finder")}. Each jurisdiction page links the official portal (Accela for the county, the FTG portal for the City of Sarasota, eTRAKiT for Venice, Click2Gov for North Port) and says who normally pulls the permit.'))
    body += cap("Which pool deck surface stays coolest barefoot in July?",
                "Nobody in this market has published a local measurement, so this site won't either until it exists. The Sarasota Pool Deck Surface Temperature Study will read nine surfaces with an infrared thermometer at 10 a.m., 2 p.m. and 5 p.m. on a typical July day and a typical January day, and publish the raw numbers as JSON. Until then the page states the method and the physics.",
                p(f'Read the {link("/coastal/pool-deck-surface-temperature-study/", "study page")} for the protocol, the instrument and the surfaces, and the {link("/compare/pool-deck-surfaces-heat/", "surface comparison")} for what color, mass and texture do to a deck at 2 p.m. If a contractor tells you travertine is \"25 degrees cooler\", ask where the thermometer was.'))
    body += cap("What changes when the property is in a flood zone on the keys?",
                "Three things. The NFIP 50 percent rule limits improvements to the building, but driveways, pool decks and other site work sit outside that calculation, so hardscape rarely triggers it. Anything seaward of Sarasota County's Gulf Beach Setback Line needs a coastal setback variance, pool decks included. And from May 1 to October 31, any light visible from the beach must be long-wavelength and shielded.",
                p(f'Those three rules, with the code sections and the offices that enforce them, are on {link("/permits/flood-zones-50-percent-rule/", "flood zones and the 50% rule")} and {link("/permits/sea-turtle-lighting/", "sea turtle lighting")}. The {link("/coastal/", "coastal hub")} covers what salt and surge do to concrete and pavers over a decade.'))

    body += sec("Where the crew works, and who issues the permit",
                p("Every locality below gets its own page with the jurisdiction, the predominant flood zone, the soil series under the lots, the housing stock and the drive time from Sarasota. Tier 1 is Sarasota County, where every service is offered. Tier 2 is the Charlotte County coast inside the 40-mile radius, where the four highest-demand services are scheduled.") +
                table(["Locality", "Permit jurisdiction", "Drive from Sarasota", "Predominant flood zone"], tier1_rows, "Tier 1: Sarasota County") +
                table(["Locality", "Permit jurisdiction", "Drive from Sarasota", "Predominant flood zone"], tier2_rows, "Tier 2: Charlotte County coast") +
                p(f'County-level rules live on the {link("/areas/sarasota-county/", "Sarasota County hub")} and the {link("/areas/charlotte-county/", "Charlotte County hub")}. Lakewood Ranch, University Park, Bradenton, Palmetto, Anna Maria Island and the south Hillsborough communities are inside 40 miles but are served through their own local sites; the {link("/areas/", "service area page")} explains the split.'))

    body += sec("Five things the Gulf side does to hardscape",
                p("Most concrete advice online was written for Georgia clay or Midwest freeze. The Suncoast fails surfaces differently, and the service pages here are built around these five mechanisms.") +
                ul([
                    "<strong>A water table under 10 inches for months.</strong> The USDA describes Myakka fine sand, the soil under most of Sarasota County, as poorly drained with a seasonal high water table within 10 inches of the surface for two to six months a year. A base that isn't compacted in lifts and pitched to drain will pump fines and settle, and the slab or paver field settles with it.",
                    "<strong>Salt from three directions.</strong> Spray off the Gulf, brackish bay water in the canals and salt-chlorinated pool water all move chloride into concrete and stone. On the islands, sealer life is closer to 18 to 24 months than the 3 years quoted inland, and unsealed limestone-family pavers (travertine, shellstone) around salt pools flake at the waterline first.",
                    "<strong>Ninety-degree afternoons and 7 to 9 inches of rain a month.</strong> NOAA's 1991 to 2020 normals for Sarasota-Bradenton put July and August highs at 91 degrees and August rainfall at 9.11 inches. Pours are scheduled for the morning, joints are cut the same day, and cure protection matters more than mix design.",
                    "<strong>Storm surge that moves sand and pavers.</strong> Helene pushed a measured 6.68-foot surge onto Longboat Key in September 2024 and Milton followed two weeks later. Surge washes out joint sand, floats edge restraint and leaves salt in the base. The paver repair page says what to reset and what to rebuild.",
                    "<strong>Rules that change every few miles.</strong> The City of Sarasota, Sarasota County, Venice, North Port, Longboat Key and Charlotte County each permit flatwork differently, and barrier-island lots add the setback line and turtle lighting. That's why this site has a permit page per office instead of one paragraph that says \"check with your local building department\".",
                ]))

    body += sec("How an estimate works",
                p("A request through the form or the phone gets a callback the same or next business day. For most projects the provider visits, measures, checks the slope with a level and a hose if the drainage is in question, and looks at what's under the existing surface. Seasonal owners can start with a video walkthrough instead; the site plan or survey from your closing documents is enough to draft a scope.") +
                p("You get a written scope with the square footage, thickness or paver system, base depth, reinforcement, drainage plan, permit responsibility, schedule window and the price. The permit and any ARC packet are prepared before a start date is set. During the job, photos go out daily. At the end you get the care sheet, the sealing schedule for your distance from the coast, and the written workmanship warranty terms that apply to the work.") +
                p(f'The {link("/guides/snowbird-project-guide/", "snowbird project guide")} walks through the remote version step by step, and the {link("/guides/deposits-and-warranties/", "deposits and warranties guide")} explains what Florida law says a deposit and a written contract should look like before you sign anything.'))

    body += sec("Data and tools published here",
                cards([
                    ("/pricing/sarasota-concrete-cost-index/", "Sarasota Concrete Cost Index", "Quarterly installed-cost ranges by service and locality, with sample size and method, as HTML and JSON."),
                    ("/coastal/pool-deck-surface-temperature-study/", "Pool Deck Surface Temperature Study", "Nine surfaces, three times of day, July and January, infrared thermometer. Method published now, numbers when measured."),
                    ("/tools/coastal-surface-selector/", "Coastal Surface Selector", "Distance from the coast, flood zone, salt or chlorine pool, use and budget in; a surface and a maintenance cycle out."),
                    ("/tools/permit-flood-setback-finder/", "Permit, Flood-Zone & Setback Finder", "Which office, which zone, whether the setback line or the 50% rule could apply, and who pulls the permit."),
                    ("/tools/concrete-paver-calculator/", "Concrete & Paver Calculator", "Cubic yards, base tonnage, paver count, polymeric sand and a dated local cost range."),
                    ("/tools/pour-calendar/", "Pour Calendar", "Month by month: afternoon rain odds, temperature, cure window and the hour to start, from NOAA normals."),
                    ("/coastal/storm-season-playbook/", "Storm Season Hardscape Playbook", "What to do with pavers and concrete before June 1 and after a surge, and how to document damage for a claim."),
                    ("/guides/ask-the-estimator/", "Ask the Estimator", "Real questions from local homeowners, anonymized and answered weekly, with an RSS feed."),
                ]))

    feat = featured(6)
    body += sec("Recent work", p("Provider job photos from Central Florida installs. Suncoast projects are added to the gallery as they're completed and documented with the city, material, square footage and the challenge on the lot.") +
                '<div class="gallery">' + "".join(figure_html(x) for x in feat) + "</div>" + p(link("/gallery/", "Full gallery") + " · " + link("/projects/", "Documented projects")))

    body += sec("What a written scope from this provider contains",
                p("A scope you can compare line by line, not a total on a business card. Square footage measured on site or from your survey; thickness or paver system; base depth and material, with geotextile where the subgrade pumps; reinforcement; joint layout; drainage plan with where the water goes; demolition and disposal; permit responsibility and fees; association packet contents; schedule window with the weather clause stated; payment schedule tied to stages; warranty terms; and the legal name of the entity doing the work.") +
                p("Two things are deliberately missing. There's no license number, because none has been documented for this trade name and a number invented for a website is fraud under Florida Statute 489. And there's no star rating, because the provider's reviews belong to the profiles that earned them and will be shown here only when the entity match is confirmed and the source is named."))
    body += sec("Seasons and scheduling on the Suncoast",
                table(["Months", "What's happening", "What it means for a job"], [
                    ["January to April", "Peak population (Sarasota County passes 570,000 in winter) and peak demand", "Longest lead times; book two months ahead; dry, cool pours"],
                    ["May", "Owners leaving; turtle season starts May 1 on the islands", "Best month to sign a summer job; lighting swapped to amber"],
                    ["June to September", "Highs above 90, 6 to 9 inches of rain a month, afternoon storms", "Pours at 7 a.m.; joint sand and sealing in dry gaps; shortest lead times"],
                    ["August to October", "Peak hurricane weeks (Ian 2022, Helene and Milton 2024)", "No island pours inside a watch; storm playbook applies"],
                    ["November to December", "Owners returning; turtle season ends October 31", "Finish line for summer jobs; sealing season opens"]], "The Suncoast hardscape year") +
                p(f'The {link("/tools/pour-calendar/", "pour calendar")} turns the NOAA normals into a start hour for any month, and the {link("/guides/snowbird-project-guide/", "snowbird guide")} lays out the March-to-November plan for owners who spend summers elsewhere.'))
    body += faq_block(FAQ, "Straight answers before you call")
    body += sec("Tell us more about the project",
                p(f'The hero form is four fields because that is all a first contact needs. This one asks '
                  f'for the location, a description and a photo, which is what makes the first call short. '
                  f'{("Call or text " + link("tel:" + BUSINESS["phone_tel"], BUSINESS["phone_display"]) + " if you prefer." ) if has("phone_display") else ""}')
                + lead_form(prefix="bf"))
    body += reviewed("September 10, 2026", "First publication.")

    return [{
        "route": "/", "is_home": True, "title_full": True,
        "title": "Sarasota Concrete | Concrete & Paver Contractor, Sarasota FL",
        "meta_description": "Concrete, pavers and pool decks for Sarasota County and the Charlotte County coast: local prices with dates, permits by jurisdiction, flood and salt facts, free written estimates.",
        "h1": "Concrete, pavers and pool decks for Sarasota's coast, built for salt, sand and a 91-degree July",
        "kicker": "Sarasota County · Charlotte County coast · 40 miles from Sarasota",
        "lede": "Poured concrete and paver hardscape for Sarasota, the keys, Palmer Ranch, Venice, North Port and the Englewood coast. Local cost ranges with a date on them, the permit office for your address, and the flood, salt and turtle-lighting rules explained before you spend anything.",
        "body_html": body, "faq": FAQ,
        # Real provider job photo, full-bleed behind the hero, under a graphite wash. The alt text
        # says what is visible and does not claim a Sarasota address, because this install is a
        # Central Florida job. The credit line under the hero says the same thing in the open.
        "hero_photo": {
            "slug": "hero-surface", "w": 1440, "h": 810,
            "alt": ("Charcoal slate-texture concrete pavers with a soldier-course border, laid tight "
                    "with even joints across a finished driveway"),
            "credit": "Provider job photo. Suncoast project photos are added as each one is documented.",
        },
        "hero_badges": ["Insured", "Free written estimate", "Sarasota County and the Charlotte coast",
                        "Concrete and pavers, priced separately"],
        "schema": image_schema(feat, BASE_URL),
    }]
