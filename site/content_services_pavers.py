# -*- coding: utf-8 -*-
"""Paver and hardscape service pages."""
from _data import SERVICES, CITIES, CITY_SERVICE
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
            "breadcrumbs": [("Home", "/"), ("Pavers", "/pavers/"), (s["name"], None)], "body_html": body, "faq": faq, "schema": [service_schema(key, s["route"])]}


# ---------------------------------------------------------------- POOL DECKS
def pool_decks():
    key = "pavers-pool-decks"
    faq = [
        ("Sand-set or mortar-set around a pool?", "Sand-set on a compacted base for most residential decks, because it drains, flexes and can be lifted. Mortar-set over a slab for coping and for elevated decks on the islands where an engineered slab already exists. Never a thin bed over sand."),
        ("Do paver pool decks need a deck drain?", "Less than concrete does, because water passes the joints, but a lanai under a cage still traps water and a linear drain at the low side keeps the base from staying saturated. On a salt pool, the drain also carries the rinse water away."),
        ("How are pavers finished at the pool edge?", "With coping: bullnose or square-edge pieces in the same material or a contrasting one, mortar-set on the pool beam, with a flexible joint between the coping and the field so the shell and the deck move separately."),
        ("Can a condo pool deck be done in phases?", "Yes, and it should be. Half the deck stays open while the other half is rebuilt, with a temporary edge restraint at the phase line. Boards usually schedule it for May through September when occupancy is lowest."),
        ("What is the best paver for a salt pool?", "Porcelain or a dense concrete paver, sealed. Travertine and shellstone work beautifully but need rinsing and annual sealing at the coping; the comparison page has the trade-offs."),
        ("How long does a paver pool deck take?", "Five to eight working days for a typical 600 to 800 square feet: demolition, base, drains, coping, field, compaction, joint sand, and a 30-day wait before sealing."),
    ]
    body = facts([("Typical size", "500 to 1,000 sq ft"), ("Materials", "Concrete pavers, travertine, shellstone, marble, porcelain"), ("Time on site", "5 to 8 working days"), ("Planning range", "$13 to $16 concrete pavers; $20 to $26 travertine")])
    body += cap("What does a paver pool deck cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts installed concrete pavers at roughly $13 to $16 per square foot and travertine at $20 to $26, with marble and large-format porcelain higher. A 700-square-foot deck therefore lands near $9,000 to $11,000 in concrete pavers and $14,000 to $18,000 in travertine, before demolition, coping and drains.",
                '<p class="src-note">' + SRC + '</p>' + p(f' The {link("/pricing/pool-decks/", "pool deck cost guide")} has size bands and the concrete alternative.'))
    body += cap("How long does a paver pool deck take?",
                "Five to eight working days on site. Demolition and haul-off, subgrade and base compaction in lifts, deck drain, coping set on the beam, field laid in the pattern, compaction, polymeric sand, and a dry day for the sand to cure. Sealing waits 30 days so any efflorescence works out first. Permit or board approval comes before day one.")
    body += sec("Scope", ul(["Full deck replacement inside a screen cage, with cage anchors reset into new concrete curbs or edge beams.", "Paver overlay on a sound existing deck where the height under the door allows it.", "Coping replacement in travertine, marble, porcelain or precast concrete.", "Condo and HOA common-area decks, phased to keep the pool open.", "Deck extensions beyond the cage for a fire pit or a sun shelf."]))
    body += sec("Price factors", table(["Factor", "Effect"], [["Material", "Concrete pavers lowest; travertine +$7 to $10 per sq ft; marble and porcelain higher"], ["Coping", "$25 to $60 per linear foot depending on material"], ["Demolition", "+$2 to $4 per sq ft; more for pavers over concrete"], ["Deck drain", "$300 to $900 per run"], ["Cage anchors", "New curb or edge beam along the cage line, $20 to $40 per linear foot"], ["Barrier island logistics", "+5 to 15%"], ["Sealing at 30 days", "$1 to $3 per sq ft"]], "Paver pool deck price factors, Sarasota County, 2026 (planning ranges)"))
    body += sec("The base spec around a Sarasota pool", p("Compacted subgrade pitched away from the pool and the house, geotextile where the sand pumps, 4 inches of crushed limerock compacted in two lifts, 1 inch of screeded concrete sand, and the pavers. The edge is a concrete curb or edge beam wherever the cage anchors land or a surge could reach, and spiked plastic restraint only on the protected inside edges. The coping is mortar-set on the pool beam with a flexible joint to the field.") +
                p("Around a salt-chlorinated pool the field is rinsed with fresh water weekly and the coping is sealed annually with a breathable penetrating sealer. Limestone-family stones (travertine, shellstone) flake at the waterline when that's skipped; dense concrete pavers and porcelain don't."))
    body += sec("Materials compared for a pool deck", table(["Material", "Barefoot heat", "Wet slip", "Salt pool", "Repair"], [
        ["Light concrete pavers", "Moderate", "Good", "Fine when sealed", "Lift and reset any unit"],
        ["Tumbled travertine", "Cool", "Good", "Seal and rinse; annual coping", "Replace pieces; refill holes"],
        ["Shellstone", "Cool", "Very good", "Same as travertine", "Replace pieces"],
        ["Honed marble", "Cool", "Good if honed", "Etches with acid", "Replace pieces"],
        ["2 cm porcelain", "Moderate", "Excellent (R11)", "Immune", "Replace tiles; base must be perfect"]],
        "Heat column to be replaced by measured values from the temperature study"))
    body += sec("Permits, flood zones and turtle lighting", p(f'Replacing a deck on the same footprint is reviewed differently by each office; the {link("/permits/", "permit hub")} has them. On the keys, a paver deck is a site improvement outside the NFIP 50 percent calculation, but a deck seaward of the Gulf Beach Setback Line needs a coastal setback variance and any deck light must meet the {link("/permits/sea-turtle-lighting/", "May 1 to October 31 lighting rules")}. Elevated homes in VE zones may need an engineered slab under the deck; the {link("/permits/flood-zones-50-percent-rule/", "flood page")} explains when.'))
    body += sec("What goes wrong on this coast", ul(["Edge restraint set in the bedding sand instead of on the base; the first surge lifts it.", "Polymeric sand activated the day before a storm and washed out.", "Travertine coping on a salt pool never sealed; flaking at the waterline in two seasons.", "Overlay pavers raising the deck above the door threshold.", "Cage anchors drilled into paver joints."]))
    body += sec("Maintenance", p(f'Rinse salt splash, keep sprinklers off the deck, re-sand joints when they drop more than a quarter inch, and seal on the {link("/coastal/maintenance-calendar/", "coastal cycle")}: 18 to 24 months within a mile of open water, 2 to 3 years inland, annually for coping on a salt pool.'))
    body += sec("Comparisons", cards([("/compare/travertine-vs-concrete-pavers/", "Travertine vs concrete pavers", "Cost, heat, salt, repair."), ("/compare/travertine-vs-shellstone-vs-porcelain/", "Travertine, shellstone or porcelain", "The three coolest options."), ("/compare/cool-deck-vs-pavers/", "Cool deck vs pavers", "Overlay or rebuild."), ("/concrete/pool-decks/", "Concrete pool decks", "The poured alternative.")]))
    body += gallery(key, "Paver pool decks from the provider's crews", 4)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a paver pool deck estimate", "/contact/", "Tell us the material, whether the pool is salt, and how far you are from the water.")
    body += reviewed("September 10, 2026")
    return page(key, "Pool Deck Pavers in Sarasota, FL – Cost, Heat, Salt & Permits", "Paver pool decks in Sarasota County: concrete pavers $13 to $16 and travertine $20 to $26 per sq ft planning ranges, base and coping spec, salt-pool rules, permits, flood zones and turtle lighting.",
                "Paver pool decks for Sarasota County, built on a base that drains", "Pavers · pool decks", "Concrete pavers, travertine, shellstone, marble and porcelain around residential and condo pools, with the coping, edge and sealing details that survive salt and surge.", body, faq)


