# -*- coding: utf-8 -*-
"""FAQ hub and five topic pages. Each topic page answers questions not answered elsewhere on the site and indexes
the canonical answers that live on other URLs, so no question has two canonical answers."""
import csv, pathlib
from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, link, ext, facts, cards, esc

Q_CSV = pathlib.Path(__file__).resolve().parent.parent / "research" / "06-150-questions.csv"


def question_index():
    rows = list(csv.DictReader(Q_CSV.open(encoding="utf-8")))
    groups = {}
    for r in rows:
        groups.setdefault(r["owner_url"], []).append(r)
    out = []
    for url in sorted(groups):
        qs = groups[url]
        out.append(f'<div class="qa"><h3>{esc(url)}</h3><ul>' + "".join(f'<li>{link(url, esc(q["question"]))} <span class="pill">{esc(q["evidence"])}</span></li>' for q in qs) + "</ul></div>")
    return f"<p>{len(rows)} questions gathered in the research phase, each answered once on the page that owns it. The tag shows the evidence class behind the question (VOLUME: measured search demand; COMPETITOR: asked or answered by a local competitor; EXPERT-GAP: gap found in the audit).</p>" + "".join(out)



def pg(slug, title, meta, h1, lede, body, faq):
    return {"route": f"/faq/{slug}/" if slug else "/faq/", "title": title, "meta_description": meta, "h1": h1, "kicker": "FAQ", "lede": lede,
            "breadcrumbs": [("Home", "/"), ("FAQ", "/faq/"), (h1.split(":")[0][:40], None)] if slug else [("Home", "/"), ("FAQ", None)],
            "body_html": body, "faq": faq}


def index(items):
    return ul([f'{link(u, q)}' for q, u in items])


def hub():
    faq = [("Why are the FAQs split by topic instead of one long page?", "Because a question deserves one canonical answer on one URL. The topic pages here answer the questions that don't belong to a service, permit or comparison page, and index the ones that do, so you land on the full answer rather than a summary of it."),
           ("Where do the answers come from?", "From the county and city codes, FEMA, FWC, USDA and NOAA for anything regulatory or physical; from published Sarasota-area pricing on a stated date for costs; and from the provider's practice for how the work is done. Each topic page lists its sources."),
           ("Can I ask a question that isn't here?", "Yes. Real questions from calls and the form are answered weekly on Ask the Estimator and, when they earn it, get a page of their own.")]
    body = p("Five topic pages, each with its own questions and an index of the canonical answers elsewhere on the site.")
    body += cards([("/faq/concrete/", "Concrete", "Mix, thickness, joints, cure, color, repair."), ("/faq/pavers/", "Pavers", "Base, patterns, sand, sealing, weeds, storm damage."), ("/faq/pool-decks/", "Pool decks", "Heat, slip, salt pools, resurfacing, condo decks."), ("/faq/permits-hoa-flood/", "Permits, HOA and flood", "Offices, exemptions, ARC packets, the 50% rule, turtle lighting."), ("/faq/cost/", "Cost", "Ranges, what moves them, deposits, estimates."), ("/guides/ask-the-estimator/", "Ask the Estimator", "Real questions answered weekly.")])
    body += faq_block(faq, "About this FAQ")
    body += sec("Every question this site answers, by page", question_index())
    body += reviewed("September 10, 2026")
    return pg("", "FAQ: Concrete, Pavers, Pool Decks, Permits & Cost in Sarasota", "Sarasota Concrete's FAQ, split into concrete, pavers, pool decks, permits and HOA and flood, and cost, with each question answered once on one canonical page and indexed here.",
              "Concrete and pool deck questions Sarasota homeowners ask, answered once each", "Five topic pages and an index of every canonical answer on the site.", body, faq)


