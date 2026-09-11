# -*- coding: utf-8 -*-
from _data import SERVICES, CONCRETE_ORDER, PAVER_ORDER, CITIES, TIER1
from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, svc_link, city_link, link, ext, facts, cards, service_schema
from _photos import gallery

CONCRETE_FAQ = [
    ("How thick should residential concrete be in Sarasota County?", "Four inches is the floor for driveways, patios and pool decks under the Florida Building Code, Residential (Chapter 19 references ACI 332). Five to six inches is specified for RV, boat-trailer and dumpster pads and for aprons where a jurisdiction's right-of-way detail calls for it. Thickness without a compacted base is wasted money on Myakka sand."),
    ("What PSI mix is used?", "A 3,000 PSI mix is code-minimum for flatwork; 4,000 PSI is the working default here because it finishes better in heat, resists salt scaling longer and costs a few dollars more per yard. Air entrainment isn't needed for freeze but a low water-cement ratio is, because that's what keeps chloride out."),
    ("Rebar, wire mesh or fiber?", "Fiber controls plastic shrinkage cracks in the first hours. Steel controls crack width after the slab has cracked at a joint. Vehicle slabs get #3 or #4 bar on chairs, walkways and patios often do fine with fiber plus properly spaced joints. The comparison page shows what each costs and where mesh laid on the ground fails."),
    ("How long before I can drive on a new driveway?", "Seven days for cars in normal summer heat, with light foot traffic after 24 hours and full design strength at 28 days. Heavier vehicles, boat trailers and delivery trucks wait the full 28 days. Rain in the first two hours is the real risk; after the surface sets it's mostly harmless."),
    ("Can you match the color of my existing slab?", "Not exactly, and anyone who promises it hasn't poured in this humidity. Cement source, finishing time and cure all shift the gray. The honest options are a full replacement of the visible section, a decorative overlay across both, or accepting a color line at a control joint."),
]

PAVER_FAQ = [
    ("What base do pavers need on a high water table?", "Six inches of compacted crushed limerock or recycled concrete for driveways and four for patios and pool decks, placed in lifts of no more than three inches and compacted to a plate-compactor refusal, over a geotextile where the subgrade pumps. On barrier islands the base is often the whole story: the pavers are fine, the base washed out."),
    ("Do pavers need a permit?", "In Charlotte County, yes: the county states that all flatwork including pavers requires a permit and inspections. In Sarasota County and the cities it depends on whether you touch the right-of-way, the footprint changes, or the lot is on the coast. The permit hub has each office."),
    ("How often are pavers sealed near the Gulf?", "Every 18 to 24 months within roughly a mile of open water, every 2 to 3 years inland, and annually for travertine coping on a salt-chlorinated pool. The maintenance calendar sets the interval by distance from the coast and by material."),
    ("Are pavers or concrete better in a VE flood zone?", "Pavers, usually. A surge that lifts a slab destroys it; a surge that shifts a paver field leaves reusable units on a base that can be rebuilt. The flood page covers the exceptions, including elevated homes where an engineered slab is required under the deck."),
    ("Can pavers go over my existing lanai slab?", "When the slab is sound, drains and can carry the extra weight without raising the finished floor above the door threshold, a thin-set or sand-set overlay works. When it's cracked through, hollow-sounding or pitched toward the house, it comes out. The paver patio page shows the tests used to decide."),
]