# ---------------------------------------------------------------- TRAVERTINE & SHELLSTONE
def travertine():
    key = "pavers-travertine-shellstone"
    faq = [
        ("Does a salt-water pool damage travertine coping?", "Over time, yes, if it isn't sealed and rinsed. Salt crystallizes in the stone's pores at the splash line and pushes the surface off in flakes. Annual sealing of the coping with a breathable penetrating product and a weekly fresh-water rinse keep it sound for decades."),
        ("Which travertine finish is best for a pool deck?", "Tumbled for slip resistance and a soft look, honed for a cleaner modern surface with good wet grip, brushed for a middle ground. Polished travertine is an indoor product."),
        ("Is shellstone the same as travertine?", "Both are limestone-family stones and behave the same chemically; shellstone is a Florida quarry product with visible shell fragments and a more open texture, so it grips better wet and collects more organics."),
        ("Do the holes in travertine need filling?", "Tumbled travertine is sold unfilled; the holes fill with polymeric sand at install and get topped up over the years. Filled and honed travertine arrives with the holes resin-filled."),
        ("What does travertine cost installed?", "Roughly $20 to $26 per square foot in Sarasota as a planning range on September 10, 2026, with coping at $30 to $60 per linear foot."),
    ]
    body = facts([("Uses", "Pool decks, patios, lanais, driveways (thick French pattern)"), ("Finishes", "Tumbled, honed, brushed; filled or unfilled"), ("Salt rule", "Seal coping annually on a salt pool"), ("Planning range", "$20 to $26 per sq ft")])
    body += cap("What does travertine cost in Sarasota and what changes near salt water?",
                "Published Sarasota-area pricing on September 10, 2026 puts installed travertine at roughly $20 to $26 per square foot and shellstone in the same band, with coping at $30 to $60 per linear foot. Near salt water the number that matters is maintenance: annual sealing of the coping and rinsing keep the stone from flaking at the waterline.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a travertine deck take?",
                "Six to nine working days for a typical pool deck, a day or two longer than concrete pavers because natural stone is cut and sorted on site and the French pattern needs a tighter base. Sealing waits 30 days.")
    body += sec("Why travertine is the Sarasota pool deck stone", p("It stays cooler underfoot than most alternatives because it's light in color and porous, it grips wet in a tumbled or honed finish, and it looks like what buyers on the keys expect. The trade is chemistry: travertine and shellstone are calcium carbonate. Salt, acid cleaners and long wet exposure dissolve or fracture the surface. Sealed, rinsed and cleaned with pH-neutral products, a travertine deck lasts as long as the house."))
    body += sec("Finishes and formats", table(["Finish", "Wet grip", "Look", "Use"], [["Tumbled, unfilled", "Best", "Soft, aged edges", "Pool decks, patios"], ["Honed, filled", "Good", "Clean, flat", "Lanais, modern homes"], ["Brushed", "Good", "Textured, matte", "Pool decks"], ["Chiseled edge", "Good", "Rustic", "Borders and steps"]], "Formats: 6×12, 12×12, 12×24, 16×24 French pattern; 1-1/4 in. thick for foot traffic, 2 in. for vehicular"))
    body += sec("Shellstone", p("Quarried in Florida, shellstone shows fossil shell in a light cream to gray field. It's cooler than most concrete pavers, grips very well wet and reads as coastal. The open texture collects leaves and mildew in shade, so it wants the same rinse-and-seal routine as travertine and a soft-bristle scrub rather than a pressure washer at close range."))
    body += sec("Spec", p("Sand-set on 4 inches of compacted base for decks and patios, 6 inches and 2-inch-thick pieces for driveways, mortar-set coping on the pool beam with a flexible joint, polymeric sand in the joints, and a breathable penetrating sealer after 30 days. No acid washes, ever; efflorescence is removed with a neutral cleaner and time."))
    body += sec("Permits", p(f'Same as any paver deck or patio: see the {link("/permits/", "permit hub")}. On the keys the turtle-lighting and setback rules apply to the deck regardless of material.'))
    body += sec("Comparisons", cards([("/compare/travertine-vs-concrete-pavers/", "Travertine vs concrete pavers", "Where the extra cost pays and where it doesn't."), ("/compare/travertine-vs-shellstone-vs-porcelain/", "Travertine, shellstone or porcelain", "Heat, slip and salt side by side."), ("/compare/sealer-types-coastal/", "Sealers near the coast", "Penetrating vs film.")]))
    body += gallery(key, "Natural-stone decks from the provider's crews", 3)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a travertine estimate", "/contact/", "Say whether the pool is salt-chlorinated; it changes the sealing plan.")
    body += reviewed("September 10, 2026")
    return page(key, "Travertine & Shellstone Pavers in Sarasota, FL – Cost & Salt", "Travertine and shellstone pool decks and patios in Sarasota County: $20 to $26 per sq ft planning range, finishes for wet grip, the salt-pool sealing rule, formats and spec on a compacted base.",
                "Travertine and shellstone for Sarasota pool decks, with the salt chemistry stated up front", "Pavers · travertine and shellstone", "Natural limestone that stays cool and grips wet, sealed and rinsed so the waterline doesn't flake.", body, faq)


