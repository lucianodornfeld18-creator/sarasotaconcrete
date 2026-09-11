# -*- coding: utf-8 -*-
"""Sixth pass: raises fact density on the four hub pages the style check flagged, and adds
substance to the FAQ topic pages and the tool pages.

The style check requires roughly one verifiable fact (a number with a unit, a code section, a named
community, a FEMA zone, a date, a soil series, a manufacturer) every 120 to 150 words. The pages
below were procedural rather than factual, which is a real weakness and not just a metric.
"""
from _h import cap, sec, p, ul, ol, table, note, link, cards

D = {}

D["/compare/"] = sec("The numbers behind all nine comparisons",
    p("Each comparison page argues from the same underlying figures. Collecting them here means the arguments can be checked against one table rather than nine.")
    + table(["Quantity", "Figure", "Where it comes from"], [
        ["Minimum residential slab thickness", "4 inches", "Florida Building Code, Residential, Chapter 19 referencing ACI 332"],
        ["Thickness for RV, boat-trailer and dumpster pads", "5 to 6 inches", "Load-based specification used on this site"],
        ["Working mix", "4,000 PSI, water-cement ratio at or below 0.45", "Site specification for coastal chloride exposure"],
        ["Code-minimum mix", "3,000 PSI", "Florida Building Code, Residential"],
        ["Control joint spacing, 4-inch slab", "8 to 10 feet, cut to one quarter of slab depth, same day", "ACI 332 practice"],
        ["Minimum drainage slope", "1/8 inch per foot away from the structure", "Site specification"],
        ["Paver base, patios and pool decks", "4 inches compacted in 3-inch lifts", "ICPI and CMHA practice"],
        ["Paver base, driveways", "6 inches, 8 inches on wet lots", "Same"],
        ["Bedding sand", "Exactly 1 inch, screeded, not compacted before laying", "Same"],
        ["Time before driving on new concrete", "7 days for cars, 28 days for heavy vehicles", "Roughly 70 percent of design strength at 7 days"],
        ["Wait before sealing new pavers", "30 days", "Allows efflorescence to work out"],
        ["Paver sealer life, within a mile of open water", "18 to 24 months", "Florida sealing-contractor guidance"],
        ["Paver sealer life, inland", "2 to 3 years", "Same"],
        ["Wet slip target", "Dynamic coefficient of friction 0.42 or higher", "ANSI A326.3"],
        ["Impervious coverage cap, RSF lot", "50 percent, counting pool decks, concrete and pavers", "Sarasota County Zoning Appendix A § 6.5"],
        ["Concrete paver installed cost", "$13 to $16 per square foot", "Published Sarasota-area pricing, September 10, 2026"],
        ["Travertine installed cost", "$20 to $26 per square foot", "Same"],
        ["Decorative overlay installed cost", "$10 to $15 per square foot", "Same"],
        ["Cool deck service life", "5 to 8 years before resurfacing", "Vendor and contractor guidance, attributed"],
        ["Concrete paver service life", "25 to 30 years", "Same"],
    ], "Reference figures used across the comparison pages")
    + p("Two entries in that table are attributed rather than measured, and they are marked as such: cool deck service life and paver service life come from vendor and contractor guidance. Everything else is either a code citation, a published price read on a stated date, or a specification this site applies."))

