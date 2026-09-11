# -*- coding: utf-8 -*-
from _data import BUSINESS, has, SERVICES, CITIES, TIER1, TIER2, BASE_URL
from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, svc_link, city_link, link, ext, facts, cards
from _photos import PHOTOS, figure_html, image_schema
from templates import lead_form


def about():
    entity = f"The requests are handled by {BUSINESS['legal_entity']}." if has("legal_entity") else "The provider's legal name is printed on every estimate and contract; it is listed here as soon as the owner confirms which entity invoices Sarasota County work."
    body = sec("What this site is",
               p("Sarasota Concrete is a local resource and lead-generation site for poured concrete, pavers and hardscape in Sarasota County and the Charlotte County coast within 40 miles of Sarasota. It is not a directory, not a marketplace and not a franchise landing page. One insured provider receives the requests and does the work.") +
               p(entity + " The site's job is to explain the work honestly enough that you can compare any estimate, including ours, against what the ground and the code actually require here."))
    body += sec("What we don't claim",
                ul(["No street address is shown, because the provider is a service-area business that works at your property, not a storefront.",
                    "No license number is shown, because none has been documented for this site yet. The footer says \"Insured\" and nothing more until a Sarasota County Certificate of Competency or a state license number is supplied, at which point Florida Statute 489.119(5)(b) requires it in every advertisement and it will appear here.",
                    "No star rating, review count, years in business or project count appears anywhere on the site. Those numbers exist for the provider's other trade names, but they belong to those profiles, and the reviews page explains how they'll be shown here only once the entity match is confirmed.",
                    "No temperature, cost or durability figure is presented as our own measurement unless the method and date are published on the data and methods page."]))
    body += sec("How the site is organized",
                p(f'Two pillars, {link("/concrete/", "concrete")} and {link("/pavers/", "pavers")}, each with its services. Fifteen {link("/areas/", "locality pages")} with the jurisdiction, flood zone, soil and housing stock. A {link("/permits/", "permit hub")} with one page per office. {link("/pricing/", "Pricing")} with dates and sources. {link("/compare/", "Comparisons")}, {link("/tools/", "tools")}, a {link("/coastal/", "coastal hub")} and {link("/guides/", "guides")} that answer the 150 questions the research turned up, each once, on one URL.'))
    body += sec("Who writes and reviews the pages",
                p(("Pages are written and reviewed by " + BUSINESS["author_name"] + ", " + BUSINESS["author_title"] + ".") if has("author_name") else "Pages are drafted by the site's editorial team and reviewed by the provider's technical lead. The reviewer's name, bio and credential are added to every page as soon as the owner supplies them; until then no page claims a named author.") +
                p(f'The {link("/editorial-standards/", "editorial standards")} page states the rules: primary sources for every regulatory claim, a date on every price, no borrowed statistics, and a changelog when a page changes.'))
    body += sec("Contact", p(f'Email {link("mailto:" + BUSINESS["email"], BUSINESS["email"])}' + (f' or call or text {link("tel:" + BUSINESS["phone_tel"], BUSINESS["phone_display"])}' if has("phone_display") else "") + f'. Hours: {BUSINESS["hours"]}. The {link("/contact/", "contact page")} has the estimate form.'))
    body += reviewed("September 10, 2026")
    return {"route": "/about/", "title": "About Sarasota Concrete", "meta_description": "Who is behind sarasotaconcrete.com, what the site claims and refuses to claim, how requests are handled, and how pages are written and reviewed for Sarasota County homeowners.",
            "h1": "About this site and the provider behind it", "breadcrumbs": [("Home", "/"), ("About", None)], "body_html": body}


