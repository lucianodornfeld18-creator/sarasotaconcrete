# -*- coding: utf-8 -*-
"""Pricing hub, three cost guides and the Cost Index page. All ranges are labeled planning ranges compiled from
published Sarasota-area sources on 2026-09-10; the Cost Index publishes methodology now and data when it exists."""
import json
import pathlib

from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, link, ext, facts, cards, dataset_schema

SRC = "Planning ranges compiled on September 10, 2026 from published Sarasota-area pricing (Sarasota paver and sealing contractors, regional concrete contractors, and national cost aggregators as cross-checks). Not quotes. Method on the data and methods page."
DATA = pathlib.Path(__file__).resolve().parent / "data"


def pg(route, title, meta, h1, kicker, lede, body, faq=None, crumb=None, schema=None):
    return {"route": route, "title": title, "meta_description": meta, "h1": h1, "kicker": kicker, "lede": lede,
            "breadcrumbs": [("Home", "/"), ("Pricing", "/pricing/"), (crumb, None)] if crumb else [("Home", "/"), ("Pricing", None)],
            "body_html": body, "faq": faq or [], "article": True, "schema": schema or []}


def hub():
    faq = [
        ("Why do three Sarasota quotes for the same driveway differ by thousands of dollars?", "Usually because they aren't for the same driveway. One includes demolition and haul-off, one assumes the old slab stays as base, one has 4 inches of compacted limerock and one has none, one carries a right-of-way permit and a culvert and one doesn't mention them. Line up the scopes item by item before you compare the totals."),
        ("Do hardscape prices rise during snowbird season from January to April?", "Lead times do; the county's population rises past 570,000 in winter and every crew's calendar fills. Material prices don't move with the season, but a job that has to squeeze into a March window before an owner leaves will cost more in overtime and scheduling than the same job in July."),
        ("What should a written estimate include?", "Square footage, thickness or paver system, base depth and material, reinforcement, drainage, demolition and haul-off, permit responsibility and fees, schedule window, payment schedule, warranty terms and the legal name of the contractor. If any of those is missing, the total isn't comparable."),
        ("Is the low bid a bad sign?", "Not by itself. A low bid with a full scope is a good bid; a low bid with no base, no joints and no permit is a driveway you'll replace again in ten years."),
    ]
    body = cap("What do concrete and pavers cost in Sarasota County in 2026?",
               "As of September 10, 2026, published Sarasota-area pricing supports these installed planning ranges: broom concrete flatwork $7 to $13 per square foot, stamped concrete $12 to $20, decorative overlays $10 to $15, concrete pavers $13 to $16 (patios and decks) and $14 to $22 (driveways), travertine $20 to $26, marble and porcelain $22 to $34, and cleaning-re-sanding-sealing $1 to $3. Demolition adds $2 to $4.",
               p(SRC + " From the first quarter of 2027 the Sarasota Concrete Cost Index replaces these third-party ranges with the provider's own completed-job data."))
    body += cards([("/pricing/concrete/", "Concrete cost guide", "Driveways, patios, pool decks, slabs, stamped, repair and resurfacing by size band."),
                   ("/pricing/pavers/", "Paver cost guide", "Pool decks, driveways, patios, walkways, sealing and repair by material."),
                   ("/pricing/pool-decks/", "Pool deck cost guide", "Concrete, overlay, pavers, travertine and porcelain for 400 to 1,000 square feet."),
                   ("/pricing/sarasota-concrete-cost-index/", "Sarasota Concrete Cost Index", "Quarterly installed-cost index by service and locality, CC BY 4.0, JSON at /api/cost-index.json."),
                   ("/tools/concrete-paver-calculator/", "Calculator", "Quantities and a dated cost range for your dimensions."),
                   ("/financing/", "Financing", "Payment schedules and the lender partner when confirmed.")])
    body += sec("What moves the number in this market", table(["Factor", "Direction", "Typical effect"], [
        ["Demolition of an old slab or pavers", "Up", "$2 to $4 per sq ft; more for pavers over concrete"],
        ["Base depth (4 vs 6 in.) and geotextile", "Up", "$1 to $1.50 per sq ft"],
        ["Right-of-way apron, culvert, swale work", "Up", "$500 to $5,000 by jurisdiction"],
        ["Barrier-island logistics (bridges, staging, salt-resistant mix)", "Up", "5 to 15 percent"],
        ["Access (backyard by wheelbarrow, pump truck)", "Up", "$600 to $1,200 for a pump; labor for wheelbarrow"],
        ["Job size", "Down per foot as size grows", "Mobilization spreads over more feet"],
        ["Season", "Lead time up Jan to Apr", "Overtime to hit a window"],
        ["Material tier", "Up", "Concrete pavers → travertine → porcelain/marble"],
        ["Permit fees", "Up", "$22 to $400 in fees; Charlotte line-and-grade $310"]], "Price drivers, Sarasota County, 2026"))
    body += sec("How to read a range on this site", p("Every range has a date and a source. \"Planning range\" means compiled from published local pricing on the stated date; \"Cost Index\" means the provider's own completed-job data with sample size. Neither is a quote. A written estimate after a site visit or video walkthrough is the number that binds, and it should be comparable line by line to any other estimate you get."))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("/pricing/", "Concrete & Paver Prices in Sarasota, FL (2026 Ranges)", "Installed planning ranges for concrete, stamped work, overlays, concrete pavers, travertine, porcelain and sealing in Sarasota County as of September 2026, the nine factors that move them, and how to compare estimates.",
              "What concrete and pavers cost in Sarasota County, with the date on it", "Pricing hub", "Installed planning ranges by service and material, compiled from published local pricing on a stated date, and the factors that move a quote in this market.", body, faq)