def concrete_page():
    body = facts([("Services", "9 poured-concrete services"), ("Code baseline", "Florida Building Code, Residential; ACI 332 for slabs"), ("Working mix", "4,000 PSI, low water-cement ratio, morning pours"), ("Permits", "6 jurisdictions, each with its own page")])
    body += cap("What does a concrete contractor in Sarasota actually do differently?",
                "The trade is the same; the ground and the weather aren't. Sarasota concrete work means a compacted base over poorly drained sand, joints cut the same afternoon because a 91-degree July drives shrinkage fast, and mixes and covers chosen for chloride rather than freeze. Every service below is specified for that, and priced on a stated date.",
                p("The concrete pillar covers pool decks, driveways, patios and lanai slabs, stamped and decorative work, slabs and pads, sidewalks and walkways, repair and leveling, resurfacing and overlays, and architectural finishes. Pavers are a separate pillar because they're a separate trade with a separate base, a separate permit conversation and a separate maintenance cycle.") +
                p("This page is the map. Each service page carries the full structure: what it is, what it costs in this market, how long it takes, the spec for local soil and salt exposure, the permit by jurisdiction, what goes wrong here, maintenance, comparisons, and a short FAQ that isn't repeated anywhere else on the site."))
    body += sec("Concrete services", cards([(SERVICES[k]["route"], SERVICES[k]["name"], SERVICES[k]["short"]) for k in CONCRETE_ORDER]))
    body += sec("The spec that every Sarasota pour starts from",
                table(["Item", "Residential flatwork baseline", "Where it changes"],
                      [["Thickness", "4 in. (driveways, patios, pool decks)", "5 to 6 in. for RV, boat and dumpster pads; 6 in. in some right-of-way aprons (Venice detail)"],
                       ["Mix", "4,000 PSI, 0.45 or lower water-cement ratio", "3,000 PSI is code minimum; higher cement content near salt water"],
                       ["Base", "4 in. compacted crushed limerock over compacted subgrade", "6 in. where the water table sits within a foot in the wet season; geotextile where sand pumps"],
                       ["Reinforcement", "Fiber plus #3 rebar on chairs for vehicle slabs; fiber for walks and patios", "#4 bar at 18 in. for heavy pads; mesh only if lifted to mid-depth"],
                       ["Joints", "Control joints at 8 to 10 ft, depth one quarter of the slab, cut same day", "Isolation joints at the house, pool shell, columns and existing slabs"],
                       ["Slope", "1/8 in. per foot away from the house; pool decks pitched to deck drains", "Flatter in lanais with a screened floor drain; steeper for a driveway that meets a swale"],
                       ["Cure", "Curing compound or wet cure for 7 days; no vehicles for 7 days, heavy loads 28", "Shade cloth and evaporation retarder on windy, dry winter days"]],
                      "Sarasota Concrete flatwork baseline, 2026") +
                p(f'The reasoning behind each row, with the code and ACI references, is on the {link("/compare/4-inch-vs-6-inch/", "4-inch vs 6-inch")} and {link("/compare/rebar-vs-fiber/", "rebar vs fiber")} comparisons and in the guide on {link("/guides/why-concrete-cracks-sarasota/", "why concrete cracks in Sarasota")}.'))
    body += cap("What does concrete cost per square foot in Sarasota?",
                "As of September 10, 2026, published Sarasota-area ranges put plain broom-finished flatwork at roughly $7 to $12 per square foot installed, stamped or colored work at $12 to $20, and decorative overlays at $10 to $15 over a sound slab. Demolition of an old driveway adds $2 to $4 per square foot. A two-car driveway therefore lands around $6,000 to $11,000.",
                p(f'The {link("/pricing/concrete/", "concrete cost guide")} breaks this down by service, size band and condition, and states the sources. The {link("/pricing/", "pricing hub")} explains why three quotes for the same driveway can differ by thousands.'))
    body += sec("Permits: one office per address", p("The City of Sarasota, unincorporated Sarasota County, Venice, North Port, the Town of Longboat Key and Charlotte County each treat flatwork differently. The county needs a culvert permit or right-of-way use permit when the work touches the road frontage. The City of Sarasota owns the apron between the sidewalk and the street. Charlotte County permits every slab. Rather than summarize badly, each office has a page.") +
                cards([("/permits/sarasota-county/", "Sarasota County", "Unincorporated county, including Siesta Key, Casey Key, Osprey, Nokomis, South Venice and north Englewood."),
                       ("/permits/city-of-sarasota/", "City of Sarasota", "Downtown, west of the Trail, Lido and Bird Key, Indian Beach, Arlington Park and the city portion of Gulf Gate."),
                       ("/permits/venice/", "City of Venice", "Venice Island, the mainland city and the Wellen Park villages inside city limits."),
                       ("/permits/north-port/", "City of North Port", "GDC-platted lots with swales and culverts, Wellen Park's North Port side, Warm Mineral Springs."),
                       ("/permits/longboat-key/", "Town of Longboat Key", "Both county halves of the island; substantial-improvement review on every permit."),
                       ("/permits/charlotte-county/", "Charlotte County", "Port Charlotte, Rotonda West, Placida, Grove City and the south side of Englewood.")]))
    body += sec("Where concrete work is scheduled", p("Every Tier 1 locality in Sarasota County gets the full concrete catalog; the Charlotte County coast gets driveways, pool decks and repair.") +
                ul([f'{city_link(c)}: {d}' for c, d in [
                    ("sarasota", "city permits, the apron rule and the bayfront keys"), ("fruitville-bee-ridge", "county permits on flatwoods sand that holds water"),
                    ("gulf-gate", "sixty-year-old slabs on sand, no master association"), ("siesta-key", "AE and VE, setback line, turtle lighting, surge"),
                    ("palmer-ranch", "two levels of ARC review and 1990s builder slabs"), ("longboat-key", "Town permits for both county halves"),
                    ("osprey", "estate lots inland, Casey Key by a swing bridge"), ("nokomis", "native sand west of I-75, imported fill east of it"),
                    ("venice", "eTRAKiT permits and an engineering review at the street"), ("south-venice", "septic, wells and small platted lots"),
                    ("north-port", "GDC swales and a city-sized culvert on every crossing"), ("englewood", "two counties, one town, a conservation district on the key")]]))
    body += gallery("concrete-driveways", "Concrete and paver work from the provider's crews", 3)
    body += faq_block(CONCRETE_FAQ, "Concrete questions answered once, here")
    body += cta("Request a concrete estimate", "/contact/", "Send the square footage and a photo of what's there now; a written scope follows a site visit or video walkthrough.")
    body += reviewed("September 10, 2026")
    return {"route": "/concrete/", "title": "Concrete Contractor in Sarasota, FL – Pool Decks & Driveways", "title_full": True,
            "meta_description": "Poured concrete in Sarasota County: pool decks, driveways, patios, slabs, repair and resurfacing, with the 4,000 PSI spec, dated local prices and the permit office for your address.",
            "h1": "Poured concrete in Sarasota County, specified for sand, salt and summer heat", "kicker": "Concrete pillar",
            "lede": "Nine poured-concrete services with the same structure on every page: what it is, what it costs here, how long it takes, the local spec, the permit, and what fails on this coast.",
            "breadcrumbs": [("Home", "/"), ("Concrete", None)], "body_html": body, "faq": CONCRETE_FAQ,
            "schema": [service_schema("concrete-driveways", "/concrete/")]}


