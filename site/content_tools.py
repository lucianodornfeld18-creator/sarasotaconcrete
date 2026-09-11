# -*- coding: utf-8 -*-
"""Tools: each page carries an inline <script> (hashed into the CSP at build) that defines
window.SCTools[name](root). The HTML form works without JS as a static reference."""
from _h import cap, sec, p, ul, ol, table, note, faq_block, cta, reviewed, link, ext, facts, cards
from _data import CITIES, CITY_ORDER


def pg(slug, title, meta, h1, lede, body, faq=None):
    return {"route": f"/tools/{slug}/" if slug else "/tools/", "title": title, "meta_description": meta, "h1": h1, "kicker": "Tools", "lede": lede,
            "breadcrumbs": [("Home", "/"), ("Tools", "/tools/"), (h1.split(":")[0][:40], None)] if slug else [("Home", "/"), ("Tools", None)],
            "body_html": body, "faq": faq or []}


def hub():
    body = p("Four planning tools built for Sarasota County's rules and ground. Each one states its inputs, its logic and its date, and none of them replaces a written estimate or a call to the permit office.")
    body += cards([("/tools/coastal-surface-selector/", "Coastal Surface Selector", "Seven inputs about your lot, your pool and your budget; one surface recommendation with its reasons and sealing cycle."),
                   ("/tools/permit-flood-setback-finder/", "Permit, Flood-Zone & Setback Finder", "Locality plus work type in; office, portal, phone, coastal rules and who pulls the permit out."),
                   ("/tools/concrete-paver-calculator/", "Concrete & Paver Calculator", "Length and width in; yards, tons, rebar, pavers, sand, restraint and a printable dated range out."),
                   ("/tools/pour-calendar/", "Pour Calendar", "Twelve months of Sarasota-Bradenton normals turned into a start hour, a rain plan and a cure note.")])
    body += reviewed("September 10, 2026")
    return pg("", "Planning Tools for Concrete & Pavers in Sarasota", "Four tools for Sarasota County hardscape: a coastal surface selector, a permit and flood-zone finder by locality, a concrete and paver quantity and cost calculator, and a pour calendar from NOAA normals.",
              "Planning tools for Sarasota County hardscape", "Surface selector, permit finder, calculator and pour calendar, each with its logic and date stated.", body)


