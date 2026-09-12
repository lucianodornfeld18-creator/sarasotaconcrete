# -*- coding: utf-8 -*-
"""Master data for sarasotaconcrete.com.

Rules baked in here (see ../OWNER-INPUTS.md before changing):
  * Public name is exactly "Sarasota Concrete". No FL, no suffix, anywhere.
  * No invented address, license, years, project counts, ratings or reviews.
    Anything the owner has not supplied is a {{PLACEHOLDER}} and the templates
    hide the block instead of printing the placeholder.
  * "Insured" only. Never "Licensed" until LICENSE_NUMBER is filled in.
"""

DOMAIN = "sarasotaconcrete.com"
BASE_URL = "https://sarasotaconcrete.com"
PUBLIC_NAME = "Sarasota Concrete"
BUILD_DATE = "2026-09-10"

BUSINESS = {
    "name": PUBLIC_NAME,
    "tagline": "Solid foundations. Beautiful spaces.",
    "tagline_plain": "Concrete, pavers and pool decks built for the Gulf side of Florida.",
    # Owner-supplied (placeholders hide the block until filled)
    # Twilio number provisioned 2026-09-11. Voice webhook -> sarasota-voice-9463-prod.twil.io/incoming:
    # greeting, press-any-key robocall screen, whisper on answer, then forward to the owner.
    "phone_display": "(941) 274-3561",
    "phone_tel": "+19412743561",
    "email": "hello@sarasotaconcrete.com",
    # Web3Forms access key. Public by design: the service authenticates the form from the browser,
    # so the key ships in the HTML of every page and there is no way to hide it. It identifies the
    # destination inbox, it is not a credential that can read anything, and it is revocable from the
    # Web3Forms dashboard. Because anyone can post to it, the honeypot below and the dashboard's
    # captcha are the only spam protection, which is worth turning on.
    "web3forms_key": "aa494292-272d-492c-a968-1d63f9d9f865",
    "legal_entity": "{{LEGAL_ENTITY}}",
    "license_number": "",                                  # blank = no license claim anywhere
    "insurance_statement": "Insured",                      # only "Insured" until proof + license supplied
    "years_active": "",                                    # blank = not shown
    "google_profile": "",                                  # blank = not shown
    "yelp": "",
    "facebook": "",
    "instagram": "",
    "nextdoor": "",
    "hours": "Monday to Friday 7:30 a.m. to 5:30 p.m., Saturday by appointment",
    "service_area_short": "Sarasota County and the Charlotte County coast within 40 miles of Sarasota",
    "author_name": "{{AUTHOR_NAME}}",                      # owner or technical lead; hidden until filled
    "author_title": "{{AUTHOR_TITLE}}",
    "disclosure_short": (
        "Sarasota Concrete is a lead-generation site for concrete, paver and hardscape work in Sarasota County "
        "and the Charlotte County coast. Requests are handled by the insured provider that serves your area."
    ),
    "consent_text": (
        "By submitting, you agree that Sarasota Concrete may contact you by phone, text or email about this request "
        "and may forward it to the insured provider that serves your area. Message and data rates may apply. "
        "Reply STOP to opt out of texts."
    ),
}


def has(key):
    v = BUSINESS.get(key, "")
    return bool(v) and not (v.startswith("{{") and v.endswith("}}"))


TURNSTILE_SITE_KEY = "{{TURNSTILE_SITE_KEY}}"

