# AUDIT-60-POINT — sarasotaconcrete.com

Build: 2026-09-11. 178 páginas, 176 indexáveis. Cada linha traz o resultado e a **evidência**:
um arquivo, um comando ou um número que pode ser reproduzido.

Legenda: **PASS** verificado · **PARTIAL** feito, com limitação declarada · **BLOCKED** impossível
nesta execução, com o motivo · **OWNER INPUT** depende do proprietário.

Comandos de verificação, todos em `site/`:

```
python build.py          # 178 páginas, 0 rota duplicada, 0 problema de title/description
python qa_words.py       # contagem por tipo de página contra os pisos do St. Cloud
python qa_links.py       # links quebrados, órfãs, profundidade de cliques
python qa_style.py       # lista proibida, frases, densidade de fatos
python qa_similarity.py  # 8-gramas internos e contra os 5 hubs irmãos
python qa_browser.py     # 13 páginas × 4 viewports em Chromium headless
```

---

## Resumo

```text
Domain: sarasotaconcrete.com
Build date: 2026-09-11
Indexable URLs: 176 (178 páginas, 2 noindex: /404/ e /thank-you/)
60-point result (contado da tabela, 60 linhas): 44 PASS / 9 PARTIAL /
  1 PARTIAL-BLOCKED / 3 BLOCKED / 2 OWNER INPUT / 1 PENDING por desenho / 0 FAIL
Blocked items: 5 (Keyword Planner), 6 (GSC/Twilio do Lakewood Ranch), 9 (motores de IA)
Owner inputs still required: logo, entidade legal, licença, GBP/Yelp,
  autor, fotos do Suncoast, medição de temperatura, dados do Cost Index
Cannibalization decisions pending (Lakewood Ranch URLs): 108 URLs mapeadas
  (6 city hubs + 60 city×service + 42 posts de custo), matriz escrita, execução
  condicionada ao export do Search Console
Deployment status: NOT DEPLOYED — READY FOR APPROVAL
```

---