def concrete():
    faq = [
        ("What does a two-car concrete driveway cost in Sarasota County?", "About $5,500 to $9,500 for 600 square feet of broom-finished 4-inch concrete on a compacted base as a planning range on September 10, 2026, plus $1,200 to $2,400 for demolition of the old slab and $500 to $2,500 if the apron or a culvert is in scope."),
        ("What does a 12x20 lanai slab cost in Venice?", "About $2,000 to $3,200 for 240 square feet of 4-inch broom concrete on compacted base, plus $300 to $700 for a floor drain and any cage re-anchoring. Venice's permit and, on the island, engineering review add time rather than much cost."),
        ("What does a generator or AC pad cost?", "AC pads $350 to $700; standby generator pads $600 to $1,400 including anchor bolts to the template; small pads cost more per foot because mobilization is fixed."),
        ("How much more does a 6-inch driveway cost than 4-inch?", "About $1.50 to $2.50 per square foot more, or $900 to $1,500 on a 600-square-foot driveway, for the extra concrete and heavier steel."),
    ]
    rows = [["Concrete driveway, broom", "400 to 900 sq ft", "$7 to $12", "$5,500 to $9,500 (600 sq ft)", "+$2 to $4 demolition; apron/culvert separate"],
            ["Driveway, 6 in. for heavy loads", "same", "$9 to $14", "$6,500 to $11,000", "#4 bar"],
            ["Patio or lanai slab, broom", "150 to 600 sq ft", "$8 to $13", "$2,000 to $3,200 (240 sq ft)", "Drain $300 to $700"],
            ["Exposed aggregate or colored slab", "same", "$11 to $17", "$2,800 to $4,500 (240 sq ft)", ""],
            ["Concrete pool deck, textured, new", "500 to 1,000 sq ft", "$9 to $14", "$7,000 to $10,000 (700 sq ft)", "Demolition, drains, cage anchors separate"],
            ["Pool deck resurfacing, basic overlay", "same", "$4 to $8", "$3,000 to $5,500 (700 sq ft)", "Slab must pass the tests"],
            ["Pool deck resurfacing, decorative overlay", "same", "$10 to $15", "$7,000 to $10,500 (700 sq ft)", ""],
            ["Stamped concrete", "200 to 800 sq ft", "$12 to $20", "$5,000 to $8,000 (400 sq ft)", "Reseal every 2 to 3 yrs"],
            ["Sidewalk or walkway", "100 to 300 sq ft", "$9 to $14", "$1,500 to $2,300 (160 sq ft)", ""],
            ["Slabs and pads", "16 to 200 sq ft", "$9 to $15", "$350 to $2,200", "Hot tub 6 in."],
            ["Crack routing and sealing", "per lin ft", "$8 to $20", "$300 to $900 typical", ""],
            ["Slab lifting (polyurethane)", "per area", "n/a", "$500 to $2,500", "Fix the water first"],
            ["Panel replacement", "per panel", "n/a", "$400 to $900", ""]]
    body = facts([("Date", "September 10, 2026"), ("Basis", "Published Sarasota-area pricing; planning ranges"), ("Spec assumed", "4 in., 4,000 PSI, fiber, compacted base"), ("Not included", "Permit fees, culverts, cage work unless stated")])
    body += cap("What does concrete cost per square foot in Sarasota in 2026?",
                "Broom-finished flatwork runs roughly $7 to $13 per square foot installed on a compacted base as a planning range on September 10, 2026, with exposed aggregate and integral color at $11 to $17, stamped work at $12 to $20, basic pool deck overlays at $4 to $8 and decorative overlays at $10 to $15. A 600-square-foot two-car driveway lands near $5,500 to $9,500 before demolition.",
                p(SRC))
    body += sec("Concrete cost table", table(["Service", "Typical size", "Installed per sq ft", "Typical project", "Notes"], rows, "Concrete planning ranges, Sarasota County, September 10, 2026"))
    body += sec("What's inside the number", ul(["Ready-mix at roughly $150 to $190 per cubic yard delivered in the Sarasota market in 2026 (regional pricing), which for a 4-inch slab is about $2 to $2.40 per square foot of concrete alone.", "Base material, compaction and forming.", "Reinforcement: fiber, and #3 or #4 bar on chairs for vehicle slabs.", "Finishing, same-day joint cutting and cure.", "Mobilization, which is why a 40-square-foot pad costs $15 per foot and a 900-square-foot driveway costs $8."]))
    body += sec("What's outside it", ul(["Demolition and haul-off: $2 to $4 per square foot.", "Right-of-way apron to a city detail, culvert, swale regrading: $500 to $5,000.", "Permit fees and a recorded Notice of Commencement.", "Deck drains, cage re-anchoring, coping.", "Barrier-island logistics: 5 to 15 percent."]))
    body += sec("Comparing estimates line by line", p(f'Use the {link("/pricing/", "pricing hub")}\'s checklist: square footage, thickness, base depth and material, reinforcement, joints, drainage, demolition, permits, schedule, payment terms, warranty, legal name. A quote missing the base or the permit line isn\'t cheaper; it\'s incomplete.'))
    body += sec("Sources used for this guide", ul(["Sarasota-area concrete contractor cost pages for driveways, overlays and pool deck resurfacing (read September 10, 2026).", "National cost aggregators' Sarasota driveway and stamped-concrete pages as cross-checks.", "Regional ready-mix pricing.", f"Full list on the {link('/data-and-methods/', 'data and methods page')}."]))
    body += faq_block(faq)
    body += cta("Get a written concrete estimate", "/contact/", "A site visit or video walkthrough replaces every range on this page with one number.")
    body += reviewed("September 10, 2026")
    return pg("/pricing/concrete/", "Concrete Cost in Sarasota, FL (2026): Driveways, Decks, Slabs", "Concrete planning ranges for Sarasota County on September 10, 2026: driveways $7 to $12 per sq ft, patios, pool decks new and resurfaced, stamped, walkways, pads and repair, with what's inside and outside each number.",
              "Concrete cost guide for Sarasota County, September 2026", "Pricing · concrete", "Installed planning ranges per square foot and per typical project for every concrete service, what's inside the number, and what's charged separately.", body, faq, "Concrete cost guide")


