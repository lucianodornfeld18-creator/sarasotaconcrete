# 00 — Resumo da pesquisa (sarasotaconcrete.com)

Data: 2026-09-10. Execução do `09-PROMPT-SARASOTA-CONCRETE.md`. Tudo que está aqui tem fonte e data nos arquivos 01–07. Onde não houve acesso autenticado, o item está marcado **BLOCKED** e não foi substituído por estimativa.

## Arquivos

| # | Arquivo | Conteúdo |
|---|---|---|
| 01 | `01-inventario-rede-e-canibalizacao.md` | Inventário do Lakewood Ranch (URLs de Sarasota/Charlotte), GCM, Ocoee, Windermere, Groveland; matriz de canibalização aplicada; fingerprints proibidos |
| 02 | `02-territorio-40-milhas.md` | Localidades, tiers, jurisdição de permit, população oficial (EDR 2025), flood/GBSL/tartarugas, solos, HOAs, NOAA normals |
| 03 | `03-keyword-research.md` + `03-keywords.csv` | Dados Google Ads da planilha EMD (VOLUME), famílias sem volume mensurável, o que ficou BLOCKED |
| 04 | `04-concorrentes-e-benchmark.md` | 22 concorrentes medidos (palavras, H1, schema), benchmark St. Cloud, matriz tem/falta/como superar |
| 05 | `05-ai-citation-e-perguntas.md` + `06-150-questions.csv` | Método, classificação por evidência e as 150 perguntas com URL proprietária |
| 07 | `07-dominio-entidade-licenca.md` | Histórico do domínio (Wayback + RDAP), Sunbiz, USPTO, licenciamento (DBPR, Sarasota County Ch. 22, Charlotte), estatuto 489.119 |

## Achados que mudam o projeto