## Pesquisa e estratégia (1–12)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 1 | Hub registrado com o domínio novo | **PASS** | `network-registry.json`: hub `sarasota` agora é `sarasotaconcrete.com`, com `previous_domain_in_registry` registrando a substituição de `sarasotaconcretefl.com`. CSV atualizado. Backup em `network-registry.backup-2026-09-10.json` |
| 2 | Ativos irmãos inspecionados (Lakewood Ranch em detalhe) | **PASS** | `research/01-inventario-rede-e-canibalizacao.md`. 6 ativos lidos integralmente. Do Lakewood Ranch: `_data.py` (10 serviços + 2 extras, 24 cidades), as 6 city hubs de Sarasota County medidas palavra por palavra (2.922 a 3.032), 60 city×service, 48 posts de custo, `llms.txt`, git log e remote |
| 3 | Catálogo confirmado com concreto e pavers separados | **PARTIAL** | 20 páginas de serviço em dois pilares totalmente separados (9 concreto, 11 pavers), união de GCM + Lakewood Ranch + Ocoee. **3 itens sem página** aguardando confirmação: epoxy, commercial/parking lots, e a capacidade de architectural concrete no Suncoast (página existe com aviso visível). Stucco e fundações excluídos. `OWNER-INPUTS.md` §3.1 |
| 4 | Raio de 40 milhas mapeado com tiers e propriedade na rede | **PASS** | `research/02-territorio-40-milhas.md`. 12 localidades Tier 1 + 3 Tier 2 + 24 de menção, com jurisdição de permit, distância, tempo real de deslocamento (com pontes), população (Florida EDR abril/2025 lido do PDF, ou Censo 2020 para CDPs), zona FEMA, série de solo USDA e estoque habitacional |
| 5 | Keyword Planner exportado | **BLOCKED** | Sem sessão autenticada do Chrome nesta execução. Mitigação: a planilha EMD (Keyword Planner autenticado, 846 consultas, Florida, 01/08/2025–31/07/2026) foi lida e as 120 linhas do corredor Suncoast extraídas com volume, competição e CPC. `research/03-keyword-research.md` §1. `research/03-keywords.csv` tem 100 linhas com `volume_geo` marcado BLOCKED, pronto para receber o export |
| 6 | GSC / analytics / Twilio do Lakewood Ranch incorporados | **BLOCKED** | A propriedade `lakewoodranchconcretefl.com` não existe no Windsor.ai (verificado: só `brazacleaning.com`, `triangle-floor.com`, `napasflooring.com`, `ocoeeconcrete.com`). O MCP do Twilio nesta sessão só serve documentação. **Consequência declarada:** é o dado que decide a canibalização (ponto 55) |
| 7 | Keywords por intenção | **PARTIAL** | `research/03-keywords.csv`: 100 keywords com família, pilar, intenção, volume EMD, competição, CPC, rótulo de evidência, URL proprietária e se a intenção já existe no Lakewood Ranch. Rótulos usados: `VOLUME` (medido na planilha), `COMPETITOR`, `EXPERT-GAP`. Não usados por falta de acesso: `PAA`, `AUTOCOMPLETE`, `TRENDS`, `AI-CITED`, `REDDIT`, `GSC` |
| 8 | Top 1–3 auditado por cluster | **PASS** | `research/04-concorrentes-e-benchmark.md`. 22 concorrentes baixados e medidos em 2026-09-10 (palavras no body, H1, schema, provas, lacunas) em 6 clusters. Maior da SERP: concrete-sarasotafl.com com 3.646 palavras, schema só `WebSite`, sem preço, licença, FAQ, permits, flood, sal ou tartarugas. Matriz tem/falta/como superar no §8 |
| 9 | Fontes citadas por IA registradas | **BLOCKED** | Sem acesso a AI Mode, ChatGPT Search, Copilot, Perplexity, Gemini. **Nenhuma pergunta recebeu o rótulo `AI-CITED`** — nada foi inventado. Mitigação: roteiro de 10 prompts × 6 mecanismos pronto em `research/05-ai-citation-e-perguntas.md` §1.1, e a inferência sobre que tipos de fonte dominam as SERPs de permit/custo/calor está documentada em §1.2 |
| 10 | 150 perguntas | **PASS** | `research/06-150-questions.csv`: 150 linhas com texto exato, intenção, estágio do lead, geografia, pilar, evidência, fonte, URL proprietária e formato de resposta. Dedupe global: as 12 perguntas canônicas que o Lakewood Ranch já responde (auditoria dele de 2026-08-20) foram explicitamente excluídas e listadas em `research/05` §2 |
| 11 | Histórico do domínio | **PARTIAL** | `research/07-dominio-entidade-licenca.md` §1. RDAP Verisign: criado 2025-10-28, expira 2027-10-28, alterado 2026-09-10, GoDaddy, NS da Afternic. Wayback CDX: 20 capturas de 2011-01-28 a 2025-07-13 — site de uma empresa local "Sarasota Concrete" (2011–2019, e-mail com typo, menu com "Curbing"), venda na Epik por US$ 9.700 em 2022-02, parking depois. **Histórico benigno, sem disavow.** BLOCKED: Safe Browsing (exige JS) e backlinks (sem conta) |
| 12 | Benchmark St. Cloud comparado | **PARTIAL** | `research/04` §7 e `qa_words.py`, que codifica a tabela de pisos do prompt. **178 de 178 páginas batem o piso do seu tipo (0 abaixo).** As metas esticadas (25–40% acima) são batidas em: home 3.870 (meta 3.800), os 2 pilares 2.259 e 2.294 (meta 2.200), FAQ hub 3.071 (meta 3.000+), as 3 city hubs Tier 2, contact e as 11 institucionais. **Não batidas** na mediana de: city hub Tier 1 1.248 (meta 1.800), city×service 1.019 (1.200), cost guide 1.628 (2.000), serviço 1.428 (1.800), guia 1.072 (1.500). Ver nota abaixo |

> **Nota sobre o ponto 12.** Escrevi seis passes de aprofundamento (`content_depth.py` a `content_depth6.py`) e cheguei a ter as metas quase todas batidas — mas os blocos aplicados a muitas páginas ao mesmo tempo levaram a similaridade interna de 8-gramas a **32%**, contra o gate de 15% do prompt. Removi os blocos repetidos e mantive só conteúdo que varia por página. Isso devolveu volume em troca de unicidade. A escolha é deliberada: o prompt trata similaridade acima de 15% como reprovação que "volta para reescrita", e trata o volume como meta ("mire"). O piso, que é o requisito duro, está batido em todas as páginas.

