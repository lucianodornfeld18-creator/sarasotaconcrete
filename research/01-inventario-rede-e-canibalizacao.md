# 01 — Inventário da rede e resolução de canibalização

Data: 2026-09-10. Fontes: arquivos locais listados na seção 2 do prompt, lidos integralmente sem sobrescrever.

## 1. Ativos inspecionados

| Ativo | Caminho | O que foi verificado |
|---|---|---|
| Lakewood Ranch Concrete (build atual) | `C:\Users\luana\Documents\Codex\Projects\lakewoodranchconcretefl` (git, último commit "Swap phone number to (941) 263-0948", remote github.com/lucianodornfeld18-creator/lakewoodranchfl) | `_data.py`: 10 serviços + 2 extras (`/pavers/`, `/concrete-walkways/`, `/concrete-garage-floors/`), 24 cidades (12 Tier 1 + 12 Tier 2), reviews reais (5), checklist "42-Point Install Standard", `llms.txt` declarando raio de ~60 milhas e Sarasota County na área |
| Lakewood Ranch (cópia SSD) | `C:\Users\luana\SSD-Antigo-Lucia\Projetos\lakewoodranchconcretefl` | versão de 2026-07-29; a do Codex (2026-08-20) é a mais recente e foi usada como referência |
| GCM Best Services Corp | `C:\Users\luana\SSD-Antigo-Lucia\gcm-site` | catálogo real de 8 serviços (Luxury Pavers, Architectural Concrete, Custom Driveways, Pool Decks, Patios & Outdoor Living, Retaining Walls, Artificial Turf, Outdoor Lighting); `/es/`, `/pt/`; schema Organization + LocalBusiness com endereço Orlando 32819, rating 4.9/59; fontes Playfair Display + Inter |
| Ocoee Concrete | `C:\Users\luana\SSD-Antigo-Lucia\Projetos\ocoeeconcrete` | páginas `/concrete/` (driveways, patios, stamped, repair, resurfacing, commercial, parking-lot + 12 cidades), `/pavers/` (driveways, patios, pool-decks, travertine, walkways, sealing, repair + cidades), `/epoxy-floors/`, `/stucco/`, `/sidewalks/`, `/foundation-installation/`, `/retaining-walls/`; fontes Outfit + Lato; paleta laranja #D05A1E / marrom |
| Windermere Concrete | `C:\Users\luana\SSD-Antigo-Lucia\Projetos\windermereconcrete` | 12 serviços (inclui `driveway-extensions`, `travertine-pool-decks`, `paver-sealing-repair`), 24 cidades, checklist "38-Point"; fontes Fraunces + Figtree; paleta pine/lake navy/linen |
| Groveland Concrete | `C:\Users\luana\Documents\Codex\2026-09-07\groveland-concrete` | pipeline `site/build.py` → `dist/`, `templates.py`, `_seo.py`, `_photos.py`, Pages Function `/api/contact` com Turnstile/honeypot/KV rate limit, Worker `contact-email` (send_email binding), fontes self-hosted (Fjalla One, IBM Plex), CSP com hashes gerados no build. **Base técnica adotada**; texto e design não reutilizados |
| Planilha EMD | `...\emd-concreto-fl\pesquisa_emd_concreto_florida_google_ads_2026-09-07.xlsx` | 846 consultas do Keyword Planner autenticado (Florida, Google, 01/08/2025–31/07/2026); linhas do corredor Suncoast extraídas para o arquivo 03 |
| Fotos | `C:\Users\luana\Projetos\Concreto Fotos` (26 arquivos) | 18 fotos reais + 8 renderings; processadas em `images/process_photos.py` (EXIF, strip de metadados, WebP 480/960/1600); alt text descreve o que se vê, nunca a cidade |
| Prompts irmãos | `05-PROMPT-LAKEWOOD-RANCH-CONCRETE-FL.md`, `06-PROMPT-BRADENTON-CONCRETE-FL.md` | Lakewood Ranch fica com East Manatee (Lakewood Ranch, University Park, Parrish, Ellenton, Myakka City, Palmetto, Fruitville "e partes de Sarasota/Manatee"); Bradenton fica com Bradenton, Palmetto, Ellenton, Bayshore Gardens, Cortez, Anna Maria Island e "Longboat Key" como seed a validar |