def pavers_page():
    body = facts([("Services", "11 paver and hardscape services"), ("Standard", "ICPI/CMHA base and bedding practice"), ("Materials", "Concrete pavers, brick, travertine, shellstone, marble, porcelain"), ("Coastal cycle", "Seal every 18 to 24 months within a mile of open water")])
    body += cap("What is different about pavers on the Suncoast?",
                "The paver is the least important part. In Sarasota County the base sits on poorly drained Myakka sand with a wet-season water table under 10 inches, salt arrives from the Gulf, the bays and salt-chlorinated pools, and a surge can lift edge restraint and wash out joints. Paver work here is base work, drainage work and a sealing schedule, then the pattern.",
                p("The paver pillar covers pool decks, travertine and shellstone, marble and porcelain, driveways, patios and lanais, walkways and steps, sealing and cleaning, repair and storm restoration, seat walls and outdoor living, artificial turf and hardscape lighting. Poured concrete lives on its own pillar because the two trades are bid, permitted and maintained differently.") +
                p("Every service page below follows the same order: what the work is, what it costs in this market on a stated date, how long it takes, the base and bedding spec for this soil, the permit by jurisdiction, what fails on the coast, the maintenance cycle, comparisons, and a short FAQ that isn't repeated elsewhere on the site."))
    body += sec("Paver and hardscape services", cards([(SERVICES[k]["route"], SERVICES[k]["name"], SERVICES[k]["short"]) for k in PAVER_ORDER]))
    body += sec("The base and bedding spec for a high water table",
                table(["Layer", "Pool deck / patio", "Driveway", "Why here"],
                      [["Subgrade", "Compacted, pitched 1/8 in. per ft, geotextile if it pumps", "Same, proof-rolled", "Myakka and EauGallie sands lose bearing when saturated"],
                       ["Base", "4 in. compacted crushed limerock or recycled concrete", "6 in., in 3-in. lifts", "Lifts compact fully; one thick lift stays soft in the middle"],
                       ["Bedding", "1 in. concrete sand, screeded, never compacted before laying", "1 in. concrete sand", "Thicker bedding migrates and creates the dips people call sinking pavers"],
                       ["Pavers", "2-3/8 in. concrete or 1-1/4 in. travertine, marble or porcelain on a mortar-set or sand-set system", "2-3/8 in. or 3-1/8 in. vehicular units, herringbone for load", "Herringbone interlocks under turning tires; running bond creeps"],
                       ["Edge restraint", "Concrete curb or spiked plastic restraint on the base, not on the bedding", "Concrete curb where a surge or truck can reach it", "Surge lifts spiked restraint set in bedding sand"],
                       ["Joints", "Polymeric sand, activated, cured dry for 24 to 48 hours", "Polymeric sand", "Rain in the first day reactivates and washes it"],
                       ["Sealing", "Breathable penetrating sealer after 30 days; wet-look film only where drainage is perfect", "Same", "Film sealers trap moisture and turn white over a wet base"]],
                      "Sarasota Concrete paver baseline, 2026") +
                p(f'The reasoning is on the {link("/pavers/driveways/", "paver driveway page")} and the {link("/compare/sealer-types-coastal/", "sealer comparison")}; the failure catalog is on {link("/pavers/repair-storm-restoration/", "repair and storm restoration")}.'))
    body += cap("What do pavers cost per square foot in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts installed concrete pavers at roughly $13 to $16 per square foot, travertine at $20 to $26, and marble or large-format porcelain higher, with cleaning, re-sanding and sealing at $1 to $3 per square foot. A 600-square-foot paver pool deck therefore lands between $8,000 and $16,000 before demolition or drainage work.",
                p(f'Size bands, material tiers and what moves the number are in the {link("/pricing/pavers/", "paver cost guide")} and the {link("/pricing/pool-decks/", "pool deck cost guide")}.'))
    body += sec("Materials, in one honest table",
                table(["Material", "Barefoot heat", "Wet slip", "Salt pool", "Sealing", "Notes"],
                      [["Concrete pavers (light blend)", "Warmer than stone, cooler than dark concrete", "Good with textured face", "Fine; seal to keep color", "2 to 3 years inland, 18 to 24 months coastal", "Widest range of vehicular units"],
                       ["Travertine (tumbled)", "Among the coolest", "Good", "Etches and flakes at the waterline unless sealed and rinsed", "Annually on salt-pool coping", "Fills need periodic re-grouting"],
                       ["Shellstone", "Cool, light color", "Very good", "Same limestone chemistry as travertine", "Annually near salt", "Open texture collects organics"],
                       ["Marble (honed)", "Cool", "Honed is fine, polished is not", "Etches with acid cleaners", "Penetrating sealer", "Best as a lanai floor with coping"],
                       ["Porcelain (2 cm)", "Warmer than travertine, cooler than dark concrete", "Excellent with R11 face", "Immune", "None needed", "Needs a perfect base or it rocks"],
                       ["Clay brick", "Warm", "Good", "Good", "Optional", "Traditional look, fewer vehicular sizes"]],
                      "Working comparison; heat column to be replaced by measured values from the temperature study") +
                p(f'Deeper comparisons: {link("/compare/travertine-vs-concrete-pavers/", "travertine vs concrete pavers")}, {link("/compare/travertine-vs-shellstone-vs-porcelain/", "travertine vs shellstone vs porcelain")} and the {link("/tools/coastal-surface-selector/", "coastal surface selector")}.'))
    body += sec("Barrier islands: three rules that ride along with every paver job",
                ul([f'{link("/permits/flood-zones-50-percent-rule/", "Flood zones and the 50% rule")}: site improvements are outside the calculation, but VE zones and elevated homes change how a deck is built.',
                    f'{link("/permits/flood-zones-50-percent-rule/", "The Gulf Beach Setback Line")}: pool decks seaward of the line need a coastal setback variance from the County Commission.',
                    f'{link("/permits/sea-turtle-lighting/", "Sea turtle lighting")}: May 1 to October 31, any fixture visible from the beach must be long-wavelength and fully shielded; hardscape lighting is designed to that rule from the start.']))
    body += gallery("pavers-pool-decks", "Paver pool decks and driveways from the provider's crews", 6)
    body += faq_block(PAVER_FAQ, "Paver questions answered once, here")
    body += cta("Request a paver estimate", "/contact/", "Tell us the material you're leaning toward and how far you are from the water; the base and sealing plan follows from that.")
    body += reviewed("September 10, 2026")
    return {"route": "/pavers/", "title": "Paver Installation in Sarasota, FL – Pool Decks & Driveways", "title_full": True,
            "meta_description": "Paver pool decks, travertine, driveways, patios, sealing and storm repair in Sarasota County: the base spec for a high water table, dated local prices and the barrier-island rules.",
            "h1": "Pavers and hardscape for Sarasota County, from the base up", "kicker": "Pavers pillar",
            "lede": "Eleven paver and hardscape services, each with the base and bedding spec for this soil, the sealing cycle for your distance from the Gulf, the permit office, and what fails after a surge.",
            "breadcrumbs": [("Home", "/"), ("Pavers", None)], "body_html": body, "faq": PAVER_FAQ,
            "schema": [service_schema("pavers-pool-decks", "/pavers/")]}


def get_pages():
    return [concrete_page(), pavers_page()]