def editorial():
    body = sec("Sources", p("Every regulatory statement links a primary source: the Sarasota County Code of Ordinances, the City of Sarasota, Venice, North Port and Longboat Key portals, Charlotte County's permit pages, FEMA, the Florida Department of Environmental Protection and the Florida Fish and Wildlife Conservation Commission, the USDA Natural Resources Conservation Service, NOAA's National Centers for Environmental Information, the Florida Building Code and the American Concrete Institute. Where a page could only reach a secondary source, it says so and tells you what to verify."))
    body += sec("Prices", p("A price on this site carries a date and a method. Until the provider's own completed-job data is large enough to publish, ranges are compiled from published Sarasota-area sources and labeled as such. No range is presented as a quote. The Sarasota Concrete Cost Index, once live, publishes sample size, period and limitations with every release."))
    body += sec("Measurements", p("Any figure described as measured (surface temperature, slip resistance, cure time) comes with the instrument, the conditions and the date on the data and methods page. Until a measurement exists, the page publishes the protocol and cites an applicable technical source instead of a number."))
    body += sec("What is not allowed on these pages",
                ul(["Invented addresses, licenses, insurance limits, warranties, years, project counts, ratings, reviews, awards or statistics.",
                    "Claims about heat, slip, salt, flooding or hurricanes without a measurement or a technical source.",
                    "Text, images, tables, tools or layouts copied from competitors or from the provider's other sites.",
                    "Pages generated by swapping a city name. Every locality page and every city-service page is written from that place's jurisdiction, flood zone, soil, housing and community rules.",
                    "Hidden text, keyword stuffing, link schemes, fake dates."]))
    body += sec("Review and changes", p("Cost guides and permit pages are reviewed quarterly and after every hurricane season. A visible \"last reviewed\" line at the bottom of each page states the date and, when a page changes materially, a one-line changelog. Structured data mirrors what is visible on the page and nothing else."))
    body += sec("Corrections", p(f'If you find an error, email {link("mailto:" + BUSINESS["email"], BUSINESS["email"])} with the page URL. Corrections are made on the page and noted in its changelog.'))
    body += reviewed("September 10, 2026")
    return {"route": "/editorial-standards/", "title": "Editorial Standards", "meta_description": "How sarasotaconcrete.com sources regulatory claims, dates every price, labels measurements, refuses invented proof, and reviews cost and permit pages quarterly.",
            "h1": "Editorial standards", "breadcrumbs": [("Home", "/"), ("Editorial standards", None)], "body_html": body}


def data_methods():
    body = cap("Where do the cost ranges on this site come from?",
               "As of September 10, 2026, every cost range is compiled from published Sarasota-area pricing pages read on that date: paver cleaning and sealing rates from Sarasota sealing companies, installed paver and travertine rates from Sarasota paver contractors, overlay and driveway rates from regional concrete contractors, and national cost aggregators for cross-checks. Each guide lists the sources it used. Nothing is a quote.",
               p("From the first quarter of 2027 the Sarasota Concrete Cost Index replaces those third-party ranges with the provider's own completed jobs: installed price per square foot by service, material and locality, with the sample size, the period and the limitations stated in the release. The index is published as a table and as JSON under a CC BY 4.0 license so anyone can cite or reuse it with attribution."))
    body += cap("How will the pool deck surface temperatures be measured?",
                "Nine surfaces (gray broom concrete, light broom concrete, cool-deck overlay, gray concrete paver, light concrete paver, tumbled travertine, shellstone, honed marble and 2 cm porcelain) will be read with a calibrated infrared thermometer at 10 a.m., 2 p.m. and 5 p.m. on one clear July day and one clear January day in Sarasota, with air temperature, sky and shade recorded.",
                p("Samples are placed side by side on the same base, fully sun-exposed, dry, and read three times each with the emissivity set for masonry; the median is published. Measurement dates are set for January 2027 and July 2027. The raw readings go to the study page and to a JSON file the day they exist. Until then the page shows the protocol, not numbers."))
    body += cap("Where do the flood, permit and lighting facts come from?",
                "From the codes and offices themselves: Sarasota County Code chapters 22, 54 and 98 and Appendix A zoning, the Sarasota County Property Appraiser's 50 percent rule page, FEMA's substantial improvement guidance, Charlotte County's residential permit pages, the Town of Longboat Key's marine turtle pages, and the FDEP model lighting ordinance. Where a city portal blocked automated reading, the page says so.",
                p("Each permit page ends with the office, the portal and the phone number so you can confirm the current fee and form. Fees change by resolution; the page states the date it was last checked."))
    body += cap("How is the site kept honest about the provider?",
                "By leaving blanks. The footer says Insured. There is no license number, address, rating, review count or years-in-business figure on the site because none has been documented for this trade name. Each of those appears only when the owner supplies the document, and the audit file that ships with the site lists every placeholder still open.",
                p(f'See the {link("/editorial-standards/", "editorial standards")} and the {link("/about/", "about page")}.'))
    body += reviewed("September 10, 2026")
    return {"route": "/data-and-methods/", "title": "Data & Methods", "meta_description": "How the cost ranges, the Sarasota Concrete Cost Index, the pool deck surface temperature study and the permit and flood facts on this site are collected, dated and published.",
            "h1": "Data and methods", "breadcrumbs": [("Home", "/"), ("Data & methods", None)], "body_html": body}