Observação sobre Longboat Key: o prompt 06 lista Longboat Key como seed do Bradenton; o prompt 09 (este) atribui Longboat Key **inteira** a Sarasota. Registrado no registry como decisão deste hub (09 é posterior). Fruitville aparece no seed do Lakewood Ranch; pelo prompt 09 pertence a Sarasota County e portanto a este hub. Ambos os pontos estão em OWNER-INPUTS para confirmação.

## 2. URLs do Lakewood Ranch que competem com este hub (inventário medido)

Medição: HTML local, texto do body sem scripts, 2026-09-10.

### 2.1 City hubs (6)

| URL | Palavras | Title | H1 |
|---|---|---|---|
| `/sarasota/` | 2.994 | Paver & Concrete Contractor Sarasota, FL | Paver & concrete contractor. Sarasota, Florida. |
| `/venice/` | 2.978 | Paver & Concrete Contractor Venice, FL \| Lakewood Ranch Concrete | idem, Venice |
| `/north-port/` | 3.032 | Paver & Concrete Contractor North Port, FL | idem |
| `/osprey/` | 2.929 | … Osprey, FL \| Lakewood Ranch Concrete | idem |
| `/nokomis/` | 2.922 | … Nokomis, FL \| Lakewood Ranch Concrete | idem |
| `/longboat-key/` | 2.994 | Paver & Concrete Contractor Longboat Key, FL | idem |

H2 em template idêntico nas 6 (e nas 24): "Local concrete & paver crew. Real [City] addresses." / "Why concrete & pavers in [City] aren't the same as anywhere else." / "Every surface we pour & pave, in [City]." / "Our 42-Point Install Standard for [City] Homes" / "Where we work in [City]." / "Five-star rated by local homeowners." / "Questions [City] homeowners ask, weekly." / "Ready for a real estimate, on a real [City] project?"

### 2.2 City × service (60 URLs)

10 serviços × 6 cidades: `/concrete-driveways/`, `/concrete-patios/`, `/concrete-pool-decks/`, `/stamped-concrete/`, `/concrete-slabs/`, `/concrete-resurfacing/`, `/paver-driveways/`, `/paver-patios-walkways/`, `/pool-deck-pavers/`, `/paver-sealing/` × `sarasota`, `venice`, `north-port`, `osprey`, `nokomis`, `longboat-key`. Amostras: `/concrete-driveways/sarasota/` 3.104 palavras, `/pool-deck-pavers/venice/` 3.110, `/concrete-pool-decks/sarasota/` 3.090. H2 em template: "[Service] in [City], done the right way." / "What every [service] project includes." / "Our 42-Point Install Standard for [City] Homes" / "Five expensive [service] mistakes to avoid in [City]." / "[Service] in [City] — the questions buyers search."

### 2.3 Charlotte County no Lakewood Ranch

`/port-charlotte/` (2.995 palavras) e `/punta-gorda/` (3.011) + 20 city×service + 12 posts de custo. Port Charlotte está a 36,8 mi de Sarasota (dentro do raio) e passa a este hub; Punta Gorda (41 mi) fica com o Lakewood Ranch.

### 2.4 Posts de custo

48 posts `/blog/<serviço>-cost-<cidade>/` para as 8 cidades acima (6 serviços: concrete-driveways, paver-driveways, concrete-patios, concrete-pool-decks, pool-deck-pavers, stamped-concrete). Os 36 de Sarasota County + os 6 de Port Charlotte migram (42); os 6 de Punta Gorda ficam.

### 2.5 `llms.txt` do Lakewood Ranch

Declara "Sarasota County" e "Charlotte County" na área e lista Sarasota, Venice, North Port, Port Charlotte, Punta Gorda, Osprey, Nokomis e Longboat Key como cidades servidas. Precisa ser reescrito quando os 301 entrarem.

## 3. Matriz de canibalização aplicada