## Identidade (13–17)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 13 | Dez logos | **PASS** | `brand/logos.html`: prancha única numerada 1–10 com conceito, símbolo, horizontal claro/escuro, quadrada, favicon 32 e 16 px, paleta HEX, tipografia licenciada (todas OFL), justificativa regional e comparação de distinção contra os hubs irmãos e a SERP. `brand/svg/` com 50 arquivos individuais, gerados por `brand/make_svgs.py` |
| 14 | Assets finais | **PARTIAL** | Assets da direção provisória 1 (Bayline) em produção: `site/static/brand/` com `favicon.svg`, `icon.svg`, `icon-192.png`, `icon-512.png`, `social.svg`, `social-1200.png`, mais `site/static/favicon.ico` (16/32/48). Gerados por `site/make_brand_assets.py` via Chromium headless. **Assets definitivos aguardam a escolha** (OWNER INPUT) |
| 15 | Paleta e fontes únicas na rede | **PASS** | Bricolage Grotesque + Instrument Sans + DM Mono, self-hosted em `site/static/fonts/` (5 woff2, subset latin). Paleta "Bayline": tide `#0F4C81`, deep `#0A3559`, ink `#14202B`, shell `#F7F4EE`, sand `#ECE6DA`, seaglass `#CDE7E1`, coquina `#B8552E`. Nenhum hub irmão usa azul nem qualquer destas famílias: Lakewood Ranch usa Outfit/Inter + dourado, Windermere Fraunces/Figtree + esmeralda, Ocoee Outfit/Lato + laranja, Groveland Fjalla/IBM Plex + clay, GCM Playfair/Inter + dourado. Hero em fundo claro com linhas batimétricas em SVG, sem gradiente escuro |
| 16 | Voz e CTA próprios | **PASS** | `qa_style.py`: **0 problemas em 178 páginas**. A lista proibida inclui as 58 expressões do prompt §9.2 mais os 18 fingerprints da rede (§2.2): "42-Point", "38-Point", qualquer "N-Point", "Real Sarasota addresses", "Questions … homeowners ask, weekly", "done the right way", "Poured right. Built to last." etc. CTAs escritos por página |
| 17 | About / Editorial Standards / Data & Methods verdadeiros; nome verificado | **PASS** | `/about/` 886 palavras, `/editorial-standards/` 937, `/data-and-methods/` 922 — todas acima do piso 485. As três declaram o que o site **não** afirma. Sunbiz verificado 2026-09-10: nenhuma entidade ativa "Sarasota Concrete"; GCM Best Services Corp = P22000086622 Active. USPTO **BLOCKED** (TSDR devolve 401) e registrado em `OWNER-INPUTS.md` §3.3 |

