# -*- coding: utf-8 -*-
from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, link, ext, facts, cards

SRC = "Planning ranges compiled September 10, 2026 from published Sarasota-area pricing; not quotes."


def pg(slug, title, meta, h1, lede, body, faq):
    return {"route": f"/compare/{slug}/" if slug else "/compare/", "title": title, "meta_description": meta, "h1": h1, "kicker": "Compare", "lede": lede,
            "breadcrumbs": [("Home", "/"), ("Compare", "/compare/"), (h1.split(":")[0][:40], None)] if slug else [("Home", "/"), ("Compare", None)],
            "body_html": body, "faq": faq, "article": True}


def hub():
    body = p("Nine side-by-side decisions, each written for Sarasota's ground, salt and heat rather than for a generic climate. Every comparison states what is documented, what is inference, and what this site will measure itself.")
    body += cards([("/compare/pool-deck-surfaces-heat/", "Pool deck surfaces and heat", "What color, mass and texture do at 2 p.m., and the slip rating to ask for."),
                   ("/compare/travertine-vs-concrete-pavers/", "Travertine vs concrete pavers", "Cost, heat, salt, repair and resale."),
                   ("/compare/travertine-vs-shellstone-vs-porcelain/", "Travertine vs shellstone vs porcelain", "The three coolest deck options compared."),
                   ("/compare/concrete-vs-pavers-driveway/", "Concrete vs paver driveway", "Twenty-year cost, flood zones, repairability."),
                   ("/compare/resurface-vs-replace-pool-deck/", "Resurface vs replace a pool deck", "Six tests and the price gap."),
                   ("/compare/cool-deck-vs-pavers/", "Cool deck vs pavers", "Lifespan, heat and what a 1990s overlay is doing now."),
                   ("/compare/4-inch-vs-6-inch/", "4-inch vs 6-inch concrete", "Loads, cost and PSI."),
                   ("/compare/rebar-vs-fiber/", "Rebar vs wire mesh vs fiber", "What each does on Myakka sand."),
                   ("/compare/sealer-types-coastal/", "Sealer types near the coast", "Penetrating, film and hybrid sealers and why film blushes.")])
    body += reviewed("September 10, 2026")
    return pg("", "Compare: Pool Deck Surfaces, Pavers, Concrete & Sealers", "Nine comparisons for Sarasota homeowners: pool deck surfaces and heat, travertine vs pavers vs porcelain, concrete vs paver driveways, resurface vs replace, cool deck, thickness, reinforcement and sealers.",
              "Comparisons written for Sarasota's ground, salt and heat", "Nine decisions, each with what's documented, what's inferred and what will be measured.", body, [])