# ---------------------------------------------------------------- MARBLE & PORCELAIN
def marble():
    key = "pavers-marble-porcelain"
    faq = [
        ("Are marble pavers slippery when wet around a pool?", "Honed or tumbled marble is not; polished marble is. Outdoor marble is sold honed or sandblasted for that reason, and a wet dynamic coefficient of friction of 0.42 or better is the number to ask for."),
        ("Are large-format porcelain pavers a good pool deck in Florida?", "Yes, with a perfect base. Porcelain is immune to salt, acid and stains and comes with an R11 slip face; its weakness is that a 2 cm tile on a bedding layer that isn't dead flat will rock and crack at the corners."),
        ("What is Belgard Luxury?", "Belgard's premium line of porcelain and natural-stone-look pavers in large formats, which the provider installs in Central Florida. Availability for Sarasota projects is confirmed with the estimate."),
        ("How do marble and travertine differ around a pool?", "Marble is denser and etches from acid rather than flaking from salt; it stays cool and reads as a lanai floor. Travertine is more porous and more forgiving of an imperfect base."),
        ("What do marble and porcelain cost installed?", "Planning ranges on September 10, 2026: honed marble roughly $24 to $34 per square foot, 2 cm porcelain roughly $22 to $32, both above travertine because of material and the base tolerance."),
    ]
    body = facts([("Uses", "Lanai floors, pool decks, entries, coping"), ("Materials", "Honed marble, 2 cm porcelain, Belgard Luxury"), ("Base", "Dead-flat screed; mortar-set over slab for porcelain where possible"), ("Planning range", "$22 to $34 per sq ft")])
    body += cap("What do marble and porcelain pavers cost in Sarasota?",
                "Planning ranges compiled on September 10, 2026 put honed marble pavers at roughly $24 to $34 per square foot installed and 2 cm porcelain at $22 to $32, both above concrete pavers and travertine. The premium buys density and stain resistance in marble and near-total chemical immunity in porcelain, and it pays for a base tolerance of about 1/8 inch across the whole floor.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a marble or porcelain deck take?",
                "Six to ten working days. The base and screed take longer than for other pavers because these materials show every hump, and porcelain is often mortar-set over a slab or set on a bedding layer with a rubber mallet and a level on every piece.")
    body += sec("Marble on a Sarasota lanai", p("Honed marble pavers and bullnose coping give a lanai the look of an interior floor that continues outside, which is exactly what buyers on Bird Key, Longboat Key and west of the Trail expect in a renovation. Marble stays cool, resists salt better than travertine, and etches from acid, so cleaning is neutral-pH only. Sandblasted or tumbled faces are used around water; polished marble belongs indoors."))
    body += sec("Porcelain pavers", p("Two-centimeter porcelain pavers in 24-by-24 and 16-by-32 formats are dense, non-porous, colorfast and made with a textured R11 face for wet slip resistance. They don't need sealing and shrug off salt pools, well water and mildew. What they need is a base that doesn't move: a dead-flat compacted base with a thin screed, or a sound concrete slab with a mortar bed. Around pools the coping is porcelain bullnose or a matching stone."))
    body += sec("Spec", table(["Item", "Marble", "Porcelain"], [["Thickness", "1-1/4 in. (3 cm)", "2 cm"], ["Setting", "Sand-set on 4 in. base or mortar-set on slab", "Mortar-set on slab preferred; sand-set on screed with pedestal or spacer system"], ["Joints", "Polymeric sand, 1/8 in.", "1/8 to 3/16 in., polymeric or grout when mortar-set"], ["Sealer", "Penetrating, at 30 days", "None"], ["Cleaning", "Neutral pH only", "Anything reasonable"]], "Marble and porcelain paver spec"))
    body += sec("Permits", p(f'As for any paver deck; see {link("/permits/", "permits")}. On elevated coastal homes the deck is set over the engineered slab, which is where porcelain in a mortar bed is at its best.'))
    body += sec("Comparisons", cards([("/compare/travertine-vs-shellstone-vs-porcelain/", "Travertine, shellstone or porcelain", "Heat, slip and salt."), ("/pavers/travertine-shellstone/", "Travertine and shellstone", "The porous alternatives."), ("/concrete/architectural/", "Architectural concrete", "Honed concrete as another lanai floor.")]))
    body += gallery(key, "Marble and porcelain from the provider's crews", 3)
    body += extra(key)
    body += faq_block(faq)
    body += cta("Get a marble or porcelain estimate", "/contact/", "Send a photo of the lanai and the door threshold height.")
    body += reviewed("September 10, 2026")
    return page(key, "Marble & Porcelain Pavers in Sarasota, FL – Pool Decks & Lanais", "Marble and 2 cm porcelain pavers for Sarasota County lanais and pool decks: $22 to $34 per sq ft planning ranges, honed faces for wet slip, salt and acid behavior, base tolerance and Belgard Luxury lines.",
                "Marble and porcelain pavers for Sarasota lanais and pool decks", "Pavers · marble and porcelain", "Honed marble and large-format porcelain that read as interior floors, set on a base flat enough to deserve them.", body, faq)


# ---------------------------------------------------------------- DRIVEWAYS
def driveways():
    key = "pavers-driveways"
    faq = [
        ("What base depth do driveway pavers need on a high-water-table lot?", "Six inches of compacted crushed limerock in two or three lifts over a proof-rolled subgrade, with geotextile where the sand pumps, per ICPI practice for vehicular pavements. Eight inches where the lot floods in the wet season."),
        ("How long does a paver driveway last in Florida?", "Twenty-five to thirty years for the pavers; the base and the joint sand are the maintenance items. Units can be lifted and reset, which is the whole argument for pavers over concrete near the water."),
        ("How long does a paver driveway take to install?", "Four to seven working days for a two-car driveway, including demolition, base, laying and compaction, plus 24 to 48 dry hours for the polymeric sand. You can drive on it as soon as the sand cures."),
        ("Are permeable pavers strong enough for a driveway?", "Yes: permeable interlocking concrete pavement is designed for vehicular loads on an open-graded stone base. It costs more because the base is deeper and the stone is washed, and it's the answer when the lot is at the 50 percent impervious limit."),
        ("Which pattern for a driveway?", "Herringbone, 45 or 90 degrees, for the field, because it interlocks under turning tires; running bond and basketweave creep. A soldier-course border in a contrasting color holds the edge."),
        ("Does the apron have to be concrete?", "In the City of Sarasota and Venice the apron in the right-of-way follows the city detail, which may require concrete or a license agreement for pavers. Unincorporated Sarasota County and Charlotte County allow pavers to the road with a permit."),
    ]
    body = facts([("Typical size", "500 to 1,000 sq ft"), ("Spec", "6 in. compacted base, 1 in. bedding, 2-3/8 in. or 3-1/8 in. vehicular pavers, herringbone"), ("Time on site", "4 to 7 working days"), ("Planning range", "$14 to $22 per sq ft")])
    body += cap("What does a paver driveway cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts an installed concrete-paver driveway at roughly $14 to $22 per square foot, above the $13 to $16 quoted for patios because of the deeper base, vehicular units and edge curbs. A 600-square-foot two-car driveway therefore runs about $8,500 to $13,000, with demolition of the old concrete adding $2 to $4 per square foot.",
                '<p class="src-note">' + SRC + '</p>' + p(f' Size bands and the concrete comparison are in the {link("/pricing/pavers/", "paver cost guide")} and {link("/compare/concrete-vs-pavers-driveway/", "concrete vs pavers")}.'))
    body += cap("How long does a paver driveway take?",
                "Four to seven working days. One for demolition and haul-off, one or two for subgrade and base in lifts, two for laying and cutting, one for compaction and polymeric sand, then 24 to 48 dry hours. Rain during the sand cure is the one schedule risk, so summer installs end early in the day.")
    body += sec("Scope", ul(["Full driveway replacement to the apron, with the apron in concrete or pavers per the jurisdiction's detail.", "Widening and turnouts with a curb at the new edge.", "Permeable paver driveways on an open-graded base for lots at the impervious limit.", "Clay brick driveways in traditional neighborhoods west of the Trail.", "Repair and re-leveling of an existing paver driveway (see the repair page)."]))
    body += sec("Price factors", table(["Factor", "Effect"], [["Paver thickness", "3-1/8 in. vehicular units add $1 to $2 per sq ft over 2-3/8 in."], ["Pattern and borders", "Two-color borders, inlays and 45-degree herringbone add cutting labor"], ["Base depth", "8 in. on wet lots adds $1 to $1.50 per sq ft"], ["Edge restraint", "Concrete curb $12 to $20 per linear foot; spiked restraint less"], ["Apron and culvert", "$500 to $5,000 depending on the office and the crossing"], ["Permeable system", "+$4 to $8 per sq ft for the open-graded base and washed stone"]], "Paver driveway price factors, Sarasota County, 2026 (planning ranges)"))
    body += sec("The base spec for a Sarasota driveway", p("The subgrade is excavated to firm sand, proof-rolled and pitched 1/8 inch per foot. A geotextile goes down where the sand pumps under the roller. Six inches of crushed limerock or recycled concrete is placed in lifts of no more than 3 inches, each compacted with a plate compactor to refusal. One inch of concrete sand is screeded, never compacted before laying. Vehicular pavers go down in herringbone, the field is compacted with a pad on the plate, polymeric sand is swept, compacted and activated, and the edge is a concrete curb where a truck tire or a surge could reach it."))
    body += sec("Permits by jurisdiction", table(["Office", "What applies", "Page"], [["Sarasota County", "Culvert permit or right-of-way use permit for the crossing; pavers allowed to the road", link("/permits/sarasota-county/", "Sarasota County")], ["City of Sarasota", "Apron is city property; permit required for the apron", link("/permits/city-of-sarasota/", "City of Sarasota")], ["Venice", "Pavers in the right-of-way need a license agreement and the city detail", link("/permits/venice/", "Venice")], ["North Port", "Right of Way Use Permit; swale restoration", link("/permits/north-port/", "North Port")], ["Longboat Key", "Planning & Zoning review of at-grade driveways", link("/permits/longboat-key/", "Longboat Key")], ["Charlotte County", "Driveway permit; all flatwork including pavers is permitted", link("/permits/charlotte-county/", "Charlotte County")]], "Checked September 10, 2026"))
    body += sec("What goes wrong", ul(["Base placed in one 6-inch lift and compacted only on top; the middle stays soft and the driveway ruts.", "Running bond under turning tires.", "Spiked edge restraint at the street; the first delivery truck pushes the border out.", "Bedding sand at 2 inches to fix a low base; the dips show within a year.", "Polymeric sand activated before a storm."]))
    body += sec("Maintenance", p(f'Re-sand joints when they drop, seal on the {link("/coastal/maintenance-calendar/", "coastal cycle")}, and keep well-water sprinklers off the field. Rust and efflorescence guides are in {link("/guides/", "guides")}.'))
    body += sec("Comparisons", cards([("/compare/concrete-vs-pavers-driveway/", "Concrete vs paver driveway", "Twenty-year cost and flood behavior."), ("/guides/permeable-pavers-impervious-limit/", "Permeable pavers and the 50% limit", "When permeable is the only option."), ("/concrete/driveways/", "Concrete driveways", "The poured alternative.")]))
    body += gallery(key, "Paver driveways from the provider's crews", 6)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a paver driveway estimate", "/contact/", "Send the width and length and whether the driveway meets a swale or a sidewalk.")
    body += reviewed("September 10, 2026")
    return page(key, "Paver Driveways in Sarasota, FL – Cost, Base & Permits", "Paver driveways in Sarasota County: $14 to $22 per sq ft planning range, 6-inch base in lifts for a high water table, herringbone and curbs, permeable options, permits by office.",
                "Paver driveways for Sarasota County, built in lifts on a base that carries the load", "Pavers · driveways", "Concrete, brick and permeable paver driveways with the base depth, pattern and edge that hold up under tires, rain and the occasional surge.", body, faq)