def selector():
    form = '''<form class="tool" data-tool="selector" id="selector">
<fieldset><label for="s-dist">Distance from open water (Gulf, bay or canal)</label><select id="s-dist" name="dist"><option value="near">Under half a mile (barrier island, bayfront, canal)</option><option value="mid">Half a mile to two miles</option><option value="far" selected>Over two miles inland</option></select></fieldset>
<fieldset><label for="s-zone">FEMA flood zone</label><select id="s-zone" name="zone"><option value="X" selected>X (or not sure, inland)</option><option value="AE">AE</option><option value="VE">VE</option></select></fieldset>
<fieldset><label for="s-pool">Pool</label><select id="s-pool" name="pool"><option value="none" selected>No pool on this surface</option><option value="chlorine">Chlorine pool</option><option value="salt">Salt-chlorinated pool</option></select></fieldset>
<fieldset><label for="s-use">Main use</label><select id="s-use" name="use"><option value="barefoot" selected>Pool deck or patio, barefoot</option><option value="vehicle">Driveway, cars and trucks</option><option value="cart">Golf cart path or pad</option><option value="walk">Walkway or entry</option></select></fieldset>
<fieldset><label for="s-hoa">Association review</label><select id="s-hoa" name="hoa"><option value="no" selected>None</option><option value="yes">Yes, with a color list</option></select></fieldset>
<fieldset><label for="s-budget">Budget tier</label><select id="s-budget" name="budget"><option value="1">Lowest sound option</option><option value="2" selected>Middle</option><option value="3">Premium</option></select></fieldset>
<fieldset><label for="s-shade">Sun exposure</label><select id="s-shade" name="shade"><option value="sun" selected>Full sun most of the afternoon</option><option value="shade">Mostly shaded or under a cage with shade cloth</option></select></fieldset>
<div class="out" aria-live="polite" id="selector-out">Choose your inputs; the recommendation updates here.</div>
</form>'''
    js = r'''window.SCTools=window.SCTools||{};window.SCTools.selector=function(root){var v=function(n){return root.querySelector('[name="'+n+'"]').value};
var d=v('dist'),z=v('zone'),pool=v('pool'),use=v('use'),hoa=v('hoa'),b=v('budget'),sh=v('shade');var out=[];var seal=(d==='near')?'every 18 to 24 months':(d==='mid')?'every 2 years':'every 2 to 3 years';
if(use==='vehicle'){if(z==='VE'||(d==='near'&&z==='AE')){out.push('Recommended: vehicular concrete pavers (3-1/8 in.) in herringbone on 6 in. of compacted base with concrete curbs. Reason: in a surge, a paver field is rebuilt and reused; a slab is replaced.');}
else if(b==='1'){out.push('Recommended: 4-in. broom concrete, 4,000 PSI, on 4 in. of compacted base with joints at 8 to 10 ft. Reason: lowest sound cost inland; 30-year life with little maintenance.');}
else{out.push('Recommended: vehicular concrete pavers in herringbone on 6 in. of compacted base'+(hoa==='yes'?' in a color from the association list':'')+'. Alternative: broom concrete if the budget is tight and the lot is inland. Permeable pavers if the lot is at the 50% impervious cap.');}
out.push('Maintenance: '+(d==='far'&&b==='1'?'penetrating sealer on coastal lots only; keep joints sealed.':'re-sand and seal '+seal+' with a penetrating sealer.'));}
else if(use==='cart'){out.push('Recommended: 4-in. broom concrete or concrete pavers on 4 in. of base; either carries a cart. Check the community rule first: cart pads and second driveways are the most common ARC denial, and at the street the jurisdiction reviews the apron.');out.push('Maintenance: seal '+seal+'.');}
else if(use==='walk'){out.push('Recommended: '+(b==='3'?'travertine or porcelain pavers':b==='2'?'concrete pavers with a soldier-course border':'4-in. broom concrete')+' on 4 in. of compacted base, cross-sloped 1/4 in. per foot.');if(d==='near'){out.push('Lighting: amber, fully shielded fixtures if the beach can see the walk (May 1 to Oct 31).');}out.push('Maintenance: seal '+seal+'.');}
else{var mat;if(pool==='salt'){mat=(b==='3')?'2 cm porcelain (R11 face) or honed marble':(b==='2')?'light concrete pavers, sealed':'light-colored textured concrete or a light overlay on a sound slab';out.push('Recommended: '+mat+'. Reason: salt water flakes unsealed limestone (travertine, shellstone) at the waterline; porcelain and dense pavers do not need annual coping sealing.');if(b==='3'){out.push('If you want travertine anyway: seal the coping every year and rinse the field weekly.');}}
else{mat=(b==='3')?'tumbled travertine or shellstone (coolest tier), or porcelain for a modern floor':(b==='2')?'light travertine-look or light-blend concrete pavers':'light-colored textured concrete, or a light overlay if the slab passes the six tests';out.push('Recommended: '+mat+(sh==='sun'?'. In full sun choose the lightest color available; color drives most of the 2 p.m. temperature.':'. In shade, heat matters less; choose by look and slip.'));}
if(z==='VE'){out.push('VE zone: build as pavers on a rebuildable base with concrete curbs; if the deck sits under an elevated home, an engineered slab is specified by the engineer.');}
out.push('Slip: ask for a wet DCOF of 0.42 or higher (ANSI A326.3); use a matte penetrating sealer, never a glossy film, around water.');
out.push('Maintenance: seal '+seal+(pool==='salt'?'; travertine coping annually':'')+'; re-sand joints when they drop 1/4 in.');
if(d==='near'){out.push('Barrier island: check the Gulf Beach Setback Line for Gulf-front lots and use amber, shielded lighting May 1 to Oct 31.');}}
if(hoa==='yes'){out.push('Association: submit the material sample, color name, pattern and drainage arrows with the ARC form before the permit.');}
out.push('Next: the pool deck cost guide (/pricing/pool-decks/) and the paver or concrete service page for the spec. Planning logic dated September 10, 2026; not a quote.');
root.querySelector('.out').innerHTML='<ul><li>'+out.join('</li><li>')+'</li></ul>';};'''
    body = cap("How does the Coastal Surface Selector choose?",
               "It applies the same order the estimate uses: use (barefoot, vehicle, cart, walk), then flood zone (VE pushes to rebuildable pavers), then pool chemistry (salt pushes away from unsealed limestone), then sun and budget, then the association's color list. The output names a surface, a base, a sealing cycle by distance from the water and the island rules that apply. It doesn't price the job.",
               p("Logic dated September 10, 2026. It encodes the reasoning on the comparison pages, not a measurement; when the surface temperature study is published, the heat step will use measured values."))
    body += form + f'<script>{js}</script>'
    body += sec("What the inputs mean", ul(["Distance from open water sets the sealing cycle: 18 to 24 months within half a mile, 2 years to two miles, 2 to 3 years inland.", "FEMA zone VE changes the construction to pavers on a rebuildable base with concrete curbs.", "Salt-chlorinated pools flake unsealed travertine and shellstone at the waterline; porcelain and dense pavers don't need annual coping sealing.", "Full sun makes color the dominant heat factor; shade makes it secondary.", "Association review adds the color-list step and the packet."]))
    body += sec("Related", cards([("/compare/pool-deck-surfaces-heat/", "Surfaces and heat", "The reasoning behind the heat step."), ("/compare/travertine-vs-shellstone-vs-porcelain/", "Three light surfaces", "Stone vs porcelain."), ("/pricing/pool-decks/", "Pool deck cost guide", "Prices by material.")]))
    body += reviewed("September 10, 2026")
    return pg("coastal-surface-selector", "Coastal Surface Selector: Pool Deck & Driveway Materials", "Choose a pool deck, patio, driveway or walkway surface for a Sarasota-area lot from distance to the water, FEMA zone, pool chemistry, use, sun and budget, with the sealing cycle and island rules that follow.",
              "Coastal Surface Selector: the right material for your distance from the water", "Seven inputs, one recommendation with its reasons, a base spec and a maintenance cycle.", body)