def warranty():
    body = cap("What warranty applies to the work?",
               "The written workmanship warranty terms are issued with the contract and depend on the service: poured flatwork, paver installation and sealing carry different periods and different exclusions. The exact terms are not printed here until the owner confirms them, because a warranty you can't read in full isn't a warranty. What you can rely on is that the terms are written, signed and attached to the estimate.",
               p("What a written warranty should cover for concrete: workmanship defects such as scaling from a bad finish, joints cut too late, base failure under the contractor's control. What it normally excludes: hairline shrinkage cracks that don't affect function, color variation, cracks from tree roots or vehicles over the design load, and damage from storm surge. For pavers: settling from a base the contractor built, joint sand loss in the first season, edge restraint failure; not weeds, efflorescence, stains from irrigation or salt."))
    body += sec("Manufacturer warranties", p("Concrete pavers from Belgard, Tremron and Oldcastle carry manufacturer warranties on the units against structural defects; sealers carry product warranties tied to the application method. Those documents are handed over with the care sheet and are separate from the workmanship warranty."))
    body += sec("How claims are handled", p("Email the photos and the contract number. The provider inspects within a stated window, documents the condition and states in writing whether the item is covered. Storm damage is documented for your insurer even when it isn't a warranty matter."))
    body += note("Owner input pending: the exact warranty periods and exclusions per service. Until they're supplied, this page describes what a proper warranty contains and does not state a number.", "warn")
    body += reviewed("September 10, 2026")
    return {"route": "/warranty/", "title": "Workmanship Warranty", "meta_description": "What the written workmanship warranty covers and excludes for concrete, pavers and sealing in Sarasota County, how manufacturer warranties differ, and how a claim is handled.",
            "h1": "Warranty", "breadcrumbs": [("Home", "/"), ("Warranty", None)], "body_html": body}


def financing():
    body = cap("Can a pool deck or driveway be financed?",
               "Financing is offered through a third-party lender when the owner confirms the partner; the name, terms and application link will appear here once that agreement is in place. Until then the estimate can be split into a deposit and progress payments as Florida law allows, and the guide on deposits explains what those limits are.",
               p(f'Read the {link("/guides/deposits-and-warranties/", "deposits and warranties guide")} before signing anything. A contractor who asks for more than a modest deposit on flatwork, or who won\'t put the payment schedule in the contract, is telling you something.'))
    body += note("Owner input pending: financing partner and terms.", "warn")
    body += reviewed("September 10, 2026")
    return {"route": "/financing/", "title": "Financing", "meta_description": "Financing options for concrete, pavers and pool decks in Sarasota County: what is offered now, what is pending a lending partner, and how deposits and progress payments work under Florida law.",
            "h1": "Financing and payment schedules", "breadcrumbs": [("Home", "/"), ("Financing", None)], "body_html": body}


def directories():
    live = [(k, BUSINESS[k]) for k in ("google_profile", "yelp", "facebook", "instagram", "nextdoor") if BUSINESS.get(k)]
    body = sec("Profiles", (ul([link(u, k.replace("_", " ").title()) for k, u in live]) if live else p("No profile is listed yet. Profiles appear here only when they exist for the exact name Sarasota Concrete, with a matching phone number and service description. Listing a profile that belongs to another trade name would misrepresent the business.")))
    body += sec("What will be listed, in order", ol(["Google Business Profile (service-area business, no address shown), the first source for Google's AI answers in local search.", "Yelp, the first source for ChatGPT's local answers.", "Bing Places and Apple Business Connect.", "Facebook, Instagram and Nextdoor.", "BBB, Houzz, Angi, Thumbtack and Porch.", "Greater Sarasota, Venice Area and North Port Area chambers."]) + p("Every listing will carry the same name, phone, categories and description. No listing will be created with a fictitious address."))
    body += reviewed("September 10, 2026")
    return {"route": "/directories/", "title": "Sarasota Concrete on the Web", "meta_description": "Where Sarasota Concrete is listed online, with the rule that every profile must match the exact business name, phone and services, and no listing may use a fictitious address.",
            "h1": "Directories and profiles", "breadcrumbs": [("Home", "/"), ("Directories", None)], "body_html": body}