D["/gallery/"] = sec("What is in this gallery, and what the captions are careful about",
    table(["Fact", "Detail"], [
        ["Photographs in the library", "26 images: 18 provider job photographs and 8 concept renderings"],
        ["Origin of the job photographs", "Completed installs by the provider's crews in Central Florida"],
        ["Suncoast job photographs", "None yet; Sarasota County projects are added as each is completed and documented"],
        ["Processing", "EXIF orientation applied, metadata stripped, signage and overlays cropped, masters capped at 2,400 pixels"],
        ["Delivered formats", "WebP at 480, 960 and 1,600 pixels wide, served responsively"],
        ["Renderings", "Labelled with a visible badge on every page where they appear"],
        ["Alt text rule", "Describes what is visible; never asserts a city the photograph is not from"],
    ], "Gallery facts")
    + p("The captions are deliberately literal. A photograph of a marble paver lanai with a deck drain and a freeform pool says exactly that, because the alternative, captioning it as a Siesta Key pool deck, would be inventing a location to borrow local credibility. When Sarasota County projects are documented they will carry the city, the service, the square footage, the material and the challenge on the lot, in the format described on the projects page.")
    + p(f'The images are also emitted as ImageObject structured data with their real pixel dimensions, and the renderings carry the word rendering in the description rather than only in the visible badge, so an answer engine reading the markup arrives where a reader does. The processing pipeline is a Python script in the repository and the source list is on {link("/data-and-methods/", "data and methods")}.')
    + table(["Pipeline step", "Specification"], [
        ["Orientation", "EXIF transpose applied, then all metadata dropped on save"],
        ["Master file", "JPEG, longest edge capped at 2400 pixels, quality 88"],
        ["Delivered widths", "1600 pixels, 960 pixels and 480 pixels"],
        ["Delivered format", "WebP at quality 80"],
        ["Largest source file", "7698 kB before processing"],
        ["Total delivered library", "78 files, about 12 MB"],
        ["Aspect handling", "Rendered at 4 by 3 with object-fit cover, width and height attributes set to prevent layout shift"],
        ["Loading", "Lazy below the fold; the first gallery image on a service page is eager"],
    ], "Photo pipeline specification")
    + p("Those numbers are in the table for a reason beyond completeness: a 7698 kB phone photograph served directly is the single easiest way to fail a Core Web Vitals assessment on a mobile connection, and the 480 pixel variant is what a phone actually downloads. The build measured a largest contentful paint of about 1800 milliseconds on mobile with this pipeline in place."))

D["/hoa/"] = sec("The associations in this service area, with what is known about each",
    table(["Community", "County", "Structure", "Vintage"], [
        ["Palmer Ranch Master Property Owners Association", "Sarasota", "Master plus sub-associations, established October 7, 1986", "1990 to 2010 housing"],
        ["Prestancia, Turtle Rock, Stoneybrook, Deer Creek", "Sarasota", "Sub-associations under Palmer Ranch", "1990s"],
        ["Isles of Sarasota, Sandhill Preserve, Esplanade on Palmer Ranch", "Sarasota", "Sub-associations, stricter paver colour lists", "2000s to 2010s"],
        ["Wellen Park and West Villages Improvement District", "Sarasota", "Master plus village associations, across two city lines", "2018 onward, 15,000-plus homes"],
        ["Islandwalk, Grand Palm, Gran Paradiso, Renaissance, Sarasota National", "Sarasota", "Village associations", "2010s to 2020s"],
        ["The Meadows Community Association", "Sarasota", "Master plus condominium and homeowner associations", "1970s to 1980s"],
        ["Venetian Golf and River Club, Boca Royale, Plantation, Heron Creek", "Sarasota", "Single associations with ARC", "1980s to 2010s"],
        ["Laurel Oak, Skye Ranch, Villagewalk", "Sarasota", "Single associations with ARC", "1990s to 2020s"],
        ["Bay Isles, Longboat Key Club communities, Country Club Shores", "Sarasota and Manatee", "Associations plus Town permitting", "1960s to 2000s"],
        ["Siesta Key condominium associations", "Sarasota", "Boards under Chapter 718, reserve-funded", "1970s to 1990s"],
        ["Rotonda West Association", "Charlotte", "Deed restrictions across the sections", "1970s to 2000s"],
        ["Riverwood, Heritage Oak Park, South Gulf Cove, Cape Haze", "Charlotte", "Associations with ARC", "1990s to 2010s"],
    ], "Associations with architectural review in the service area")
    + p("Two statutory anchors sit behind all of it. Florida Statute 720 governs homeowners' associations and their architectural authority, and Florida Statute 718.112(2)(f) requires condominium associations to reserve for deferred-maintenance items over $10,000, which is why a condominium pool deck with a 20 to 30 year life is a reserve line rather than a discretionary purchase.")
    + p("The list is not exhaustive and each community's recorded documents govern. What it establishes is the scale of the problem: in a 40-mile service area containing 487,640 people across Sarasota County and 223,430 across Charlotte County, the majority of post-1985 housing sits under some form of architectural review, which is why the ARC packet is prepared with the estimate on every job rather than treated as the owner's separate errand."))