# --------------------------------------------------------------------------- services
SERVICES = {
    # ---- CONCRETE pillar ----
    "concrete-pool-decks": {"pillar": "concrete", "route": "/concrete/pool-decks/", "name": "Concrete Pool Decks",
        "short": "New pool decks, cool-deck textures, deck extensions and condo pool decks poured for barefoot use.",
        "nav": "Pool decks"},
    "concrete-driveways": {"pillar": "concrete", "route": "/concrete/driveways/", "name": "Concrete Driveways",
        "short": "New, replacement, widened and extended driveways, aprons and golf-cart paths where communities allow them.",
        "nav": "Driveways"},
    "concrete-patios-lanais": {"pillar": "concrete", "route": "/concrete/patios-lanais/", "name": "Concrete Patios & Lanai Slabs",
        "short": "Broom, smooth, exposed-aggregate and colored slabs for patios, lanai extensions and screened rooms.",
        "nav": "Patios & lanais"},
    "concrete-stamped": {"pillar": "concrete", "route": "/concrete/stamped/", "name": "Stamped & Decorative Concrete",
        "short": "Stamped, stained and textured concrete for patios, walks and driveways, sealed for coastal sun.",
        "nav": "Stamped"},
    "concrete-slabs": {"pillar": "concrete", "route": "/concrete/slabs/", "name": "Concrete Slabs & Pads",
        "short": "Shed, AC, generator, hot-tub, boat-lift and dumpster pads and dock approaches sized for their loads.",
        "nav": "Slabs & pads"},
    "concrete-sidewalks-walkways": {"pillar": "concrete", "route": "/concrete/sidewalks-walkways/", "name": "Sidewalks & Walkways",
        "short": "Front walks, side-yard paths, sidewalk replacement and trip-hazard fixes.",
        "nav": "Sidewalks & walkways"},
    "concrete-repair": {"pillar": "concrete", "route": "/concrete/repair/", "name": "Concrete Repair",
        "short": "Cracks, spalling, lifting and leveling, trip hazards and post-storm damage.",
        "nav": "Repair"},
    "concrete-resurfacing": {"pillar": "concrete", "route": "/concrete/resurfacing/", "name": "Concrete Resurfacing & Overlays",
        "short": "Pool deck resurfacing, textured overlays and cool-deck renewal over sound slabs.",
        "nav": "Resurfacing"},
    "concrete-architectural": {"pillar": "concrete", "route": "/concrete/architectural/", "name": "Architectural Concrete",
        "short": "Honed, board-formed and cast finishes for entries, steps and modern Sarasota homes.",
        "nav": "Architectural"},
    # ---- PAVERS pillar ----
    "pavers-pool-decks": {"pillar": "pavers", "route": "/pavers/pool-decks/", "name": "Paver Pool Decks",
        "short": "Concrete pavers, travertine, shellstone and porcelain around residential and condo pools.",
        "nav": "Pool decks"},
    "pavers-travertine-shellstone": {"pillar": "pavers", "route": "/pavers/travertine-shellstone/", "name": "Travertine & Shellstone",
        "short": "Natural stone for pool decks, patios and driveways, with the salt and sealing facts that matter here.",
        "nav": "Travertine & shellstone"},
    "pavers-marble-porcelain": {"pillar": "pavers", "route": "/pavers/marble-porcelain/", "name": "Marble & Porcelain Pavers",
        "short": "Marble, large-format porcelain and Belgard luxury lines for pool decks and lanais.",
        "nav": "Marble & porcelain"},
    "pavers-driveways": {"pillar": "pavers", "route": "/pavers/driveways/", "name": "Paver Driveways",
        "short": "Concrete, brick and permeable paver driveways on a compacted base built for a high water table.",
        "nav": "Driveways"},
    "pavers-patios-lanais": {"pillar": "pavers", "route": "/pavers/patios-lanais/", "name": "Paver Patios & Lanais",
        "short": "Paver patios, lanai floors and extensions, including overlays where the slab is sound.",
        "nav": "Patios & lanais"},
    "pavers-walkways-steps": {"pillar": "pavers", "route": "/pavers/walkways-steps/", "name": "Paver Walkways & Steps",
        "short": "Entry walks, garden paths, steps and stoops in pavers and natural stone.",
        "nav": "Walkways & steps"},
    "pavers-sealing": {"pillar": "pavers", "route": "/pavers/sealing/", "name": "Paver Sealing, Cleaning & Re-Sanding",
        "short": "Cleaning, polymeric re-sanding and sealing on a schedule that respects salt air.",
        "nav": "Sealing & cleaning"},
    "pavers-repair-storm-restoration": {"pillar": "pavers", "route": "/pavers/repair-storm-restoration/", "name": "Paver Repair & Storm Restoration",
        "short": "Settled, sunken, shifted or surge-damaged pavers reset on a rebuilt base.",
        "nav": "Repair & storm restoration"},
    "pavers-retaining-walls-outdoor-living": {"pillar": "pavers", "route": "/pavers/retaining-walls-outdoor-living/", "name": "Seat Walls, Fire Pits & Outdoor Kitchens",
        "short": "Decorative retaining and seat walls, fire features and outdoor kitchen bases in block and stone.",
        "nav": "Walls & outdoor living"},
    "pavers-artificial-turf": {"pillar": "pavers", "route": "/pavers/artificial-turf/", "name": "Artificial Turf",
        "short": "Synthetic turf paired with pavers for pool surrounds, side yards and pet areas.",
        "nav": "Artificial turf"},
    "pavers-outdoor-lighting": {"pillar": "pavers", "route": "/pavers/outdoor-lighting/", "name": "Hardscape Lighting",
        "short": "Path, step and wall lighting integrated into pavers, turtle-compliant on the barrier islands.",
        "nav": "Outdoor lighting"},
}
SERVICE_ORDER = [
    "concrete-pool-decks", "concrete-driveways", "concrete-patios-lanais", "concrete-stamped", "concrete-slabs",
    "concrete-sidewalks-walkways", "concrete-repair", "concrete-resurfacing", "concrete-architectural",
    "pavers-pool-decks", "pavers-travertine-shellstone", "pavers-marble-porcelain", "pavers-driveways",
    "pavers-patios-lanais", "pavers-walkways-steps", "pavers-sealing", "pavers-repair-storm-restoration",
    "pavers-retaining-walls-outdoor-living", "pavers-artificial-turf", "pavers-outdoor-lighting",
]
CONCRETE_ORDER = [k for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "concrete"]
PAVER_ORDER = [k for k in SERVICE_ORDER if SERVICES[k]["pillar"] == "pavers"]

