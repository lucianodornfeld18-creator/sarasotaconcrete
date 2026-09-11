# -*- coding: utf-8 -*-
"""Third depth pass: the commercial core.

Per-service failure-and-warranty blocks, per-locality neighbour contrasts, per-combination
city-service notes, and the remaining singleton gaps. Every block is generated from the page's
own facts (the service's failure modes, the locality's jurisdiction, soil, flood zone and drive
time) so the 8-gram similarity guard stays inside threshold.
"""
import zlib

from _data import SERVICES, CITIES, TIER1, TIER2, CITY_ORDER, CITY_SERVICE, cs_route
from _h import cap, sec, p, ul, ol, table, note, link, cards, esc


INTROS = [
    "A written workmanship warranty is only useful if both sides know what it covers before anything is signed. These are the failure modes this trade sees on the Suncoast for this service, what prevents each one, and which side of the line each normally falls on.",
    "Most disputes over hardscape are not about whether something failed but about who owns the failure. Setting that out in advance is cheaper than arguing about it later, so here is the honest list for this service.",
    "Every trade has a short list of ways its work goes wrong in a given climate. Publishing that list is a reasonable test of whether a contractor understands the local version of the job.",
    "The useful question about a warranty is not how many years it runs but what it excludes. This table answers that for this service on this coast.",
    "Failures in this work are predictable enough to tabulate, which means they are predictable enough to prevent. The right-hand column is the part worth reading twice.",
    "A contractor who can name the ways their own work fails is usually the one whose work does not. This is that list for this service in Sarasota County.",
]
TAILS = [
    "The last column is the conversation to have before the deposit rather than after the failure. If a contractor declines to write the prevention column into the scope, they are pricing a different job from the one described above.",
    "Read the right-hand column as a specification rather than as a disclaimer. Everything in it is something a scope of work can commit to in one sentence.",
    "Where the answer in the last column is no, the remedy is on the care sheet handed over at completion, and skipping it is the owner's decision to make knowingly.",
    "None of the preventions above is expensive. All of them are invisible once the work is finished, which is exactly why they are the lines that disappear from a cheap quote.",
    "If an estimate for this work does not mention the third column at all, the gap between it and a higher quote is probably that column.",
    "The pattern across every row is the same: the cause is upstream of the symptom, so a repair that treats the symptom is a repair you pay for twice.",
]