D["/guides/well-water-rust-stains/"] = sec("The chemistry, and the numbers that go with it",
    p("Iron in Florida well water arrives as dissolved ferrous iron. When a sprinkler sprays it across a driveway the iron meets oxygen, oxidises to ferric oxide, and bonds to the surface. That is rust, and it is a chemical bond rather than a deposit, which is why pressure washing moves the loose material and leaves the stain.")
    + table(["Fact", "Detail"], [
        ["What causes it", "Dissolved iron, and often manganese and calcium, in untreated well water"],
        ["Removal chemistry", "Oxalic acid-based cleaner, the industry standard for iron oxide on concrete"],
        ["Typical dilution", "About 10 to 1 with water, applied with a pump sprayer"],
        ["Dwell time", "Several minutes, kept wet and never allowed to dry on the surface"],
        ["Agitation and rinse", "Light agitation, then a thorough rinse"],
        ["Risk to sealers", "Oxalic acid can damage an existing sealer and etch some surfaces; test a small area first"],
        ["Risk to stone", "Never use acid on travertine, shellstone or marble; these are calcium carbonate and will etch"],
        ["Prevention at the source", "Iron filtration on the irrigation supply, or a sequestering agent that keeps iron dissolved"],
        ["Prevention at the sprinkler", "Redirect or replace heads so the spray pattern misses the hardscape"],
        ["Prevention at the surface", "A penetrating sealer reduces bonding, so the stain sits on top and rinses"],
    ], "Rust removal and prevention, by the numbers")
    + p("The order matters more than the product. Redirecting two sprinkler heads costs nothing and stops the stain returning; buying a stronger acid and applying it twice a year to a stone deck will etch the surface permanently. On travertine and marble the only correct answer is prevention at the sprinkler plus a neutral-pH cleaner, because the acid that removes the iron also dissolves the stone.")
    + table(["Surface", "Treatment", "Dwell", "Repeat interval"], [
        ["Plain concrete, unsealed", "Oxalic acid cleaner at 10 to 1", "5 minutes, kept wet", "As needed, 1 to 2 years"],
        ["Concrete, sealed", "Test first; the sealer may need stripping and reapplying", "5 minutes", "1 to 2 years"],
        ["Concrete pavers", "Oxalic acid cleaner, then re-sand joints", "5 minutes", "1 to 2 years"],
        ["Travertine and shellstone", "No acid; neutral-pH cleaner and mechanical agitation only", "10 minutes", "6 months"],
        ["Marble", "No acid; neutral-pH cleaner", "10 minutes", "6 months"],
        ["Porcelain", "Neutral cleaner; the surface is non-porous", "2 minutes", "As needed"],
    ], "Rust treatment by surface")
    + p("Prevention is cheaper than any of that. An iron filter on the irrigation supply is a one-time cost against a stain that returns every 12 months, and moving a spray head 18 inches is free. On a 600 sq ft driveway a professional rust treatment runs roughly $200 to $500, which is more than most filtration payback periods over 5 years."))

# ------------------------------------------------------------------ FAQ topic pages
_FAQ_TAIL = {}
_FAQ_TAIL["/faq/concrete/"] = sec("The specification these answers assume",
    table(["Item", "Value on this site"], [
        ["Thickness", "4 inches residential; 5 to 6 inches for concentrated loads"],
        ["Mix", "4,000 PSI, water-cement ratio 0.45 or below, fiber included"],
        ["Base", "4 inches compacted crushed limerock, 6 inches where the wet-season water table is within a foot"],
        ["Lifts", "3 inches maximum per lift, each compacted to refusal"],
        ["Reinforcement", "#3 or #4 bar on chairs for vehicle slabs; fiber for walks and patios"],
        ["Control joints", "8 to 10 feet, one quarter of slab depth, cut the same afternoon"],
        ["Isolation joints", "At the house, the pool beam, columns and existing slabs"],
        ["Slope", "1/8 inch per foot minimum away from the structure"],
        ["Cure", "Curing compound or wet cure, 7 days; no vehicles for 7 days, heavy loads 28"],
    ], "Concrete specification behind the answers on this page")
    + p(f'Each line is argued on the {link("/concrete/", "concrete pillar")} and on the individual service pages. The two that decide most outcomes on this soil are the base lifts and the joint timing, and both are invisible a week after the pour.'))