# --------------------------------------------------------------------------- cities
# Population: Florida EDR, Adjusted Population Estimates April 1 2025 (municipalities) or
# U.S. Census 2020 (CDPs). Distances: straight-line from Sarasota (27.3364, -82.5307), 2026-09-10.
CITIES = {
    "sarasota": {"name": "Sarasota", "tier": 1, "county": "Sarasota County", "jurisdiction": "City of Sarasota",
        "permit_route": "/permits/city-of-sarasota/", "miles": 0, "drive": "0 to 15 minutes",
        "population": "58,279 (Florida EDR, April 2025)", "wiki": "https://en.wikipedia.org/wiki/Sarasota,_Florida",
        "lat": 27.3364, "lng": -82.5307, "flood": "X inland; AE along Sarasota Bay, Lido Key, Bird Key and St. Armands; VE on the Gulf side of Lido",
        "soil": "Myakka and EauGallie fine sands east of the Trail; fill and shell over sand on the bayfront keys",
        "housing": "1920s to 1960s west of the Trail, 1950s to 1980s ranches east of it, new infill on the keys",
        "zips": "34230, 34231, 34232, 34234, 34236, 34237, 34239, 34242 (Siesta Key mail), 34243"},
    "fruitville-bee-ridge": {"name": "Fruitville & Bee Ridge", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 5, "drive": "10 to 20 minutes",
        "population": "part of the 189,453 people in unincorporated Sarasota County (Florida EDR, April 2025)", "wiki": "https://en.wikipedia.org/wiki/Fruitville,_Florida",
        "lat": 27.3520, "lng": -82.4380, "flood": "mostly X; AE pockets along Phillippi Creek and the Celery Fields drainage",
        "soil": "Myakka, EauGallie and Immokalee fine sands with a seasonal high water table under 10 inches in the wet season",
        "housing": "1970s to 2000s subdivisions (The Meadows 1970s to 80s, Kensington Park 1960s, Sarasota Springs 1950s to 70s)",
        "zips": "34232, 34233, 34235, 34240, 34241"},
    "gulf-gate": {"name": "Gulf Gate", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 4, "drive": "10 to 15 minutes",
        "population": "10,083 in the Gulf Gate Estates CDP (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Gulf_Gate_Estates,_Florida",
        "lat": 27.2650, "lng": -82.5150, "flood": "X in the interior blocks; AE toward Little Sarasota Bay and Phillippi Creek",
        "soil": "Myakka fine sand with a shallow water table; original 1960s slabs poured with little or no base",
        "housing": "1960s to 1970s block homes on quarter-acre lots, most with the original 3.5-inch driveway",
        "zips": "34231, 34238"},
    "siesta-key": {"name": "Siesta Key", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 4.9, "drive": "15 to 25 minutes via the Siesta Drive or Stickney Point bridges",
        "population": "5,454 (Census 2020; seasonal population far higher)", "wiki": "https://en.wikipedia.org/wiki/Siesta_Key,_Florida",
        "lat": 27.2670, "lng": -82.5460, "flood": "AE across most of the island, VE on the Gulf front; Gulf Beach Setback Line runs along the beach",
        "soil": "quartz beach sand and fill over shell; salt spray and surge exposure on every street",
        "housing": "1950s cottages, 1970s to 80s condos, elevated new construction since the 2024 storms",
        "zips": "34242"},
    "palmer-ranch": {"name": "Palmer Ranch", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 7.6, "drive": "15 to 20 minutes",
        "population": "no CDP; dozens of sub-associations under the Palmer Ranch Master Property Owners Association (1986)", "wiki": "https://en.wikipedia.org/wiki/Palmer_Ranch,_Florida",
        "lat": 27.2380, "lng": -82.4680, "flood": "mostly X with AE along the lake and preserve edges",
        "soil": "Myakka and Oldsmar fine sands, graded and filled during development",
        "housing": "1990 to 2010 production homes (Prestancia, Turtle Rock, Stoneybrook, Deer Creek) now at driveway and pool-deck replacement age",
        "zips": "34238"},
    "longboat-key": {"name": "Longboat Key", "tier": 1, "county": "Sarasota and Manatee Counties", "jurisdiction": "Town of Longboat Key",
        "permit_route": "/permits/longboat-key/", "miles": 9.4, "drive": "25 to 40 minutes via the Ringling Causeway and St. Armands, or from the north via Cortez Road and the Longboat Pass bridge",
        "population": "7,445 (2,663 in the Sarasota County part plus 4,782 in the Manatee County part, Florida EDR, April 2025)", "wiki": "https://en.wikipedia.org/wiki/Longboat_Key,_Florida",
        "lat": 27.4131, "lng": -82.6587, "flood": "AE and VE island-wide; Helene measured a 6.68-foot surge here in September 2024",
        "soil": "beach sand and dredged fill; salt on every surface",
        "housing": "1960s to 80s canal homes and condos (Bay Isles, Country Club Shores, Longboat Key Club), estate rebuilds",
        "zips": "34228"},
    "osprey": {"name": "Osprey & Casey Key", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 10.5, "drive": "20 to 25 minutes on US-41; Casey Key by the Blackburn Point swing bridge",
        "population": "6,729 in the Osprey CDP (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Osprey,_Florida",
        "lat": 27.1956, "lng": -82.4904, "flood": "X and AE inland; AE and VE on Casey Key, which sits inside the North Casey Key Conservation District",
        "soil": "Myakka fine sand inland; beach sand and fill on the key",
        "housing": "The Oaks and Southbay estates, 1980s to 2000s Rivendell and Park Trace homes, Casey Key waterfront",
        "zips": "34229"},
    "nokomis": {"name": "Nokomis & Laurel", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 15, "drive": "25 to 35 minutes by I-75 or US-41",
        "population": "3,808 in Nokomis and 9,184 in Laurel (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Nokomis,_Florida",
        "lat": 27.1208, "lng": -82.4445, "flood": "AE around Dona and Roberts bays and Shakett Creek; X east of I-75",
        "soil": "Myakka and Immokalee fine sands; new communities east of I-75 built on imported fill",
        "housing": "1970s Sorrento East and Calusa Lakes homes; 2016 to 2024 production homes in Toscana Isles, Bellacina, Talon Preserve and Vicenza",
        "zips": "34275"},
    "venice": {"name": "Venice", "tier": 1, "county": "Sarasota County", "jurisdiction": "City of Venice",
        "permit_route": "/permits/venice/", "miles": 17, "drive": "30 to 40 minutes",
        "population": "29,802 (Florida EDR, April 2025)", "wiki": "https://en.wikipedia.org/wiki/Venice,_Florida",
        "lat": 27.0998, "lng": -82.4543, "flood": "AE and VE on Venice Island and along the Intracoastal; X in most of the mainland city",
        "soil": "fill and shell over sand on the island; Myakka fine sand on the mainland",
        "housing": "1926 to 1960s island homes, 1970s to 90s mainland ranches, 2018 and newer Wellen Park villages",
        "zips": "34285, 34292, 34293"},
    "south-venice": {"name": "South Venice & Venice Gardens", "tier": 1, "county": "Sarasota County", "jurisdiction": "Sarasota County",
        "permit_route": "/permits/sarasota-county/", "miles": 20.5, "drive": "35 to 45 minutes",
        "population": "15,283 in South Venice and 7,328 in Venice Gardens (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/South_Venice,_Florida",
        "lat": 27.0530, "lng": -82.4240, "flood": "AE along Lemon Bay and Alligator Creek; X inland",
        "soil": "Myakka fine sand; many lots on septic and well, so irrigation rust and drain fields shape the layout",
        "housing": "1950s to 1980s block homes on small platted lots, many with original driveways",
        "zips": "34285, 34293"},
    "north-port": {"name": "North Port", "tier": 1, "county": "Sarasota County", "jurisdiction": "City of North Port",
        "permit_route": "/permits/north-port/", "miles": 27, "drive": "40 to 50 minutes by I-75",
        "population": "96,301 (Florida EDR, April 2025), the largest city in Sarasota County", "wiki": "https://en.wikipedia.org/wiki/North_Port,_Florida",
        "lat": 27.0442, "lng": -82.2359, "flood": "X across most of the GDC grid; AE along the Myakkahatchee Creek and the Myakka River",
        "soil": "deep Myakka and Immokalee sands with shallow drainage swales on lots platted by General Development Corp. from the 1950s to 1980s",
        "housing": "1970s to 2000s homes on quarter-acre GDC lots plus Wellen Park and Warm Mineral Springs",
        "zips": "34286, 34287, 34288, 34289, 34291"},
    "englewood": {"name": "Englewood & Manasota Key", "tier": 1, "county": "Sarasota and Charlotte Counties", "jurisdiction": "Sarasota County north of the county line, Charlotte County south of it",
        "permit_route": "/permits/sarasota-county/", "miles": 29, "drive": "45 to 60 minutes by SR-776",
        "population": "20,150 in the Englewood CDP (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Englewood,_Florida",
        "lat": 26.9620, "lng": -82.3530, "flood": "AE along Lemon Bay; AE and VE on Manasota Key, which also sits in the Manasota Key Conservation District",
        "soil": "Myakka fine sand inland; beach sand and fill on the key",
        "housing": "1960s to 1990s block homes, Manasota Key cottages and rebuilds after the 2024 surge",
        "zips": "34223, 34224"},
    "port-charlotte": {"name": "Port Charlotte", "tier": 2, "county": "Charlotte County", "jurisdiction": "Charlotte County",
        "permit_route": "/permits/charlotte-county/", "miles": 36.8, "drive": "50 to 65 minutes by I-75 or US-41",
        "population": "61,964 (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Port_Charlotte,_Florida",
        "lat": 26.9762, "lng": -82.0906, "flood": "AE along the canals and Charlotte Harbor; X on the interior grid",
        "soil": "Myakka and Immokalee sands on a 1950s to 80s GDC grid with roadside swales",
        "housing": "1970s to 1980s block homes; canal-front lots in Gulf Cove and South Gulf Cove",
        "zips": "33948, 33952, 33953, 33954, 33980, 33981"},
    "rotonda-west": {"name": "Rotonda West", "tier": 2, "county": "Charlotte County", "jurisdiction": "Charlotte County",
        "permit_route": "/permits/charlotte-county/", "miles": 34.6, "drive": "50 to 60 minutes by SR-776",
        "population": "10,114 (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Rotonda_West,_Florida",
        "lat": 26.8840, "lng": -82.2900, "flood": "AE around the canal system and the Cape Haze peninsula; X in the interior of the circle",
        "soil": "Myakka fine sand over a network of drainage canals",
        "housing": "1970s to 2000s single-story homes, many with pool cages, under the Rotonda West Association's deed restrictions",
        "zips": "33947"},
    "placida": {"name": "Placida, Grove City & Cape Haze", "tier": 2, "county": "Charlotte County", "jurisdiction": "Charlotte County",
        "permit_route": "/permits/charlotte-county/", "miles": 35, "drive": "55 to 65 minutes by SR-776 and Placida Road",
        "population": "2,402 in the Grove City CDP (Census 2020)", "wiki": "https://en.wikipedia.org/wiki/Placida,_Florida",
        "lat": 26.8340, "lng": -82.2650, "flood": "AE and VE along Lemon Bay, Gasparilla Sound and the Cape Haze peninsula",
        "soil": "sand and shell fill on filled waterfront lots; Myakka fine sand inland",
        "housing": "waterfront homes with boat lifts, 1980s to 2010s golf-course homes in Cape Haze",
        "zips": "33946, 33947"},
}
CITY_ORDER = ["sarasota", "fruitville-bee-ridge", "gulf-gate", "siesta-key", "palmer-ranch", "longboat-key", "osprey",
              "nokomis", "venice", "south-venice", "north-port", "englewood", "port-charlotte", "rotonda-west", "placida"]