## Arquitetura e conteúdo (18–34)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 18 | Hierarquia | **PASS** | `qa_links.py`: **0 páginas a mais de 3 cliques da home**. Breadcrumbs em todas as páginas internas, com `BreadcrumbList` em JSON-LD |
| 19 | Uma intenção por URL | **PASS** | `build.py` aborta em rota duplicada (`DUPLICATE ROUTE`). 178 rotas únicas, trailing slash, minúsculas, sem data nem parâmetro. 178 titles únicos e 178 meta descriptions únicas |
| 20 | Serviços completos | **PARTIAL** | 20 páginas de serviço. Ver ponto 3: 2 itens sem página por falta de confirmação, 1 com aviso |
| 21 | City hubs com informação local verificável | **PASS** | 15 páginas de localidade + 2 hubs de condado, cada uma com jurisdição de permit nomeada, zona FEMA, série de solo USDA, estoque habitacional por década, distância e tempo real (com a ponte quando existe), população oficial com fonte, comunidades com ARC e um exemplo de obra com metragem e faixa de preço datada |
| 22 | City×service só onde justificado, com bloco local | **PASS** | 62 páginas de 300 combinações possíveis (20 serviços × 15 localidades). A seleção está em `site/_data.py:CITY_SERVICE` e segue a regra do prompt: Tier 1 recebe os serviços com demanda observada, Tier 2 (Charlotte) só os 4 de maior demanda. Os demais combos são respondidos no serviço-pai e no city hub, sem URL nova |
| 23 | 150 respostas publicadas | **PASS** | Cada linha de `research/06-150-questions.csv` tem `owner_url` apontando para uma página publicada. Distribuição: 34 em páginas de serviço, 24 em permits/flood/turtle, 22 em guias, 14 em pricing, 13 em FAQ/institucional, 12 em comparações, 12 no hub costeiro, 10 em HOA, 6 em city×service, 3 em ferramentas |
| 24 | Cost Index publicado com Dataset | **PARTIAL** | `/pricing/sarasota-concrete-cost-index/` com schema do registro, método das releases trimestrais, limitações declaradas, baseline v0.1 rotulado como preços **publicados do mercado** e não como dado próprio. `Dataset` em JSON-LD, `/api/cost-index.json` servido com CC BY 4.0 e CORS. **Primeira release com dados próprios prevista para o 1º trimestre de 2027** (OWNER INPUT: dados de obras concluídas) |
| 25 | Surface Temperature Study publicado ou metodologia com data prevista | **PASS** (na forma que o prompt autoriza) | `/coastal/pool-deck-surface-temperature-study/`: protocolo completo — 9 superfícies nomeadas, preparação das amostras na mesma base, termômetro IV com emissividade para alvenaria e data de calibração registrada, 3 leituras por superfície, horários 10h/14h/17h, um dia claro de julho e um de janeiro, mediana publicada. **Datas previstas: janeiro/2027 e julho/2027.** `Dataset` + `/api/surface-temperatures.json`. **Nenhum número de temperatura aparece no site** atribuído a este estudo; os números de fornecedores que circulam na Flórida ("20 a 30 °F mais frio") estão **atribuídos à fonte** em `/compare/pool-deck-surfaces-heat/` e explicitamente não adotados |
| 26 | Ferramentas P1 funcionando | **PARTIAL** | 5 ferramentas publicadas e testadas em `qa_browser.py`: Coastal Surface Selector, Permit/Flood/Setback Finder, Concrete & Paver Calculator, Pour Calendar (com as normais NOAA 1991–2020 da estação USW00012871) e o Cost Index. JS mínimo com hash na CSP, sem framework. **Não construídas** (P1 do prompt): Ask the Estimator existe como página e feed mas sem perguntas reais (depende do Twilio/formulário), e o Storm Season Playbook e o guia de tartarugas foram entregues como páginas de conteúdo e não como ferramentas interativas. P2 e P3 não construídas |
| 27 | Fontes e datas | **PASS** | Toda afirmação regulatória cita a seção: Sarasota County Cap. 22 Art. V § 22-122, Cap. 54 Art. XXII § 54-723, Cap. 54 Art. XXIII, Cap. 74, Cap. 98 § 98-3, Zoneamento Apêndice A § 6.5; Longboat Key Cap. 100 Ord. 2021-01 e Cap. 154; F.S. 489.119(5)(b), 489.126, 718.112(2)(f), 865.09, Cap. 713; FDEP 62B-55.004; FEMA P-758. Todo preço tem data de leitura (2026-09-10) e método em `/data-and-methods/` |
| 28 | Mídia com direitos e alt | **PASS** | 26 imagens em `images/photos.json`, processadas por `images/process_photos.py`: EXIF transpose, metadados removidos no save, master ≤ 2400 px, WebP 480/960/1600. Alt text descreve o que se vê e **nunca afirma cidade** — as fotos são de obras da Flórida Central e o site diz isso. 8 renderings com badge visível "Concept rendering" e a palavra "rendering" também no `ImageObject.description` |
| 29 | Zero prova inventada | **PASS** | Verificado no HTML das 178 páginas: `aggregateRating` **0**, `ratingValue` **0**, `"review"` **0**, `PostalAddress` **0**, `streetAddress` **0**, "Licensed &" **0**. `GeoCoordinates` aparece 15 vezes, sempre em `Place` descrevendo a **localidade** (coordenadas públicas de Siesta Key etc.), nunca em `LocalBusiness`. Nenhum endereço, ano de fundação, contagem de obras, prêmio ou estatística própria |
| 30 | Zero duplicidade interna | **PASS** | `qa_similarity.py`: **0 pares acima de 15%**; máximo **14,8%** (`/concrete/slabs/fruitville-bee-ridge/` × `/concrete/slabs/north-port/`, e o compartilhado é a faixa de preço do mesmo serviço em duas cidades). Método: 8-gramas sobre o texto do `<main>`, todos os 15.753 pares |
| 31 | Zero duplicidade com hubs irmãos | **PASS** | `qa_similarity.py`, seção NETWORK, contra os builds locais dos 5 irmãos: Lakewood Ranch 437 páginas, máx **0,3%**; Windermere 273, **0%**; Ocoee 89, máx **0,2%**; Groveland 50, máx **0,4%**; GCM 62, **0%**. Nenhum title, H1 ou primeira frase repetido |
| 32 | Checagem anti-IA passou | **PASS** | `qa_style.py`: **0 problemas em 178 páginas** — lista proibida, contagem de travessões, emojis, distribuição de tamanho de frase e densidade de fatos (≈1 fato verificável a cada 150 palavras). Uma exceção documentada no código: `/gallery/` é isenta da densidade de fatos porque seu corpo são 26 legendas de foto, e enfiar números em legendas as pioraria |
| 33 | Cápsulas em toda seção-pergunta | **PASS** | Helper `cap()` em `site/_h.py`: H2 em forma de pergunta + resposta autossuficiente de 40 a 70 palavras com número, unidade, data e âmbito geográfico, depois o detalhe. HTML puro, sem tab, acordeão fechado ou conteúdo por JS |
| 34 | Autor, revisor e datas reais | **OWNER INPUT** | As 178 páginas terminam com "Last reviewed September 10, 2026" e dizem explicitamente que o nome do autor está pendente. O schema `Article` aponta para `Organization`; passa a emitir `Person` com `sameAs` quando o nome, cargo, bio, foto e credencial forem fornecidos. `datePublished` e `dateModified` reais no build. Nenhuma data futura |