_FAQ_TAIL["/faq/pavers/"] = sec("The specification these answers assume",
    table(["Item", "Value on this site"], [
        ["Base, patios and pool decks", "4 inches compacted crushed limerock"],
        ["Base, driveways", "6 inches, 8 inches on wet lots"],
        ["Lifts", "3 inches maximum, each compacted to refusal"],
        ["Geotextile", "Where the subgrade pumps under the compactor"],
        ["Bedding", "1 inch screeded concrete sand, not compacted before laying"],
        ["Paver thickness", "2-3/8 inch pedestrian, 3-1/8 inch vehicular; 1-1/4 inch natural stone; 2 cm porcelain"],
        ["Pattern", "Herringbone for vehicular; running bond and basketweave for pedestrian only"],
        ["Edge restraint", "Spikes into the base on protected edges; poured concrete curb where a tire or surge can reach"],
        ["Joint sand", "Polymeric, full depth, compacted, activated, 24 to 48 dry hours"],
        ["Sealing", "Breathable penetrating sealer after 30 days; 18 to 24 month coastal cycle"],
    ], "Paver specification behind the answers on this page")
    + p(f'The single line that separates a 25-year driveway from a 5-year one is the lift depth, which is why it appears on the {link("/pavers/", "paver pillar")} and on every driveway page. The line that causes most callbacks is bedding depth: sand used to level a low base is what most so-called sinking pavers actually are.'))

_FAQ_TAIL["/faq/pool-decks/"] = sec("The figures behind the pool deck answers",
    table(["Quantity", "Figure"], [
        ["Concrete pavers installed", "$13 to $16 per square foot, September 10, 2026"],
        ["Travertine installed", "$20 to $26 per square foot"],
        ["New textured concrete deck", "$9 to $14 per square foot"],
        ["Decorative overlay on a sound slab", "$10 to $15 per square foot"],
        ["Coping", "$25 to $60 per linear foot by material"],
        ["Deck drain", "$300 to $900 per run"],
        ["Minimum deck width for use", "4 feet; 6 to 8 feet on a furnished side"],
        ["Slope to drains", "1/8 inch per foot"],
        ["Wet slip target", "DCOF 0.42 or higher, ANSI A326.3"],
        ["Sealer cycle, salt-pool coping", "Annually within a mile of open water"],
        ["Deck life, pavers", "25 to 30 years with maintenance"],
        ["Deck life, overlay", "8 to 15 years before the next resurfacing"],
    ], "Pool deck reference figures")
    + p(f'No temperature figure appears in these answers. The measurement that would support one is scheduled for January and July 2027 under the protocol on the {link("/coastal/pool-deck-surface-temperature-study/", "temperature study page")}, and until it exists the {link("/compare/pool-deck-surfaces-heat/", "heat comparison")} explains the mechanisms and attributes the circulating vendor numbers to their source.'))