TIER1 = [c for c in CITY_ORDER if CITIES[c]["tier"] == 1]
TIER2 = [c for c in CITY_ORDER if CITIES[c]["tier"] == 2]

# city × service pages that get their own URL (justified by demand or a real local difference;
# every other combination is answered on the service page and the city hub without a new URL).
CITY_SERVICE = [
    ("sarasota", "concrete-pool-decks"), ("sarasota", "pavers-pool-decks"), ("sarasota", "concrete-driveways"),
    ("sarasota", "pavers-driveways"), ("sarasota", "concrete-repair"), ("sarasota", "pavers-sealing"),
    ("siesta-key", "pavers-pool-decks"), ("siesta-key", "concrete-pool-decks"), ("siesta-key", "pavers-sealing"),
    ("siesta-key", "pavers-repair-storm-restoration"),
    ("longboat-key", "pavers-pool-decks"), ("longboat-key", "pavers-driveways"), ("longboat-key", "pavers-sealing"),
    ("longboat-key", "pavers-repair-storm-restoration"),
    ("palmer-ranch", "concrete-driveways"), ("palmer-ranch", "pavers-driveways"), ("palmer-ranch", "concrete-pool-decks"),
    ("palmer-ranch", "pavers-pool-decks"),
    ("gulf-gate", "concrete-driveways"), ("gulf-gate", "concrete-repair"), ("gulf-gate", "concrete-pool-decks"),
    ("gulf-gate", "pavers-driveways"),
    ("fruitville-bee-ridge", "concrete-driveways"), ("fruitville-bee-ridge", "concrete-slabs"),
    ("fruitville-bee-ridge", "pavers-patios-lanais"), ("fruitville-bee-ridge", "concrete-repair"),
    ("osprey", "pavers-pool-decks"), ("osprey", "pavers-driveways"), ("osprey", "pavers-travertine-shellstone"),
    ("osprey", "concrete-driveways"),
    ("nokomis", "pavers-driveways"), ("nokomis", "pavers-pool-decks"), ("nokomis", "concrete-driveways"),
    ("nokomis", "concrete-patios-lanais"),
    ("venice", "concrete-driveways"), ("venice", "concrete-pool-decks"), ("venice", "pavers-pool-decks"),
    ("venice", "concrete-resurfacing"),
    ("south-venice", "concrete-driveways"), ("south-venice", "concrete-repair"), ("south-venice", "pavers-patios-lanais"),
    ("south-venice", "concrete-slabs"),
    ("north-port", "concrete-driveways"), ("north-port", "concrete-repair"), ("north-port", "pavers-pool-decks"),
    ("north-port", "concrete-slabs"),
    ("englewood", "pavers-pool-decks"), ("englewood", "pavers-repair-storm-restoration"), ("englewood", "concrete-driveways"),
    ("englewood", "concrete-repair"),
    ("port-charlotte", "pavers-pool-decks"), ("port-charlotte", "pavers-driveways"), ("port-charlotte", "concrete-driveways"),
    ("port-charlotte", "concrete-repair"),
    ("rotonda-west", "pavers-pool-decks"), ("rotonda-west", "pavers-driveways"), ("rotonda-west", "concrete-driveways"),
    ("rotonda-west", "concrete-repair"),
    ("placida", "pavers-pool-decks"), ("placida", "pavers-driveways"), ("placida", "concrete-driveways"),
    ("placida", "concrete-repair"),
]