def pavers():
    faq = [
        ("Is a paver driveway or a concrete driveway cheaper over 20 years in North Port?", "Concrete is cheaper to install ($7 to $12 versus $14 to $22 per square foot) and, on a GDC lot where the swale and the base are handled properly, lasts 30 years with little spending. Pavers cost more up front, need re-sanding and sealing every 2 to 3 years, and win when repairs happen: a settled section is lifted and reset for hundreds, not replaced for thousands. Over 20 years they're close; flood exposure tips it toward pavers."),
        ("How much does paver cleaning and sealing cost?", "$1 to $3 per square foot for cleaning, polymeric re-sanding and sealing together, with cleaning alone at $0.40 to $0.60 and a service minimum of about $150 to $250, per published Sarasota sealing-company pricing."),
        ("What does it cost to lift and reset sunken pavers?", "$8 to $15 per square foot of the affected area as a planning range, plus base material, and less per foot on larger areas."),
        ("What does travertine cost installed?", "$20 to $26 per square foot in Sarasota on September 10, 2026, with coping at $30 to $60 per linear foot."),
    ]
    rows = [["Concrete pavers, patio or pool deck", "300 to 1,000 sq ft", "$13 to $16", "$9,000 to $11,000 (700 sq ft)", "Coping, drains, demolition separate"],
            ["Concrete pavers, driveway", "400 to 900 sq ft", "$14 to $22", "$8,500 to $13,000 (600 sq ft)", "6 in. base, curbs"],
            ["Travertine or shellstone", "same", "$20 to $26", "$14,000 to $18,000 (700 sq ft)", "Coping $30 to $60 per lin ft"],
            ["Honed marble", "same", "$24 to $34", "$17,000 to $24,000 (700 sq ft)", ""],
            ["2 cm porcelain", "same", "$22 to $32", "$15,500 to $22,500 (700 sq ft)", "Base tolerance 1/8 in."],
            ["Permeable paver driveway", "400 to 900 sq ft", "$18 to $30", "$11,000 to $18,000 (600 sq ft)", "Open-graded base"],
            ["Walkway", "100 to 250 sq ft", "$14 to $20", "$2,200 to $3,200 (160 sq ft)", ""],
            ["Steps", "per riser", "n/a", "$250 to $500", "Concrete or block core"],
            ["Seat wall", "per lin ft", "n/a", "$60 to $120", "With cap"],
            ["Outdoor kitchen base", "per lin ft", "n/a", "$250 to $600", "Before appliances"],
            ["Cleaning only", "per sq ft", "$0.40 to $0.60", "$150 to $400 (600 sq ft)", "Minimum $150 to $250"],
            ["Clean, re-sand and seal", "per sq ft", "$1 to $3", "$600 to $1,800 (600 sq ft)", ""],
            ["Lift and reset", "per sq ft affected", "$8 to $15", "", "Plus base"],
            ["Hardscape lighting", "per fixture", "n/a", "$150 to $350", "Transformer $300 to $700"],
            ["Artificial turf", "per sq ft", "$10 to $18", "$3,000 to $5,400 (300 sq ft)", ""]]
    body = facts([("Date", "September 10, 2026"), ("Basis", "Published Sarasota-area pricing; planning ranges"), ("Spec assumed", "Compacted base in lifts, 1 in. bedding, polymeric sand"), ("Not included", "Demolition, coping, drains, permit fees unless stated")])
    body += cap("What do pavers cost per square foot in Sarasota in 2026?",
                "Installed concrete pavers run roughly $13 to $16 per square foot for patios and pool decks and $14 to $22 for driveways as planning ranges on September 10, 2026; travertine and shellstone $20 to $26; marble $24 to $34; 2 cm porcelain $22 to $32; permeable driveways $18 to $30. Cleaning, re-sanding and sealing together run $1 to $3 per square foot.",
                p(SRC))
    body += sec("Paver cost table", table(["Service", "Typical size", "Installed per sq ft", "Typical project", "Notes"], rows, "Paver and hardscape planning ranges, Sarasota County, September 10, 2026"))
    body += sec("What's inside the number", ul(["Pavers: concrete units roughly $3 to $6 per square foot at the yard, travertine $6 to $12, porcelain $8 to $15, marble $10 to $20, in 2026 regional pricing.", "Base: 6 inches of crushed limerock or recycled concrete for a driveway is about 0.02 tons per square foot, delivered and compacted in lifts.", "Bedding sand, polymeric sand, edge restraint or curb.", "Cutting, laying, compaction.", "Mobilization."]))
    body += sec("What's outside it", ul(["Demolition and haul-off: $2 to $4 per square foot, more for pavers over concrete.", "Coping: $25 to $60 per linear foot by material.", "Deck drains: $300 to $900 per run.", "Right-of-way apron, license agreement, culvert.", "Sealing at 30 days: $1 to $3 per square foot.", "Barrier-island logistics: 5 to 15 percent."]))
    body += sec("Sources used for this guide", ul(["Sarasota paver contractor cost pages and installed-price articles (read September 10, 2026).", "Sarasota paver-sealing company price pages.", "Florida paver patio and travertine cost guides as cross-checks.", f"Full list on the {link('/data-and-methods/', 'data and methods page')}."]))
    body += faq_block(faq)
    body += cta("Get a written paver estimate", "/contact/", "Say the material and whether the property is on the water; both change the number.")
    body += reviewed("September 10, 2026")
    return pg("/pricing/pavers/", "Paver Cost in Sarasota, FL (2026): Pool Decks, Driveways, Sealing", "Paver planning ranges for Sarasota County on September 10, 2026: concrete pavers $13 to $22 per sq ft, travertine $20 to $26, marble, porcelain, permeable driveways, walkways, walls, sealing and repair, with what's inside each number.",
              "Paver cost guide for Sarasota County, September 2026", "Pricing · pavers", "Installed planning ranges by material and service, from concrete pavers to porcelain, plus cleaning, sealing, repair and lighting.", body, faq, "Paver cost guide")


