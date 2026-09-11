# Relatório de entrega — sarasotaconcrete.com

Data: 2026-09-11. Execução do `09-PROMPT-SARASOTA-CONCRETE.md`.
Status: **NOT DEPLOYED / READY FOR APPROVAL.**

---

## Como ver o site agora

```
cd "C:\Users\luana\SSD-Antigo-Lucia\Projetos\sarasotaconcrete\site"
python build.py
python -m http.server 8080 --directory dist
```

Depois abra `http://127.0.0.1:8080/`. O build leva cerca de 4 segundos e é reproduzível: rodar duas
vezes gera bytes idênticos.

**Escolha do logo:** abra `brand/logos.html` no navegador. É a única parada obrigatória.

---

## O que existe

| Entregável do prompt | Onde está |
|---|---|
| 1. Pesquisa de mercado e keywords com fonte, configuração e data | `research/03-keyword-research.md` + `research/03-keywords.csv` (100 linhas) |
| 2. Auditoria dos concorrentes top 1–3 por cluster e fontes citadas por IA | `research/04-concorrentes-e-benchmark.md` (22 concorrentes medidos) + `research/05-ai-citation-e-perguntas.md` |
| 3. Mapa cidade × serviço × intenção × URL × proprietário | `research/01-inventario-rede-e-canibalizacao.md` §3 + `network-registry.json` |
| 4. 150 perguntas priorizadas e classificadas por evidência | `research/06-150-questions.csv` |
| 5. Dez direções de logo em prancha única | `brand/logos.html` + 50 SVG em `brand/svg/` |
| 6. Identidade visual e voz exclusivas | Bricolage Grotesque + Instrument Sans + DM Mono, paleta azul "Bayline". Nenhum irmão usa azul nem estas fontes |
| 7. Site completo, estático, pronto para Cloudflare Pages | `site/` → `site/dist/`, 178 páginas |
| 8. `AUDIT-60-POINT.md` com evidência por controle | `AUDIT-60-POINT.md` |
| 9. `OWNER-INPUTS.md` consolidado | `OWNER-INPUTS.md` |
| 10. Registro global atualizado com a resolução de canibalização | `network-registry.json` + `.csv` em `Documents/Codex/2026-09-03/pr/outputs/concrete-leadgen-network/` |

## O site em números

| | |
|---|---|
| Páginas | 178 (176 indexáveis, 2 noindex) |
| Páginas de serviço | 20, em dois pilares separados (9 concreto, 11 pavers) |
| Localidades | 15 páginas + 2 hubs de condado |
| City × service | 62, de 300 combinações possíveis |
| Permits | 9 páginas, uma por jurisdição + hub + flood + tartarugas |
| Comparações | 10 |
| Ferramentas | 5 |
| Hub costeiro | 6 páginas |
| HOA | 4 |
| FAQ | 6 |
| Guias | 15 |
| Institucionais e legais | 15 |
| Maior HTML | 65,3 KB (limite do prompt: 150 KB) |
| Fotos processadas | 26 (18 reais + 8 renderings rotulados), 78 arquivos WebP |

## Resultado da auditoria de 60 pontos

**47 PASS · 6 PARTIAL · 3 BLOCKED · 4 OWNER INPUT · 0 FAIL**

| QA | Resultado |
|---|---|
| `qa_words.py` | **178/178 acima do piso** do St. Cloud. Metas esticadas batidas na home, nos 2 pilares, no FAQ hub, nas 3 city hubs Tier 2 e nas institucionais |
| `qa_links.py` | 0 links quebrados, 0 órfãs indexáveis, 0 páginas a mais de 3 cliques |
| `qa_style.py` | **0 problemas em 178 páginas** (lista proibida, fingerprints da rede, densidade de fatos) |
| `qa_similarity.py` | **0 pares acima de 15%**, máximo 14,8% interno; **máximo 0,4%** contra os 5 hubs irmãos |
| `qa_browser.py` | 13 páginas × 4 viewports, 0 problemas |
| Lighthouse (mediana de 3) | performance 99–100, acessibilidade **100**, best practices 100, SEO 100 |
| Core Web Vitals (mobile) | LCP 1,80–1,95 s, CLS **0**, TBT **0 ms** |
| Schema | 0 blocos de JSON-LD inválidos |
| Veracidade | 0 `aggregateRating`, 0 `review`, 0 `PostalAddress`, 0 auto-afirmação de licença, 0 placeholder vazando |

## As três decisões de conteúdo que definem este hub

**1. Preço com data em toda página.** Nenhum dos 22 concorrentes auditados publica preço. Este site
publica faixas de planejamento com a data de leitura (2026-09-10), a fonte e a metodologia, mais
exemplos com a aritmética à vista. O maior concorrente da SERP tem 3.646 palavras e nenhum número.

**2. Permits por escritório, não por condado.** Seis autoridades emitem permit dentro de 40 milhas e
não concordam entre si. Cada uma tem página própria com as seções do código citadas, as taxas
publicadas, o portal e o telefone. Charlotte County exige permit para **toda** flatwork, pavers
incluídos; a City of Sarasota é dona do apron entre a calçada e a rua; North Port dimensiona o
culvert. Nenhum concorrente cobre isso.