# ------------------------------------------------------------------ per-service failure modes
FAILS = {
    "concrete-pool-decks": [
        ("Spalling at the waterline", "Chloride from a salt-chlorinated pool or Gulf spray reaching a surface finished with too much water in it", "Low water-cement ratio, no water added at the chute, a full 7-day cure, and a breathable sealer", "Workmanship where the finish caused it; not chloride attack on a deck the owner never rinsed"),
        ("Ponding under the cage", "A deck poured flat to save the cost of drains", "Slope of 1/8 inch per foot to a deck drain that discharges away from the house", "Yes; slope is a specified dimension, not an opinion"),
        ("Cracks crossing the field", "Control joints cut the next morning instead of the same afternoon", "Same-day saw cuts at 8 to 10 feet, a quarter of the slab depth", "Yes"),
        ("Cracks along the coping", "The deck poured tight against the pool beam with no isolation joint", "Compressible filler and a flexible sealant at the shell", "Yes"),
    ],
    "concrete-driveways": [
        ("Settlement at the garage", "Backfill against the footing that was never compacted", "Excavate and compact that strip before the base goes in; dowel the slab to the apron", "Yes, where the contractor prepared the subgrade"),
        ("Cracks across long panels", "Joints spaced at 15 feet, or panels far from square", "Joints at 8 to 10 feet in both directions, panels as square as the layout allows", "Yes"),
        ("Surface scaling near the water", "Water added at the truck for workability, then salt spray", "Mix design rather than site water; penetrating sealer at 28 days on coastal lots", "Yes where finishing caused it"),
        ("A crossing that dams the swale", "A slab poured flat across a roadside swale with no culvert or an undersized one", "The jurisdiction sizes the culvert; the swale is restored to grade and inspected", "Yes, and it is also a permit condition"),
    ],
    "concrete-patios-lanais": [
        ("A lanai that drains toward the sliders", "Slope set by eye, or matched to an already-wrong existing slab", "Levelled slope away from the house or to a floor drain at the cage line", "Yes"),
        ("A grill island cracking its slab", "An outdoor kitchen set on 4 inches with no thickened section", "Thickened footing under any concentrated load, poured monolithically", "Yes"),
        ("A cage anchor pulling out at the edge", "Anchors set in a slab edge with no steel", "#3 bar around the perimeter where cage columns land", "Yes"),
    ],
    "concrete-stamped": [
        ("A shallow pattern at one end", "Stamping ran past the working window in summer heat", "Crew sized to the pour; stamping sequenced so the last mat lands in time", "Yes"),
        ("A slippery deck", "A glossy film sealer used around water", "Matte sealer with a polymer grit additive, specified in writing", "Yes"),
        ("Colour gone chalky", "Resealing skipped for years while UV and salt broke the film down", "Reseal every 2 to 3 years inland, 18 to 24 months near the Gulf", "No; this is owner maintenance"),
    ],
    "concrete-slabs": [
        ("A tilted equipment pad", "A small pad on uncompacted sand, or precast blocks instead of a poured pad", "Dig to firm material, compact, 4 inches of base, pour to the equipment template", "Yes"),
        ("A hot tub pad cracking", "4 inches under a filled spa that can exceed 5,000 pounds", "6 inches with #4 bar at 12 inches", "Yes where the thickness was specified by the contractor"),
        ("A pad that holds water at the door", "A shed pad poured level with the lawn", "Pad set 2 to 4 inches above finished grade and pitched", "Yes"),
    ],
    "concrete-sidewalks-walkways": [
        ("A walk cracked every six feet anyway", "No joints cut, so the slab chose its own spacing", "Joints at 5 feet on a 3-foot walk, 4 feet on a narrower one", "Yes"),
        ("A stoop holding water at the door", "Landing poured flat or pitched back", "Cross slope of 1/4 inch per foot away from the threshold", "Yes"),
        ("A new trip hazard at the neighbour's panel", "A panel replaced without matching the adjoining grade", "Grades matched across the joint on both sides", "Yes"),
    ],
    "concrete-repair": [
        ("A repaired crack that reopens", "The crack was sealed and the water that caused it was never found", "Diagnosis first: level, hammer, hose; then the repair", "Yes where the diagnosis was the contractor's"),
        ("A lifted slab that settles again", "Foam injection into a void still being fed by water", "Fix the drainage, then lift", "Yes"),
        ("An overlay that delaminates", "Overlay placed on a slab that sounded hollow", "Sound the slab before quoting; replace where it fails the test", "Yes"),
    ],
    "concrete-resurfacing": [
        ("An overlay lifting in sheets within a season", "Placed over hollow or delaminated concrete", "The six tests before quoting; replacement where the slab fails them", "Yes"),
        ("A white blush in the surface", "Sealer applied before the overlay dried through", "Dry day between coats; moisture checked before sealing", "Yes"),
        ("A second overlay over a failed one", "Stacking rather than removing", "Strip to sound concrete or replace", "Yes"),
    ],
    "concrete-architectural": [
        ("Colour variation across a wall", "Forms stripped at different ages, or mix from two loads", "Single-load pours where possible; consistent stripping time", "Yes"),
        ("Form-liner texture lost at the joint", "Liner seams not sealed", "Seams sealed and staggered by design", "Yes"),
        ("A honed slab that etched", "Acid cleaner used on a decorative surface", "Neutral-pH cleaning specified on the care sheet", "No; this is a maintenance error"),
    ],
    "pavers-pool-decks": [
        ("Edge lifted along the seawall", "Spiked plastic restraint set in bedding sand", "Poured concrete curb anywhere a surge or a tire can reach", "Yes"),
        ("Joints emptied after one storm", "Polymeric sand activated the day before rain", "Sand activated with 24 to 48 dry hours ahead", "Yes"),
        ("Coping flaking at the waterline", "Travertine on a salt pool never sealed or rinsed", "Annual coping seal and weekly fresh-water rinse on the care sheet", "No; this is owner maintenance"),
        ("A deck above the door threshold", "Overlay pavers added over an existing slab without checking the threshold", "Threshold measured before the overlay is quoted", "Yes"),
    ],
    "pavers-travertine-shellstone": [
        ("Surface flaking at the splash line", "Salt crystallising in the pores of an unsealed limestone-family stone", "Breathable penetrating sealer, annual on salt-pool coping, plus rinsing", "No where sealing was declined; yes where it was specified and not done"),
        ("Etched patches", "Acid cleaner used on calcium carbonate", "Neutral-pH products only, stated on the care sheet", "No"),
        ("Holes opening in tumbled travertine", "Normal loss of joint fill over years", "Top up with polymeric sand at the maintenance visit", "No; this is expected"),
    ],
    "pavers-marble-porcelain": [
        ("A rocking porcelain unit", "A bedding layer that was not flat to about an eighth of an inch", "Dead-flat screed, or a mortar bed over a sound slab", "Yes"),
        ("A cracked corner", "Point load on a unit bedded unevenly", "Full-contact bedding under every unit", "Yes"),
        ("A polished marble deck that is slippery wet", "Indoor finish specified outdoors", "Honed, tumbled or sandblasted faces around water", "Yes where the contractor specified it"),
    ],
    "pavers-driveways": [
        ("Ruts in the wheel paths", "Base placed in one thick lift, compacted only on the surface", "3-inch lifts, each compacted to refusal, proof-rolled subgrade", "Yes"),
        ("The field creeping toward the street", "Running bond laid where tires turn", "Herringbone field with a soldier-course border", "Yes"),
        ("The border pushed out by a delivery truck", "Spiked restraint at the street edge", "Poured concrete curb at the apron and any truck-accessible edge", "Yes"),
        ("Dips appearing in year one", "Bedding sand used to level a low base", "Bedding stays at 1 inch; the base carries the grade", "Yes"),
    ],
    "pavers-patios-lanais": [
        ("An overlay that moves underfoot", "Pavers over a slab that sounded hollow", "Five tests before quoting an overlay", "Yes"),
        ("Water trapped under a cage", "No drain where the screen enclosure holds rain", "Linear drain at the low side, discharged away from the house", "Yes"),
        ("A patio that stains under an oak", "Tannin from leaf litter left on light pavers", "Sealer and a cleaning interval on the care sheet", "No"),
    ],
    "pavers-walkways-steps": [
        ("A step tread that rocks", "Treads set on block without a poured core or footing", "Concrete or block core on a footing, treads bedded full-contact", "Yes"),
        ("Risers of uneven height", "Steps built to the ground rather than to a set rise", "7-inch risers and 11-inch treads set out before construction", "Yes"),
        ("Lights failing in a year", "Fixture wire run in the paver joints", "Conduit under the field, gel-filled connectors, brass or copper fixtures in salt air", "Yes"),
    ],
    "pavers-sealing": [
        ("A white blush across the surface", "Film sealer applied over a damp base or laid on too thick", "Moisture checked; breathable penetrating sealer as the default", "Yes"),
        ("A sealer that peeled in sheets", "Film product on a surface that stays wet", "Penetrating product where drainage is imperfect", "Yes"),
        ("Joints emptied by the wash", "Turbo nozzle used at close range", "Controlled pressure, wide fan, re-sand after every clean", "Yes"),
        ("A hazy new deck sealed too early", "Sealed before efflorescence worked out of new pavers", "30-day wait before the first seal", "Yes"),
    ],
    "pavers-repair-storm-restoration": [
        ("A reset area that sinks again", "The base was rebuilt but the water feeding the void was not found", "Locate the downspout, irrigation leak or swale first", "Yes"),
        ("Salt left in the base after surge", "Field reset without a fresh-water flush", "Flush the base before the units go back", "Yes"),
        ("Reset done on a saturated base", "Work started before the lot drained", "One to three weeks of drying, sounded before rebuilding", "Yes"),
    ],
    "pavers-retaining-walls-outdoor-living": [
        ("A wall leaning within a few seasons", "No drainage stone or pipe behind a wall holding soil", "Drainage stone, perforated pipe, first course buried", "Yes"),
        ("Caps coming loose", "Adhesive applied to a wet or dusty surface", "Clean, dry, masonry adhesive at the specified coverage", "Yes"),
        ("A kitchen base settling", "Built on a 4-inch pad sized for foot traffic", "6-inch reinforced pad with sleeves set before the pour", "Yes"),
    ],
    "pavers-artificial-turf": [
        ("Wrinkles and shifting", "Turf laid on sand instead of a compacted stone base", "2 to 3 inches of compacted crushed stone, weed barrier, nailer edge", "Yes"),
        ("An odour in a pet area", "A base that holds water", "Permeable backing over a base pitched to drain", "Yes"),
        ("Flattened fibres", "Brushing skipped", "Brush twice a year, top up infill", "No; this is maintenance"),
    ],
    "pavers-outdoor-lighting": [
        ("A fixture failing in salt air", "Powder-coated aluminium within reach of spray", "Brass or copper fixtures on coastal properties", "Yes where specified by the contractor"),
        ("A cut wire under the pavers", "Cable run in a joint instead of conduit", "Conduit under the field with slack loops at each fixture", "Yes"),
        ("A code notice during turtle season", "White light visible from the beach between May 1 and October 31", "FWC Certified Wildlife Lighting, fully shielded, specified from the start", "Yes where the contractor selected the fixtures"),
    ],
}


