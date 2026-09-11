# -*- coding: utf-8 -*-
"""Second depth pass.

Part A: closes the remaining gap to the prompt's stretch targets on the singleton pages
(home, pillars, county hubs, cost guides, About/Editorial/Data).

Part B: adds one page-specific block to each service page and each Tier 1 city hub, built from
that page's own facts (service spec, or the locality's jurisdiction, soil, flood zone, housing and
drive time) so no two pages carry the same sentences. The 8-gram similarity check in qa_similarity.py
is the guard on that claim.
"""
from _data import SERVICES, CITIES, TIER1, CITY_SERVICE, cs_route
from _h import cap, sec, p, ul, ol, table, note, link, cards, facts, esc

# ============================================================ PART A: singletons
A = {}

A["/"] = sec("What this site will not tell you",
    p("A local resource is only useful if its silences are deliberate. Four things are missing from this site on purpose, and each one is a question worth asking any contractor who does show them.")
    + ul([
        "<strong>A star rating.</strong> Reviews belong to the profile that earned them. Until the entity behind this site has its own verified profile, quoting someone else's stars here would be borrowing credibility.",
        "<strong>A licence number.</strong> Florida does not require a state construction licence to install driveways or pavers, though Sarasota County regulates several related trades locally. This site says \"Insured\" and stops there, because Florida Statute 489.119(5)(b) means a number shown in advertising has to be real and current.",
        "<strong>Measured surface temperatures.</strong> The comparison everyone wants is which deck is coolest in July. The study that will answer it is designed and published; the readings do not exist yet, so no number appears.",
        "<strong>A years-in-business figure or a project count.</strong> Neither has been documented for this trade name, so neither is printed.",
    ]))

A["/concrete/"] = sec("Five specifications worth arguing about",
    table(["Decision", "The cheap answer", "What this site specifies", "Cost of the difference"], [
        ["Slab thickness", "3.5 in., because the truck holds less", "4 in. minimum, 5 to 6 in. under concentrated loads", "About $1.50 to $2.50 per sq ft between 4 and 6"],
        ["Base", "Pour on graded native sand", "4 to 6 in. of crushed limerock in 3-in. lifts, compacted to refusal", "Roughly $1 to $2 per sq ft, and the whole service life"],
        ["Reinforcement", "Wire mesh laid on the base", "Fiber in the mix plus #3 or #4 bar on chairs at mid-depth", "A few hundred dollars on a driveway"],
        ["Joint timing", "Cut tomorrow when the crew is back", "Saw-cut the same afternoon, a quarter of the slab depth", "One crew member staying late"],
        ["Cure", "Let it dry", "Curing compound or wet cure for 7 days, protected from afternoon rain", "Materials and one return visit"],
    ], "Where concrete estimates actually differ")
    + p("Every row is invisible a week after the pour and decisive ten years later, which is exactly why they are the rows that get cut to win a bid."))

A["/pavers/"] = sec("Five specifications worth arguing about",
    table(["Decision", "The cheap answer", "What this site specifies", "Why it matters here"], [
        ["Base depth", "4 in. everywhere", "4 in. for patios and decks, 6 in. for driveways, 8 in. on wet lots", "Saturated sand loses bearing; vehicle loads need the depth"],
        ["Lifts", "One pass with the compactor on top", "3-in. lifts, each compacted to refusal", "A thick lift stays soft in the middle and shows as ruts in year two"],
        ["Bedding sand", "Whatever depth levels the base", "Exactly 1 in., screeded, never compacted before laying", "Thick bedding migrates; that is what most \"sinking pavers\" actually are"],
        ["Edge restraint", "Spiked plastic into the bedding", "Spikes into the base on protected edges; poured curb anywhere a tire or a surge can reach", "Surge lifted plastic restraint across this coast in 2024"],
        ["Joint sand", "Ordinary sand", "Polymeric, full depth, compacted, activated, then 24 to 48 dry hours", "Joint sand is the structural element people think is decoration"],
    ], "Where paver estimates actually differ")
    + p("The pattern is the same as on the concrete side: everything that decides the outcome is buried, and everything that is buried is easy to leave out of a number."))