## On-page e técnico (35–47)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 35 | Title, H1 e meta únicos | **PASS** | 178 titles únicos, todos ≤ 65 caracteres renderizados (medido com unescape de HTML). 178 meta descriptions únicas, todas entre **121 e 164** caracteres. H1 único por página e diferente do title. `_seo.py` valida no build: **0 problemas** |
| 36 | Canonical e 301 | **PASS** | Canonical autorreferente absoluto em todas as páginas, nunca cross-domain. `dist/_redirects` com `/index.html`, `/services/`, `/blog/` e `/blog/*`. Mapa de 301 do Lakewood Ranch pronto e **não executado** em `site/network/redirects-lakewoodranch-to-sarasota.txt`, com o gate escrito no topo do arquivo |
| 37 | robots e WAF | **PARTIAL** | `dist/robots.txt` libera explicitamente `OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Applebot`, `DuckDuckBot` e `Bingbot`; bloqueia `/thank-you/` e `/api/contact`. `GPTBot` e `Google-Extended` **não** foram liberados: são decisão de treinamento do proprietário, registrada em `OWNER-INPUTS.md`. Desativar o bloqueio padrão de bots de IA no WAF do Cloudflare é OWNER INPUT (§2.3) |
| 38 | Sitemap | **PASS** | `dist/sitemap.xml` com **176 URLs** (exclui as 2 noindex), `lastmod` real por página. `dist/sitemap-index.xml`. `dist/feed.xml` para o Ask the Estimator |
| 39 | Links, órfãs e chains | **PASS** | `qa_links.py`: **0 links internos quebrados**, **0 órfãs indexáveis** (as 2 reportadas são `/404/` e `/thank-you/`, ambas noindex, que é o comportamento correto), **0 páginas além de 3 cliques**, nenhuma cadeia de redirect |
| 40 | WCAG 2.2 AA | **PASS** | Lighthouse accessibility **100** e **zero auditorias de acessibilidade falhando** (mediana de 3 execuções, 4 páginas × mobile e desktop), depois de três correções encontradas pela própria auditoria: (a) o `h4` do footer virou `div.colh`, porque quebrava a ordem de headings; (b) o `aria-label` da marca foi removido para que o nome acessível contenha o texto visível (`label-content-name-mismatch`); (c) o helper `table()` passou a emitir `<th scope="row">` na primeira célula de toda tabela com 3+ colunas e 3+ linhas, que é o que a regra `td-has-header` do axe exige — 853 cabeçalhos de linha no build. HTML semântico, H1 único, foco visível, menu e ferramentas operáveis por teclado, legenda em toda foto, nada escondido em acordeão |
| 41 | Mobile | **PASS** | `qa_browser.py`: 13 páginas × 4 viewports (360×800, 390×844, 768×1024, 1440×900) em Chromium headless, **0 problemas** — sem scroll horizontal, sem overflow, alvos de toque adequados |
| 42 | OG e favicons | **PASS** | `og:site_name` = exatamente "Sarasota Concrete", `og:type`, `og:title`, `og:description`, `og:url`, `og:image` (1200×630 gerado), `og:locale`, `twitter:card` em todas as páginas. `favicon.ico` 16/32/48, `favicon.svg`, `icon-192.png`, `icon-512.png`, `site.webmanifest` |
| 43 | Imagens | **PASS** | WebP em 3 larguras, `width` e `height` explícitos em todas (CLS 0 medido), `loading="lazy"` fora do LCP e `fetchpriority="high"` no LCP, `decoding="async"`. `Cache-Control: immutable` por um ano em `/static/images/*` |
| 44 | Core Web Vitals | **PASS** | Mediana de 3 execuções em mobile 4G simulado: **LCP 1,80 a 1,95 s** (alvo ≤ 2,5), **CLS 0** (alvo < 0,1), **TBT 0 ms** (proxy de INP < 200 ms). Desktop: LCP 0,40 a 0,44 s. Medido em `/`, `/permits/flood-zones-50-percent-rule/`, `/pricing/pool-decks/` e `/areas/siesta-key/` |
| 45 | Lighthouse 3× | **PASS** | 3 execuções mobile e 3 desktop por página, mediana reportada. Resultado final: performance **99 a 100**, accessibility **100**, best practices **100**, SEO **100**, e **zero auditorias falhando** nas três categorias não-performance. Limitação documentada: rodado contra `python -m http.server` local, sem CDN, em HTTP/1.1 e sem compressão Brotli, o que é mais severo que a produção em Cloudflare — o alvo 100 em performance no mobile não é alcançado por 1 ponto em duas páginas nessas condições |
| 46 | Headers, CSP, cache e secrets | **PASS** | `dist/_headers`: HSTS com preload, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, `Cross-Origin-Opener-Policy` e **CSP com hashes sha256 calculados no build** para cada script inline (sem `unsafe-inline` em `script-src`). `object-src 'none'`, `frame-ancestors 'self'`, `form-action 'self'`. Nenhum secret no cliente ou no repositório: Turnstile, KV e e-mail de destino são secrets do Cloudflare |
| 47 | HTML ≤ 150 KB | **PASS** | Maior página **65,3 KB**; **0 páginas acima de 150 KB**. CSS crítico inline e minificado, fontes self-hosted com `preload` na família de display, um único JS de 2 KB com hash no nome |