# ---------------------------------------------------------------- PATIOS & LANAIS
def patios():
    key = "pavers-patios-lanais"
    faq = [
        ("When can pavers go over an existing lanai slab, and when must the slab come out?", "Over: the slab rings solid, drains away from the house, has no offset cracks, and the pavers plus bedding keep the floor below the door threshold. Out: hollow spots, offset cracks, a pitch toward the sliders, or a threshold too tight. The tests take twenty minutes on site."),
        ("How big should a paver patio be?", "A dining set needs about 12 by 14 feet; a lounge area another 10 by 12. Sarasota patios that get used are the ones with shade, so plan the paver area around where the shade falls at 4 p.m."),
        ("Sand-set or mortar-set on a lanai?", "Sand-set over a compacted base for new patios; thin-set over a sound slab for overlays where height is tight. A mortar bed on sand is the combination that fails."),
        ("How long does a paver patio take?", "Three to five working days for 300 to 500 square feet, plus a dry day for the polymeric sand."),
        ("What does a paver patio cost?", "Roughly $13 to $16 per square foot in concrete pavers as a planning range, $20 to $26 in travertine, so a 400-square-foot patio lands near $5,500 to $10,500."),
    ]
    body = facts([("Typical size", "200 to 600 sq ft"), ("Spec", "4 in. base, 1 in. bedding, 2-3/8 in. pavers or 1-1/4 in. stone"), ("Time on site", "3 to 5 working days"), ("Planning range", "$13 to $16 concrete pavers; $20 to $26 stone")])
    body += cap("What does a paver patio or lanai floor cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts installed concrete pavers at roughly $13 to $16 per square foot and travertine at $20 to $26, so a 400-square-foot patio runs about $5,500 in concrete pavers and up to $10,500 in stone as a planning range. An overlay on a sound lanai slab is at the low end because there's no excavation.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a paver patio take?",
                "Three to five working days for a typical patio: excavation or slab prep, base in lifts, bedding, laying and cutting, compaction and polymeric sand, plus a dry day. A lanai overlay on a sound slab can be done in two days.")
    body += sec("Scope", ul(["New backyard patios with a soldier-course border and a seat wall if wanted.", "Lanai floors under an existing cage, sand-set or thin-set over the slab.", "Lanai extensions beyond the cage with a new base and a matching pattern.", "Side-yard and courtyard patios on small keys lots.", "Fire pit and outdoor kitchen surrounds (see walls and outdoor living)."]))
    body += sec("The overlay tests", table(["Test", "Pass", "Fail"], [["Sound with a hammer", "Solid ring", "Hollow"], ["Cracks", "Hairline, no offset", "Offset or wide"], ["Slope", "Away from the house", "Toward the house or ponding"], ["Threshold", "Pavers plus bedding stay 1 in. below the door", "Floor would rise to the door"], ["Drainage", "Water leaves the lanai", "Cage traps water with no drain"]], "Five tests before an overlay"))
    body += sec("Spec", p("New patios: compacted subgrade, 4 inches of crushed base in two lifts, 1 inch of screeded concrete sand, pavers, edge restraint on the base, polymeric sand. Overlays: pressure-washed slab, thin-set mortar or a 1-inch sand bed with a perimeter curb, and a drain at the low side of the cage. Light colors for heat; textured faces for wet grip near a pool."))
    body += sec("Permits and HOAs", p(f'An at-grade patio that doesn\'t change the lot\'s impervious cover is often below the permit threshold in unincorporated Sarasota County and permitted in Charlotte County; extensions that push the lot over the 50 percent impervious limit are a zoning question. Associations from The Meadows to Wellen Park need an ARC application for any extension. See {link("/permits/", "permits")} and {link("/hoa/", "HOA guides")}.'))
    body += sec("What goes wrong", ul(["Overlay over a hollow slab.", "Floor raised to the door threshold.", "Bedding sand used to level a low base.", "No drain under a cage that traps water.", "Dark pavers on a sunny lanai."]))
    body += sec("Comparisons", cards([("/concrete/patios-lanais/", "Concrete patios and lanais", "The poured alternative."), ("/pavers/travertine-shellstone/", "Travertine and shellstone", "Stone for the same patio."), ("/pavers/retaining-walls-outdoor-living/", "Walls, fire pits and kitchens", "What goes on the patio.")]))
    body += gallery(key, "Paver patios from the provider's crews", 6)
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a paver patio estimate", "/contact/", "Send a photo of the slab or the yard and the height of the door threshold.")
    body += reviewed("September 10, 2026")
    return page(key, "Paver Patios & Lanais in Sarasota, FL – Cost & Overlays", "Paver patios and lanai floors in Sarasota County: $13 to $26 per sq ft planning ranges by material, the five tests for an overlay on an existing slab, base spec, drains, permits and HOA approvals.",
                "Paver patios and lanai floors for Sarasota County", "Pavers · patios and lanais", "New patios, lanai floors and extensions, including overlays on slabs that pass five tests and tear-outs on slabs that don't.", body, faq)