def concrete():
    faq = [("Can concrete be poured on a Sarasota lot in the rainy season?", "Yes, in the morning, with the forecast checked the night before and plastic on the truck. Pours here run from 7 a.m. and are finished and covered by early afternoon from June through September."),
           ("How soon can a screen cage go back on a new slab?", "Seven days for anchors into a 4-inch slab; the edge beam or curb along the cage line is poured with the deck so the anchors have steel behind them."),
           ("Why does the estimate say 4,000 PSI when the code says 3,000?", "Because 3,000 is the minimum and 4,000 finishes better in heat, scales less near salt and costs a few dollars a yard more. It's a working standard here, not a code requirement."),
           ("Will the new slab match my old slab's texture?", "The finish can be matched (broom direction and coarseness); the color won't be exact. Plan the joint between old and new as a straight line, not a patch."),
           ("What is a proof roll?", "Driving a loaded truck or roller over the subgrade before the base goes down to find soft spots; on Myakka sand it's how a contractor finds the wet pocket that would have become a settled panel."),
           ("Do I need to water new concrete?", "Not if a curing compound was applied; if the crew wet-cures, the slab is kept damp for 7 days with burlap or sprinklers on a timer. Letting it dry out in the first week is the most common owner-caused defect."),
           ("Can concrete be tinted after it's poured?", "Stained, yes: acid or water-based stains change the color permanently; paints and coatings peel. Integral color at the pour is more even."),
           ("Are there concrete trucks small enough for Siesta Key streets?", "Mini-mixers and pump trucks handle the keys' narrow streets and weight-limited bridges; the estimate says which is planned and whether a pump adds cost.")]
    idx = [("How thick should residential concrete be in Sarasota County?", "/concrete/#faq"), ("Should a Sarasota driveway be 4 or 6 inches?", "/compare/4-inch-vs-6-inch/"), ("Rebar, wire mesh or fiber?", "/compare/rebar-vs-fiber/"), ("Why does concrete crack in Sarasota?", "/guides/why-concrete-cracks-sarasota/"), ("What happens if it rains on my pour?", "/guides/cure-times-and-rain/"), ("How long before I can drive on a new driveway?", "/guides/cure-times-and-rain/"), ("Why is my new driveway a different color in patches?", "/concrete/driveways/#faq"), ("Can a cracked driveway be repaired or must it be replaced?", "/concrete/repair/#faq"), ("Does slab lifting work on sandy soil?", "/concrete/repair/#faq"), ("What is spalling?", "/concrete/repair/#faq"), ("Can an overlay fix a spalled pool deck?", "/concrete/resurfacing/#faq"), ("What is the best month to pour concrete in Sarasota?", "/tools/pour-calendar/")]
    body = faq_block(faq, "Concrete questions answered here") + sec("Canonical answers on other pages", index(idx)) + reviewed("September 10, 2026")
    return pg("concrete", "Concrete FAQ for Sarasota Homeowners", "Concrete questions from Sarasota County homeowners: rainy-season pours, cage anchors, 4,000 PSI, matching old slabs, proof rolls, curing, staining and island access, plus an index of canonical answers on thickness, reinforcement, cracks and repair.",
              "Concrete FAQ: the questions that don't belong to one service page", "Eight answers here, twelve pointers to where the full answer lives.", body, faq)


def pavers():
    faq = [("Why do my new pavers have a white haze?", "Efflorescence: soluble salts carried to the surface by water in the first weeks. It's harmless and mostly washes out; sealing over it traps it. The efflorescence guide has the timeline."),
           ("What pattern should a pool deck use?", "Running bond or a modular pattern for stone and large pavers; herringbone isn't needed without vehicle loads. Driveways are herringbone."),
           ("Do pavers need edge restraint on a lanai under a cage?", "Yes, but a spiked plastic restraint on the base is fine there because nothing can lift it; concrete curbs go where the cage anchors land and on any edge the water can reach."),
           ("Can old pavers be reused in a new layout?", "Usually. Concrete and stone pavers are lifted, rinsed and stacked; the base is rebuilt; the same units go back in the new pattern with new polymeric sand. Expect 5 to 10 percent breakage."),
           ("Why did the pavers along my seawall lift?", "Surge or high tide got under a plastic restraint set in bedding sand and floated it, then the field followed. The fix is a concrete curb on the base."),
           ("How much slope do pavers need?", "1/8 inch per foot away from the house, same as concrete, and toward a drain under a cage."),
           ("Are clay brick pavers a good idea here?", "For walks and patios in traditional neighborhoods west of the Trail, yes. Fewer vehicular sizes and colors; they handle salt well and don't fade."),
           ("Can pavers go directly on sand?", "On sand alone, no. On 1 inch of bedding sand over a compacted crushed base, yes. Pavers on raw sand is why so many Gulf Gate patios roll like waves.")]
    idx = [("What base do pavers need on a high water table?", "/pavers/#faq"), ("Base depth for driveway pavers", "/pavers/driveways/#faq"), ("How long does a paver driveway last in Florida?", "/pavers/driveways/#faq"), ("Are permeable pavers strong enough for a driveway?", "/guides/permeable-pavers-impervious-limit/"), ("What is polymeric sand and when is it replaced?", "/guides/polymeric-sand-weeds-ants/"), ("Why do weeds and ants keep coming back?", "/guides/polymeric-sand-weeds-ants/"), ("What is efflorescence?", "/guides/efflorescence/"), ("How often are pavers sealed near the Gulf?", "/pavers/sealing/#faq"), ("Why did my sealer peel or turn white?", "/pavers/sealing/#faq"), ("What makes pavers sink?", "/pavers/repair-storm-restoration/#faq"), ("What to do with pavers after storm surge", "/coastal/post-storm-restoration/"), ("When can pavers go over a lanai slab?", "/pavers/patios-lanais/#faq"), ("Rust stains from well water", "/guides/well-water-rust-stains/")]
    body = faq_block(faq, "Paver questions answered here") + sec("Canonical answers on other pages", index(idx)) + reviewed("September 10, 2026")
    return pg("pavers", "Paver FAQ for Sarasota Homeowners", "Paver questions from Sarasota County: white haze on new pavers, patterns, edge restraint under a cage, reusing pavers, seawall lift, slope, clay brick and sand-only installs, plus an index of canonical answers on base, sealing, sinking and storms.",
              "Paver FAQ: the questions that don't belong to one service page", "Eight answers here, thirteen pointers to the full answers.", body, faq)


