# -*- coding: utf-8 -*-
"""Coastal hub: salt, storm season, post-storm, maintenance calendar, and the Surface Temperature Study
(methodology published now; measurements published when they exist; no invented numbers)."""
import json
import pathlib

from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, link, ext, facts, cards, dataset_schema

DATA = pathlib.Path(__file__).resolve().parent / "data"


def pg(slug, title, meta, h1, lede, body, faq=None, schema=None):
    return {"route": f"/coastal/{slug}/" if slug else "/coastal/", "title": title, "meta_description": meta, "h1": h1, "kicker": "Coastal", "lede": lede,
            "breadcrumbs": [("Home", "/"), ("Coastal", "/coastal/"), (h1.split(":")[0][:40], None)] if slug else [("Home", "/"), ("Coastal", None)],
            "body_html": body, "faq": faq or [], "article": True, "schema": schema or []}


def hub():
    faq = [("Does an elevated coastal home need an engineered slab under a paver deck?", "In a VE zone, anything under the elevated floor is governed by the flood code: breakaway walls, open lattice, no obstruction to flow, and a slab designed by the structural engineer to be frangible or at grade. A paver deck goes over that slab or on a base beside the house, never as an unengineered pour under the living floor. In AE the rules are looser but the engineer still decides what sits under the house.")]
    body = cap("What does the Gulf side of Florida do to concrete and pavers?",
               "Five things, in order of how often they show up on estimates: a wet-season water table under 10 inches that pumps fines out of any base that isn't compacted in lifts; chloride from Gulf spray, brackish bays and salt-chlorinated pools that scales concrete and flakes limestone; 91-degree afternoons with 7 to 9 inches of monthly summer rain that rush the set and the cure; storm surge that lifts edge restraint and salts the base; and a rulebook that changes every few miles.",
               p("The pages in this hub take each of those apart and end in a schedule. None of them quotes a temperature, a durability figure or a storm statistic without a source or a published method."))
    body += cards([("/coastal/pool-deck-surface-temperature-study/", "Pool Deck Surface Temperature Study", "Nine surfaces, three times of day, July and January, infrared thermometer. Method now; numbers when measured."),
                   ("/coastal/salt-and-concrete/", "Salt and concrete", "How chloride gets in, what scaling and spalling look like, and the mix and cure that slow it."),
                   ("/coastal/storm-season-playbook/", "Storm Season Hardscape Playbook", "Before June 1, during a watch, and after: pavers, concrete, documentation."),
                   ("/coastal/post-storm-restoration/", "Post-storm restoration", "The sequence for pavers and slabs that stood in surge, and what not to do first."),
                   ("/coastal/maintenance-calendar/", "Coastal maintenance calendar", "Sealing, re-sanding and inspection intervals by distance from the water and by material.")])
    body += sec("The numbers behind the hub", table(["Fact", "Value", "Source"], [["Wet-season water table, Myakka fine sand", "Within 10 in. of the surface, 2 to 6 months", "USDA-NRCS Official Soil Series Description"], ["July / August average highs", "91.1 / 91.5 °F", "NOAA 1991–2020 normals, Sarasota-Bradenton"], ["August rainfall", "9.11 in.", "NOAA 1991–2020 normals"], ["Helene surge, Longboat Key", "6.68 ft (Sept 2024)", "NPR, Oct 14 2024"], ["Milton surge, Siesta Key", "Water and sand into first floors within 150 yd of the beach", "Your Observer, Oct 10–11 2024"], ["Sealer life within a mile of open water", "18 to 24 months", "Published Florida sealing-contractor experience; site practice"], ["Turtle season", "May 1 to Oct 31", "Sarasota County Ch. 54 Art. XXIII; Longboat Key Ch. 100"]], "Coastal facts used across this site"))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("", "Coastal Concrete & Paver Guide for Sarasota", "How Sarasota's water table, salt, heat, surge and rulebook affect concrete and pavers, with the surface temperature study, the salt guide, the storm season playbook, post-storm restoration and a maintenance calendar.",
              "Coastal hub: what the Gulf side does to hardscape, and the schedule that answers it", "Water table, salt, heat, surge and rules, each taken apart and turned into a maintenance date.", body, faq)