# ---------------------------------------------------------------- WALKWAYS & STEPS
def walkways():
    key = "pavers-walkways-steps"
    faq = [
        ("Can paver steps be built without a concrete core?", "Small garden steps can be built from wall block on a compacted base; entry steps that carry traffic get a concrete core or a block core with a poured cap so the treads don't rock."),
        ("How wide should a paver walkway be?", "Four feet for a front walk, 3 feet for a garden path, 30 inches for a side-yard utility path."),
        ("Do walkway lights have to be turtle-friendly?", "On Siesta Key, Longboat Key, Casey Key, Manasota Key and Venice Island, any fixture visible from the beach must be long-wavelength (560 nm or more) and fully shielded from May 1 to October 31. The lighting page has the rule and the fixtures."),
        ("What does a paver walkway cost?", "Roughly $14 to $20 per square foot as a planning range because of the cutting on a narrow path, so a 4-by-40-foot walk lands near $2,200 to $3,200."),
        ("Can a paver path be laid around oak roots?", "Yes, more easily than concrete: the base is thinner, the path can bend, and pavers can be lifted later if a root heaves them. Cutting roots on a protected tree still needs a permit."),
    ]
    body = facts([("Uses", "Entry walks, garden paths, side-yard paths, steps and stoops"), ("Spec", "4 in. base on walks; concrete or block core under steps"), ("Time on site", "1 to 4 working days"), ("Planning range", "$14 to $20 per sq ft walks; steps per riser")])
    body += cap("What does a paver walkway cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 supports a planning range of $14 to $20 per square foot for a paver walkway, higher per foot than a patio because a narrow path is mostly cuts and border. A 4-by-40-foot entry walk runs about $2,200 to $3,200; paver-faced steps are priced per riser, roughly $250 to $500 each depending on the core.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a walkway or steps take?",
                "One to four working days. A straight walk is a two-day job; curved paths, steps with a poured core and integrated lighting take longer because the core cures before the treads go on.")
    body += sec("Scope", ul(["Front entry walks with a border and a landing at the door.", "Garden and side-yard paths, straight or curved, around trees.", "Entry steps and stoops with paver treads and risers on a concrete or block core.", "Step and path lighting built into the hardscape, turtle-compliant on the islands.", "Stepping-stone paths in large-format porcelain or travertine set in turf or gravel."]))
    body += sec("Spec", p("Walks: compacted subgrade, 4 inches of crushed base, 1 inch of bedding, pavers with a soldier-course border, edge restraint on the base, polymeric sand, cross slope of 1/4 inch per foot. Steps: a poured or block core on a footing, paver treads with a 1-inch overhang, risers faced in the same paver, and 7-inch risers with 11-inch treads so they're safe barefoot."))
    body += sec("Lighting", p(f'Path and step lights are set during the base work so wire runs in conduit under the pavers, not in the joints. Within sight of the beach the fixtures are amber or red long-wavelength and fully shielded; see {link("/permits/sea-turtle-lighting/", "sea turtle lighting")} and {link("/pavers/outdoor-lighting/", "hardscape lighting")}.'))
    body += sec("Permits and trees", p(f'Walks on your lot are usually below permit thresholds outside Charlotte County; public sidewalks are right-of-way work. Oak roots are protected under the county tree ordinance and the City of Sarasota\'s 4-inch rule; the path bends. See {link("/permits/", "permits")}.'))
    body += sec("Comparisons", cards([("/concrete/sidewalks-walkways/", "Concrete walkways", "The poured version."), ("/pavers/outdoor-lighting/", "Hardscape lighting", "Fixtures and the island rule."), ("/pavers/retaining-walls-outdoor-living/", "Walls and steps", "Seat walls and step cores.")]))
    body += gallery(key, "Walkways and steps from the provider's crews", 6)
    body += extra(key)
    body += faq_block(faq)
    body += cta("Get a walkway or steps estimate", "/contact/", "Send a photo from the street to the door and note any trees the path passes.")
    body += reviewed("September 10, 2026")
    return page(key, "Paver Walkways & Steps in Sarasota, FL – Cost & Lighting", "Paver walkways, garden paths and entry steps in Sarasota County: $14 to $20 per sq ft planning range, step cores and riser sizes, oak-root rules, and turtle-compliant lighting on the barrier islands.",
                "Paver walkways and steps for Sarasota County", "Pavers · walkways and steps", "Entry walks, garden paths and steps on a real core, with lighting wired under the pavers and amber where the beach can see it.", body, faq)