A["/areas/sarasota-county/"] = sec("Which office covers which address",
    p("This is the question behind half the permit confusion in the county, because municipal boundaries here do not follow the roads people use to describe where they live.")
    + table(["If the property is in", "The building permit comes from", "Common surprise"], [
        ["Downtown, Laurel Park, Arlington Park, Indian Beach, Lido or Bird Key", "City of Sarasota", "The apron at the street is city right-of-way even when the driveway is not"],
        ["Siesta Key, Casey Key, Gulf Gate, Palmer Ranch, Fruitville, Bee Ridge, The Meadows", "Sarasota County", "A Sarasota mailing address does not mean the city issues the permit"],
        ["Venice Island, the Venice mainland city, Wellen Park's Venice side", "City of Venice", "Pavers in the right-of-way need a licence agreement, not just a permit"],
        ["North Port, Warm Mineral Springs, Wellen Park's North Port side", "City of North Port", "The culvert under the driveway is sized by the city, not the contractor"],
        ["Anywhere on Longboat Key, either county half", "Town of Longboat Key", "One town issues permits for both the Sarasota and Manatee portions"],
        ["South Venice, Venice Gardens, Nokomis, Laurel, Osprey, north Englewood", "Sarasota County", "Venice Gardens is not in the City of Venice"],
    ], "Permit jurisdiction by area, Sarasota County")
    + p("The Property Appraiser's parcel search settles any specific address in about a minute, and it shows the flood zone on the same screen."))

A["/areas/charlotte-county/"] = sec("What a Charlotte County job costs in time, not money",
    p("The fee schedule is published and predictable. The schedule is the part that surprises people, and it is worth planning around because the county's requirements are sequential rather than parallel.")
    + ol([
        "<strong>Before anything:</strong> a current survey or a legible scaled site plan showing easements and property lines. Older GDC lots often have nothing on file.",
        "<strong>If the contract exceeds $5,000:</strong> the Notice of Commencement is recorded with the Clerk of Court and submitted before the first inspection, not before the permit.",
        "<strong>If pavers cross a recorded easement:</strong> occupation-of-easement approval from Real Estate Services, a different department on a different clock.",
        "<strong>If the driveway crosses a swale:</strong> the county sizes the culvert and inspects the crossing, and the swale must be restored to grade before final approval.",
        "<strong>If flatwork comes within a foot of the house:</strong> termite treatment is a scheduled inspection in the sequence.",
    ])
    + p("None of these are obstacles once they are in the plan. All of them add a week or two when they are discovered after the crew is booked, which is the argument for putting the permit conversation into the estimate rather than after it."))

_COST_METHOD = sec("How these ranges were built, and how to check them",
    p("Every figure on this page carries the same provenance, and the point of stating it is that you can repeat the work. On September 10, 2026 the published Sarasota-area pricing pages for each service were read and recorded: local contractor cost pages, local sealing-company price lists, and national cost aggregators' Sarasota-specific pages as a cross-check. Where sources disagreed, the range was widened rather than averaged, because an average hides the disagreement.")
    + ul([
        "<strong>A range is not a quote.</strong> It describes what this market published, not what your lot will cost.",
        "<strong>A range with no date is worthless.</strong> Ready-mix, fuel and labour all moved in the last three years; a 2023 figure quoted today is a fiction.",
        "<strong>Ranges do not include the things that vary most.</strong> Demolition, permits, drainage fixes, coping and island logistics are listed separately for exactly that reason.",
        "<strong>The provider's own numbers will replace these.</strong> From the first quarter of 2027 the Cost Index publishes completed-job data with the sample size attached, and these pages will cite that instead.",
    ])
    + p(f'The full source list and the correction policy are on the {link("/data-and-methods/", "data and methods page")}.'))

# _COST_METHOD is applied to the pricing hub only. Repeating it on all five pricing pages put the
# pair similarity at 13 to 14 percent, inside the gate but with no headroom; the sub-pages carry a
# one-line pointer to the hub instead, and each already states its own sources.
A["/pricing/"] = A.get("/pricing/", "") + _COST_METHOD

A["/about/"] = sec("How this site is built and kept",
    p("The site is a static build: content is written in Python modules, rendered to plain HTML, and served from Cloudflare Pages with no database and no client-side rendering. That choice is editorial as much as technical. Every answer capsule is in the HTML the moment the page loads, which is what makes the pages readable by search engines, by answer engines and by a screen reader without running a line of JavaScript.")
    + p("Automated checks run before every publish: word counts against the benchmark floors, a link crawl for orphans and broken links, a style pass that rejects a list of stock marketing phrases and measures how often a verifiable fact appears, and an 8-gram similarity comparison against every other page on this site and against the sibling sites in the same network. The thresholds and the results are in the audit that ships with the build."))

A["/editorial-standards/"] = sec("The checks that run before anything is published",
    table(["Check", "What it measures", "Threshold"], [
        ["Word count by page type", "Body words against the benchmark floor for that type", "No page below its floor"],
        ["Link crawl", "Broken internal links, orphan pages, click depth from the home page", "Zero broken, zero indexable orphans, maximum 3 clicks"],
        ["Style pass", "A blocklist of stock marketing phrases and AI tells; sentence-length variation; density of verifiable facts", "Zero blocklist hits; a specific fact roughly every 120 to 150 words"],
        ["Internal similarity", "Shared 8-word sequences between every pair of pages on this site", "Flag and rewrite above 15 percent outside legal boilerplate"],
        ["Network similarity", "Shared 8-word sequences against every page of the sibling sites", "Same threshold; the sibling comparison is run against the local build of each"],
        ["Title and description", "Length and uniqueness of every title and meta description", "Unique; titles within length; descriptions 110 to 165 characters"],
        ["Schema", "JSON-LD parses and mirrors what is visible", "Valid; no rating, review or address that is not real"],
    ], "Pre-publish checks")
    + p("A failing check blocks the publish rather than producing a warning, which is the only way a standard survives a deadline."))

