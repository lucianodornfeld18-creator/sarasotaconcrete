# -*- coding: utf-8 -*-
from _data import BUSINESS, has, PUBLIC_NAME
from _h import sec, p, ul, ol, link, cards


def privacy():
    body = sec("What is collected", p("When you send the estimate form we receive the fields you fill in: name, phone, email, property location and type, service, flood zone if you know it, timeline, your presence at the property, your message and an optional photo. We also record the page you sent it from, the referring page, campaign tags in the URL, the time, and the fact that you checked the consent box. If you call or text the number on the site, the call is routed through a Twilio number and the caller ID and time are logged."))
    body += sec("How it is used", p(f"To respond to your request, prepare an estimate and forward the request to the insured provider that serves your area{(' (' + BUSINESS['legal_entity'] + ')') if has('legal_entity') else ''}. Contact details are not sold or shared with anyone else. Site analytics (Cloudflare Web Analytics, and Google Analytics 4 only if enabled with consent) do not receive your form fields."))
    body += sec("Texts", p("If you consent to texts, messages are limited to your request and scheduling. Message and data rates may apply. Reply STOP to opt out and HELP for help. Consent to texts isn't a condition of getting an estimate."))
    body += sec("Retention", p("Requests are kept for as long as needed to complete the work and meet Florida record-keeping obligations for construction contracts, then deleted. You can ask for a copy or deletion of your data at the email below."))
    body += sec("Cookies and storage", p("The site sets no advertising cookies. Cloudflare may set a security cookie to protect the form; analytics, if enabled, use anonymized identifiers."))
    body += sec("Contact", p(link("mailto:" + BUSINESS["email"], BUSINESS["email"])))
    body += p("Effective September 10, 2026.")
    return {"route": "/privacy/", "title": "Privacy Policy", "meta_description": "What sarasotaconcrete.com collects when you request an estimate, how it is used and forwarded, text-message consent terms, retention, cookies and how to reach us about your data.",
            "h1": "Privacy policy", "breadcrumbs": [("Home", "/"), ("Privacy", None)], "body_html": body}


def terms():
    body = sec("Estimates and prices", p("Cost ranges, calculators and tools on this site are planning aids with a stated date and method. They are not offers or quotes. A binding price exists only in a written estimate signed after a site visit or video walkthrough."))
    body += sec("Permits, codes and rules", p("Permit, flood-zone, setback, lighting and HOA information is summarized from official sources on the date shown on each page and can change. Confirm current requirements with the office listed on the page before you rely on them. This site does not give legal advice."))
    body += sec("Tools", p("The calculators and the permit finder produce estimates from the inputs you give. They can be wrong when the inputs are wrong or when a rule changes. Nothing they output creates a contract."))
    body += sec("Use of the site", p("You may read, link to and quote pages with attribution. Do not scrape the lead form, submit false requests or reuse the site's photos without permission. Data files under /api/ are licensed CC BY 4.0."))
    body += sec("Liability", p(f"{PUBLIC_NAME} is not liable for decisions made on the basis of planning ranges, tool outputs or summarized rules. Work performed under a contract is governed by that contract and by Florida law."))
    body += sec("Texts and calls", p("By providing a phone number and checking the consent box you agree to be contacted about your request. Reply STOP to end texts."))
    body += p("Effective September 10, 2026. Questions: " + link("mailto:" + BUSINESS["email"], BUSINESS["email"]))
    return {"route": "/terms/", "title": "Terms of Use", "meta_description": "Terms for using sarasotaconcrete.com: how cost ranges and tools should be read, the limits of summarized permit and flood information, data licensing, and contact consent.",
            "h1": "Terms of use", "breadcrumbs": [("Home", "/"), ("Terms", None)], "body_html": body}


def accessibility():
    body = sec("Goal", p("This site aims to meet WCAG 2.2 Level AA. Pages use semantic HTML, a single H1, visible focus, keyboard-operable menus and tools, sufficient contrast, real text rather than text in images, captions on every photo and no content hidden in closed accordions or tabs."))
    body += sec("Known limits", ul(["Concept renderings are labeled but decorative detail in job photos is described only in the caption.", "The tools output plain text in a live region; screen readers announce the result once per change."]))
    body += sec("Report a barrier", p(f"Email {link('mailto:' + BUSINESS['email'], BUSINESS['email'])} with the page and what didn't work. Fixes are made on the page and noted in the changelog."))
    return {"route": "/accessibility/", "title": "Accessibility", "meta_description": "Sarasota Concrete aims for WCAG 2.2 AA: semantic HTML, keyboard-operable menus and tools, contrast, captions, no hidden content. How to report a barrier and get it fixed.",
            "h1": "Accessibility", "breadcrumbs": [("Home", "/"), ("Accessibility", None)], "body_html": body}


def thank_you():
    body = sec("Request received", p("Thanks. You'll hear back the same or next business day to confirm the address, the jurisdiction and, if you're on the coast, the flood zone. If you didn't attach a photo or a survey, you can reply to the confirmation email with them."))
    body += sec("While you wait", cards([("/tools/permit-flood-setback-finder/", "Check the permit office", "Which office issues the permit for your address and whether the setback line or the 50% rule could apply."),
                                          ("/pricing/", "See the cost guides", "Planning ranges by service with a date and a method."),
                                          ("/coastal/maintenance-calendar/", "Coastal maintenance calendar", "Sealing and re-sanding intervals by distance from the water.")]))
    return {"route": "/thank-you/", "title": "Thank You", "meta_description": "Your estimate request reached Sarasota Concrete. Expect a callback the same or next business day to confirm the address, jurisdiction and flood zone before a site visit or video walkthrough.",
            "h1": "Your request is in", "breadcrumbs": [("Home", "/"), ("Thank you", None)], "body_html": body, "noindex": True}


def not_found():
    body = sec("That page isn't here", p("The address may have changed or never existed. The links below cover most of what people come here for."))
    body += cards([("/concrete/", "Concrete services", "Pool decks, driveways, patios, slabs, repair, resurfacing."), ("/pavers/", "Pavers and hardscape", "Pool decks, travertine, driveways, sealing, storm repair."),
                   ("/areas/", "Service area", "Sarasota County and the Charlotte County coast."), ("/permits/", "Permits", "One page per jurisdiction."), ("/pricing/", "Pricing", "Dated planning ranges."), ("/contact/", "Contact", "Request a written estimate.")])
    return {"route": "/404/", "title": "Page Not Found", "meta_description": "That page doesn't exist on sarasotaconcrete.com. Jump to concrete or paver services, the service area, permits by jurisdiction, pricing or the estimate form.",
            "h1": "Page not found", "breadcrumbs": [("Home", "/"), ("404", None)], "body_html": body, "noindex": True}


def get_pages():
    return [privacy(), terms(), accessibility(), thank_you(), not_found()]