# ---------------------------------------------------------------- SEALING
def sealing():
    key = "pavers-sealing"
    faq = [
        ("How long does paver sealer last one mile from the Gulf?", "Eighteen to twenty-four months for a penetrating sealer, sometimes less on the Gulf-front row where spray is constant. Inland the same product lasts two to three years. Sun, salt and sprinkler water are what shorten it."),
        ("Why did the sealer on my pool deck peel or turn white?", "A film-forming sealer applied over a damp base or too thick traps moisture and blushes white; on a deck that stays wet, it peels. The fix is stripping and switching to a breathable penetrating product."),
        ("Should I pressure wash my pavers myself?", "Lightly, with a wide fan tip and from a distance. A turbo nozzle up close blasts the joint sand out and etches soft stone. Professional cleaning uses controlled pressure and re-sands afterward."),
        ("Do new pavers need sealing?", "Not immediately. Wait 30 days for efflorescence to work out, then seal if you want color retention and stain resistance. Porcelain never needs it."),
        ("What does cleaning and sealing cost?", "About $1 to $3 per square foot for cleaning, re-sanding and sealing together as a planning range, with cleaning alone at $0.40 to $0.60 and a service minimum of roughly $150 to $250."),
    ]
    body = facts([("Scope", "Clean, re-sand, seal; strip and reseal"), ("Products", "Breathable penetrating sealers; matte film sealers only where drainage is perfect"), ("Coastal cycle", "18 to 24 months within a mile of open water"), ("Planning range", "$1 to $3 per sq ft full service")])
    body += cap("What does paver cleaning and sealing cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 puts cleaning alone at $0.40 to $0.60 per square foot and complete restoration (cleaning, polymeric re-sanding and sealing) at about $1 to $3 per square foot depending on condition, with a service minimum around $150 to $250. A 600-square-foot driveway therefore runs about $600 to $1,800 for the full service.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How often should pavers be sealed near the coast?",
                "Every 18 to 24 months within roughly a mile of the Gulf or the bays, every 2 to 3 years inland, and annually for travertine or shellstone coping on a salt-chlorinated pool. That's shorter than the 3-year figure quoted for inland Florida because salt, spray and UV break the sealer down faster here.",
                p(f'The {link("/coastal/maintenance-calendar/", "maintenance calendar")} sets the month by distance from the water and by material.'))
    body += sec("What the service includes", ol(["Inspection: joint depth, efflorescence, rust, mildew, settled units and the state of the old sealer.", "Cleaning with controlled pressure and the right chemistry: neutral for stone, an efflorescence cleaner for concrete pavers, oxalic for well-water rust.", "Re-sanding with polymeric sand to full joint depth, compacted, then activated and left dry for 24 to 48 hours.", "Sealing after the surface is dry through: a breathable penetrating sealer as the default, a matte film sealer with grit only where the base drains perfectly.", "A care sheet with the next date."]))
    body += sec("Sealer choice near the coast", table(["Sealer type", "Look", "Best for", "Risk here"], [["Penetrating (silane/siloxane)", "Natural, no sheen", "Anything near water; stone; salt pools", "Low"], ["Matte film (acrylic, water-based)", "Slight enhancement", "Driveways and patios that drain well", "Blushing over a damp base"], ["Wet-look film (solvent acrylic)", "Glossy, darkened", "Shaded, well-drained patios", "Slippery around water; peels; traps moisture"], ["Polyurethane / hybrid", "Durable satin", "High-traffic driveways", "Hard to strip if it fails"]], "Sealers compared for the Sarasota coast") + p(f'More on the {link("/compare/sealer-types-coastal/", "sealer comparison")}.'))
    body += sec("What goes wrong", ul(["Sealing a wet base; white blush within weeks.", "Wet-look sealer around a pool.", "Pressure washing with a turbo nozzle; joints emptied and stone etched.", "Acid wash on travertine.", "Sealing before efflorescence has worked out of new pavers."]))
    body += sec("Comparisons", cards([("/compare/sealer-types-coastal/", "Sealer types near the coast", "Penetrating, film, hybrid."), ("/guides/efflorescence/", "Efflorescence", "Why new pavers go white and how to wait it out."), ("/guides/well-water-rust-stains/", "Rust stains", "Well-water irrigation and oxalic acid."), ("/guides/polymeric-sand-weeds-ants/", "Polymeric sand, weeds and ants", "Joint sand explained.")]))
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Book cleaning and sealing", "/contact/", "Tell us the square footage, the material and when it was last sealed.")
    body += reviewed("September 10, 2026")
    return page(key, "Paver Sealing & Cleaning in Sarasota, FL – Cost & Cycle", "Paver cleaning, polymeric re-sanding and sealing in Sarasota County: $1 to $3 per sq ft planning range, the 18-to-24-month coastal cycle, sealer types that don't blush or peel, and what to avoid.",
                "Paver sealing, cleaning and re-sanding on a coastal schedule", "Pavers · sealing and cleaning", "Controlled cleaning, full-depth polymeric sand and a breathable sealer, on an interval set by how far you are from the water.", body, faq)


# ---------------------------------------------------------------- REPAIR & STORM
def repair():
    key = "pavers-repair-storm-restoration"
    faq = [
        ("What makes pavers sink on a Nokomis lot and how is it fixed?", "Water moving fines out of the base: a downspout, a sprinkler leak, or a swale that stopped draining. The pavers over the void are lifted, the base is rebuilt and compacted, the water problem is fixed, and the same pavers go back. New pavers aren't the fix."),
        ("How much does it cost to lift and reset sunken pavers after a storm?", "Roughly $8 to $15 per square foot of the affected area as a planning range, plus base material, and less per foot for larger areas. Re-sanding and sealing the whole surface afterward is separate."),
        ("Can shifted pavers be reused after surge?", "Almost always. Concrete and stone pavers aren't damaged by water; the base under them is. Units are lifted, stacked, rinsed, and reset on a rebuilt base with new polymeric sand."),
        ("How soon after a storm should pavers be reset?", "After the base has drained and dried, usually one to three weeks, and after the insurer has photos. Resetting on a saturated base means doing it twice."),
        ("Do weeds mean the pavers are failing?", "No. Weeds mean the joint sand is gone or was never polymeric. Re-sanding fixes it; the pavers are fine."),
    ]
    body = facts([("Problems", "Settling, sinking, shifting, edge failure, weeds, ants, efflorescence, surge damage"), ("Method", "Lift, rebuild base, reset, re-sand, seal"), ("Time on site", "Half a day to 5 days"), ("Planning range", "$8 to $15 per sq ft affected area")])
    body += cap("What does paver repair cost in Sarasota?",
                "Published Sarasota-area pricing on September 10, 2026 supports a planning range of $8 to $15 per square foot for the affected area when pavers are lifted, the base rebuilt and the same units reset, plus $1 to $3 per square foot if the whole surface is re-sanded and sealed afterward. Storm restoration of a full driveway or pool deck is scoped after a void survey.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("What should I do with pavers that shifted during storm surge?",
                "Photograph everything before touching it, let the base drain for one to three weeks, then have the field lifted where it's low or heaved, the base sounded for voids and rebuilt in lifts, the edge restraint replaced with a concrete curb, the units rinsed of salt and reset, and new polymeric sand installed on a dry day. Resurfacing or sealing before that is wasted.",
                p(f'The full sequence, with what to document for the insurer, is on {link("/coastal/post-storm-restoration/", "post-storm restoration")} and the {link("/guides/hurricane-insurance-documentation/", "insurance documentation guide")}.'))
    body += sec("Repairs and their causes", table(["Symptom", "Cause here", "Fix"], [["Dip or sink in the field", "Fines washed out of the base by water", "Lift, rebuild base, fix the water, reset"], ["Pavers heaved along an edge", "Edge restraint failed or was set in sand", "Concrete curb, reset border"], ["Rocking units", "Bedding too thick or base not compacted", "Lift, re-screed at 1 in., reset"], ["Weeds and ants", "Joint sand gone or not polymeric", "Clean joints, polymeric re-sand"], ["White haze", "Efflorescence or sealer blush", "Wait or clean; strip film sealer"], ["Salt crust after surge", "Seawater in base and joints", "Fresh-water flush, re-sand"], ["Cracked pavers at corners", "Point loads on a poor base (porcelain especially)", "Replace units on a re-screeded bed"]], "Paver repair catalog for the Sarasota coast"))
    body += sec("The base is the repair", p("A paver surface that moved is a base that moved. On Myakka and EauGallie sands the base loses fines to water, so the repair starts with finding the water: a gutter, a leaking irrigation line, a swale, a pool overflow, or the Gulf. Once it's stopped, the base is rebuilt in 3-inch lifts and compacted to refusal, the bedding is re-screeded to 1 inch, and the original pavers go back. The result is indistinguishable from the rest of the field, which is the point of pavers."))
    body += sec("Permits", p(f'Repairs that don\'t change the footprint are generally not permitted work in Sarasota County and the cities; Charlotte County can treat larger resets as slab work; the Town of Longboat Key tracks storm repairs against substantial-damage review even though site work is excluded. See {link("/permits/", "permits")}.'))
    body += sec("Comparisons", cards([("/coastal/post-storm-restoration/", "Post-storm restoration", "The sequence after surge."), ("/coastal/storm-season-playbook/", "Storm season playbook", "What to do before June 1."), ("/pavers/sealing/", "Sealing and re-sanding", "The maintenance that prevents most of this.")]))
    body += extra(key)
    body += faq_block(faq)
    body += city_links(key)
    body += cta("Get a paver repair assessment", "/contact/", "Send photos of the low spots and tell us where the water comes from.")
    body += reviewed("September 10, 2026")
    return page(key, "Paver Repair & Storm Restoration in Sarasota, FL", "Paver repair in Sarasota County: sunken, shifted and surge-damaged pavers lifted and reset on a rebuilt base, $8 to $15 per sq ft planning range, causes on sandy soil, and the post-storm sequence.",
                "Paver repair and storm restoration for Sarasota County", "Pavers · repair and storm restoration", "Sunken, heaved, weedy or surge-shifted pavers reset on a base that's been rebuilt and a water problem that's been found.", body, faq)