def contact():
    body = sec("Request a written estimate", p(f'Fill in what you know; a photo of the current surface and a survey or site plan speed things up. {("Call or text " + link("tel:" + BUSINESS["phone_tel"], BUSINESS["phone_display"]) + " if you prefer. ") if has("phone_display") else ""}Hours: {BUSINESS["hours"]}.') + lead_form())
    body += sec("What happens next", ol(["A callback the same or next business day to confirm the address, the jurisdiction and the flood zone.", "A site visit, or a video walkthrough if you're away.", "A written scope with size, spec, drainage, permit responsibility, schedule window and price.", "Permit and ARC packet prepared before a start date is set."]))
    body += sec("Email", p(link("mailto:" + BUSINESS["email"], BUSINESS["email"])))
    return {"route": "/contact/", "title": "Contact & Free Estimate", "meta_description": "Request a written estimate for concrete, pavers or a pool deck anywhere in Sarasota County or the Charlotte County coast. Video walkthroughs for seasonal owners. Same or next business day callback.",
            "h1": "Contact Sarasota Concrete", "breadcrumbs": [("Home", "/"), ("Contact", None)], "body_html": body}


def gallery_page():
    real = [x for x in PHOTOS if x["kind"] == "real"]
    rend = [x for x in PHOTOS if x["kind"] == "rendering"]
    body = sec("Job photos", p("Provider job photos from Central Florida installs, processed to remove metadata and any signage. Captions describe what is visible; none claims a Sarasota address. Suncoast projects are added as they're completed and documented.") + '<div class="gallery">' + "".join(figure_html(x) for x in real) + "</div>")
    body += sec("Concept renderings", p("These are illustrations of finishes and layouts, labeled as renderings on every page where they appear. They are not job photos.") + '<div class="gallery">' + "".join(figure_html(x) for x in rend) + "</div>")
    body += reviewed("September 10, 2026")
    return {"route": "/gallery/", "title": "Photo Gallery: Pool Decks, Driveways, Patios", "meta_description": "Provider job photos of paver pool decks, marble and travertine lanais, paver driveways and patios, plus labeled concept renderings. Suncoast projects added as documented.",
            "h1": "Gallery", "breadcrumbs": [("Home", "/"), ("Gallery", None)], "body_html": body, "schema": image_schema(PHOTOS, BASE_URL)}


def projects():
    body = cap("Where are the documented Sarasota projects?",
               "Not published yet, on purpose. A project entry on this site needs the city, the service, the square footage, the material, the challenge on the lot, the solution, the schedule and the price band, plus photos with the owner's permission. The provider is documenting the first five to ten Suncoast jobs to that standard; entries appear here as they're verified.",
               p("What an entry will look like: \"Gulf Gate, 780-square-foot pool deck, 1972 home on Myakka fine sand two blocks from Little Sarasota Bay. Original slab spalled at the coping; deck replaced with 4-inch 4,000 PSI concrete on 4 inches of compacted base, deck drains added, textured finish. Eight working days. Price band C.\" Each entry links the service page and the locality page it belongs to."))
    body += note("Owner input pending: 5 to 10 documented Suncoast projects with photos and permission.", "warn")
    body += reviewed("September 10, 2026")
    return {"route": "/projects/", "title": "Documented Projects", "meta_description": "Documented concrete and paver projects in Sarasota County with city, size, material, challenge, solution, schedule and price band. Entries appear as each job is verified.",
            "h1": "Projects", "breadcrumbs": [("Home", "/"), ("Projects", None)], "body_html": body}


def reviews():
    body = cap("Why are there no reviews on this page yet?",
               "Because reviews belong to the profile that earned them. The provider has reviews under other trade names on Google and Yelp, but showing them here as Sarasota Concrete reviews would only be honest if the legal entity is the same and the page says which profile they come from. That confirmation is pending, so the page stays empty rather than borrowed.",
               p("When reviews are shown here they will be quoted verbatim, attributed to the profile and date they were left on, and never marked up as an aggregate rating unless the profile belongs to this exact business."))
    body += note("Owner input pending: entity match and permission to display reviews from the existing profiles, with the source named.", "warn")
    body += reviewed("September 10, 2026")
    return {"route": "/reviews/", "title": "Reviews", "meta_description": "Customer reviews for Sarasota Concrete will be shown verbatim with their source profile and date once the business entity match is confirmed. No borrowed ratings.",
            "h1": "Reviews", "breadcrumbs": [("Home", "/"), ("Reviews", None)], "body_html": body}


def get_pages():
    return [about(), editorial(), data_methods(), warranty(), financing(), directories(), contact(), gallery_page(), projects(), reviews()]