def pool_decks():
    faq = [
        ("How much does a paver pool deck cost per square foot in Sarasota in 2026?", "$13 to $16 installed in concrete pavers and $20 to $26 in travertine as planning ranges on September 10, 2026, before demolition, coping and drains. A 700-square-foot deck therefore lands at $9,000 to $11,000 or $14,000 to $18,000."),
        ("What does travertine cost installed around a pool on Siesta Key?", "The same $20 to $26 per square foot as the mainland plus 5 to 15 percent for island logistics, and an annual sealing line for the coping if the pool is salt-chlorinated."),
        ("What does a marble or porcelain paver pool deck cost on Longboat Key?", "$24 to $34 for honed marble and $22 to $32 for porcelain per square foot, plus the island premium; the base tolerance for those materials is part of the price."),
        ("When is resurfacing cheaper than replacement and when is it wasted?", "A basic overlay at $4 to $8 per square foot is cheaper than any replacement when the slab rings solid, drains and has no offset cracks. It's wasted when the slab is hollow, cracked through or pitched toward the house, because the overlay follows the slab down within a couple of summers."),
    ]
    body = facts([("Date", "September 10, 2026"), ("Typical deck", "500 to 1,000 sq ft"), ("Cheapest sound option", "Basic overlay on a solid slab"), ("Longest life", "Pavers or stone on a rebuilt base")])
    body += cap("What does a pool deck cost in Sarasota in 2026, by material?",
                "For a 700-square-foot deck as planning ranges on September 10, 2026: basic overlay on a sound slab $3,000 to $5,500; new textured concrete $7,000 to $10,000; decorative overlay $7,000 to $10,500; concrete pavers $9,000 to $11,000; travertine $14,000 to $18,000; porcelain $15,500 to $22,500; marble $17,000 to $24,000. Demolition, coping, drains and cage anchors are extra.",
                p(SRC))
    body += sec("Pool deck cost table", table(["Option", "Per sq ft", "400 sq ft", "700 sq ft", "1,000 sq ft", "Life", "Maintenance"], [
        ["Basic overlay (sound slab)", "$4 to $8", "$1,600 to $3,200", "$3,000 to $5,500", "$4,000 to $8,000", "8 to 15 yrs", "Reseal 2 to 3 yrs"],
        ["Decorative overlay", "$10 to $15", "$4,000 to $6,000", "$7,000 to $10,500", "$10,000 to $15,000", "8 to 15 yrs", "Reseal 2 to 3 yrs"],
        ["New textured concrete", "$9 to $14", "$3,600 to $5,600", "$7,000 to $10,000", "$9,000 to $14,000", "30 yrs", "Seal coastal lots"],
        ["Concrete pavers", "$13 to $16", "$5,200 to $6,400", "$9,000 to $11,000", "$13,000 to $16,000", "25 to 30 yrs", "Re-sand, seal 18 to 36 mo"],
        ["Travertine / shellstone", "$20 to $26", "$8,000 to $10,400", "$14,000 to $18,000", "$20,000 to $26,000", "30+ yrs", "Seal coping annually on salt"],
        ["Porcelain 2 cm", "$22 to $32", "$8,800 to $12,800", "$15,500 to $22,500", "$22,000 to $32,000", "30+ yrs", "None beyond cleaning"],
        ["Honed marble", "$24 to $34", "$9,600 to $13,600", "$17,000 to $24,000", "$24,000 to $34,000", "30+ yrs", "Penetrating sealer"]], "Pool deck planning ranges by material, Sarasota County, September 10, 2026 (deck field only)"))
    body += sec("Add-ons that show up on most deck jobs", table(["Item", "Range"], [["Demolition of the old deck", "$2 to $4 per sq ft; more for pavers over concrete"], ["Coping", "$25 to $60 per lin ft"], ["Deck drain", "$300 to $900 per run"], ["Cage re-anchoring or new edge beam", "$15 to $40 per anchor; $20 to $40 per lin ft of curb"], ["Barrier-island logistics", "5 to 15 percent"], ["Sealing at 30 days (pavers)", "$1 to $3 per sq ft"], ["Turtle-compliant deck lighting", "$150 to $350 per fixture"]], "Pool deck add-ons"))
    body += sec("How to decide", p(f'Start with the slab: the {link("/compare/resurface-vs-replace-pool-deck/", "six tests")} say whether an overlay is honest. Then the pool: salt-chlorinated pools push toward porcelain, dense concrete pavers or a commitment to annual travertine sealing. Then the lot: VE zones and surge history favor pavers on a rebuildable base. Then heat: light colors and the {link("/coastal/pool-deck-surface-temperature-study/", "temperature study")}, once measured. The {link("/tools/coastal-surface-selector/", "coastal surface selector")} walks through the same order.'))
    body += faq_block(faq)
    body += cta("Get a written pool deck estimate", "/contact/", "Send a photo of the deck and the cage, and say whether the pool is salt.")
    body += reviewed("September 10, 2026")
    return pg("/pricing/pool-decks/", "Pool Deck Cost in Sarasota, FL (2026): Concrete vs Pavers", "Pool deck planning ranges for Sarasota County on September 10, 2026: overlays $4 to $15, new concrete $9 to $14, pavers $13 to $16, travertine $20 to $26, porcelain and marble, for 400 to 1,000 sq ft decks, with add-ons and how to decide.",
              "Pool deck cost guide for Sarasota County, September 2026", "Pricing · pool decks", "Seven options for a 400, 700 or 1,000-square-foot deck, with life, maintenance and the add-ons that show up on nearly every job.", body, faq, "Pool deck cost guide")