# ---------------------------------------------------------------- WALLS & OUTDOOR LIVING
def walls():
    key = "pavers-retaining-walls-outdoor-living"
    faq = [
        ("Does a seat wall or decorative retaining wall need a permit in Sarasota County?", "Walls under 3.5 feet are generally not permitted as structures in unincorporated Sarasota County and the City of Sarasota; taller walls, and anything holding back a grade change that affects a neighbor, are engineered and permitted. Charlotte County reviews walls with the slab permit."),
        ("Can a fire pit go on a paver patio?", "A gas fire pit on a non-combustible base, yes, with clearances to the cage and the house per the manufacturer and the Florida Fire Prevention Code. Wood-burning pits are restricted in many communities; check the HOA."),
        ("What is an outdoor kitchen base?", "A block or steel-frame structure on a thickened pad, faced in stone or stucco, with the countertop and appliances by others. The pad and the base are the hardscape; gas, electric and plumbing are permitted trades."),
        ("How high can a seat wall be?", "Eighteen to twenty inches is a seat; anything over 3.5 feet is a retaining wall with engineering."),
        ("What do walls cost?", "Seat walls in block with a cap run roughly $60 to $120 per linear foot and outdoor kitchen bases $250 to $600 per linear foot as planning ranges, before appliances."),
    ]
    body = facts([("Uses", "Seat walls, decorative retaining walls, fire pits, outdoor kitchen bases, planters"), ("Materials", "Segmental block, veneer stone, poured caps"), ("Time on site", "2 to 8 working days"), ("Planning range", "$60 to $120 per linear ft seat walls")])
    body += cap("What do seat walls, fire pits and outdoor kitchen bases cost in Sarasota?",
                "Planning ranges compiled on September 10, 2026 put segmental-block seat walls with a cap at roughly $60 to $120 per linear foot, gas fire pit surrounds at $1,500 to $4,500 built, and outdoor kitchen bases at $250 to $600 per linear foot before appliances, countertops and utilities. Structural retaining walls above 3.5 feet are engineered and priced per design.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does outdoor-living hardscape take?",
                "Two to eight working days depending on the elements. A seat wall along a patio edge is two days; a kitchen base with a thickened pad, veneer and a poured cap is a week, with the gas and electrical trades scheduled between.")
    body += sec("What's in scope, and what isn't", p("In: decorative retaining walls and seat walls up to 3.5 feet, planters, fire pit surrounds, outdoor kitchen bases and pads, step cores, and the pavers around them. Not in: structural retaining walls above 3.5 feet or holding a grade change against a neighbor, seawall caps, and anything over the water. Those are engineered, licensed marine or structural work and this site doesn't advertise them."))
    body += sec("Spec", p("Segmental block walls sit on a compacted base of 6 inches of crushed stone in a trench, with the first course buried, drainage stone and a perforated pipe behind any wall that holds soil, and a cap adhered with masonry adhesive. Kitchen bases get a 6-inch reinforced pad, block or steel frame, veneer, and a poured or stone cap; the pad is set with the gas and electric sleeves before the pour."))
    body += sec("Permits and HOAs", p(f'Walls under 3.5 feet and at-grade fire pits are usually below permit thresholds in Sarasota County and the City of Sarasota; gas and electric for a kitchen are permitted trades regardless. Associations review walls, kitchens and fire features as exterior structures; the {link("/hoa/", "HOA guides")} cover the packet. See {link("/permits/", "permits")}.'))
    body += sec("Comparisons", cards([("/pavers/patios-lanais/", "Paver patios", "The floor under the wall."), ("/pavers/outdoor-lighting/", "Hardscape lighting", "Lights in the wall cap and steps."), ("/pavers/artificial-turf/", "Artificial turf", "Turf against the wall.")]))
    body += gallery(key, "Walls and terraces from the provider's crews", 3)
    body += extra(key)
    body += faq_block(faq)
    body += cta("Get an outdoor-living estimate", "/contact/", "Send a sketch of the patio with where the wall, pit or kitchen goes.")
    body += reviewed("September 10, 2026")
    return page(key, "Seat Walls, Fire Pits & Outdoor Kitchens in Sarasota, FL", "Decorative retaining and seat walls, fire pit surrounds and outdoor kitchen bases for Sarasota County patios: planning ranges, block and veneer spec, the 3.5-foot permit line and HOA review.",
                "Seat walls, fire pits and outdoor kitchen bases for Sarasota County patios", "Pavers · walls and outdoor living", "Decorative walls, planters and the hardscape under a fire feature or a kitchen, with the structural work above 3.5 feet left to engineers.", body, faq)


# ---------------------------------------------------------------- ARTIFICIAL TURF
def turf():
    key = "pavers-artificial-turf"
    faq = [
        ("Is artificial turf a good pairing with pavers in Florida heat?", "It's a good pairing for shade, side yards, pet runs and pool surrounds where grass won't grow, and a hot one in full sun: synthetic turf runs hotter than pavers at 2 p.m. Light-colored infill and shade help. It's not a pool-deck walking surface."),
        ("What maintenance does artificial turf need?", "Rinse to clear pollen and pet use, brush the fibers up a couple of times a year, top up infill, and keep sprinklers off it if you're on well water. Weeds don't grow through a properly installed base and weed barrier."),
        ("What base does turf need?", "Two to three inches of compacted crushed stone over a compacted subgrade with a weed barrier, pitched to drain. Turf laid on sand shifts and wrinkles."),
        ("How long does turf last?", "Ten to fifteen years for a quality product with a UV-stable yarn; the base lasts longer."),
        ("What does turf cost installed?", "Roughly $10 to $18 per square foot as a planning range depending on the product and the base."),
    ]
    body = facts([("Uses", "Pool surrounds, side yards, pet areas, putting greens, paver inlays"), ("Base", "2 to 3 in. compacted stone, weed barrier, drainage pitch"), ("Time on site", "1 to 3 working days"), ("Planning range", "$10 to $18 per sq ft")])
    body += cap("What does artificial turf cost in Sarasota?",
                "Planning ranges compiled on September 10, 2026 put installed synthetic turf at roughly $10 to $18 per square foot depending on the yarn, the infill and the base. A 300-square-foot side yard therefore runs about $3,000 to $5,400, less than repeated sod replacement in a strip that never gets sun.",
                '<p class="src-note">' + SRC + '</p>')
    body += cap("How long does a turf install take?",
                "One to three working days: base, weed barrier, turf, seams, infill and brushing. It's walkable the same day.")
    body += sec("Where turf makes sense here", ul(["Narrow side yards between the house and the fence where sod dies.", "Pet runs that get rinsed.", "Strips between paver bands on a modern driveway or patio.", "Shaded areas under oaks where grass fails.", "Putting greens and play areas."]) + p("Where it doesn't: as the walking surface around a pool in full sun, and on lots where the HOA prohibits it (several Palmer Ranch and Wellen Park sub-associations do)."))
    body += sec("Spec", p("Compacted subgrade pitched to drain, weed barrier, 2 to 3 inches of compacted crushed stone, a nailer board or paver edge, turf with a permeable backing, seams glued and nailed, and a silica or coated infill brushed in. Drainage matters as much as under pavers: turf over a base that holds water smells."))
    body += sec("Heat, honestly", p("Synthetic turf in full afternoon sun runs hotter than light pavers and much hotter than travertine; the fibers store heat and the infill holds it. It is a surface for feet in shoes, for dogs in the morning, and for the strips between paver bands, not for the walk from the pool to the lanai at 2 p.m. in August. Shade cloth over a cage or a tree canopy changes that math, and lighter yarn colors help at the margin."))
    body += sec("Permits and HOAs", p(f'Turf isn\'t permitted work, but it can be restricted or banned by community rules, and some associations count it as impervious in their own calculations even though Sarasota County treats permeable surfaces differently. See {link("/hoa/", "HOA guides")}.'))
    body += sec("Comparisons", cards([("/pavers/patios-lanais/", "Paver patios", "Turf inlays between paver bands."), ("/pavers/retaining-walls-outdoor-living/", "Walls and outdoor living", "Turf against seat walls.")]))
    body += extra(key)
    body += faq_block(faq)
    body += cta("Get a turf estimate", "/contact/", "Send the dimensions and how much sun the area gets.")
    body += reviewed("September 10, 2026")
    return page(key, "Artificial Turf in Sarasota, FL – With Pavers & Hardscape", "Artificial turf paired with pavers in Sarasota County side yards, pet areas and pool surrounds: $10 to $18 per sq ft planning range, base and drainage spec, heat facts and HOA restrictions.",
                "Artificial turf paired with pavers for Sarasota County yards", "Pavers · artificial turf", "Synthetic turf where grass gives up, on a base that drains, with an honest note about how hot it gets at 2 p.m.", body, faq)