Regra: uma intenção `cidade × serviço` tem uma única URL proprietária na rede. Este hub é o proprietário de todo o Sarasota County e do Charlotte County dentro do raio (Englewood, Manasota Key, Grove City, Placida, Rotonda West, Port Charlotte).

O passo 1 da matriz (exportar Search Console dos últimos 16 meses por URL) está **BLOCKED**: a propriedade `lakewoodranchconcretefl.com` não existe no Windsor.ai e não há outro acesso ao Search Console nesta sessão. Por isso a decisão de cada URL fica **condicionada** aos dados, com a regra já escrita:

| Grupo | URLs | Decisão condicionada | Quando |
|---|---|---|---|
| A — city hubs de Sarasota County | `/sarasota/`, `/venice/`, `/north-port/`, `/osprey/`, `/nokomis/`, `/longboat-key/` | < 50 impressões/mês e 0 leads → 301 para `/areas/<cidade>/` deste hub. Com tráfego/leads → manter 90 dias com intro reescrita ("serving Sarasota from Lakewood Ranch"), remover blocos de preço e FAQ que este hub passa a possuir, canonical autorreferente; reavaliar em 90 dias | só depois que este hub estiver indexado (checar `site:sarasotaconcrete.com` + Search Console) |
| B — city×service de Sarasota County (60) | `/<serviço>/<cidade>/` | mesma regra; mapa 301 pronto abaixo (para combos que este hub publica agora); combos sem página equivalente aqui vão para o serviço-pai deste hub (`/concrete/<serviço>/` ou `/pavers/<serviço>/`) | mesma janela |
| C — Port Charlotte (hub + 10 city×service + 6 posts) | `/port-charlotte/…` | mesma regra; destino `/areas/port-charlotte/` e city×service Tier 2 | mesma janela |
| D — posts de custo (42) | `/blog/<serviço>-cost-<cidade>/` | 301 para o cost guide deste hub (`/pricing/concrete/`, `/pricing/pavers/`, `/pricing/pool-decks/`) | mesma janela |
| E — Punta Gorda | `/punta-gorda/…` | permanece no Lakewood Ranch (41 mi, fora do raio) | — |
| F — `llms.txt`, sitemap, página de áreas do Lakewood Ranch | — | reescrever removendo Sarasota County e Port Charlotte da área declarada | junto com os 301 |

Nunca haverá duas URLs da rede com mesmo title, H1 ou primeira frase: os titles deste hub seguem o padrão `/concrete/<serviço>/<cidade>/` com fórmula "X in City, FL – Cost & Permits" e o Lakewood Ranch usa "Paver & Concrete Contractor City, FL"; verificado no build por comparação de titles/H1 (script `site/qa_network_similarity.py`).

### 3.1 Mapa 301 (Lakewood Ranch → Sarasota Concrete)

Arquivo: `site/network/redirects-lakewoodranch-to-sarasota.txt` (formato `_redirects` do Cloudflare Pages, pronto para colar no Lakewood Ranch quando a janela abrir). Resumo:

- `/sarasota/` → `https://sarasotaconcrete.com/areas/sarasota/`; `/venice/` → `/areas/venice/`; `/north-port/` → `/areas/north-port/`; `/osprey/` → `/areas/osprey/`; `/nokomis/` → `/areas/nokomis/`; `/longboat-key/` → `/areas/longboat-key/`; `/port-charlotte/` → `/areas/port-charlotte/`.
- `/concrete-driveways/<c>/` → `/concrete/driveways/<c>/` (Sarasota, Venice, North Port, Osprey, Nokomis, Port Charlotte) e → `/concrete/driveways/` para Longboat Key (sem city×service de concreto lá).
- `/pool-deck-pavers/<c>/` → `/pavers/pool-decks/<c>/` (Sarasota, Venice, Osprey, Nokomis, Longboat Key, North Port, Port Charlotte).
- `/concrete-pool-decks/<c>/` → `/concrete/pool-decks/<c>/` (Sarasota, Venice, Port Charlotte) e → `/concrete/pool-decks/` nos demais.
- `/paver-driveways/<c>/` → `/pavers/driveways/<c>/` (Sarasota, Osprey, Nokomis, Longboat Key, Port Charlotte) e → `/pavers/driveways/` nos demais.
- `/concrete-patios/<c>/` → `/concrete/patios-lanais/`; `/stamped-concrete/<c>/` → `/concrete/stamped/`; `/concrete-slabs/<c>/` → `/concrete/slabs/`; `/concrete-resurfacing/<c>/` → `/concrete/resurfacing/`; `/paver-patios-walkways/<c>/` → `/pavers/patios-lanais/`; `/paver-sealing/<c>/` → `/pavers/sealing/<c>/` (Sarasota, Siesta Key não existe no LWR; Longboat Key) ou `/pavers/sealing/`.
- `/blog/concrete-driveways-cost-<c>/`, `/blog/paver-driveways-cost-<c>/`, `/blog/concrete-patios-cost-<c>/`, `/blog/stamped-concrete-cost-<c>/` → `/pricing/concrete/` ou `/pricing/pavers/`; `/blog/concrete-pool-decks-cost-<c>/` e `/blog/pool-deck-pavers-cost-<c>/` → `/pricing/pool-decks/`.