def cs_route(city, service):
    return SERVICES[service]["route"] + city + "/"


# --------------------------------------------------------------------------- navigation
NAV_PRIMARY = [
    ("Concrete", "/concrete/", [(SERVICES[k]["nav"], SERVICES[k]["route"]) for k in CONCRETE_ORDER]),
    ("Pavers", "/pavers/", [(SERVICES[k]["nav"], SERVICES[k]["route"]) for k in PAVER_ORDER]),
    ("Areas", "/areas/", [(CITIES[c]["name"], f"/areas/{c}/") for c in TIER1] + [("Charlotte County coast", "/areas/charlotte-county/")]),
    ("Pricing", "/pricing/", [("Concrete cost guide", "/pricing/concrete/"), ("Paver cost guide", "/pricing/pavers/"),
                              ("Pool deck cost guide", "/pricing/pool-decks/"), ("Sarasota Concrete Cost Index", "/pricing/sarasota-concrete-cost-index/")]),
    ("Permits", "/permits/", [("Sarasota County", "/permits/sarasota-county/"), ("City of Sarasota", "/permits/city-of-sarasota/"),
                              ("Venice", "/permits/venice/"), ("North Port", "/permits/north-port/"), ("Longboat Key", "/permits/longboat-key/"),
                              ("Charlotte County", "/permits/charlotte-county/"), ("Flood zones & the 50% rule", "/permits/flood-zones-50-percent-rule/"),
                              ("Sea turtle lighting", "/permits/sea-turtle-lighting/")]),
    ("Coastal", "/coastal/", [("Pool deck surface temperature study", "/coastal/pool-deck-surface-temperature-study/"),
                              ("Salt and concrete", "/coastal/salt-and-concrete/"), ("Storm season playbook", "/coastal/storm-season-playbook/"),
                              ("Post-storm restoration", "/coastal/post-storm-restoration/"), ("Maintenance calendar", "/coastal/maintenance-calendar/")]),
    ("Tools", "/tools/", [("Coastal surface selector", "/tools/coastal-surface-selector/"), ("Permit, flood & setback finder", "/tools/permit-flood-setback-finder/"),
                          ("Concrete & paver calculator", "/tools/concrete-paver-calculator/"), ("Pour calendar", "/tools/pour-calendar/")]),
    ("Guides", "/guides/", []),
]
FOOTER_COLUMNS = [
    ("Concrete", [(SERVICES[k]["name"], SERVICES[k]["route"]) for k in CONCRETE_ORDER]),
    ("Pavers & hardscape", [(SERVICES[k]["name"], SERVICES[k]["route"]) for k in PAVER_ORDER]),
    ("Sarasota County", [(CITIES[c]["name"], f"/areas/{c}/") for c in TIER1]),
    ("Charlotte County", [(CITIES[c]["name"], f"/areas/{c}/") for c in TIER2] + [("Charlotte County hub", "/areas/charlotte-county/")]),
    ("Resources", [("Compare surfaces", "/compare/"), ("HOA & ARC guides", "/hoa/"), ("FAQ", "/faq/"), ("Ask the Estimator", "/guides/ask-the-estimator/"),
                   ("Gallery", "/gallery/"), ("Projects", "/projects/"), ("Reviews", "/reviews/"), ("Data & methods", "/data-and-methods/"),
                   ("Editorial standards", "/editorial-standards/"), ("Directories", "/directories/")]),
    ("Company", [("About", "/about/"), ("Warranty", "/warranty/"), ("Financing", "/financing/"), ("Contact", "/contact/"),
                 ("Privacy", "/privacy/"), ("Terms", "/terms/"), ("Accessibility", "/accessibility/")]),
]

# Form select options (section 4 of the prompt)
FORM_LOCALITIES = [CITIES[c]["name"] for c in CITY_ORDER] + ["Lido Key / Bird Key / St. Armands", "Warm Mineral Springs", "Casey Key", "Manasota Key", "Laurel", "Somewhere else within 40 miles"]
FORM_SERVICES_CONCRETE = [SERVICES[k]["name"] for k in CONCRETE_ORDER]
FORM_SERVICES_PAVERS = [SERVICES[k]["name"] for k in PAVER_ORDER]
FORM_PROPERTY = ["Single-family home", "Condo or HOA common area", "Barrier-island home", "Commercial or multi-family"]
FORM_FLOOD = ["Not sure", "Zone X", "Zone AE", "Zone VE"]
FORM_TIMELINE = ["As soon as possible", "Next 1 to 3 months", "Before the season (November)", "Planning for next year"]
FORM_PRESENCE = ["I'm at the property year-round", "I'm here seasonally", "I'm out of state right now"]