def heat():
    faq = [("What slip rating (DCOF) should a pool deck surface have?", "A wet dynamic coefficient of friction of 0.42 or higher under ANSI A326.3 for level surfaces that get wet; textured concrete, tumbled or honed stone and R11 porcelain meet it, polished stone and glossy film sealers don't. Ask the supplier for the tested value of the exact product and finish."),
           ("Is a light-colored concrete deck as cool as travertine?", "Not as cool, in most published comparisons, but far closer than a gray or charcoal deck. Color drives most of the difference; mass and porosity do the rest. The study will put local numbers on it."),
           ("Does a sealer make a deck hotter?", "A glossy film sealer darkens the surface and can raise its temperature; a penetrating sealer doesn't change color or heat.")]
    body = facts([("Biggest factor", "Color (solar reflectance)"), ("Second", "Porosity and thermal mass"), ("Slip standard", "ANSI A326.3, wet DCOF ≥ 0.42"), ("Local data", "Pending: Sarasota Pool Deck Surface Temperature Study")])
    body += cap("Which pool deck surface stays coolest, and why?",
                "Light color first, then porosity and mass. A surface that reflects more sunlight absorbs less heat; a porous stone like travertine or shellstone sheds heat and holds a little moisture; a dense dark slab stores heat all afternoon. Published Florida comparisons claim 20 to 35 degree differences between light stone and dark concrete, but none was measured in Sarasota, so this site publishes its own study before quoting a number.",
                p(f'The {link("/coastal/pool-deck-surface-temperature-study/", "study")} reads nine surfaces at 10 a.m., 2 p.m. and 5 p.m. on a July and a January day with an infrared thermometer. Until those numbers exist, the ranking below is by physics and published claims, labeled as such.'))
    body += sec("Ranking by the physics", table(["Surface", "Color", "Porosity / mass", "Expected barefoot heat", "Wet slip", "Notes"], [
        ["Shellstone (light)", "Very light", "Porous", "Coolest tier", "Very good", "Limestone chemistry; seal near salt"],
        ["Tumbled travertine (light)", "Light", "Porous", "Coolest tier", "Good", "Same chemistry; annual coping seal on salt pools"],
        ["Honed marble (white/cream)", "Light", "Dense", "Cool", "Good if honed", "Etches from acid"],
        ["Light concrete pavers", "Light", "Dense", "Moderate", "Good", "Wide range of blends; pick the lightest"],
        ["Cool-deck overlay (light)", "Light", "Porous, thin", "Moderate", "Good", "Short life; absorbs water"],
        ["Light broom concrete", "Medium-light", "Dense", "Moderate to warm", "Good", "Better than gray, not stone"],
        ["2 cm porcelain (light)", "Light", "Dense, thin", "Moderate", "Excellent (R11)", "Thin tile heats and cools fast"],
        ["Gray broom concrete", "Medium", "Dense", "Warm", "Good", "The default that gets replaced"],
        ["Charcoal pavers / dark stamped", "Dark", "Dense", "Hottest tier", "Varies", "Avoid on sun-exposed decks"]], "Expected order pending measurement; published Florida claims of 20 to 35 °F between light stone and dark concrete are unverified locally"))
    body += sec("Slip, wet", p("The number to ask for is the wet dynamic coefficient of friction under ANSI A326.3; 0.42 or higher is the threshold for level interior surfaces expected to be wet and the working target for pool decks. Textured concrete (broom, knockdown), tumbled or honed natural stone and R11 porcelain meet it; polished stone, smooth trowel and glossy film sealers don't. A sealer with a grit additive keeps a stamped or overlay deck on the right side of the line."))
    body += sec("What to do with this today", ul(["Choose the lightest color your community allows.", "On sun-exposed decks, prefer porous light stone or light pavers over dense dark surfaces.", "Specify a matte penetrating sealer, never a glossy film, around water.", "Ask for the tested wet DCOF of the exact product.", "Plan shade: the coolest deck at 2 p.m. is the one under a cage or a tree."]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("pool-deck-surfaces-heat", "Coolest Pool Deck Surface in Florida: What Drives Heat & Slip", "Why light, porous pool deck surfaces stay cooler in Sarasota (color, porosity, mass), the expected ranking of nine surfaces pending local measurement, and the wet slip rating (DCOF 0.42, ANSI A326.3) to demand.",
              "Pool deck surfaces and heat: what drives the 2 p.m. temperature, and the slip rating to demand", "Color first, porosity second, mass third. Here is the expected order, labeled as expected, until the local study replaces it with measurements.", body, faq)


def trav_vs_pavers():
    faq = [("Is travertine worth the extra cost over concrete pavers?", "On a sun-exposed deck used barefoot, yes for most owners: it's cooler, reads as stone and lasts as long as the house. On a shaded lanai or a salt pool where the owner won't keep up annual coping sealing, dense concrete pavers or porcelain are the better value."),
           ("Which is easier to repair?", "Both lift and reset. Concrete pavers are easier to match years later because manufacturers keep blends; travertine lots vary, so order 5 to 10 percent extra and store it."),
           ("Which handles salt better?", "Sealed concrete pavers. Travertine is calcium carbonate and flakes at the waterline of a salt pool unless sealed annually and rinsed.")]
    body = facts([("Concrete pavers", "$13 to $16 per sq ft installed"), ("Travertine", "$20 to $26 per sq ft installed"), ("Cooler", "Travertine (light, porous)"), ("Salt tolerance", "Concrete pavers, sealed")])
    body += cap("Travertine or concrete pavers for a Sarasota pool deck?",
                "Travertine costs about $20 to $26 per square foot installed against $13 to $16 for concrete pavers (planning ranges, September 10, 2026), stays cooler barefoot because it's light and porous, and grips well wet in a tumbled or honed finish. Concrete pavers cost less, come in vehicular thicknesses for driveways, match years later, and handle a salt-chlorinated pool with a routine sealer instead of an annual coping schedule.",
                p(SRC))
    body += sec("Side by side", table(["", "Travertine", "Concrete pavers"], [["Installed cost", "$20 to $26 per sq ft", "$13 to $16 per sq ft (deck); $14 to $22 (driveway)"], ["Barefoot heat", "Cooler (light, porous)", "Moderate; pick a light blend"], ["Wet slip", "Good, tumbled or honed", "Good, textured face"], ["Salt pool", "Seal coping annually; rinse", "Seal every 18 to 36 months"], ["Freeze", "Not a factor here", "Not a factor here"], ["Repair", "Lift and reset; keep spares", "Lift and reset; blends stay available"], ["Driveway use", "2 in. thick pieces, higher cost", "Vehicular units, herringbone"], ["Look", "Natural stone, varies by lot", "Uniform; many blends"], ["Life", "30+ years", "25 to 30 years"], ["Resale", "Reads as premium on the keys", "Neutral"]], "Travertine vs concrete pavers, Sarasota"))
    body += sec("The decision in three questions", ol(["Is the deck in full sun and used barefoot? Travertine's heat advantage matters; in shade it doesn't.", "Is the pool salt-chlorinated, and will you seal the coping every year? If not, concrete pavers or porcelain.", "Is this also a driveway? Concrete pavers, unless the budget allows 2-inch travertine and the look is worth it."]))
    body += sec("Related", cards([("/pavers/travertine-shellstone/", "Travertine and shellstone", "Finishes, formats, salt."), ("/pavers/pool-decks/", "Paver pool decks", "Spec and price."), ("/compare/travertine-vs-shellstone-vs-porcelain/", "Travertine vs shellstone vs porcelain", "The other stone comparison.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("travertine-vs-concrete-pavers", "Travertine vs Concrete Pavers for a Sarasota Pool Deck", "Travertine ($20 to $26) vs concrete pavers ($13 to $16 per sq ft) for Sarasota pool decks: heat, wet slip, salt-pool maintenance, repair, driveway use, look and resale, with three questions that settle it.",
              "Travertine vs concrete pavers: cost, heat, salt and repair", "The stone is cooler and reads as premium; the concrete paver is cheaper, tougher around salt and easier to match later.", body, faq)


def trav_shell_porc():
    faq = [("Is light travertine cooler than white porcelain?", "By the physics and by published Florida claims, yes: travertine is porous and thick, porcelain is dense and 2 cm thin, so porcelain heats faster in sun and cools faster in shade. The local study will measure the difference; expect it to be smaller than the gap between either and gray concrete."),
           ("Is shellstone a good pool deck around a salt pool?", "It's the same calcium carbonate chemistry as travertine, so yes with the same discipline: seal the coping annually, rinse the field, never use acid cleaners. Its open texture grips very well wet."),
           ("Which needs the least maintenance?", "Porcelain: no sealing, no etching, no efflorescence. Its one demand is a base flat to 1/8 inch.")]
    body = facts([("Travertine", "$20 to $26 per sq ft"), ("Shellstone", "$20 to $26 per sq ft"), ("Porcelain 2 cm", "$22 to $32 per sq ft"), ("Salt-proof", "Porcelain")])
    body += cap("Travertine, shellstone or porcelain for a Sarasota pool deck?",
                "All three are light and cooler than gray concrete. Travertine and shellstone are porous limestone: coolest by the physics, excellent wet grip, and a chemistry that needs sealing and rinsing near salt. Porcelain is dense, colorfast and immune to salt and acid, needs no sealing, grips with an R11 face, and demands a base flat to 1/8 inch. Installed planning ranges on September 10, 2026: $20 to $26 for the stones, $22 to $32 for porcelain.",
                p(SRC))
    body += sec("Side by side", table(["", "Travertine", "Shellstone", "Porcelain 2 cm"], [["Chemistry", "Calcium carbonate", "Calcium carbonate with shell", "Fired ceramic"], ["Barefoot heat", "Coolest tier", "Coolest tier", "Moderate"], ["Wet slip", "Good (tumbled/honed)", "Very good", "Excellent (R11)"], ["Salt pool", "Seal annually, rinse", "Seal annually, rinse", "Immune"], ["Acid / cleaners", "Etches", "Etches", "Immune"], ["Efflorescence", "Possible", "Possible", "None"], ["Base tolerance", "Forgiving", "Forgiving", "1/8 in. or it rocks"], ["Look", "Warm, varied", "Coastal, fossil shell", "Uniform, modern or stone-look"], ["Maintenance", "Seal 18 to 36 mo; grout holes", "Same; scrub open texture", "Clean"], ["Cost installed", "$20 to $26", "$20 to $26", "$22 to $32"]], "Three light deck surfaces, Sarasota"))
    body += sec("Pick by the pool and the owner", ul(["Salt pool, owner away half the year: porcelain.", "Chlorine pool, full sun, owner who'll seal on schedule: travertine or shellstone.", "Coastal look with shell: shellstone, with the scrub-not-blast cleaning routine.", "Modern lanai that continues an interior floor: porcelain or honed marble."]))
    body += sec("Related", cards([("/pavers/travertine-shellstone/", "Travertine and shellstone", "Finishes and formats."), ("/pavers/marble-porcelain/", "Marble and porcelain", "Base tolerance and setting."), ("/tools/coastal-surface-selector/", "Coastal surface selector", "Your inputs, a recommendation.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("travertine-vs-shellstone-vs-porcelain", "Travertine vs Shellstone vs Porcelain Pool Decks in Florida", "Travertine, shellstone and 2 cm porcelain for Sarasota pool decks compared on heat, wet slip, salt-pool chemistry, acid, efflorescence, base tolerance, look, maintenance and installed cost, with a pick by pool type and owner.",
              "Travertine vs shellstone vs porcelain: the three light options for a hot deck", "Two porous limestones that stay coolest and need sealing near salt, and a fired tile that shrugs off salt and demands a perfect base.", body, faq)


def concrete_vs_pavers():
    faq = [("Should I choose pavers or poured concrete in a VE zone?", "Pavers on a rebuildable base with concrete curbs, unless an engineer specifies a slab under an elevated home. Surge that lifts a slab destroys it; surge that shifts pavers leaves reusable units."),
           ("Which is cheaper over 20 years?", "Close, when both are built right. Concrete at $7 to $12 per square foot needs little for 30 years; pavers at $14 to $22 need re-sanding and sealing every 2 to 3 years but repair for hundreds instead of thousands. Flood exposure and the owner's willingness to maintain decide it."),
           ("Which looks better to buyers on the keys?", "Pavers, by the market's behavior: most waterfront listings show paver driveways. Inland the difference is smaller.")]
    body = facts([("Concrete", "$7 to $12 per sq ft; 30 yrs; little maintenance"), ("Pavers", "$14 to $22 per sq ft; 25 to 30 yrs; seal every 2 to 3 yrs"), ("Flood zone", "Pavers win"), ("Repair", "Pavers win")])
    body += cap("Concrete or pavers for a Sarasota driveway?",
                "Concrete costs about $7 to $12 per square foot installed and pavers $14 to $22 (planning ranges, September 10, 2026). Concrete on a compacted base with same-day joints lasts 30 years with little spending; pavers need re-sanding and sealing every 2 to 3 years but a settled section is lifted and reset for hundreds of dollars. On the keys and in any VE zone, pavers' rebuildability decides it.",
                p(SRC))
    body += sec("Side by side", table(["", "Concrete driveway", "Paver driveway"], [["Installed cost (600 sq ft)", "$5,500 to $9,500", "$8,500 to $13,000"], ["Base", "4 in. compacted", "6 in. compacted in lifts"], ["Time on site", "3 to 6 days + 7-day cure", "4 to 7 days, drive on when sand cures"], ["Cracks", "Controlled at joints; visible if not", "None; settlement instead"], ["Repair", "Patch shows; panel replacement", "Lift and reset, invisible"], ["Maintenance", "Seal on coastal lots; keep joints sealed", "Re-sand, seal every 2 to 3 yrs (18 to 24 mo coastal)"], ["Flood / surge", "Slab can lift and crack", "Units reusable; base rebuilt"], ["Salt", "Scaling if finished wet", "Sealer wears faster"], ["Impervious cover", "Counts", "Counts, unless permeable system"], ["HOA color rules", "Rarely an issue", "Approved color lists"], ["20-year cost (inland)", "Lower", "Higher by the maintenance"], ["20-year cost (keys)", "Risk of one replacement", "Repairs instead of replacement"]], "Concrete vs paver driveway, Sarasota County"))
    body += sec("Related", cards([("/concrete/driveways/", "Concrete driveways", "Spec and prices."), ("/pavers/driveways/", "Paver driveways", "Base and pattern."), ("/guides/permeable-pavers-impervious-limit/", "Permeable pavers", "When the 50% cap forces the choice.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("concrete-vs-pavers-driveway", "Concrete vs Paver Driveway in Sarasota: 20-Year Cost & Floods", "Concrete ($7 to $12) vs paver ($14 to $22 per sq ft) driveways for Sarasota County compared on base, time, cracks, repair, maintenance, surge, salt, impervious cover, HOA rules and 20-year cost inland and on the keys.",
              "Concrete vs paver driveway: the 20-year answer for Sarasota County", "Cheaper and quieter to own inland; more expensive and far easier to repair where the water comes up.", body, faq)


def resurface():
    faq = [("When is pool deck resurfacing cheaper than replacement in Sarasota and when is it money wasted?", "Cheaper whenever the slab passes six tests: solid sound, no offset cracks, drains away from the house, no rust bleed, room under the threshold, no stacked prior overlays. Wasted whenever it fails one, because the overlay follows the slab down within a couple of summers and you pay for both."),
           ("How much cheaper?", "A basic overlay at $4 to $8 per square foot against a new deck at $9 to $14 or pavers at $13 to $16 (September 10, 2026 planning ranges): $3,000 to $5,500 versus $7,000 to $11,000 on a 700-square-foot deck."),
           ("How long does an overlay last?", "Eight to fifteen years with resealing every 2 to 3 years; a new deck lasts 30.")]
    body = facts([("Overlay", "$4 to $15 per sq ft; 8 to 15 yrs"), ("New concrete", "$9 to $14; 30 yrs"), ("Pavers", "$13 to $16; 25 to 30 yrs"), ("Deciding factor", "Whether the slab passes six tests")])
    body += cap("Resurface or replace a Sarasota pool deck?",
                "Resurface when the slab rings solid with a hammer, has only hairline cracks with no offset, drains away from the house and pool, shows no rust bleeding, leaves room under the door threshold, and hasn't already been overlaid twice. Replace when it fails any one of those. Planning ranges on September 10, 2026: overlay $4 to $15 per square foot, new concrete $9 to $14, pavers $13 to $16.",
                p(SRC))
    body += sec("The six tests", table(["Test", "How", "Pass", "Fail"], [["Sound", "Tap with a hammer across the deck", "Solid ring everywhere", "Hollow patches"], ["Cracks", "Straightedge across each crack", "No step, hairline", "Offset or wide"], ["Slope", "Level and hose", "Water leaves", "Ponds or runs to the house"], ["Steel", "Look for orange bleed", "None", "Rust staining"], ["Threshold", "Measure slab to door", "Overlay stays 1 in. below", "Already tight"], ["History", "Ask, look at the edge", "Original or one overlay", "Two or more overlays"]], "Resurface-or-replace tests"))
    body += sec("What each path costs on a 700-square-foot deck", table(["Path", "Range", "Life", "Notes"], [["Basic textured overlay", "$3,000 to $5,500", "8 to 15 yrs", "Slab must pass"], ["Decorative overlay", "$7,000 to $10,500", "8 to 15 yrs", "Stone patterns"], ["New textured concrete", "$7,000 to $10,000 + demolition", "30 yrs", "Drains, cage anchors extra"], ["Concrete pavers", "$9,000 to $11,000 + demolition", "25 to 30 yrs", "Rebuildable"], ["Travertine", "$14,000 to $18,000 + demolition", "30+ yrs", "Seal near salt"]], "Planning ranges, September 10, 2026"))
    body += sec("Related", cards([("/concrete/resurfacing/", "Resurfacing and overlays", "Finishes and process."), ("/concrete/pool-decks/", "New concrete pool decks", "Spec."), ("/compare/cool-deck-vs-pavers/", "Cool deck vs pavers", "The 1990s overlay question.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("resurface-vs-replace-pool-deck", "Resurface or Replace a Pool Deck in Sarasota? Six Tests", "Six on-site tests that decide whether a Sarasota pool deck can be resurfaced or must be replaced, with the cost gap on a 700-square-foot deck: overlay $3,000 to $5,500 vs new concrete or pavers $7,000 to $11,000 (September 2026 ranges).",
              "Resurface or replace: six tests before anyone quotes an overlay", "An overlay on a sound slab is the cheapest deck you can buy; an overlay on a failed slab is the most expensive.", body, faq)


def cool_deck():
    faq = [("Does cool deck really stay cool and how long does it last?", "It stays cooler than bare gray concrete because it's light-colored and porous, and the same porosity absorbs water and shortens its life to roughly 5 to 8 years before it needs recoating, in published Florida experience. Most 1990s cool-deck surfaces in Sarasota are past that."),
           ("Can cool deck be repaired?", "Patched and recoated, yes, if the slab underneath passes the six tests; the patches show. Recoating runs $3 to $5 per square foot for basic work."),
           ("Is a paver overlay possible over cool deck?", "If the slab is sound and the threshold allows the height, a sand-set or thin-set paver overlay goes over it; the cool deck is just a surface at that point.")]
    body = facts([("Cool deck", "$4 to $8 per sq ft new; 5 to 8 yrs"), ("Pavers", "$13 to $16; 25 to 30 yrs"), ("Heat", "Both light; pavers by mass, cool deck by porosity"), ("Repair", "Pavers invisible; cool deck patches show")])
    body += cap("Cool deck or pavers for a Sarasota pool deck?",
                "Cool deck (the generic name for a light, textured cementitious overlay) costs $4 to $8 per square foot and lasts about 5 to 8 years before recoating, because the porosity that keeps it cool also lets water in. Pavers cost $13 to $16, last 25 to 30 years, and repair invisibly. On an existing sound slab with a small budget, cool deck; for the next decade and beyond, pavers.",
                p(SRC))
    body += sec("Side by side", table(["", "Cool deck overlay", "Pavers"], [["Cost (700 sq ft)", "$3,000 to $5,500", "$9,000 to $11,000"], ["Requires", "Sound slab (six tests)", "Any base, rebuilt"], ["Life", "5 to 8 yrs to recoat; 8 to 15 for better overlays", "25 to 30 yrs"], ["Heat", "Cooler than gray concrete", "Cooler than gray concrete; light blends"], ["Water", "Absorbs; blushes under film sealers", "Drains through joints"], ["Repair", "Patch and recoat, visible", "Lift and reset, invisible"], ["Salt pool", "Recoat more often", "Seal every 18 to 36 mo"], ["Surge", "Overlay and slab fail together", "Units reusable"], ["Maintenance", "Reseal 2 to 3 yrs", "Re-sand, seal"]], "Cool deck vs pavers, Sarasota"))
    body += sec("Related", cards([("/concrete/resurfacing/", "Resurfacing and overlays", "What a modern overlay is."), ("/pavers/pool-decks/", "Paver pool decks", "Spec."), ("/compare/resurface-vs-replace-pool-deck/", "Resurface or replace", "The tests.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("cool-deck-vs-pavers", "Cool Deck vs Pavers for Florida Pool Decks: Life, Heat, Cost", "Cool deck overlays ($4 to $8 per sq ft, 5 to 8 years) vs pavers ($13 to $16, 25 to 30 years) for Sarasota pool decks: heat, water absorption, repair, salt pools, surge and maintenance.",
              "Cool deck vs pavers: a cheap decade or a long one", "The overlay is the cheapest cool surface on a sound slab and the shortest-lived; pavers cost three times as much and outlast two of them.", body, faq)


def thickness():
    faq = [("Should a Sarasota driveway be 4 inches or 6 inches thick?", "Four inches for cars and SUVs on a compacted base, which is the Florida Building Code, Residential floor. Six inches for RVs, boat trailers, delivery trucks, dumpster pads and aprons where a city detail requires it. The base matters more than the extra inches on Myakka sand."),
           ("Should a driveway mix in Sarasota County be 3,000 or 4,000 PSI?", "Four thousand, with a water-cement ratio at or below 0.45. Three thousand is code minimum; the extra cement costs a few dollars per yard, finishes better in heat and resists salt scaling longer."),
           ("How much more does 6 inches cost?", "About $1.50 to $2.50 per square foot for the concrete and heavier steel: $900 to $1,500 on a 600-square-foot driveway.")]
    body = facts([("4 in.", "Cars, SUVs, patios, pool decks, walks"), ("6 in.", "RV, boat trailer, dumpster, heavy pads, some aprons"), ("Mix", "4,000 PSI, w/c ≤ 0.45"), ("Base", "4 in. compacted; 6 in. where the water table is high")])
    body += cap("Four inches or six, and 3,000 or 4,000 PSI?",
                "Four inches on 4 inches of compacted base carries residential vehicles and is the Florida Building Code floor; 6 inches with #4 rebar carries RVs, boat trailers and trucks, and some right-of-way aprons (Venice's detail, for example) call for it. A 4,000 PSI mix with a low water-cement ratio is the working standard here for heat finishing and salt resistance; 3,000 is the minimum, not the target.",
                p(SRC + " The extra 2 inches cost about $1.50 to $2.50 per square foot."))
    body += sec("By use", table(["Use", "Thickness", "Reinforcement", "Base"], [["Cars and SUVs", "4 in.", "Fiber + #3 bar", "4 in. compacted"], ["Patio, lanai, pool deck", "4 in.", "Fiber; #3 at cage line", "4 in."], ["Walkway", "4 in.", "Fiber", "4 in."], ["Boat trailer / RV pad", "6 in.", "#4 at 18 in.", "6 in."], ["Hot tub", "6 in.", "#4 at 12 in.", "4 to 6 in."], ["Dumpster / equipment", "6 in.", "#4 at 12 in.", "6 in."], ["Apron in some city rights-of-way", "6 in.", "Per detail", "Per detail"]], "Thickness by use, Sarasota Concrete practice, referencing FBC-R Chapter 19 and ACI 332"))
    body += sec("Why the base outranks the inches", p("Concrete is strong in compression and weak in bending; it bends when the ground under it moves. On Myakka fine sand with a wet-season water table under 10 inches, an uncompacted base loses fines and creates voids, and a 6-inch slab over a void cracks just like a 4-inch one, a little later. Four inches of compacted limerock in two lifts over a proof-rolled subgrade does more for a driveway than 2 more inches of concrete."))
    body += sec("Related", cards([("/compare/rebar-vs-fiber/", "Rebar vs fiber", "What holds the crack shut."), ("/concrete/driveways/", "Concrete driveways", "Spec."), ("/concrete/slabs/", "Slabs and pads", "Thickness by load.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("4-inch-vs-6-inch", "4-Inch vs 6-Inch Concrete Driveway & 3,000 vs 4,000 PSI", "When a Sarasota driveway or pad needs 4 or 6 inches of concrete, why 4,000 PSI with a low water-cement ratio is the working mix, what the extra inches cost, and why a compacted base outranks thickness on Myakka sand.",
              "Four inches or six, 3,000 or 4,000 PSI: the thickness question for Sarasota", "Four for cars, six for trailers and trucks, 4,000 PSI for heat and salt, and a compacted base before any of it.", body, faq)


def rebar():
    faq = [("Rebar, wire mesh or fiber: what actually works on Myakka fine sand?", "Fiber for the first-hours shrinkage cracks, steel for holding cracks tight after the slab has moved. Vehicle slabs get #3 rebar on chairs at mid-depth; walks and patios do well with fiber and joints. Wire mesh laid on the ground and \"pulled up\" during the pour ends up at the bottom and does nothing."),
           ("Does fiber replace rebar?", "No. Fiber reduces plastic shrinkage cracking; it doesn't distribute load or hold a structural crack shut."),
           ("What size rebar?", "#3 (3/8 inch) on an 18 to 24 inch grid for driveways; #4 (1/2 inch) on 12 to 18 inches for heavy pads.")]
    body = facts([("Fiber", "Plastic shrinkage control, first hours"), ("Wire mesh", "Only if held at mid-depth"), ["Rebar", "Crack width control under load"], ("Sarasota default", "Fiber + #3 bar on chairs for vehicles")])
    body += cap("Rebar, wire mesh or fiber for a Sarasota slab?",
                "Fiber controls the plastic shrinkage cracks that form in the first hours of a hot Sarasota afternoon; steel controls how wide a crack opens after the slab has moved on a soft base. Vehicle slabs get fiber plus #3 rebar on chairs at mid-depth; walks and patios usually get fiber and same-day joints. Wire mesh works only when supported at mid-depth, which on most jobs it isn't.",
                p("Cost: fiber adds roughly $0.10 to $0.20 per square foot, #3 rebar on chairs $0.60 to $1.20, mesh in between. Reinforcement doesn't prevent cracks; joints and base do that. Reinforcement keeps the cracks that happen anyway from becoming steps."))
    body += sec("Side by side", table(["", "Fiber", "Wire mesh", "Rebar"], [["What it does", "Reduces early shrinkage cracks", "Holds cracks tight if at mid-depth", "Holds cracks tight; distributes load"], ["Placement risk", "None", "Sinks to the bottom when walked on", "Needs chairs; easy to inspect"], ["Cost per sq ft", "$0.10 to $0.20", "$0.30 to $0.60", "$0.60 to $1.20"], ["Salt", "No corrosion", "Corrodes if shallow", "Needs 2 in. cover near salt"], ["Use here", "Everything", "Rarely", "Driveways, pads, cage lines"]], "Reinforcement compared"))
    body += sec("Related", cards([("/compare/4-inch-vs-6-inch/", "Thickness", "Inches by use."), ("/guides/why-concrete-cracks-sarasota/", "Why concrete cracks here", "Shrinkage, base and joints."), ("/concrete/driveways/", "Concrete driveways", "Spec.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("rebar-vs-fiber", "Rebar vs Wire Mesh vs Fiber for Florida Concrete Slabs", "What fiber, wire mesh and rebar each do in a Sarasota slab on Myakka fine sand, what they cost per square foot, why mesh on the ground fails, the salt-cover rule and the reinforcement used for driveways, pads and walks.",
              "Rebar vs wire mesh vs fiber: what each one does on Sarasota sand", "Fiber for the first hours, steel for the years after, and joints and base for the cracks themselves.", body, faq)


def sealers():
    faq = [("Wet-look or penetrating sealer: which is better near the coast?", "Penetrating, in nearly every coastal case. It doesn't change the look, doesn't blush white over a damp base, doesn't make a deck slippery and wears invisibly. Wet-look film sealers darken and gloss the surface and are the source of most peeling, blushing and slip complaints on Sarasota pool decks."),
           ("How long do they last here?", "Penetrating sealers 18 to 24 months within a mile of open water and 2 to 3 years inland; film sealers similar or shorter, with a failure mode you can see."),
           ("Can a film sealer be stripped?", "Yes, with a solvent stripper and pressure, at a cost close to a new sealing job. Hybrids and polyurethanes are harder to strip.")]
    body = facts([("Coastal default", "Breathable penetrating (silane/siloxane)"), ("Film sealers", "Matte with grit only where drainage is perfect"), ("Never around water", "Glossy wet-look"), ("Cycle", "18 to 24 mo coastal; 2 to 3 yrs inland")])
    body += cap("Which sealer for pavers and concrete near the Gulf?",
                "A breathable penetrating sealer (silane or siloxane based) for anything within a mile of open water, around a pool, or on natural stone: it repels water and salt without forming a film, can't blush white or peel, and doesn't change slip. Film sealers, matte and with a grit additive, only on well-drained driveways and patios where the look is wanted. Glossy wet-look sealers never around water.",
                p("Coastal reseal cycle: 18 to 24 months; inland 2 to 3 years; travertine coping on a salt pool annually."))
    body += sec("Side by side", table(["Type", "Look", "Breathes", "Slip", "Failure mode", "Best for"], [["Penetrating silane/siloxane", "Natural", "Yes", "Unchanged", "Wears invisibly", "Stone, pool decks, coastal lots"], ["Water-based acrylic (matte)", "Slight enhancement", "Partly", "Slight; add grit", "Blushes over damp base", "Inland driveways, patios"], ["Solvent acrylic (wet look)", "Dark, glossy", "No", "Slippery wet", "Peels, whitens, traps moisture", "Shaded, dry, decorative"], ["Polyurethane / hybrid", "Satin", "No", "Add grit", "Hard to strip", "High-traffic driveways"]], "Sealers for the Sarasota coast"))
    body += sec("Related", cards([("/pavers/sealing/", "Sealing and cleaning", "The service and the cycle."), ("/coastal/maintenance-calendar/", "Maintenance calendar", "Dates by distance from the water."), ("/guides/efflorescence/", "Efflorescence", "Why sealing too early traps it.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("sealer-types-coastal", "Paver & Concrete Sealers Near the Coast: Penetrating vs Film", "Penetrating vs film vs hybrid sealers for pavers, concrete and stone near the Sarasota coast: look, breathability, slip, failure modes, the coastal reseal cycle and why wet-look sealers fail around pools.",
              "Sealers near the coast: penetrating, film or hybrid", "The one that doesn't change the look is the one that doesn't fail.", body, faq)


def get_pages():
    return [hub(), heat(), trav_vs_pavers(), trav_shell_porc(), concrete_vs_pavers(), resurface(), cool_deck(), thickness(), rebar(), sealers()]