## 4. Fingerprints da rede — lista de bloqueio usada no QA

Frases/estruturas proibidas neste hub (checadas por `site/qa_style.py`): "38-Point", "42-Point", qualquer "N-Point" como marca, "Our Four Promises", "Straight answers before you spend a dollar", "in plain English", "Built Local Since", "Poured right. Built to last.", "Every surface we pour & pave", "24 cities. One crew.", "Real Sarasota addresses", "Be the first", "Questions … homeowners ask, weekly", "Concrete Specialists Serving", "Prices in … (2026)", "Neighborhoods & ZIP Codes We Serve", "done the right way", "the questions buyers search", "Five expensive … mistakes", "Where we work in", "Local concrete & paver crew"; URL `/<serviço>/<cidade>/` sem pilar; `/concrete/<cidade>/`; blog `<serviço>-cost-<cidade>`; fontes Outfit, Inter, Lato, Fraunces, Figtree, Fjalla One, IBM Plex, Playfair Display; paletas gold/cream (LWR), emerald/navy (Windermere), clay/parchment/ochre (Groveland), orange/brown (Ocoee), gold/black (GCM).

Adotado aqui: Bricolage Grotesque + Instrument Sans + DM Mono; paleta "Bayline" (tide blue #0F4C81, ink #14202B, shell #F7F4EE, sand #ECE6DA, seaglass #CDE7E1, coquina #B8552E só como acento pontual). Nenhum hub irmão usa azul.

## 5. Catálogo — decisão de união e o que fica pendente

| Item | Fonte que confirma | Decisão |
|---|---|---|
| Concrete driveways, patios/lanai slabs, pool decks, stamped, slabs & pads, sidewalks/walkways, repair, resurfacing | GCM (Custom Driveways, Pool Decks, Patios, Architectural Concrete) + Lakewood Ranch (10 serviços + walkways) + Ocoee | página |
| Architectural concrete (honed, board-formed) | GCM | página, com a capacidade no Suncoast marcada para confirmação |
| Commercial concrete / parking lots / condo pool decks | só Ocoee (legado); não está na GCM | **sem página** até confirmação; condo pool decks tratados dentro de `/pavers/pool-decks/` e `/hoa/barrier-island-condos/` como serviço residencial/associação |
| Foundations, footings, seawall caps, retaining walls estruturais | nenhuma fonte + exige licença | **sem página, sem menção** |
| Paver driveways, patios/lanais, pool decks, travertine/shellstone, marble/porcelain (Belgard Luxury), walkways/steps, sealing/cleaning/re-sanding, repair, retaining/seat walls decorativas, fire pits, outdoor kitchens, artificial turf, outdoor lighting | GCM (Luxury Pavers, Patios & Outdoor Living, Retaining Walls, Artificial Turf, Outdoor Lighting) + Lakewood Ranch + Ocoee | página |
| Epoxy / polyaspartic garage floors | só Ocoee; registry marca como não confirmado (não está na GCM) | **sem página** até confirmação (OWNER-INPUTS) |
| Stucco | registry: `not_confirmed_do_not_use` | **excluído** |