def finder():
    opts = "".join(f'<option value="{c}">{CITIES[c]["name"]}</option>' for c in CITY_ORDER)
    form = f'''<form class="tool" data-tool="finder" id="finder">
<fieldset><label for="f-loc">Locality</label><select id="f-loc" name="loc">{opts}<option value="lido">Lido Key, St. Armands, Bird Key</option><option value="casey">Casey Key</option><option value="manasota-s">Manasota Key (Sarasota side)</option><option value="manasota-c">Manasota Key or Englewood (Charlotte side)</option><option value="wellen-np">Wellen Park (North Port side)</option><option value="wellen-v">Wellen Park (Venice side)</option></select></fieldset>
<fieldset><label for="f-work">Work</label><select id="f-work" name="work"><option value="driveway">Driveway replacement</option><option value="apron">Driveway apron, culvert or anything at the street</option><option value="deck">Pool deck (same footprint)</option><option value="patio">Patio or lanai slab / pavers</option><option value="pad">Shed, AC or generator pad</option><option value="wall">Seat or retaining wall</option><option value="light">Hardscape lighting</option></select></fieldset>
<fieldset><label for="f-gulf">Is the lot on the Gulf beach?</label><select id="f-gulf" name="gulf"><option value="no" selected>No</option><option value="yes">Yes, Gulf-front</option></select></fieldset>
<fieldset><label for="f-zone">FEMA zone from the Property Appraiser map (optional)</label><select id="f-zone" name="zone"><option value="">Not sure</option><option value="X">X</option><option value="AE">AE</option><option value="VE">VE</option></select></fieldset>
<div class="out" aria-live="polite">Choose a locality and the work.</div>
</form>'''
    js = r'''window.SCTools=window.SCTools||{};window.SCTools.finder=function(root){var v=function(n){return root.querySelector('[name="'+n+'"]').value};
var J={county:{name:'Sarasota County Building (1001 Sarasota Center Blvd; Venice office 4000 S. Tamiami Trail)',portal:'Accela Citizen Access, building.scgov.net',phone:'(941) 861-5000',page:'/permits/sarasota-county/',row:'Culvert permit or right-of-way use permit (Code Ch. 98, Ch. 74) for anything in the county road frontage.',lot:'Flatwork review through Accela; documented residential exemption under $7,500 may apply; 50% impervious cap on RSF lots.'},
city:{name:'City of Sarasota Development Services',portal:'FTG portal, ftgportal.sarasotafl.gov',phone:'see sarasotafl.gov',page:'/permits/city-of-sarasota/',row:'The apron between sidewalk and street is city right-of-way and needs a city permit.',lot:'Flatwork reviewed through the FTG portal; retaining walls over 3.5 ft permitted; trees 4 in. and up protected.'},
venice:{name:'City of Venice Building Department and Engineering',portal:'eTRAKiT, trakit.venicegov.com',phone:'see venicegov.com',page:'/permits/venice/',row:'Engineering right-of-way review; pavers in the right-of-way need a license agreement and the city detail (Code Ch. 62).',lot:'Building permit via eTRAKiT.'},
np:{name:'City of North Port Building Division',portal:'Click2Gov',phone:'(941) 429-7044',page:'/permits/north-port/',row:'Right of Way Use Permit (Culvert/Driveway/Sidewalk/Concrete Slab); swale restored and inspected by Public Works.',lot:'Building permit via Click2Gov; sealed drawings if the city detail does not cover the work.'},
lbk:{name:'Town of Longboat Key Planning, Zoning & Building (501 Bay Isles Rd)',portal:'Town portal',phone:'(941) 316-1999',page:'/permits/longboat-key/',row:'At-grade driveways reviewed by Planning & Zoning as exceptions.',lot:'Town permit; substantial-improvement/damage check on every permit (Code Ch. 154).'},
cc:{name:'Charlotte County Community Development (18500 Murdock Circle)',portal:'Charlotte County online permitting',phone:'(941) 743-1200',page:'/permits/charlotte-county/',row:'ROW permit if only in the right-of-way; line-and-grade fee $310 or ROW $90.',lot:'All flatwork including pavers requires a permit and inspections; NOC over $5,000; zoning review $22.'}};
var M={'sarasota':'city','fruitville-bee-ridge':'county','gulf-gate':'county','siesta-key':'county','palmer-ranch':'county','longboat-key':'lbk','osprey':'county','nokomis':'county','venice':'venice','south-venice':'county','north-port':'np','englewood':'county','port-charlotte':'cc','rotonda-west':'cc','placida':'cc','lido':'city','casey':'county','manasota-s':'county','manasota-c':'cc','wellen-np':'np','wellen-v':'venice'};
var island={'siesta-key':1,'longboat-key':1,'lido':1,'casey':1,'manasota-s':1,'manasota-c':1,'englewood':0};
var loc=v('loc'),w=v('work'),g=v('gulf'),z=v('zone');var j=J[M[loc]];var out=[];
out.push('<strong>Office:</strong> '+j.name+' · '+j.portal+' · '+j.phone+' · <a href="'+j.page+'">rules and links</a>');
if(w==='apron'){out.push('<strong>Right-of-way:</strong> '+j.row);}else{out.push('<strong>On the lot:</strong> '+j.lot);if(w==='driveway'){out.push('If the apron or a culvert is part of the job: '+j.row);}}
if(w==='wall'){out.push('Walls over 3.5 ft are permitted structures in most jurisdictions; under that, generally not, but drainage and setbacks apply.');}
if(w==='pad'){out.push('Detached sheds of 100 sq ft or less are generally exempt in unincorporated Sarasota County; Charlotte County permits every slab.');}
if(island[loc]){out.push('<strong>Flood:</strong> expect AE, with VE on Gulf-facing rows. Hardscape is a site improvement outside the NFIP 50% calculation but is documented in the file. <a href="/permits/flood-zones-50-percent-rule/">Flood zones and the 50% rule</a>.');
out.push('<strong>Turtle lighting:</strong> May 1 to Oct 31, amber/red (560 nm+) shielded fixtures for any light visible from the beach. <a href="/permits/sea-turtle-lighting/">Rules</a>.');}
else if(z==='AE'||z==='VE'){out.push('<strong>Flood:</strong> zone '+z+'. Site work is outside the 50% calculation; VE changes the construction to rebuildable pavers with concrete curbs.');}
if(g==='yes'){out.push('<strong>Setback:</strong> Gulf-front lot. If the work is seaward of the Gulf Beach Setback Line, pools, spas and pool decks need a coastal setback variance from the County Commission (Code Ch. 54 Art. XXII). Check the line on the county GIS before design.');}
if(loc==='casey'){out.push('North Casey Key Conservation District rules also apply (Ch. 54 Art. XXVI).');}if(loc==='manasota-s'||loc==='manasota-c'){out.push('Manasota Key Conservation District rules also apply (Ch. 54 Art. XXVII).');}
if(w==='light'){out.push('Low-voltage lighting is generally not permitted work; a new transformer outlet is an electrical permit. On the islands, FWC-certified fixtures.');}
out.push('<strong>Who pulls it:</strong> the contractor when registered with this office; the owner as owner-builder for an occupied home after signing the disclosure.');
out.push('<strong>Before the permit:</strong> association approval in writing, if any. Logic dated September 10, 2026; confirm the current form and fee with the office and the zone on the Property Appraiser map.');
root.querySelector('.out').innerHTML='<ul><li>'+out.join('</li><li>')+'</li></ul>';};'''
    body = cap("What does the Permit, Flood-Zone and Setback Finder do?",
               "It maps your locality to the office that issues the permit (county, City of Sarasota, Venice, North Port, Longboat Key or Charlotte County), names the portal and phone, says what usually applies to the work you picked on the lot and at the street, flags the flood-zone expectation on the barrier islands, the turtle-lighting season and, for Gulf-front lots, the Gulf Beach Setback Line variance.",
               p("It's a lookup by locality, not a parcel search: city lines are irregular in Sarasota, Venice and Englewood, so confirm the jurisdiction and the FEMA zone on the Sarasota County or Charlotte County Property Appraiser map. Logic dated September 10, 2026."))
    body += form + f'<script>{js}</script>'
    body += sec("Verify the two things the tool can't see", ul([ext("https://www.sarasotapropertyappraiser.gov/propertysearch", "Sarasota County Property Appraiser property search") + ": shows the taxing jurisdiction and the FEMA zone for any parcel.", ext("https://msc.fema.gov/portal/home", "FEMA Flood Map Service Center") + ": the official flood map by address.", "The county GIS for the Gulf Beach Setback Line on Gulf-front lots."]))
    body += reviewed("September 10, 2026")
    return pg("permit-flood-setback-finder", "Permit, Flood-Zone & Setback Finder for Sarasota Hardscape", "Pick a locality and the work; get the permit office, portal and phone, what applies on the lot and at the street, the flood-zone expectation, turtle-lighting season and the Gulf Beach Setback Line note. Sarasota and Charlotte counties.",
              "Permit, Flood-Zone and Setback Finder", "Which office, which portal, what applies at the street and on the lot, and the coastal rules that ride along.", body)