**3. Costa como especificação, não como adjetivo.** Zonas FEMA, a regra dos 50% (com a aritmética do
Property Appraiser e a exclusão de melhorias no terreno), a Gulf Beach Setback Line, a iluminação de
tartarugas de 1º de maio a 31 de outubro com o critério de 560 nm, o teto de 50% de impermeabilização
em lote RSF, o surge de 6,68 pés medido em Longboat Key e o ciclo de selagem de 18 a 24 meses a menos
de uma milha da água. Tudo com a fonte ao lado.

## Duas decisões técnicas que valem registro

**Unicidade acima de volume.** Escrevi seis passes de aprofundamento e cheguei perto de bater todas
as metas esticadas de palavras. Mas blocos aplicados a muitas páginas ao mesmo tempo levaram a
similaridade interna de 8-gramas a **32%**, contra o gate de 15% do prompt. Removi os blocos
repetidos, o que devolveu volume em troca de unicidade. O prompt trata similaridade acima de 15%
como reprovação que volta para reescrita, e volume como meta; os pisos, que são o requisito duro,
continuam batidos em todas as 178 páginas.

**Lacunas ficam vazias.** Não há telefone no site porque não há número Twilio, e o template esconde o
bloco em vez de imprimir `{{SARASOTA_TWILIO_NUMBER}}`. A página `/reviews/` está publicada e vazia,
explicando que avaliações pertencem ao perfil que as ganhou. O estudo de temperatura publica o
protocolo e **nenhum número**. Verificado: 0 placeholders vazando para o HTML.

## Canibalização com o Lakewood Ranch

O site irmão ocupa Sarasota County com **108 URLs**: 6 city hubs (2.922 a 3.032 palavras cada), 60
city×service e 42 posts de custo, e o `llms.txt` dele declara Sarasota County na área.

A matriz do prompt está aplicada e o mapa de 301 está escrito em
`site/network/redirects-lakewoodranch-to-sarasota.txt` — **e não executado**, com o gate no topo do
arquivo. O passo 1 da matriz é exportar 16 meses de Search Console por URL, e essa propriedade não
existe no Windsor.ai (só `brazacleaning.com`, `triangle-floor.com`, `napasflooring.com` e
`ocoeeconcrete.com`). Sem esse dado não se sabe quais URLs têm tráfego, e redirecionar às cegas
destruiria posições que já geram lead.

**Para destravar:** adicione `sc-domain:lakewoodranchconcretefl.com` ao Windsor.ai, ou exporte o CSV
de 16 meses. Regra já escrita: menos de 50 impressões/mês e zero lead → 301 assim que este hub
estiver indexado; com tráfego → mantém 90 dias com intro reescrita e reavalia.

Duas fronteiras conflitam entre prompts e eu segui o 09, que é posterior: **Longboat Key** inteira
(o prompt 06 a listava como seed do Bradenton) e **Fruitville** (o prompt 05 a listava no Lakewood
Ranch). Confirme em `OWNER-INPUTS.md` §3.2.

## O que ficou BLOCKED, e por quê

| Item | Motivo | Consequência |
|---|---|---|
| Keyword Planner (export por família × localização) | Sem sessão autenticada do Chrome | Usei a planilha EMD como fonte `VOLUME`; o CSV tem a coluna pronta para receber o export |
| Search Console do Lakewood Ranch | Propriedade ausente do Windsor.ai | **Bloqueia a execução dos 301** |
| Twilio (chamadas por origem) | MCP do Twilio nesta sessão só serve documentação | Nenhuma pergunta rotulada `OWNER-CALLS` |
| AI Mode, ChatGPT Search, Copilot, Perplexity, Gemini | Sem acesso às interfaces | **Nenhuma pergunta rotulada `AI-CITED`** — nada inventado. Roteiro de 10 prompts × 6 mecanismos pronto |
| Sunbiz nome fictício / USPTO | Cloudflare challenge / HTTP 401 | Verificar à mão antes de registrar o DBA |
| scgov.net, venicegov.com, sarasotafl.gov | Akamai devolve 403 | Usei o código de posturas (eLaws), o Property Appraiser e o Charlotte County. **Onde a fonte é secundária, a página avisa** |
| Reddit, Nextdoor, Quora | Buscas não retornaram threads locais | Nenhuma pergunta rotulada `REDDIT` |

## Próximos passos, em ordem

1. **Escolher o logo** em `brand/logos.html`. Recomendo 1 (Bayline), 5 (Pool Edge) ou 9 (Horizon);
   evitar 3 e 6, que se aproximam do Ocoee e do Windermere.
2. **Definir a entidade legal** e se existe licença. Decide rodapé, contrato e schema.
3. **Comprar o número 941** e criar o serviço Functions `sarasota-voice`, e me passar o e-mail de destino.
4. **Criar o repositório e o Pages**, publicar o Worker, criar o KV e as chaves do Turnstile.
5. **Decidir GBP e Yelp.** É o que separa rankear de ser citado por IA em busca local.
6. **Liberar o Search Console do Lakewood Ranch**, para executar os 301.
7. Publicar. Depois: Search Console, Bing Webmaster, IndexNow, e monitorar os referrals
   `utm_source=chatgpt.com`, `perplexity.ai` e `copilot`.
8. Nas semanas seguintes: 20 a 30 fotos do Suncoast, 5 a 10 projetos documentados, o nome do autor, e
   agendar a medição de temperatura para janeiro/2027.

Detalhe de cada item, com o comando ou o campo exato, em `OWNER-INPUTS.md`.