1. **Domínio limpo.** `sarasotaconcrete.com` teve um site-placeholder de uma empresa local de 2011 a 2019 (e-mail com typo, sem conteúdo), ficou à venda na Epik em 2022 (US$ 9.700), foi re-registrado em 2025-10-28 e mudou de mãos em 2026-09-10 (RDAP). Nenhum sinal de spam ou uso tóxico nas capturas. Sem necessidade de disavow.
2. **Nome livre na Sunbiz.** Não existe entidade ativa "SARASOTA CONCRETE" (só "Sarasota Concrete Co", inativa, e "Sarasota Concrete Solutions LLC", ativa desde 2024, nome diferente). "Lakewood Ranch Concrete LLC" continua inexistente. GCM Best Services Corp = P22000086622, ativa. A busca de nome fictício exige JavaScript (Cloudflare challenge) e ficou BLOCKED para verificação automática — fazer à mão em sunbiz.org antes de registrar o DBA.
3. **Licença.** Instalação de driveways e pavers está na lista "não exige licença DBPR" do Estado, mas Sarasota County exige Certificate of Competency + Operating Certificate locais para as trades que regula (Código Cap. 22, Art. V, § 22-122) e a categoria local "Masonry/Concrete" cobre footers, slabs e floors. Charlotte County exige permit para **toda** flatwork, inclusive pavers, e aceita a licença local "Concrete Masonry". Conclusão operacional: o site escreve "Insured" e nunca "Licensed" até o proprietário informar `{{LICENSE_TYPE_AND_NUMBER}}`; se houver número, o F.S. 489.119(5)(b) exige que ele apareça em toda publicidade.
4. **Permits variam por jurisdição e o site precisa dizer isso.** Sarasota County: culvert permit e right-of-way use permit (Cap. 98 § 98-3; Cap. 74); exemption residencial até US$ 7.500 (HB 803, Bulletin 2026-0002) com documentação. City of Sarasota: portal FTG próprio; apron entre calçada e rua é área da cidade e exige permit. Venice: pavers na ROW exigem license agreement e padrão da cidade. North Port: "Right of Way Use Permit — Culvert/Driveway/Sidewalk/Concrete Slab", desenhos selados por engenheiro. Longboat Key: driveways, decks e patios at-grade passam por Planning & Zoning; substantial improvement revisado pela Town. Charlotte: permit para toda slab/paver, NOC acima de US$ 5.000, taxas publicadas.
5. **Regra dos 50%.** O Property Appraiser de Sarasota confirma o cálculo (improvement value × 1,2 → 50%) e a exclusão de melhorias no terreno (driveways, piscinas, paisagismo) é a leitura padrão da NFIP (FEMA P-758; FAQ de Fort Myers Beach). Hardscape em geral **não** conta. O site diz isso com a ressalva de que a jurisdição decide caso a caso.
6. **Impermeabilização.** Zoneamento RSF do condado: cobertura impermeável máxima de 50% do lote, e pool decks, concreto e pavers contam; grama, concha e superfícies permeáveis não. Isso vira uma ferramenta e um guia.
7. **Tartarugas.** 1 mai–31 out; Sarasota County Cap. 54 Art. XXIII (Marine Turtle Protection), Longboat Key Ordinance 2021-01 (Cap. 100; bulbs ≥ 560 nm, luminária fully shielded), Venice com artigo próprio (Cap. 54 Art. XXV do condado + página da cidade). Nenhum concorrente de hardscape cobre isso.
8. **Volume.** As strings com cidade têm ~50 buscas/mês cada (sarasota concrete, sarasota concrete contractor, sarasota concrete repair, venice concrete, north port concrete, nokomis concrete). O volume real está nas famílias genéricas geolocalizadas; a exportação do Keyword Planner para essas famílias ficou **BLOCKED** (sem sessão autenticada nesta execução). A arquitetura já foi desenhada para as famílias genéricas.
9. **SERP madura mas rasa.** O maior concorrente (concrete-sarasotafl.com, 3.646 palavras) não tem preços, licença, FAQ, permits, flood, sal ou tartarugas. Ninguém tem estudo de temperatura, cost index, permit finder ou guia de tartarugas.
10. **Lakewood Ranch já ocupa Sarasota County** com 6 hubs de cidade (~3.000 palavras cada), 60 city×service e 48 posts de custo — matriz de canibalização aplicada no arquivo 01 e no registry, com a data de corte ligada à indexação deste hub.

## BLOCKED nesta execução (e o que fazer)

| Item | Motivo | Ação |
|---|---|---|
| Google Ads Keyword Planner (export bruto por família × localização) | sem Chrome autenticado nesta sessão | proprietário exporta ou libera sessão; planilha EMD usada como fonte VOLUME |
| Search Console / analytics do Lakewood Ranch | propriedade não está no Windsor.ai (só brazacleaning, triangle-floor, napasflooring, ocoeeconcrete) | adicionar `sc-domain:lakewoodranchconcretefl.com` ao Windsor ou exportar CSV de 16 meses |
| Twilio (chamadas por origem) e Twilio number 941 | MCP do Twilio nesta sessão é só documentação | proprietário compra número 941 e cria service `sarasota-voice` (padrão da conta) |
| Testes em AI Mode / ChatGPT Search / Copilot / Perplexity / Gemini | sem acesso a essas interfaces | roteiro de 60 prompts pronto no arquivo 05 para rodar à mão |
| Sunbiz — nome fictício | página exige JavaScript | checar à mão e registrar o DBA |
| USPTO — marca | TESS/TSDR bloqueiam acesso automático (401) | checar à mão em tmsearch.uspto.gov ("Sarasota Concrete") |
| Reddit/Nextdoor/Quora | buscas `site:reddit.com` não retornaram threads locais | nenhuma pergunta rotulada REDDIT; nada inventado |
| Páginas scgov.net, venicegov.com, sarasotafl.gov | Akamai bloqueia fetch automatizado (403) | usado o código de posturas (eLaws), Property Appraiser, Charlotte County e fontes secundárias; links oficiais mantidos nas páginas |