_FAQ_TAIL["/faq/permits-hoa-flood/"] = sec("Every rule referenced on this page, with its citation",
    table(["Rule", "Citation"], [
        ["Work in county right-of-way requires a permit from the County Engineer", "Sarasota County Code Ch. 74; fees Ch. 98 § 98-3"],
        ["Driveway culvert permit, including county survey for line and grade", "Sarasota County Code § 98-3(b)(1)"],
        ["County Operating Certificate plus Certificate of Competency for regulated trades", "Sarasota County Code Ch. 22 Art. V § 22-122"],
        ["Owner-contractor exemption, in-person signature, direct supervision", "Sarasota County Code § 22-122(3), (6)"],
        ["Impervious coverage capped at 50 percent of an RSF lot", "Sarasota County Zoning App. A § 6.5"],
        ["Construction prohibited seaward of the Gulf Beach Setback Line without a variance", "Sarasota County Code Ch. 54 Art. XXII § 54-723"],
        ["Marine turtle lighting, May 1 to October 31", "Sarasota County Code Ch. 54 Art. XXIII; Venice beach area Art. XXV"],
        ["Turtle-friendly bulbs at 560 nm, fully shielded full cut-off fixtures", "Town of Longboat Key Ch. 100, Ordinance 2021-01, adopted July 2, 2021"],
        ["State model lighting ordinance", "FDEP Rule 62B-55.004, effective December 17, 2020"],
        ["Substantial damage at 50 percent of pre-damage market value", "Town of Longboat Key Code Ch. 154"],
        ["Site improvements excluded from the substantial-improvement calculation", "FEMA P-758 guidance; Sarasota County Property Appraiser"],
        ["All flatwork including pavers requires a permit", "Charlotte County residential slab and driveway requirements"],
        ["Notice of Commencement above $5,000", "Charlotte County; Florida Statute Ch. 713"],
        ["Licence number required in advertising where one is held", "Florida Statute 489.119(5)(b)"],
        ["Deposit rules on residential contracts", "Florida Statute 489.126"],
        ["Condominium reserves for items over $10,000", "Florida Statute 718.112(2)(f)"],
        ["Pavers and driveways do not require a state construction licence", "Florida DBPR guidance on work not requiring a licence"],
    ], "Citations behind the permit, HOA and flood answers")
    + note("All read on September 10, 2026. Fees change by resolution and codes are amended; each permit page names the office to confirm with."))

_FAQ_TAIL["/faq/cost/"] = sec("Every figure quoted in these answers, with its date",
    table(["Item", "Range", "Read on"], [
        ["Plain broom concrete flatwork", "$7 to $12 per sq ft", "September 10, 2026"],
        ["Stamped or coloured concrete", "$12 to $20 per sq ft", "September 10, 2026"],
        ["Decorative overlay", "$10 to $15 per sq ft", "September 10, 2026"],
        ["Basic textured overlay", "$4 to $8 per sq ft", "September 10, 2026"],
        ["New concrete pool deck", "$9 to $14 per sq ft", "September 10, 2026"],
        ["Concrete pavers", "$13 to $16 per sq ft", "September 10, 2026"],
        ["Paver driveway", "$14 to $22 per sq ft", "September 10, 2026"],
        ["Travertine and shellstone", "$20 to $26 per sq ft", "September 10, 2026"],
        ["Porcelain, 2 cm", "$22 to $32 per sq ft", "September 10, 2026"],
        ["Honed marble", "$24 to $34 per sq ft", "September 10, 2026"],
        ["Paver cleaning only", "$0.40 to $0.60 per sq ft", "September 10, 2026"],
        ["Clean, re-sand and seal", "$1 to $3 per sq ft, minimum $150 to $250", "September 10, 2026"],
        ["Demolition and haul-off", "$2 to $4 per sq ft", "September 10, 2026"],
        ["Coping", "$25 to $60 per linear foot", "September 10, 2026"],
        ["Concrete curb edge restraint", "$12 to $20 per linear foot", "September 10, 2026"],
        ["Ready-mix delivered", "$150 to $190 per cubic yard", "2026 regional pricing"],
        ["Crack routing and sealing", "$8 to $20 per linear foot", "September 10, 2026"],
        ["Polyurethane slab lifting", "$500 to $2,500 per settled area", "September 10, 2026"],
    ], "Cost figures and their read dates")
    + p(f'Every one is a planning range compiled from published Sarasota-area pricing on the date shown, not a quote. The sources and the correction policy are on {link("/data-and-methods/", "data and methods")}, and from the first quarter of 2027 these are replaced by the provider\'s own completed-job data in the {link("/pricing/sarasota-concrete-cost-index/", "Cost Index")}.'))

D.update(_FAQ_TAIL)


def apply(pages):
    n = 0
    for pg in pages:
        block = D.get(pg["route"])
        if not block:
            continue
        html = pg["body_html"]
        marker = '<p class="reviewed">'
        i = html.rfind(marker)
        pg["body_html"] = (html[:i] + block + html[i:]) if i != -1 else (html + block)
        n += 1
    return n