def calculator():
    form = '''<form class="tool" data-tool="calc" id="calc">
<div class="row"><div><label for="c-l">Length (ft)</label><input id="c-l" name="l" type="number" min="1" step="0.5" value="20"></div><div><label for="c-w">Width (ft)</label><input id="c-w" name="w" type="number" min="1" step="0.5" value="30"></div></div>
<fieldset><label for="c-type">Surface</label><select id="c-type" name="type"><option value="c4">Concrete, 4 in. (driveway, patio, pool deck, walk)</option><option value="c6">Concrete, 6 in. (RV, boat, dumpster, hot tub pad)</option><option value="ov">Overlay on existing slab</option><option value="pp">Concrete pavers, patio or pool deck (4 in. base)</option><option value="pd">Concrete pavers, driveway (6 in. base)</option><option value="tr">Travertine or shellstone (4 in. base)</option><option value="po">Porcelain 2 cm (4 in. base)</option><option value="mb">Honed marble (4 in. base)</option></select></fieldset>
<fieldset><label for="c-paver">Paver size (for count)</label><select id="c-paver" name="paver"><option value="0.33">6 × 8 in. (0.33 sq ft)</option><option value="1">12 × 12 in. (1 sq ft)</option><option value="2">12 × 24 in. (2 sq ft)</option><option value="2.67">16 × 24 in. (2.67 sq ft)</option><option value="4">24 × 24 in. (4 sq ft)</option></select></fieldset>
<fieldset><label for="c-demo">Demolition of an existing surface?</label><select id="c-demo" name="demo"><option value="0">No</option><option value="1">Yes</option></select></fieldset>
<fieldset><label for="c-island">Barrier-island logistics?</label><select id="c-island" name="island"><option value="0">No</option><option value="1">Yes</option></select></fieldset>
<div class="out" aria-live="polite">Enter dimensions.</div>
<p><button type="button" class="btn outline" onclick="window.print()">Print or save as PDF</button></p>
</form>'''
    js = r'''window.SCTools=window.SCTools||{};window.SCTools.calc=function(root){var v=function(n){return root.querySelector('[name="'+n+'"]').value};
var L=parseFloat(v('l'))||0,W=parseFloat(v('w'))||0,t=v('type'),ps=parseFloat(v('paver')),demo=v('demo')==='1',isl=v('island')==='1';var A=L*W;if(!A){root.querySelector('.out').textContent='Enter dimensions.';return;}
var P={c4:{lo:7,hi:12,n:'4-in. concrete'},c6:{lo:9,hi:14,n:'6-in. concrete'},ov:{lo:4,hi:15,n:'overlay'},pp:{lo:13,hi:16,n:'concrete pavers'},pd:{lo:14,hi:22,n:'vehicular concrete pavers'},tr:{lo:20,hi:26,n:'travertine/shellstone'},po:{lo:22,hi:32,n:'porcelain'},mb:{lo:24,hi:34,n:'honed marble'}}[t];
var f=function(x){return Math.round(x).toLocaleString('en-US')};var out=['<strong>Area:</strong> '+f(A)+' sq ft ('+L+' × '+W+' ft)'];
if(t==='c4'||t==='c6'){var th=(t==='c4')?4:6;var cy=A*th/12/27;out.push('<strong>Concrete:</strong> '+cy.toFixed(2)+' cu yd at '+th+' in., order '+(cy*1.1).toFixed(2)+' cu yd with 10% waste (4,000 PSI, fiber).');out.push('<strong>Base:</strong> 4 in. compacted crushed limerock ≈ '+(A*4/12*1.5/2000*1.15).toFixed(1)+' tons (1.5 t/cu yd, 15% compaction).');out.push('<strong>Reinforcement:</strong> '+(th===6?'#4 rebar at 18 in.: about '+f(A*0.9)+' linear ft':'#3 rebar at 24 in. on chairs: about '+f(A*1.0)+' linear ft for vehicle slabs; fiber for walks and patios')+'.');out.push('<strong>Joints:</strong> control joints at 8 to 10 ft, cut the same day; isolation joint at the house and pool.');}
else if(t==='ov'){out.push('<strong>Overlay:</strong> only if the slab passes the six tests (/compare/resurface-vs-replace-pool-deck/). Material ≈ '+f(A*0.25)+' lb of polymer-modified overlay at 1/8 in.');}
else{var bd=(t==='pd')?6:4;out.push('<strong>Base:</strong> '+bd+' in. compacted in '+(bd===6?'3':'2')+' lifts ≈ '+(A*bd/12*1.5/2000*1.15).toFixed(1)+' tons of crushed limerock or recycled concrete.');out.push('<strong>Bedding sand:</strong> 1 in. ≈ '+(A/12/27).toFixed(2)+' cu yd concrete sand.');out.push('<strong>Pavers:</strong> about '+f(A/ps*1.07)+' units at '+ps+' sq ft each, including 7% for cuts'+(t==='tr'||t==='mb'?' (order 10% for natural stone)':'')+'.');out.push('<strong>Polymeric sand:</strong> about '+Math.ceil(A/80)+' bags (50 lb) for '+(ps<1?'narrow':'wide')+' joints.');out.push('<strong>Edge restraint:</strong> '+f(2*(L+W))+' linear ft; concrete curb on any edge a truck or surge can reach.');}
var lo=P.lo,hi=P.hi;var mult=1;if(isl){mult=1.1;}var dlo=demo?2:0,dhi=demo?4:0;
out.push('<strong>Planning range ('+P.n+', installed):</strong> $'+f(A*lo*mult)+' to $'+f(A*hi*mult)+(demo?' plus demolition $'+f(A*dlo)+' to $'+f(A*dhi):'')+(isl?' (island logistics +10% applied; range is 5 to 15%)':'')+'. Excludes permit fees, drains, coping, culverts and lighting.');
out.push('Ranges compiled September 10, 2026 from published Sarasota-area pricing; not a quote.');
root.querySelector('.out').innerHTML='<ul><li>'+out.join('</li><li>')+'</li></ul>';};'''
    body = cap("What does the Concrete and Paver Calculator compute?",
               "From length and width it gives square footage, cubic yards of concrete with 10 percent waste at 4 or 6 inches, base tonnage at 4 or 6 inches compacted, rebar length by slab type, paver count for five common sizes with 7 percent for cuts, polymeric sand bags, edge restraint length, and an installed planning range from the September 10, 2026 cost tables, with demolition and island logistics as options.",
               p("Quantities are geometry and standard yields; the cost range is the same one the pricing guides use, dated. Print the result to keep it with your estimate requests."))
    body += form + f'<script>{js}</script>'
    body += sec("Yields and assumptions", ul(["Concrete: area × thickness ÷ 27 = cubic yards; 10% waste for forms and grade.", "Base: crushed limerock or recycled concrete at 1.5 tons per loose cubic yard, plus 15% for compaction.", "Rebar: #3 at 24 in. both ways ≈ 1 linear foot per square foot; #4 at 18 in. ≈ 0.9.", "Pavers: 7% overage for cuts; natural stone 10% and keep spares.", "Polymeric sand: one 50-lb bag per roughly 80 sq ft of standard joints.", "Prices: pricing guides, September 10, 2026."]))
    body += sec("Related", cards([("/pricing/concrete/", "Concrete cost guide", "Where the concrete ranges come from."), ("/pricing/pavers/", "Paver cost guide", "Where the paver ranges come from."), ("/compare/4-inch-vs-6-inch/", "4 or 6 inches", "Which thickness.")]))
    body += reviewed("September 10, 2026")
    return pg("concrete-paver-calculator", "Concrete & Paver Calculator: Yards, Base, Pavers, Cost (Sarasota)", "Calculate cubic yards of concrete, base tonnage, rebar, paver count, polymeric sand and edge restraint for any dimensions, plus a dated installed cost range for Sarasota County with demolition and island options. Printable.",
              "Concrete and Paver Calculator", "Quantities from geometry, a cost range from the dated pricing tables, and a print button so the numbers travel with your estimate requests.", body)