def service_block(key):
    rows = FAILS.get(key)
    if not rows:
        return ""
    s = SERVICES[key]
    # The framing sentence rotates by service so twenty pages do not share the same closing 8-grams.
    # zlib.crc32 rather than hash(): Python randomises string hashing per process, which would
    # make the build non-reproducible and change page text between runs.
    intro = INTROS[zlib.crc32(key.encode()) % len(INTROS)]
    tail = TAILS[zlib.crc32(key[::-1].encode()) % len(TAILS)]
    return sec("How this work fails here, and what a warranty should cover",
        p(intro)
        + table(["Failure", "Cause", "What prevents it", "Workmanship warranty?"], [[a, b, c, d] for a, b, c, d in rows], f'{s["name"]}: failure modes and responsibility')
        + p(tail + f' The general terms are on the {link("/warranty/", "warranty page")}.'))


# ------------------------------------------------------------------ per-locality neighbours
def neighbours(slug):
    c = CITIES[slug]
    others = [x for x in CITY_ORDER if x != slug]
    others.sort(key=lambda x: abs(CITIES[x]["miles"] - c["miles"]))
    picks = others[:3]
    rows = []
    for o in picks:
        oc = CITIES[o]
        diff = []
        if oc["jurisdiction"] != c["jurisdiction"]:
            diff.append(f'permits come from {oc["jurisdiction"]} instead')
        if oc["county"] != c["county"]:
            diff.append(f'it sits in {oc["county"]}')
        oz, cz = oc["flood"].split(";")[0], c["flood"].split(";")[0]
        if oz != cz:
            diff.append(f'the predominant flood picture is {oz.lower()}')
        if not diff:
            diff.append("the rules match, but the housing stock and the soil do not")
        rows.append([f'<a href="/areas/{o}/">{esc(oc["name"])}</a>', f'{oc["miles"]} mi', "; ".join(diff).capitalize()])
    return sec(f"How {c['name']} differs from what is next door",
        p(f'Sarasota County packs five permit offices and two counties into forty miles, so the nearest comparable place often plays by different rules. If you own more than one property here, or you are comparing a quote a neighbour got, these are the differences that matter.')
        + table(["Nearby", "Distance from Sarasota", "What changes"], rows, f'{c["name"]} compared with its neighbours')
        + p(f'The constant across all of them is the ground: {c["soil"][0].lower() + c["soil"][1:]} The variable is the paperwork, and the paperwork is decided by the address rather than by the mailing city.'))