def pool_decks():
    faq = [("Should a pool deck be sloped toward or away from the pool?", "Away, at 1/8 inch per foot, to deck drains or the edge, never toward the water. A deck that drains into the pool carries dirt and fertilizer with it and floods the coping; over a 10-foot run that slope is 1.25 inches of fall."),
           ("What is coping and does it have to match the deck?", "The finished edge at the pool beam, usually bullnose. It can match (travertine deck, travertine coping) or contrast (light concrete pavers, porcelain coping). It's mortar-set with a flexible joint to the field either way."),
           ("Can the deck be extended beyond the cage?", "Yes; the extension is a patio on its own base outside the cage, matched in material, with the cage base line kept intact."),
           ("How do I keep a light-colored deck clean?", "Rinse weekly, a neutral (pH 7) cleaner, a soft brush on stone, a controlled pressure wash under 1,500 PSI with a wide fan tip on concrete pavers, and a penetrating sealer renewed every 18 to 36 months so stains sit on top instead of in the pore."),
           ("Does a screened deck still get hot?", "Less; screen cuts some sun and shade cloth cuts more. Color still matters under a cage in the afternoon."),
           ("What about a deck for an above-ground spa?", "A 6-inch reinforced pad under the spa, tied into the deck with an isolation joint."),
           ("Is a paver deck safe for a pool cage in a hurricane?", "The cage anchors go into a concrete curb or edge beam along the cage line, not into pavers or joints. That's true for every paver deck here."),
           ("Can you match my neighbor's travertine?", "Travertine varies by quarry lot; a similar color and finish, yes; an exact match, only if the same lot is still available.")]
    idx = [("Which pool deck surface stays coolest in July?", "/coastal/pool-deck-surface-temperature-study/"), ("What drives heat and the slip rating to demand", "/compare/pool-deck-surfaces-heat/"), ("Travertine vs concrete pavers", "/compare/travertine-vs-concrete-pavers/"), ("Travertine vs shellstone vs porcelain", "/compare/travertine-vs-shellstone-vs-porcelain/"), ("Resurface or replace: six tests", "/compare/resurface-vs-replace-pool-deck/"), ("Cool deck vs pavers", "/compare/cool-deck-vs-pavers/"), ("Does a salt pool damage travertine coping?", "/pavers/travertine-shellstone/#faq"), ("Are marble pavers slippery when wet?", "/pavers/marble-porcelain/#faq"), ("How thick should a concrete pool deck be?", "/concrete/pool-decks/#faq"), ("Condo pool deck replacement", "/hoa/barrier-island-condos/"), ("Pool deck costs by material", "/pricing/pool-decks/")]
    body = faq_block(faq, "Pool deck questions answered here") + sec("Canonical answers on other pages", index(idx)) + reviewed("September 10, 2026")
    return pg("pool-decks", "Pool Deck FAQ for Sarasota Homeowners", "Pool deck questions from Sarasota County: slope, coping, extending past the cage, cleaning light decks, screened heat, spa pads, cage anchors in a hurricane and matching travertine, plus an index of the heat study, comparisons and cost guide.",
              "Pool deck FAQ: the questions that don't belong to one page", "Eight answers here, eleven pointers to the full answers.", body, faq)


