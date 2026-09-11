# 03 — Keyword research

Data: 2026-09-10.

## 1. Fonte com volume (VOLUME)

Planilha `pesquisa_emd_concreto_florida_google_ads_2026-09-07.xlsx`, aba "Google Ads Keywords": plano autenticado do Google Ads Keyword Planner, localização **Florida, United States**, rede Google, período 01/08/2025–31/07/2026. "Média mensal" agrega variantes próximas e é arredondada; célula "—" = sem volume mensurável no plano (nunca zero). CPC e competição são sinais de intenção comercial, não de dificuldade.

| Keyword | Média mensal | Competição (índice) | CPC baixo–alto (US$) |
|---|---|---|---|
| sarasota concrete | 50 | High (97) | 4,00–13,68 |
| sarasota concrete contractor | 50 | Medium (63) | 4,51–22,60 |
| sarasota concrete repair | 50 | Medium (53) | — |
| sarasota concrete company / driveway / patio | — | — | — |
| venice concrete | 50 | Medium (52) | — |
| venice concrete contractors | 50 | High (78) | — |
| north port concrete | 50 | Low (31) | — |
| north port concrete contractors | 50 | High (100) | — |
| port charlotte concrete | 50 | Low (22) | — |
| concrete port charlotte | 50 | High (92) | 3,51–12,00 |
| nokomis concrete | 50 | — | — |
| bradenton concrete | 50 | High (82) | — |
| palmetto concrete | 50 | Low (31) | — |
| parrish concrete | 50 | Low (10) | — |
| sarasota county concrete (todas as variantes), lakewood ranch concrete (todas), englewood concrete (todas), punta gorda concrete (todas), osprey concrete (todas), siesta key concrete (todas), ellenton, myakka city | — | — | — |

Leitura: as strings "cidade + concrete" têm demanda pequena e concentrada em Sarasota, Venice, North Port, Port Charlotte e Nokomis. Nenhuma string com pavers/pool deck + cidade está na planilha (não foi pesquisada no EMD). O volume comercial real está nas famílias genéricas geolocalizadas.

## 2. Famílias obrigatórias — status

A exportação do Keyword Planner com localização por cidade (Sarasota, Sarasota County, cada Tier 1/Tier 2, metro North Port–Sarasota–Bradenton) ficou **BLOCKED** nesta execução (sem sessão autenticada). O arquivo `03-keywords.csv` lista cada família com a URL proprietária e o rótulo de evidência disponível hoje (`VOLUME` só onde a planilha EMD mediu; `COMPETITOR` quando a família aparece em title/H1/FAQ de concorrentes auditados; `EXPERT-GAP` quando é lacuna editorial). Assim que o CSV bruto do Keyword Planner existir, a coluna `volume_geo` é preenchida sem mudar a arquitetura.

Famílias e URL proprietária (resumo):

| Família | URL proprietária | Evidência hoje |
|---|---|---|
| concrete contractor(s) / company / near me + Sarasota | `/` e `/concrete/` | VOLUME (50) + COMPETITOR (9 sites com esse H1) |
| concrete driveway (cost, replacement, contractor) | `/concrete/driveways/`, `/pricing/concrete/` | COMPETITOR (concrete-sarasotafl, prince, adam case) |
| concrete repair / leveling / spalling | `/concrete/repair/` | VOLUME (sarasota concrete repair 50) |
| pool deck resurfacing / cool deck / kool deck | `/concrete/resurfacing/`, `/compare/cool-deck-vs-pavers/` | COMPETITOR (paradigm, protile, garage king, elite, creative resurfacing) |
| concrete pool deck | `/concrete/pool-decks/` | COMPETITOR |
| pavers near me / paver installation / paver contractor | `/pavers/` | COMPETITOR (paver mac, prime pavers, sarasotaflpavers, tuscan) |
| pool deck pavers / travertine pool deck / shellstone / marble / porcelain | `/pavers/pool-decks/`, `/pavers/travertine-shellstone/`, `/pavers/marble-porcelain/` | COMPETITOR (tuscan, infinite pool finishes, gettle) |
| paver driveway (cost, vs concrete) | `/pavers/driveways/`, `/compare/concrete-vs-pavers-driveway/` | COMPETITOR |
| paver sealing / cleaning / re-sanding (cost, how often) | `/pavers/sealing/`, `/coastal/maintenance-calendar/` | COMPETITOR (patrick's, sarasota paver sealing, total shield, sand and seal) |
| paver repair / sinking pavers / storm | `/pavers/repair-storm-restoration/`, `/coastal/post-storm-restoration/` | EXPERT-GAP (nenhum concorrente local) |
| stamped concrete (cost, vs pavers) | `/concrete/stamped/` | COMPETITOR |
| concrete slab / pad (shed, AC, generator, boat lift) | `/concrete/slabs/` | COMPETITOR (eric schroeder "residential slabs") |
| sidewalks / walkways | `/concrete/sidewalks-walkways/`, `/pavers/walkways-steps/` | COMPETITOR |
| pool deck too hot / coolest pool deck / slip resistant | `/coastal/pool-deck-surface-temperature-study/`, `/compare/pool-deck-surfaces-heat/` | EXPERT-GAP (só blogs genéricos de FL; nenhum com medição local) |
| permit / HOA approval / flood zone / 50% rule / coastal setback / sea turtle lighting | `/permits/…`, `/hoa/…`, `/permits/flood-zones-50-percent-rule/`, `/permits/sea-turtle-lighting/` | EXPERT-GAP |
| salt damage concrete / hurricane damage pavers / storm surge pool deck | `/coastal/…` | EXPERT-GAP |
| thickness / PSI / rebar vs mesh / cure time / cracks | `/compare/4-inch-vs-6-inch/`, `/compare/rebar-vs-fiber/`, `/guides/…` | COMPETITOR (FAQ genéricas) |
| efflorescence / polymeric sand / weeds / pressure washing / sealer types | `/guides/…`, `/compare/sealer-types-coastal/` | COMPETITOR (blogs de sealing) |
| cement driveway / cement patio | `/concrete/driveways/`, `/concrete/patios-lanais/` (sinônimo no texto) | — |
| epoxy garage floor | sem página (catálogo não confirmado) | COMPETITOR (garageexperts, paradigm) — registrado para decisão |
| termos em espanhol | não priorizado (Sarasota County ~10% hispânico no ACS; confirmar) | — |

Excluídos: ready-mix, delivery, jobs/salary, precast, pumping, equipment rental, seawall construction.

## 3. Tendência e sazonalidade

Google Trends (DMA Tampa–St. Petersburg–Sarasota, 5 anos) **BLOCKED** — sem acesso à interface. Proxy usado: normais climáticas NOAA e padrão de ocupação (jan–abr pico de população); registrado como inferência, não como dado de busca.