def cost_index():
    data = {
        "name": "Sarasota Concrete Cost Index", "version": "0.1-baseline", "license": "CC BY 4.0", "publisher": "Sarasota Concrete (sarasotaconcrete.com)",
        "status": "baseline from published sources; provider completed-job data begins Q1 2027",
        "as_of": "2026-09-10", "unit": "USD per square foot installed, planning range", "geography": "Sarasota County and Charlotte County coast within 40 miles of Sarasota, Florida",
        "method": "Baseline v0.1 compiles published Sarasota-area pricing pages read on 2026-09-10 (sources listed on /data-and-methods/). From Q1 2027 each quarterly release reports installed price per square foot by service, material and locality from the provider's completed jobs in the prior quarter, with sample size (n), median, 25th and 75th percentiles, and limitations. Localities with n<3 are suppressed.",
        "series": [
            {"service": "concrete-driveway-broom", "material": "4in 4000psi", "low": 7, "high": 12, "n": None, "source": "published"},
            {"service": "concrete-patio-broom", "material": "4in", "low": 8, "high": 13, "n": None, "source": "published"},
            {"service": "concrete-pool-deck-new", "material": "4in textured", "low": 9, "high": 14, "n": None, "source": "published"},
            {"service": "pool-deck-overlay-basic", "material": "cementitious overlay", "low": 4, "high": 8, "n": None, "source": "published"},
            {"service": "pool-deck-overlay-decorative", "material": "stamped/textured overlay", "low": 10, "high": 15, "n": None, "source": "published"},
            {"service": "stamped-concrete", "material": "4in stamped", "low": 12, "high": 20, "n": None, "source": "published"},
            {"service": "concrete-walkway", "material": "4in", "low": 9, "high": 14, "n": None, "source": "published"},
            {"service": "paver-patio-pool-deck", "material": "concrete pavers", "low": 13, "high": 16, "n": None, "source": "published"},
            {"service": "paver-driveway", "material": "concrete pavers vehicular", "low": 14, "high": 22, "n": None, "source": "published"},
            {"service": "travertine-shellstone", "material": "natural stone", "low": 20, "high": 26, "n": None, "source": "published"},
            {"service": "marble", "material": "honed marble", "low": 24, "high": 34, "n": None, "source": "published"},
            {"service": "porcelain", "material": "2cm porcelain", "low": 22, "high": 32, "n": None, "source": "published"},
            {"service": "paver-clean-resand-seal", "material": "service", "low": 1, "high": 3, "n": None, "source": "published"},
            {"service": "paver-lift-reset", "material": "service", "low": 8, "high": 15, "n": None, "source": "published"},
        ],
        "localities_tracked": ["sarasota", "fruitville-bee-ridge", "gulf-gate", "siesta-key", "palmer-ranch", "longboat-key", "osprey", "nokomis", "venice", "south-venice", "north-port", "englewood", "port-charlotte", "rotonda-west", "placida"],
        "next_release": "2027-04 (Q1 2027 data)",
    }
    DATA.mkdir(exist_ok=True)
    (DATA / "cost-index.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
    faq = [("What is the Sarasota Concrete Cost Index and how is it calculated?", "A quarterly index of installed price per square foot by service, material and locality, built from the provider's completed jobs in the prior quarter: sample size, median and quartiles, with localities under three jobs suppressed. Version 0.1 is a baseline compiled from published Sarasota-area pricing on September 10, 2026 and is labeled as such; the first data release is planned for April 2027 with first-quarter 2027 jobs."),
           ("Can I cite or reuse it?", "Yes. The index is published under a Creative Commons Attribution 4.0 license as a table on this page and as JSON at /api/cost-index.json. Cite Sarasota Concrete and the release date."),
           ("Why publish this at all?", "Because cost ranges without a method are marketing, and Sarasota has none with one. Realtors, property managers, condo boards and homeowners get a number they can point to; the provider gets held to it.")]
    rows = [[s["service"], s["material"], f'${s["low"]} to ${s["high"]}', "published baseline"] for s in data["series"]]
    body = facts([("Version", "0.1 baseline (published sources)"), ("As of", "September 10, 2026"), ("License", "CC BY 4.0"), ("Next release", "April 2027 (Q1 2027 completed jobs)")])
    body += cap("What is the Sarasota Concrete Cost Index?",
                "A quarterly index of installed price per square foot for concrete and paver work in Sarasota County and the Charlotte County coast, by service, material and locality. Version 0.1, published September 10, 2026, is a baseline compiled from published Sarasota-area pricing. From the first quarter of 2027 each release reports the provider's own completed jobs with sample size, median and quartiles.",
                p("The data is published as a table here and as JSON at /api/cost-index.json under a CC BY 4.0 license. Localities with fewer than three jobs in a quarter are suppressed rather than estimated."))
    body += sec("Baseline v0.1", table(["Service", "Material", "Installed per sq ft", "Source"], rows, "Sarasota Concrete Cost Index v0.1 baseline, September 10, 2026"))
    body += sec("Method for the quarterly releases", ol(["Every completed job in the quarter is logged with service, material, locality, square footage, installed price excluding permit fees, demolition and add-ons priced separately.", "Price per square foot is computed per job.", "For each service-material-locality cell with n ≥ 3, the release reports n, median, 25th and 75th percentiles.", "Cells with n < 3 are reported at county level only.", "Each release states the period, the number of jobs, and limitations (mix of job sizes, island logistics, unusual scopes).", "Releases are dated and never overwritten; prior versions stay available."]))
    body += sec("Limitations", ul(["The baseline is not the provider's data; it's what the local market publishes.", "Quarterly samples from one provider are small; the index describes that provider's work, not the whole market.", "Installed price excludes demolition, permit fees, drains, coping and lighting unless the release says otherwise.", "Island logistics push per-foot prices up; the locality field lets readers separate them."]))
    body += sec("Download", p(link("/api/cost-index.json", "cost-index.json") + " (CC BY 4.0). Cite as: Sarasota Concrete, Sarasota Concrete Cost Index v0.1, September 10, 2026."))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    schema = [dataset_schema("Sarasota Concrete Cost Index", "Quarterly installed cost per square foot for concrete and paver work in Sarasota County, Florida, by service, material and locality. v0.1 baseline from published sources; provider job data from Q1 2027.", "/pricing/sarasota-concrete-cost-index/", "/api/cost-index.json", "2026-09-10", ["concrete cost", "paver cost", "Sarasota", "pool deck cost", "driveway cost"])]
    return pg("/pricing/sarasota-concrete-cost-index/", "Sarasota Concrete Cost Index (Quarterly, CC BY 4.0)", "The Sarasota Concrete Cost Index: installed cost per square foot for concrete and pavers in Sarasota County by service, material and locality, published quarterly with sample size and method. v0.1 baseline September 2026; JSON download.",
              "Sarasota Concrete Cost Index", "Pricing · dataset", "A quarterly, citable index of installed hardscape costs in Sarasota County, with the method published before the first data release.", body, faq, "Cost Index", schema)


def get_pages():
    return [hub(), concrete(), pavers(), pool_decks(), cost_index()]