# ---------------------------------------------------------------- OUTDOOR LIGHTING
def lighting():
    key = "pavers-outdoor-lighting"
    faq = [
        ("Do hardscape lights have to be turtle-friendly on Longboat Key?", "From May 1 to October 31, any artificial light visible from the beach must use bulbs that are FWC Certified Wildlife Lighting or produce only long-wavelength light (560 nanometers or more) and fixtures that are fully shielded and downward-directed, under Town Ordinance 2021-01. Practically, that means amber or red LEDs in shielded fixtures all year."),
        ("What is 560-nanometer lighting?", "Light at the amber-to-red end of the spectrum, which sea turtle hatchlings are far less likely to orient toward. Long-wavelength bulbs produce it without filters; a white bulb behind an amber lens doesn't qualify."),
        ("Can lights go in the paver joints?", "No. Fixtures are set in the pavers or in the wall cap with wire in conduit under the field, installed during the base work. Wire in a joint gets crushed and cut."),
        ("Low-voltage or line-voltage?", "Low-voltage (12 V) for nearly all hardscape lighting; a transformer at the house and no electrical permit for the run in most jurisdictions. Line-voltage for kitchens and outlets, by an electrician with a permit."),
        ("What does hardscape lighting cost?", "Roughly $150 to $350 per fixture installed, plus the transformer, as a planning range; a 10-fixture path-and-step system lands near $2,000 to $4,000."),
    ]
    body = facts([("Uses", "Path lights, step and riser lights, wall-cap lights, column lights, pool-cage perimeter"), ("Standard", "12 V LED; FWC Certified Wildlife Lighting on the islands"), ("Time on site", "1 to 3 working days, during the paver work"), ("Planning range", "$150 to $350 per fixture")])
    body += cap("What does hardscape lighting cost in Sarasota, and what's required on the islands?",
                "Planning ranges compiled on September 10, 2026 put low-voltage hardscape lighting at roughly $150 to $350 per fixture installed plus $300 to $700 for the transformer, so a ten-fixture system runs about $2,000 to $4,000. On Siesta Key, Longboat Key, Casey Key, Manasota Key and Venice Island, fixtures visible from the beach must be long-wavelength and fully shielded from May 1 to October 31.",
                '<p class="src-note">' + SRC + '</p>' + p(f' The rule, the ordinances and the fixture list are on the {link("/permits/sea-turtle-lighting/", "sea turtle lighting page")}.'))
    body += cap("When is lighting installed?",
                "During the paver work. Conduit and fixture housings go in with the base and bedding so nothing is cut later; the transformer and connections are finished the day the pavers are compacted. Adding lights to an existing paver field means lifting units, which is possible but costs more.")
    body += sec("Fixture types", table(["Fixture", "Where", "Island rule"], [["Recessed paver light", "In the field or border", "Amber LED, downward, shielded"], ["Riser light", "In step risers", "Amber, recessed"], ["Wall-cap / hardscape light", "Under seat-wall caps", "Amber, fully shielded"], ["Column light", "Driveway pillars", "Amber, full cut-off"], ["Path light", "Beds beside walks", "Amber, shielded, mounted low"]], "Hardscape fixtures and the barrier-island rule"))
    body += sec("Spec", p("Twelve-volt LED fixtures on a multi-tap transformer sized for the run, wire in conduit under the pavers with slack loops at each fixture, connections in gel-filled connectors, a photocell or astronomical timer, and, within sight of any beach, FWC Certified Wildlife Lighting bulbs and fixtures. Brass and copper fixtures outlast powder-coated aluminum in salt air."))
    body += sec("Permits and codes", p(f'Low-voltage lighting is generally not permitted work; the transformer\'s outlet is an electrical permit if it\'s new. Sarasota County Code Chapter 54 Article XXIII (Marine Turtle Protection), the Town of Longboat Key\'s Chapter 100 and the City of Venice\'s beach-lighting rules govern what the fixtures can be. See {link("/permits/sea-turtle-lighting/", "sea turtle lighting")}.'))
    body += sec("Comparisons", cards([("/pavers/walkways-steps/", "Walkways and steps", "Where most fixtures go."), ("/pavers/retaining-walls-outdoor-living/", "Walls and outdoor living", "Wall-cap lighting."), ("/permits/sea-turtle-lighting/", "Sea turtle lighting", "The ordinance and the fixture list.")]))
    body += gallery(key, "Lighting integrated in hardscape", 3)
    body += extra(key)
    body += faq_block(faq)
    body += cta("Add lighting to a hardscape project", "/contact/", "Tell us if the property is within sight of a beach.")
    body += reviewed("September 10, 2026")
    return page(key, "Hardscape Lighting in Sarasota, FL – Turtle-Compliant Fixtures", "Low-voltage path, step and wall lighting built into pavers in Sarasota County: $150 to $350 per fixture planning range, conduit under the field, and the 560 nm shielded-fixture rule for the barrier islands from May 1 to October 31.",
                "Hardscape lighting for Sarasota County, amber where the beach can see it", "Pavers · outdoor lighting", "Path, step and wall lights wired under the pavers during the install, with FWC-certified fixtures wherever a sea turtle could see them.", body, faq)


def get_pages():
    return [pool_decks(), travertine(), marble(), driveways(), patios(), walkways(), sealing(), repair(), walls(), turf(), lighting()]