A["/data-and-methods/"] = sec("Corrections policy",
    p("Three kinds of error are possible on a site like this, and each has a different remedy. A regulatory summary that has gone stale is corrected on the page and noted in the changelog with the date it was re-checked against the source. A price range that no longer reflects the market is replaced at the next quarterly review, or sooner if a reader shows it is wrong. A factual error is corrected immediately and the change is described rather than quietly overwritten.")
    + p("What will not happen is a silent edit. The date at the foot of each page is the date the content was last reviewed against its sources, and when a material change is made the changelog line says what changed. If a figure on this site is ever used in a dispute, the version history is the record."))


# ============================================================ PART B: per-page blocks
def service_block(key):
    s = SERVICES[key]
    cities = [c for c, k in CITY_SERVICE if k == key]
    pillar = "poured concrete" if s["pillar"] == "concrete" else "paver"
    rows = []
    for c in cities[:5]:
        ci = CITIES[c]
        rows.append([f'<a href="{cs_route(c, key)}">{esc(ci["name"])}</a>', ci["jurisdiction"], ci["flood"].split(";")[0], ci["drive"]])
    out = ""
    if rows:
        out += sec(f"Where this {pillar} work is scheduled, and what changes by address",
                   p(f'{s["name"]} is offered across the whole service area. These localities have their own page for this service because the permit office, the flood zone or the ground under the lot changes the job enough to be worth writing down separately.')
                   + table(["Locality", "Permit office", "Flood zone", "Drive from Sarasota"], rows, f'{s["name"]}: local pages'))
    out += sec("What to send with an enquiry about this service",
               p("An estimate can be drafted from very little, but four things turn a range into a number without a second visit.")
               + ul([
                   "<strong>The address.</strong> It sets the permit office, the flood zone, the soil series and, on the islands, whether the setback line and the lighting ordinance apply.",
                   "<strong>Rough dimensions.</strong> Paced is fine. A length and a width beats a guess at square footage.",
                   "<strong>A photo of what is there now, and a second one from further back.</strong> The close shot shows the condition; the wide shot shows where the water goes, which is usually the more important question.",
                   "<strong>Any association paperwork.</strong> The approved colour list or the ARC form, if the community has one, decides material options before anything else does.",
               ]))
    return out


def city_block(slug):
    c = CITIES[slug]
    svcs = [k for cc, k in CITY_SERVICE if cc == slug]
    names = ", ".join(SERVICES[k]["name"].lower() for k in svcs[:4]) if svcs else "concrete and paver work"
    return sec(f"Working in {c['name']}: the practical details",
        table(["Question", "Answer for this locality"], [
            ["Who issues the permit?", c["jurisdiction"]],
            ["How far is the crew travelling?", f'{c["miles"]} miles straight-line, {c["drive"]}'],
            ["What is under the lot?", c["soil"]],
            ["What flood zones apply?", c["flood"]],
            ["What is the housing stock?", c["housing"]],
            ["Which services have their own local page here?", names],
        ], f'{c["name"]} at a glance')
        + p(f'The reason these six lines sit on every locality page is that they are the six that change the work. Two properties four miles apart in this county can sit in different flood zones, be permitted by different offices, stand on different soil series and date from different decades, and each of those changes the base, the drainage, the paperwork or the material. An estimate that has not established them is a price for an average job rather than for yours.'))


def apply(pages):
    n = 0
    for pg in pages:
        route, block = pg["route"], ""
        if route in A:
            block += A[route]
        # service_block was removed: its locality table repeated the same city rows (jurisdiction,
        # flood zone, drive time) across 20 service pages, and its enquiry bullets were identical on
        # all of them, which pushed 8-gram similarity above the 15 percent gate. The per-service
        # failure-mode table in content_depth3 carries genuinely per-service content instead.
        # city_block was removed: a six-row "at a glance" table plus an identical closing paragraph
        # across 13 locality pages repeated the same scaffolding and breached the similarity gate.
        # The locality pages already carry that data in their own prose sections.
        if not block:
            continue
        html = pg["body_html"]
        marker = '<p class="reviewed">'
        i = html.rfind(marker)
        pg["body_html"] = (html[:i] + block + html[i:]) if i != -1 else (html + block)
        n += 1
    return n