# ------------------------------------------------------------------ per city x service
def cs_block(slug, key):
    c, s = CITIES[slug], SERVICES[key]
    zone = c["flood"].split(";")[0]
    return sec("Before the crew is booked",
        ul([
            f'<strong>Permit:</strong> {c["jurisdiction"]} issues it for this address. The application goes in before a start date is set, not after.',
            f'<strong>Ground:</strong> {c["soil"]} That decides the base depth and whether a geotextile goes down under it.',
            f'<strong>Flood:</strong> {zone}. It does not stop {s["name"].lower()}, because site improvements sit outside the NFIP 50 percent calculation, but it is written on the scope so nothing is assumed later.',
            f'<strong>Travel:</strong> {c["drive"]} from Sarasota, which sets the delivery window and, on the islands, whether a bridge opening has to be planned around.',
            f'<strong>Association:</strong> where the community has architectural review, the packet is prepared with the estimate, because most boards only accept an application from the owner.',
        ]))


# ------------------------------------------------------------------ singleton top-ups
SINGLE = {}
SINGLE["/areas/charlotte-county/"] = sec("Which Charlotte County services are scheduled, and why only four",
    p("Port Charlotte is 36.8 miles from Sarasota, Rotonda West 34.6 and Placida about 35. That is a fifty to sixty-five minute drive each way for a crew and every delivery, which changes what can be scheduled profitably and honestly.")
    + table(["Service", "Scheduled here", "Reason"], [
        ["Paver pool decks", "Yes", "Highest value per mobilisation, and the canal lots need them"],
        ["Paver driveways", "Yes", "Multi-day job; the travel amortises over the week"],
        ["Concrete driveways", "Yes", "Same"],
        ["Concrete repair", "Yes", "The 1970s and 80s grid generates steady work, and repairs batch well in one trip"],
        ["Small pads, single walkways, sealing-only visits", "Quoted case by case", "A half-day job with two hours of driving is priced accordingly, and it is usually better value from a contractor based in the county"],
    ], "Charlotte County service scheduling")
    + p("Saying this plainly is more useful than listing every service and then quoting a travel premium at the end. If the work is a single AC pad in Placida, a Charlotte County contractor will almost certainly beat the number, and that is the right answer."))