def calendar():
    normals = [("January", 72.5, 52.3, 2.79), ("February", 74.9, 54.6, 1.92), ("March", 78.2, 58.1, 2.85), ("April", 82.5, 62.7, 2.46), ("May", 87.5, 68.2, 2.58), ("June", 90.0, 73.6, 7.05), ("July", 91.1, 75.2, 7.39), ("August", 91.5, 75.3, 9.11), ("September", 90.2, 74.1, 6.00), ("October", 86.3, 68.3, 2.76), ("November", 80.0, 60.1, 1.81), ("December", 75.2, 55.2, 2.33)]
    opts = "".join(f'<option value="{i}">{m[0]}</option>' for i, m in enumerate(normals))
    form = f'''<form class="tool" data-tool="cal" id="cal"><fieldset><label for="cal-m">Month</label><select id="cal-m" name="m">{opts}</select></fieldset><div class="out" aria-live="polite">Pick a month.</div></form>'''
    data_js = "[" + ",".join(f'["{m}",{hi},{lo},{pr}]' for m, hi, lo, pr in normals) + "]"
    js = r'''window.SCTools=window.SCTools||{};window.SCTools.cal=function(root){var N=''' + data_js + r''';var i=parseInt(root.querySelector('[name="m"]').value)||0;var m=N[i];var hi=m[1],lo=m[2],pr=m[3];var out=['<strong>'+m[0]+'</strong> (NOAA 1991–2020 normals, Sarasota-Bradenton Airport): average high '+hi+' °F, low '+lo+' °F, precipitation '+pr+' in.'];
var wet=pr>=5;var hot=hi>=88;out.push('<strong>Rain pattern:</strong> '+(wet?'wet season; most rain falls in afternoon storms. Pour in the morning and plan to be finished and covered by 1 p.m.':'dry season; storms are the exception. Full-day pours are realistic; watch cold fronts for wind and fast drying.'));
out.push('<strong>Start time:</strong> '+(hot?'7 a.m. Concrete placed after 10 a.m. in this heat sets before the finishers reach the far end; use a retarder or evaporation reducer if the truck is late.':hi>=80?'7 to 8 a.m.; normal set times.':'8 a.m. or later; cooler mornings slow the set and lengthen finishing.'));
out.push('<strong>Cure window:</strong> '+(hot?'evaporation is high; curing compound or wet cure for 7 days is not optional. Foot traffic 24 h, cars 7 days, heavy loads 28.':'moderate evaporation; curing compound for 7 days. Foot traffic 24 h, cars 7 days, heavy loads 28. Low winter humidity on windy days can crack a slab faster than July heat.'));
out.push('<strong>Pavers:</strong> polymeric sand needs 24 to 48 dry hours after activation; '+(wet?'install joint sand only with a two-day dry forecast.':'most days qualify.'));
out.push('<strong>Sealing:</strong> surface must be dry through; '+(wet?'seal in a dry gap after a rain-free week.':'this is the season for sealing.'));
if(i>=5&&i<=10){out.push('<strong>Hurricane season</strong> (June 1 to Nov 30): see the storm season playbook before scheduling island work in August to October.');}
if(i<=3||i===11){out.push('<strong>Snowbird season:</strong> crews are fullest January to April; book two months ahead.');}
root.querySelector('.out').innerHTML='<ul><li>'+out.join('</li><li>')+'</li></ul>';};'''
    body = cap("What is the best month to pour concrete in Sarasota?",
               "November through April, by the NOAA 1991 to 2020 normals: highs of 72 to 83 degrees and under 3 inches of rain a month, so full-day pours and long finishing windows are realistic. June through September brings highs above 90 and 6 to 9 inches of monthly rain, almost all in afternoon storms; pours still happen, but they start at 7 a.m. and are covered by early afternoon.",
               p("The calendar below turns the monthly normals into a start hour, a rain plan and a cure note. It uses monthly normals, not a forecast; check the day's forecast the evening before any pour."))
    body += form + f'<script>{js}</script>'
    body += sec("NOAA normals used", table(["Month", "High °F", "Low °F", "Precipitation (in)"], [[m, hi, lo, pr] for m, hi, lo, pr in normals], "NOAA NCEI U.S. Climate Normals 1991–2020, station USW00012871 Sarasota-Bradenton Airport, read September 10, 2026"))
    body += sec("Related", cards([("/guides/cure-times-and-rain/", "Cure times and rain", "What rain in the first two hours does."), ("/coastal/storm-season-playbook/", "Storm season playbook", "June to November on the islands."), ("/guides/snowbird-project-guide/", "Snowbird project guide", "Scheduling around the season.")]))
    body += reviewed("September 10, 2026")
    return pg("pour-calendar", "Sarasota Pour Calendar: Best Months to Pour Concrete (NOAA)", "Month-by-month guide to pouring concrete and laying pavers in Sarasota from NOAA 1991–2020 normals: temperature, rainfall, start hour, cure window, joint-sand and sealing conditions, hurricane and snowbird seasons.",
              "Pour Calendar: month by month, from NOAA normals", "Temperature, rainfall, the hour to start and the cure window for every month of the year in Sarasota.", body)


def get_pages():
    return [hub(), selector(), finder(), calculator(), calendar()]