def salt():
    faq = [("How does salt air damage concrete near the Gulf?", "Chloride ions dissolved in spray, bay water and pool splash move into the concrete's pores with water. In the top paste they crystallize and expand as the surface dries, popping off scales; deeper, they reach reinforcing steel, strip its protective layer and start rust that expands and cracks the cover. Freeze isn't involved here; wetting and drying cycles are."),
           ("Which concrete resists it?", "A mix with a water-cement ratio at or below 0.45, 4,000 PSI or better, no water added at the truck, a proper 7-day cure, 2 inches of cover over steel, and a penetrating sealer after 28 days. Fiber instead of shallow mesh, and rebar on chairs."),
           ("Is spalling structural?", "On a slab, rarely; it's a surface problem until steel is involved. Rust bleeding through the surface is the sign that it has become one.")]
    body = facts([("Sources of chloride", "Gulf spray, bay and canal water, salt-chlorinated pools, surge"), ("Mechanism", "Crystallization in pores; corrosion of steel"), ("Defense", "w/c ≤ 0.45, cure, cover, penetrating sealer"), ("Stone", "Limestone (travertine, shellstone) flakes at the waterline")])
    body += cap("What does salt do to concrete and stone on the Sarasota coast?",
                "Salt gets into concrete as dissolved chloride carried by water: Gulf spray on the beach side, brackish canal and bay water, splash from salt-chlorinated pools, and surge. As the surface dries the salt crystallizes and expands in the pores, scaling off the top paste; if it reaches steel it starts rust that cracks the cover. Travertine and shellstone, being calcium carbonate, flake at a salt pool's waterline the same way.",
                p("The durability chapter of ACI 201 and the cover requirements of ACI 318 are the technical references; the practical defenses are a dense mix, a real cure, enough cover, and a sealer that keeps water out without trapping it."))
    body += sec("How far the salt reaches", table(["Exposure", "Where", "What it does first"], [["Direct spray", "Gulf-front rows, Longboat and Siesta beach side", "Scaling on any surface finished wet; sealer life 18 months"], ["Bay and canal", "Bird Key, Bay Isles, Country Club Shores, Gulf Cove, Placida", "Efflorescence, scaling at slab edges, rust on shallow mesh"], ["Salt pool", "Anywhere", "Coping and deck within 3 ft of the water; limestone flakes"], ["Surge", "Islands and bayfront in a storm", "Salt loaded into paver bases and slab voids"], ["Inland", "East of the Trail, Palmer Ranch, North Port", "Mostly none; irrigation minerals instead"]], "Salt exposure on the Sarasota coast"))
    body += sec("The mix and the cure", ol(["Water-cement ratio at or below 0.45; 4,000 PSI as the working strength.", "No water added at the truck; a plasticizer if the slump is low.", "Fiber for shrinkage; rebar on chairs at mid-depth with 2 inches of cover near salt.", "Finish without bleed water on the surface; overworking the paste brings water up and weakens the top.", "Cure 7 days with a compound or wet cure; the top inch is the inch that fights salt.", "Penetrating sealer after 28 days; reseal on the coastal cycle."]))
    body += sec("Stone and pavers", p("Concrete pavers are dense and sealed and handle salt well. Travertine and shellstone are calcium carbonate: salt crystallizing in their pores at a pool's waterline pushes the surface off in flakes, and acid cleaners dissolve them outright. The rule is a breathable penetrating sealer on the coping every year on a salt pool, a fresh-water rinse of the field, and neutral-pH cleaners only. Porcelain is immune."))
    body += sec("Related", cards([("/concrete/repair/", "Concrete repair", "Spalling and scaling repairs."), ("/pavers/travertine-shellstone/", "Travertine and shellstone", "Sealing discipline."), ("/coastal/maintenance-calendar/", "Maintenance calendar", "Intervals by distance.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("salt-and-concrete", "Salt and Concrete on the Sarasota Coast: Scaling & Spalling", "How chloride from Gulf spray, bays, salt pools and surge scales concrete and flakes limestone on the Sarasota coast, how far each exposure reaches, and the mix, cure, cover and sealer that slow it.",
              "Salt and concrete: how chloride gets in and what keeps it out", "Spray, bay water, salt pools and surge, and the dense mix, real cure and penetrating sealer that answer them.", body, faq)


def playbook():
    faq = [("Should I seal pavers before hurricane season?", "If they're due, yes, and finish by late May so the sealer cures before the rain pattern sets in. A fresh penetrating sealer keeps salt and silt out of the paver body; it doesn't hold the field down. What holds the field down is edge restraint and a full joint."),
           ("Can you pour concrete during hurricane season?", "Yes; June through November is half the year and most pours happen then. Pours are scheduled around the afternoon rain and, on the islands, not inside a named-storm watch window. A slab poured 48 hours before a surge is a slab poured for nothing.")]
    body = facts([("Season", "June 1 to November 30"), ("Worst weeks locally", "Mid-August to mid-October"), ("Recent events", "Ian 2022; Helene and Milton 2024"), ("First rule", "Photograph everything in May")])
    body += cap("What should hardscape owners do before June 1 on the Sarasota coast?",
                "Photograph every surface with a date stamp, including the edges and the pool coping; top up joint sand and reseal if due; check that edge restraint is concrete on any edge a surge can reach; make sure deck and yard drains run; and note where the survey pins are so a shifted field can be re-laid to the lot line. During a watch, move furniture and planters off pavers. After, follow the post-storm sequence before anyone touches the surface.",
                p("The 2024 season is the reference: Helene's 6.68-foot surge on Longboat Key on September 26 and Milton's landfall near Siesta Key on October 9 put most island hardscape under salt water twice in two weeks."))
    body += sec("Before the season (April and May)", ol(["Photograph every hardscape surface, close and wide, with the date; save to the cloud.", "Inspect edge restraint; replace spiked plastic with a concrete curb on seawall, street and Gulf-side edges.", "Re-sand joints to full depth; reseal with a penetrating product if due (18 to 24 months coastal).", "Clear deck drains, yard drains and swales; run a hose test.", "Sound the pool deck for hollows; a void now is a collapse in a surge.", "Locate the survey pins and photograph them.", "Keep the paver spares dry and stacked where they won't float."]))
    body += sec("During a watch (72 to 24 hours out)", ol(["Move furniture, planters, grills and loose pavers off the surface and indoors or strapped.", "Don't schedule a pour, a sealing or a polymeric sand install inside the window.", "Photograph again if the previous set is older than a month.", "Turn off irrigation so the base isn't saturated before the surge."]))
    body += sec("After (first 72 hours)", ol(["Photograph everything before moving anything; the insurer needs the untouched state.", "Don't pressure-wash; don't reset pavers; don't resurface. Let the base drain.", "Note the waterline height on walls and the direction the pavers moved.", "Rinse salt from concrete and stone surfaces with fresh water once the yard drains.", "File the claim with the photos and the pre-season set."]) + p(f'Then the {link("/coastal/post-storm-restoration/", "restoration sequence")} and the {link("/guides/hurricane-insurance-documentation/", "documentation guide")}.'))
    body += sec("Related", cards([("/coastal/post-storm-restoration/", "Post-storm restoration", "The sequence."), ("/pavers/repair-storm-restoration/", "Paver repair", "Lift, rebuild, reset."), ("/tools/pour-calendar/", "Pour calendar", "Month by month.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026", "Written after the 2024 season; updated after each season.")
    return pg("storm-season-playbook", "Storm Season Hardscape Playbook for Sarasota (June to November)", "What to do with pavers and concrete before June 1, during a hurricane watch and in the first 72 hours after surge on the Sarasota coast: photos, edge restraint, joints, drains, and the mistakes that cost the most after Helene and Milton.",
              "Storm Season Hardscape Playbook: before June 1, during a watch, and the first 72 hours after", "A checklist written after the 2024 season, for pavers and concrete on the Sarasota coast.", body, faq)


def post_storm():
    faq = [("What should I do with pavers that shifted during storm surge?", "Photograph, wait for the base to drain (one to three weeks), then lift the field where it's low or heaved, sound the base for voids, rebuild it in lifts, flush the salt, replace edge restraint with a concrete curb, rinse and reset the original pavers, and install polymeric sand on a dry day. Sealing waits until the surface is dry through."),
           ("What happens to a concrete driveway that sat under two feet of salt water?", "Usually nothing structural to the slab itself; the base under it is the question. Surge washes fines out from the edges and leaves voids; the slab sounds hollow and later cracks or drops. Sound it, fill voids with polyurethane foam, rinse the surface, and reseal. If it lifted or broke, it's a replacement."),
           ("Does beach sand pushed onto a paver driveway damage it?", "Not the pavers. The sand fills joints with fine, salty material that doesn't lock, and it can bury drains. Remove it, flush the joints, re-sand with polymeric sand once dry.")]
    body = facts([("First step", "Photographs before anything moves"), ("Wait", "1 to 3 weeks for the base to drain"), ("Never first", "Pressure washing, resetting, resurfacing"), ("Goal", "Reuse the pavers; rebuild the base")])
    body += cap("What is the right order after surge for pavers and concrete?",
                "Document, drain, diagnose, rebuild, reset, then sand and seal. Photographs before anything moves; one to three weeks for the base to drain; a hammer and a level to find voids and drops; the base rebuilt in lifts and flushed of salt; a concrete curb at any edge the water reached; the original pavers rinsed and reset; polymeric sand on a dry day and sealing when the surface is dry through. Slabs are sounded and foam-lifted or replaced on the same logic.",
                p("The mistakes that cost the most after the 2024 storms were pressure-washing salt into the base, resetting pavers on a saturated base that settled again, and resurfacing slabs that had voids under them."))
    body += sec("Pavers, step by step", table(["Step", "What", "Why"], [["1", "Photograph, then leave it", "Insurer and contractor need the untouched state"], ["2", "Wait 1 to 3 weeks", "A saturated base can't be compacted"], ["3", "Remove sand and debris by hand and shovel", "Pressure washing drives salt and fines into the base"], ["4", "Lift the field where it's low, heaved or shifted; stack and rinse the pavers", "Concrete and stone are reusable"], ["5", "Sound the base; dig out and rebuild voids in 3-in. lifts; flush with fresh water", "Salt in the base migrates up through the joints for years"], ["6", "Replace edge restraint with a concrete curb on exposed edges", "Spiked restraint floats"], ["7", "Re-screed bedding at 1 in.; reset to the survey line", "The lot line moved less than the pavers did"], ["8", "Polymeric sand on a two-day dry forecast", "Rain in the first day washes it"], ["9", "Seal when the surface is dry through (weeks)", "Sealing a damp base blushes white"]], "Post-surge paver restoration"))
    body += sec("Concrete slabs", ul(["Sound with a hammer across the whole slab; mark hollows.", "Check for lift, offset and cracks with a straightedge.", "Fill voids with polyurethane foam injection where the slab is sound; replace panels that broke or rocked.", "Rinse the surface with fresh water; reseal with a penetrating product after it dries.", "Never overlay or resurface a slab that hasn't been sounded."]))
    body += sec("Related", cards([("/pavers/repair-storm-restoration/", "Paver repair and storm restoration", "The service and its price range."), ("/concrete/repair/", "Concrete repair", "Lifting and replacement."), ("/guides/hurricane-insurance-documentation/", "Insurance documentation", "What to send the adjuster.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("post-storm-restoration", "Pavers & Concrete After Storm Surge: Restoration Sequence", "The order of work for pavers and concrete that stood in salt water on the Sarasota coast: document, drain, diagnose, rebuild the base, curb the edges, reset the original pavers, sand and seal, and the three mistakes that cost the most after 2024.",
              "Post-storm restoration: the sequence for pavers and slabs that stood in surge", "Document, drain, diagnose, rebuild, reset, then sand and seal. In that order.", body, faq)


def calendar():
    faq = [("What is a coastal maintenance calendar for pavers and concrete?", "A schedule of sealing, re-sanding, cleaning and inspection intervals set by distance from open water and by material: 18 to 24 months for sealer within half a mile, 2 years to two miles, 2 to 3 years inland; annual travertine coping sealing on salt pools; joint sand topped up when it drops a quarter inch; drains and edges checked every May."),
           ("How often do pavers need re-sanding near the coast?", "Full-depth polymeric joints last 8 to 12 years when installed right and drained; near the coast, spray and storms shorten that, so joints are inspected each May and topped up where they've dropped more than a quarter inch.")]
    body = facts([("Within 1/2 mile", "Seal every 18 to 24 months"), ("1/2 to 2 miles", "Every 2 years"), ("Inland", "Every 2 to 3 years"), ("Salt-pool coping (limestone)", "Annually")])
    body += cap("How often should coastal pavers and concrete be sealed, re-sanded and inspected?",
                "Seal every 18 to 24 months within half a mile of the Gulf or a bay, every 2 years out to two miles, and every 2 to 3 years inland; seal travertine or shellstone coping annually on a salt pool; top up polymeric joints when they drop a quarter inch; inspect edges, drains and hollows every May before storm season and again after any surge. Concrete slabs on coastal lots take a penetrating sealer on the same cycle.",
                p("Intervals reflect published Florida sealing experience and the site's practice; sun, salt, sprinkler water and traffic shorten them, shade lengthens them. The date on your care sheet overrides the table."))
    body += sec("By distance and material", table(["Material", "Within 1/2 mi", "1/2 to 2 mi", "Inland", "Notes"], [["Concrete pavers", "Seal 18 to 24 mo", "2 yrs", "2 to 3 yrs", "Re-sand as needed"], ["Travertine / shellstone field", "18 mo", "2 yrs", "2 to 3 yrs", "Neutral cleaners only"], ["Travertine / shellstone coping, salt pool", "Annually", "Annually", "Annually", "Rinse weekly"], ["Marble", "18 to 24 mo", "2 yrs", "2 to 3 yrs", "Penetrating sealer"], ["Porcelain", "None", "None", "None", "Clean"], ["Broom concrete", "Penetrating sealer 2 yrs", "3 yrs", "Optional", "Keep joints sealed"], ["Stamped / overlay", "18 mo", "2 yrs", "2 to 3 yrs", "Matte sealer with grit"]], "Sealing intervals by distance from open water"))
    body += sec("The year", table(["Month", "Task"], [["January to March", "Sealing season: dry, cool; book before crews fill"], ["April", "Inspect edges, joints, drains, hollows; photograph everything"], ["May", "Top up joints; finish any sealing by the end of the month; turtle lighting on by May 1 on the islands"], ["June to September", "Rinse salt splash weekly on salt pools; no sealing in the wet pattern; clear drains after storms"], ["October", "Post-storm inspection if any; sound decks"], ["November", "Reseal if due; owners returning"], ["December", "Plan next year's work; get on the calendar for January"]], "Coastal hardscape year"))
    body += sec("Related", cards([("/pavers/sealing/", "Sealing service", "What it includes and costs."), ("/compare/sealer-types-coastal/", "Sealer types", "Penetrating vs film."), ("/coastal/storm-season-playbook/", "Storm playbook", "The May checklist in detail.")]))
    body += faq_block(faq)
    body += reviewed("September 10, 2026")
    return pg("maintenance-calendar", "Coastal Hardscape Maintenance Calendar (Sarasota)", "Sealing, re-sanding, cleaning and inspection intervals for pavers, stone and concrete on the Sarasota coast by distance from the water and by material, plus a month-by-month year from sealing season to storm season.",
              "Coastal maintenance calendar: intervals by distance from the water", "Eighteen months on the Gulf, three years inland, once a year on a salt pool's coping, and a May inspection every year.", body, faq)


def temperature_study():
    data = {
        "name": "Sarasota Pool Deck Surface Temperature Study", "version": "0.1-protocol", "status": "methodology published; measurements pending",
        "publisher": "Sarasota Concrete (sarasotaconcrete.com)", "license": "CC BY 4.0", "published": "2026-09-10",
        "planned_measurement_dates": ["2027-01 (clear January day)", "2027-07 (clear July day)"],
        "location": "Sarasota, Florida (single site, samples side by side, full sun)",
        "instrument": "Calibrated infrared thermometer, emissivity set for masonry (~0.94), distance-to-spot per instrument spec; readings taken 3x per surface, median reported",
        "times_local": ["10:00", "14:00", "17:00"],
        "conditions_recorded": ["air temperature (shaded)", "sky condition", "wind", "surface dry/wet", "time since last rain", "sample color (light/medium/dark)"],
        "surfaces": [
            {"id": "concrete-gray-broom", "name": "Gray broom-finished concrete", "color": "medium"},
            {"id": "concrete-light-broom", "name": "Light (white cement) broom-finished concrete", "color": "light"},
            {"id": "cool-deck-overlay", "name": "Light textured cementitious overlay (cool deck type)", "color": "light"},
            {"id": "paver-gray", "name": "Gray concrete paver", "color": "medium"},
            {"id": "paver-light", "name": "Light-blend concrete paver", "color": "light"},
            {"id": "travertine-tumbled", "name": "Tumbled travertine, light", "color": "light"},
            {"id": "shellstone", "name": "Shellstone", "color": "light"},
            {"id": "marble-honed", "name": "Honed marble, white/cream", "color": "light"},
            {"id": "porcelain-2cm", "name": "2 cm porcelain paver, light", "color": "light"},
        ],
        "readings": [],
        "note": "No temperature values are published until measured. Third-party claims (e.g., 20-35 F differences between light stone and dark concrete) are not reproduced here as data.",
    }
    DATA.mkdir(exist_ok=True)
    (DATA / "surface-temperatures.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
    faq = [("Which pool deck surface stays coolest barefoot in Sarasota in July?", "This site will answer with its own measurement in July 2027 and won't guess before then. The physics says light, porous surfaces (tumbled travertine, shellstone) will read lowest and dark dense surfaces (charcoal pavers, gray concrete) highest, with light concrete, light pavers and porcelain between. The comparison page explains why; the numbers arrive with the study."),
           ("How hot does a gray concrete pool deck get at 2 p.m. in August in Sarasota?", "Unmeasured locally, which is why this study exists. Published claims from other parts of Florida put gray concrete well above 130 degrees on a 95-degree afternoon; those are not reproduced here as data."),
           ("Why not just quote the manufacturer numbers?", "Because they're measured elsewhere, under conditions that aren't stated, by people selling the product. A Sarasota reading with the instrument, time, sky and air temperature recorded is worth more than a hundred of them.")]
    body = facts([("Surfaces", "9"), ("Times", "10 a.m., 2 p.m., 5 p.m."), ("Days", "One clear July day, one clear January day"), ("Instrument", "Calibrated infrared thermometer"), ("Status", "Protocol published; readings pending")])
    body += cap("What is the Sarasota Pool Deck Surface Temperature Study?",
                "A side-by-side measurement of nine pool deck surfaces (gray and light broom concrete, a cool-deck overlay, gray and light concrete pavers, tumbled travertine, shellstone, honed marble and 2 cm porcelain) with a calibrated infrared thermometer at 10 a.m., 2 p.m. and 5 p.m. on one clear July day and one clear January day in Sarasota, with air temperature, sky, wind and surface condition recorded. The protocol is published now; the readings are published the day they exist.",
                p("Measurement dates are set for January 2027 and July 2027. The results go on this page as a table and to /api/surface-temperatures.json under a CC BY 4.0 license, and the comparison pages and the surface selector will switch from physics-based ordering to measured values."))
    body += sec("Protocol", ol(["Samples of each surface, minimum 12 by 12 inches, laid side by side on the same compacted base in full sun, dry, at least 48 hours after rain.", "Infrared thermometer with emissivity set for masonry (about 0.94), held at the instrument's specified distance, perpendicular to the surface.", "Three readings per surface per time, taken within two minutes; the median is recorded.", "Shaded air temperature, sky condition, wind and time since last rain recorded at each session.", "Sessions at 10:00, 14:00 and 17:00 local time.", "One clear day in July and one in January; if clouds interrupt, the session is repeated on the next clear day.", "Raw readings, medians and conditions published as JSON; nothing averaged across days."]))
    body += sec("Surfaces", table(["Surface", "Color class", "Why it's in the study"], [[s["name"], s["color"], ""] for s in data["surfaces"]], "Nine surfaces; the third column is filled with the reading table when measurements exist"))
    body += sec("What the physics predicts (not data)", p(f'Solar reflectance and thermal mass explain most of the difference between surfaces in the sun: light colors reflect more, porous stone sheds heat and holds a little moisture, thin dense tile heats and cools fast. The {link("/compare/pool-deck-surfaces-heat/", "surfaces and heat comparison")} lays out the expected order and labels it as expected. Manufacturer and blog claims of 20 to 35 degree differences are not reproduced here as measurements.'))
    body += sec("Results", note("Pending. First session planned for January 2027; second for July 2027. This block becomes the results table on the day of the first session.", "warn"))
    body += sec("Download", p(link("/api/surface-temperatures.json", "surface-temperatures.json") + " (protocol now; readings when measured; CC BY 4.0)."))
    body += faq_block(faq)
    body += reviewed("September 10, 2026", "Protocol published; no readings yet.")
    schema = [dataset_schema("Sarasota Pool Deck Surface Temperature Study", "Side-by-side infrared surface temperatures of nine pool deck materials in Sarasota, Florida at 10 a.m., 2 p.m. and 5 p.m. on a July and a January day. Protocol published September 2026; readings pending.", "/coastal/pool-deck-surface-temperature-study/", "/api/surface-temperatures.json", "2026-09-10", ["pool deck temperature", "travertine", "pavers", "Sarasota", "surface heat"])]
    return pg("pool-deck-surface-temperature-study", "Sarasota Pool Deck Surface Temperature Study (Protocol)", "A published protocol for measuring nine pool deck surfaces in Sarasota with an infrared thermometer at 10 a.m., 2 p.m. and 5 p.m. on a July and a January day: surfaces, instrument, conditions, timing, and a JSON dataset that fills with readings when measured.",
              "Sarasota Pool Deck Surface Temperature Study: the protocol, published before the numbers", "Nine surfaces, three times, two seasons, one thermometer. No temperature is quoted here until it's been measured.", body, faq, schema)


def get_pages():
    return [hub(), salt(), playbook(), post_storm(), calendar(), temperature_study()]