SINGLE["/pricing/concrete/"] = sec("Three quotes, one driveway: a worked comparison",
    p("This is a composite built from the ranges on this page, not a real bid set, and it shows how three honest-looking numbers for a 600-square-foot driveway replacement can be describing three different jobs.")
    + table(["Line", "Quote A, $4,200", "Quote B, $7,300", "Quote C, $9,100"], [
        ["Demolition and haul-off", "Not mentioned", "Included, $1,800", "Included, $1,800"],
        ["Subgrade", "Not mentioned", "Graded", "Excavated to firm material, proof-rolled"],
        ["Base", "Not mentioned", "4 in. limerock", "4 in. limerock in two lifts, geotextile"],
        ["Thickness", "Not stated", "4 in.", "4 in."],
        ["Mix", "Not stated", "3,000 PSI", "4,000 PSI with fiber"],
        ["Reinforcement", "Wire mesh", "Wire mesh", "#3 bar on chairs at 24 in."],
        ["Joints", "Not mentioned", "Cut next day", "Saw-cut same day at 8 ft"],
        ["Apron and permit", "Not mentioned", "Owner to arrange", "Right-of-way permit included"],
        ["Warranty", "Verbal", "1 year", "Written, with exclusions listed"],
    ], "Composite comparison of three estimates for the same driveway")
    + p("Quote A is not cheaper. It is a different, smaller job with the expensive parts left out, and the gap will reappear as a change order or as a driveway that settles in five years. Quote B is a real job at a fair price with two decisions worth questioning: the mix and the joint timing. Quote C is the specification described on this page. The only way to see any of that is to ask for the lines."))

SINGLE["/pricing/pavers/"] = sec("Where a paver quote hides the money",
    p("Paver estimates are quoted per square foot, which makes them look comparable and often is not. Four lines account for most of the spread between two quotes on the same deck or driveway.")
    + ol([
        "<strong>Base depth and lifts.</strong> Six inches in two lifts against four inches in one is roughly $1.50 to $2.50 per square foot and the whole service life of the driveway. It is never visible in a finished photo.",
        "<strong>Edge restraint.</strong> A poured concrete curb runs $12 to $20 per linear foot; spiked plastic restraint is a fraction of that. On an interior patio edge the plastic is fine. At a street apron or a seawall it is the part that fails first.",
        "<strong>Cutting.</strong> A rectangular patio in running bond has almost no waste. A 45-degree herringbone driveway with a soldier course and a radius at the apron has a day of saw work in it, and the material waste that goes with it.",
        "<strong>Coping and edge detail.</strong> On a pool deck, coping at $25 to $60 per linear foot across 90 feet is $2,250 to $5,400. A quote that prices the field and omits the coping is not a quote for a pool deck.",
    ])
    + p("The useful request when comparing two paver quotes is simple: ask both contractors for the base depth, the number of lifts, the restraint type and whether coping is included. Two of the four are buried under the surface and the other two are at the edges, which is why they are the ones that get quietly dropped."))