def permits():
    faq = [("Is there a fee to look up permits on my property?", "No. Sarasota County's permit search, the City of Sarasota's FTG portal, Venice's eTRAKiT and North Port's Click2Gov are public; Charlotte County's records are online too."),
           ("Can a contractor start before the permit is issued?", "Demolition and layout sometimes, the regulated work never. In Charlotte County the Notice of Commencement has to be recorded before the first inspection."),
           ("What if my HOA approves something the county won't permit?", "The permit wins; you'll need to change the design and go back to the committee. Submitting both at once catches that early."),
           ("Do I need a survey?", "For anything at a lot line, in a setback, or in an ARC packet, yes; the survey from your closing usually works. For a like-for-like pool deck inside a cage, a site sketch is often enough."),
           ("Does the county inspect a driveway?", "Right-of-way work is inspected by the county or city (line and grade, culvert, swale). Private flatwork inspections depend on the permit type; Charlotte County lists them on the job card."),
           ("What is a coastal setback variance and how long does it take?", "County Commission approval to build seaward of the Gulf Beach Setback Line, after staff review and a public hearing. Months, not weeks, and not guaranteed."),
           ("Is elevation certificate needed for a pool deck?", "Not for site work by itself; it's needed when the building's flood compliance is in play, and Longboat Key may ask for it in a substantial-improvement file."),
           ("Can I get the permit history of a house before I buy?", "Yes, from the portals above by address. Unpermitted pool decks and driveways show up as gaps.")]
    idx = [("Which office issues the permit for my address?", "/permits/"), ("Sarasota County rules", "/permits/sarasota-county/"), ("City of Sarasota rules", "/permits/city-of-sarasota/"), ("Venice rules", "/permits/venice/"), ("North Port rules", "/permits/north-port/"), ("Longboat Key rules", "/permits/longboat-key/"), ("Charlotte County rules", "/permits/charlotte-county/"), ("Flood zones, the 50% rule and the setback line", "/permits/flood-zones-50-percent-rule/"), ("Sea turtle lighting", "/permits/sea-turtle-lighting/"), ("What goes in an ARC packet", "/hoa/"), ("Palmer Ranch review", "/hoa/palmer-ranch/"), ("Wellen Park review", "/hoa/wellen-park/"), ("The 50% impervious cap and permeable pavers", "/guides/permeable-pavers-impervious-limit/"), ("Verifying a contractor's license", "/guides/verify-contractor-license-sarasota/")]
    body = faq_block(faq, "Permit, HOA and flood questions answered here") + sec("Canonical answers on other pages", index(idx)) + reviewed("September 10, 2026")
    return pg("permits-hoa-flood", "Permit, HOA & Flood FAQ for Sarasota Hardscape", "Permit, HOA and flood questions from Sarasota County: permit lookups, starting before issuance, HOA vs county conflicts, surveys, inspections, coastal setback variances, elevation certificates and permit history, plus an index of every jurisdiction page.",
              "Permit, HOA and flood FAQ: the questions between the office pages", "Eight answers here, fourteen pointers to the office and rule pages.", body, faq)


def cost():
    faq = [("Does the estimate include the permit fee?", "It states who pays it and passes it through at cost; fees range from $22 to a few hundred dollars, with Charlotte County's $310 line-and-grade fee at the top."),
           ("Is a per-square-foot price the right way to compare?", "Only with the same scope. Base depth, thickness, demolition, drains and permits move the per-foot number by half; compare line items."),
           ("Why is the small pad so expensive per foot?", "Mobilization: the truck, the crew and the setup cost the same for 40 square feet as for 600."),
           ("Do prices change if I'm on an island?", "Five to fifteen percent for bridge timing, staging on small lots and salt-resistant materials."),
           ("Will the price hold if I wait until next season?", "Material prices move; a written estimate states how long it's valid, usually 30 days."),
           ("Does resurfacing always save money?", "No; on a failed slab it costs more because the replacement follows. The six tests decide."),
           ("Is there a minimum job?", "Cleaning and sealing companies quote $150 to $250 minimums; small concrete pads are priced as mobilization plus material rather than per foot."),
           ("How does financing change the total?", "Interest, when a partner is in place. Until then, a deposit and progress payments under Florida's rules.")]
    idx = [("All planning ranges", "/pricing/"), ("Concrete cost guide", "/pricing/concrete/"), ("Paver cost guide", "/pricing/pavers/"), ("Pool deck cost guide", "/pricing/pool-decks/"), ("Sarasota Concrete Cost Index", "/pricing/sarasota-concrete-cost-index/"), ("Why quotes differ by thousands", "/pricing/#faq"), ("Deposits and warranties", "/guides/deposits-and-warranties/"), ("Concrete vs paver driveway over 20 years", "/compare/concrete-vs-pavers-driveway/"), ("Calculator", "/tools/concrete-paver-calculator/"), ("Financing", "/financing/")]
    body = faq_block(faq, "Cost questions answered here") + sec("Canonical answers on other pages", index(idx)) + reviewed("September 10, 2026")
    return pg("cost", "Cost FAQ: Concrete & Paver Prices in Sarasota", "Cost questions from Sarasota County homeowners: permit fees in the estimate, comparing per-square-foot prices, small-pad pricing, island premiums, price validity, resurfacing savings, minimums and financing, plus an index of every cost guide.",
              "Cost FAQ: the questions between the price tables", "Eight answers here, ten pointers to the cost guides and the index.", body, faq)


def get_pages():
    return [hub(), concrete(), pavers(), pool_decks(), permits(), cost()]