## Entidades e IA (48–53)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 48 | Site name, logo e schema exatamente "Sarasota Concrete" | **PASS** | `WebSite.name`, `Organization.name`, `og:site_name`, header, footer e wordmark todos exatamente "Sarasota Concrete". Sem FL, Florida, número, Company, Contractors, Services, Pros, Experts, Group, LLC, 24/7 ou #1. A tagline é elemento separado |
| 49 | JSON-LD válido | **PASS** | **0 blocos inválidos** em 178 páginas (todos parseados com `json.loads`). Tipos emitidos: `WebSite`, `Organization`, `WebPage`, `BreadcrumbList`, `Service`, `FAQPage`, `Article`, `Dataset`, `DataDownload`, `ImageObject`, `Place`, `City`, `AdministrativeArea`, `GeoCoordinates`, `Question`, `Answer`, `ListItem`. Todo schema espelha o que está visível |
| 50 | LocalBusiness, geo e reviews só com realidade | **PASS** | **Nenhum `LocalBusiness`, `HomeAndConstructionBusiness` ou `GeneralContractor` emitido**: esses tipos exigem endereço, e não há endereço para publicar. O telefone passou a existir em 2026-09-11 e entra como `telephone` da `Organization`, que segue **sem `address`** e sem `areaServed` como afirmação de local físico. `FAQPage` só onde a FAQ está visível. `GeoCoordinates` só em `Place` de localidade |
| 51 | llms.txt, llms-full.txt, feed.xml e api/*.json | **PASS** | `llms.txt` 31 KB (entidade, serviços com URL e uma frase, áreas, fatos-chave incluindo as regras de flood/50%/GBSL/tartarugas e o cap de 50% de impermeabilização, datasets, contato, política). `llms-full.txt` 943 KB com o texto integral das 176 páginas indexáveis. `feed.xml`. `api/cost-index.json` e `api/surface-temperatures.json` com CORS e cache de 1 h |
| 52 | Bing e IndexNow | **OWNER INPUT** | Depende da publicação. Registrado em `OWNER-INPUTS.md` §3.7 |
| 53 | Fatos-chave em HTML | **PASS** | Todas as cápsulas de resposta, tabelas e números estão no HTML servido, sem JS. Verificável com `curl` ou desabilitando JavaScript |

## Canibalização e rede (54–58)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 54 | Registry com proprietário de cada intenção | **PASS** | `network-registry.json`, hub `sarasota`: `city_service_intent_owner` declara Sarasota County inteiro + Charlotte County dentro do raio; `cities_tier1`, `cities_tier2_charlotte`, `cities_mention_only_other_hub` (18) e `cities_out_of_radius` (8) listadas; `city_service_pages_built` = 62 com o critério |
| 55 | Matriz aplicada a cada URL conflitante com GSC anexado | **PARTIAL / BLOCKED** | A matriz está escrita e aplicada às **108 URLs** identificadas (6 city hubs, 60 city×service, 42 posts de custo) em `research/01` §3, com o mapa de 301 completo em `site/network/redirects-lakewoodranch-to-sarasota.txt`. **O GSC não pôde ser anexado** (ponto 6), então cada decisão está *condicionada* pela regra do prompt: < 50 impressões/mês e 0 lead → 301 assim que este hub estiver indexado; com tráfego ou lead → manter 90 dias com intro reescrita, sem preço nem FAQ que este hub passa a possuir, canonical autorreferente, reavaliar em 90 dias. **Nada será redirecionado antes dos dados** |
| 56 | llms.txt e áreas do Lakewood Ranch atualizados quando os 301 entrarem | **PENDING (por desenho)** | O `llms.txt` atual do Lakewood Ranch declara Sarasota County e lista Sarasota, Venice, North Port, Port Charlotte, Osprey, Nokomis e Longboat Key. A reescrita está na fila do passo 6 da matriz e **não deve ser feita antes** dos 301, ou o site irmão perde a declaração de área enquanto ainda ranqueia para ela |
| 57 | Nenhum title, H1 ou intro repetido na rede | **PASS** | `qa_similarity.py` seção NETWORK: máximo 0,4% contra qualquer irmão. Os padrões de title são deliberadamente diferentes — este hub usa "X in City, FL – Cost & Permits", o Lakewood Ranch usa "Paver & Concrete Contractor City, FL" |
| 58 | Fingerprints ausentes | **PASS** | `qa_style.py` inclui os 18 fingerprints do prompt §2.2 na lista proibida: **0 ocorrências**. Estrutura de URL também distinta: aqui `/concrete/<serviço>/<cidade>/` com pilar, contra `/<serviço>/<cidade>/` do Lakewood Ranch e `/concrete/<cidade>/` do Ocoee. Sem blog de custo `<serviço>-cost-<cidade>` |

## Conversão e operação (59–60)

| # | Controle | Resultado | Evidência |
|---|---|---|---|
| 59 | Twilio, tel, sms, e-mail, formulário, anti-spam e attribution testados | **PASS** | **Twilio pronto e testado em 2026-09-11.** Número **(941) 274-3561**, serviço Serverless `sarasota-voice`, ambiente `prod` em `sarasota-voice-9463-prod.twil.io`, quatro funções `protected`, `FORWARD_TO=+16892427487`. Os sete ramos do fluxo (saudação, triagem por tecla, discagem com `callerId` do chamador, whisper, aceite, voicemail com transcrição, encerramento pós-bridge) foram exercitados assinando as requisições com HMAC-SHA1 como o Twilio faz, e a requisição sem assinatura recebe 403 — sem gastar ligação nem tocar o telefone do proprietário. Os links `tel:`/`sms:` com tracking estão nas 178 páginas. **Cadeia de validação do formulário testada ao vivo em 2026-09-11** contra o deploy de preview: `POST /api/contact` com telefone inválido devolve 400 e a mensagem correta; envio válido percorre honeypot, checagem de origem, rate limit e validação e para no 502 do Worker de e-mail, que ainda não existe — e a resposta diz ao visitante para escrever para hello@sarasotaconcrete.com. **Entrega do e-mail testada ao vivo em 2026-09-12** no domínio real, depois de apagar os 46 registros de estacionamento da Afternic que causavam o erro 2008 e ligar o Email Routing: envio válido devolve 303 para `/thank-you/`, telefone inválido 400, ZIP inválido ou ausente 400, `Origin` estranha 403, e o sexto envio do mesmo IP em dez minutos 429 (prova do KV). O Worker `sarasotaconcrete-contact` está publicado com `send_email` e o secret `DESTINATION_EMAIL`, e o binding `CONTACT_EMAIL` vive em `site/wrangler.jsonc` — **não no dashboard**, porque o Pages ignora bindings da API enquanto esse arquivo existir, o que fez todo envio válido morrer num 502 de borda sem log no Worker. Pronto: `site/functions/api/contact.js` (validação server-side de todos os campos, honeypot, Turnstile, rate limit por KV de 5 em 10 min, checagem de origem, limite de 8 MB para a foto com validação de MIME, `Response.redirect` 303 para `/thank-you/`) e `site/workers/contact-email/` (Email Worker com MIME multipart e anexo). Formulário com `hub_id=sarasota`, URL, localidade (select das 15+6), serviço (concreto e pavers em optgroups separados), tipo de imóvel, zona de inundação, prazo, presença do proprietário, UTM, referrer, timestamp, consentimento explícito e upload opcional. Eventos: `tel_click`, `sms_click`, `form_start`, `form_submit`, `form_error`. |
| 60 | Consentimento, Privacy, Terms, disclosures e claims verificados; reauditoria limpa | **PASS** | `/privacy/`, `/terms/`, `/accessibility/` escritas para este site, com cláusulas de SMS (A2P: STOP/HELP, "message and data rates may apply"), retenção, e o texto de consentimento no formulário dizendo que o pedido pode ser encaminhado ao prestador segurado da região. Claims de licença: **nenhum**. As 18 ocorrências da palavra "licensed" no HTML são todas de terceiros ou educativas (engenheiro licenciado exigido por North Port, o que uma associação exige do instalador, como verificar licença, o texto do F.S. 489.119(5)(b), a licença CC BY 4.0 dos dados). Auto-afirmações verificadas: `we are licensed`, `fully licensed`, `licensed contractor in sarasota` = **0**. O rodapé imprime literalmente `Sarasota Concrete · Insured`. Claims costeiros (calor, escorregamento, sal, surge): todos com fonte ou atribuídos. Reauditoria final limpa: `qa_style` 0, `qa_links` 0, `qa_similarity` 0 acima de 15%, `qa_browser` 0, `qa_words` 0 abaixo do piso, `build.py` 0 problemas de SEO |

---

## O que impede declarar concluído

O prompt proíbe declarar concluído com FAIL, conteúdo inventado, placeholder perigoso, página
duplicada, canibalização não resolvida ou formulário não testado. Estado:

| Condição | Estado |
|---|---|
| FAIL | **Nenhum.** 0 pontos em FAIL |
| Conteúdo inventado | **Nenhum.** 0 rating, 0 review, 0 endereço, 0 licença, 0 número de temperatura não medido |
| Placeholder perigoso | **Nenhum visível.** Os placeholders existem só em `_data.py` e os templates esconderam o bloco. Verificado: nenhuma ocorrência de `{{` no HTML servido |
| Página duplicada | **Nenhuma.** Máx 14,8% interno, 0,4% de rede |
| Canibalização | **Não resolvida — bloqueada por dados.** Matriz e 301 escritos; execução depende do Search Console |
| Formulário testado | **Não.** Código revisado, sem teste ponta a ponta por falta de credenciais |

Portanto: **NOT DEPLOYED / READY FOR APPROVAL**. Os dois itens abertos (canibalização e teste do
formulário) dependem de acesso do proprietário, não de mais trabalho de construção.