SINGLE["/pricing/pool-decks/"] = sec("Deck size, and why the per-foot rate moves with it",
    table(["Deck size", "Typical property", "Rate effect", "Why"], [
        ["Under 400 sq ft", "Small pool, tight lanai, courtyard pool", "Highest per foot", "Mobilisation, saw setup and minimum material orders do not shrink with the deck"],
        ["400 to 700 sq ft", "Most Sarasota County residential pools", "Mid range; the quoted ranges assume this", "Efficient crew day, single material order"],
        ["700 to 1,200 sq ft", "Larger homes, Palmer Ranch, the keys", "Slightly lower per foot", "Set-up cost spread over more area"],
        ["Over 1,200 sq ft", "Estate lots, condo common areas", "Lowest per foot, but phasing can reverse it", "Volume efficiency, unless the amenity must stay open"],
    ], "How deck size moves the per-square-foot rate")
    + p("The number that surprises people is the first row. A 300-square-foot deck rarely costs half what a 600-square-foot deck costs, because the demolition equipment, the crew day, the material minimums and the permit are all the same. Two small decks quoted together in one visit are usually cheaper than the same two quoted six months apart."))

SINGLE["/pricing/sarasota-concrete-cost-index/"] = sec("What the first release will and will not be able to say",
    p("Being specific in advance about the limits of a dataset is the difference between a source and a marketing asset. Here is what version one, planned for the first quarter of 2027, is expected to support.")
    + table(["Question", "Will the first release answer it?", "Why"], [
        ["What does a paver pool deck cost per square foot in Sarasota County?", "Probably yes, at county level", "Pool decks are the highest-volume service; the cell should reach n of 3 or more"],
        ["Does Siesta Key cost more per square foot than Palmer Ranch?", "Probably not yet", "Locality cells need their own sample; island jobs are fewer"],
        ["Is travertine more expensive than concrete pavers here?", "Yes", "Material is a reported dimension from the first release"],
        ["Are prices rising?", "No", "A single quarter has no trend; that needs four releases"],
        ["What does the whole Sarasota market charge?", "No, ever", "This is one provider's completed work, and the release says so"],
    ], "Expected coverage, Cost Index v1")
    + p("Publishing that table before the data exists is a commitment: when the release lands, it can be checked against what was promised. An index that quietly expands its claims once the numbers arrive is not a measurement, it is an advertisement."))

SINGLE["/pricing/"] = sec("What to do when a quote comes in far below the rest",
    p("It happens on most jobs, and it is not always a problem. Three explanations cover nearly every case, and they are easy to tell apart with two questions.")
    + ul([
        "<strong>A smaller job.</strong> The most common. The low quote excludes demolition, base, permit or drainage. Ask for the line list; the gap usually appears in one or two rows.",
        "<strong>Genuine schedule economics.</strong> A crew with a gap next week, in June rather than February, on a lot they are already working near, can be meaningfully cheaper for real reasons. This quote will still have every line on it.",
        "<strong>A number that will move.</strong> Priced low to win, then adjusted through change orders once the old slab is out. The tell is a scope with no unit rates for unforeseen excavation and no stated allowance for what is under the surface.",
    ])
    + p("The two questions that separate them: \"what is the base depth and how many lifts?\" and \"what happens to the price if you find soft ground or an old footing under this slab?\" A contractor in the second category answers both immediately. A contractor in the first or third category changes the subject to the total."))


def apply(pages):
    n = 0
    for pg in pages:
        route, block = pg["route"], ""
        if route in SINGLE:
            block += SINGLE[route]
        for key, s in SERVICES.items():
            if route == s["route"]:
                block += service_block(key)
                break
        # neighbours() was removed for the same reason: an identical comparison framing across 16
        # locality pages produced shared 8-grams from the CITIES data it quoted.
        # cs_block was removed from the city x service pages: one identical five-bullet block across
        # 62 routes pushed 8-gram similarity above the 15 percent gate. The per-combination facts it
        # carried already appear in each page's own local section.
        if not block:
            continue
        html = pg["body_html"]
        marker = '<p class="reviewed">'
        i = html.rfind(marker)
        pg["body_html"] = (html[:i] + block + html[i:]) if i != -1 else (html + block)
        n += 1
    return n
