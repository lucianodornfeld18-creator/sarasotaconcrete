# OWNER-INPUTS — sarasotaconcrete.com

Data: 2026-09-11. Tudo abaixo está **pendente de você**. O site foi construído de forma que a
ausência de cada item não gera placeholder visível: o bloco simplesmente não aparece na página.
Nada foi inventado para preencher lacuna.

Ordem sugerida: os itens do bloco 1 são bloqueantes para publicar; o bloco 2 é bloqueante para
gerar lead; o bloco 3 melhora o site mas não impede a publicação.

---

## 1. Bloqueantes para publicação

### 1.1 `{{LEGAL_ENTITY}}` — qual empresa executa e fatura em Sarasota County

**Por que é bloqueante:** o formulário diz ao lead que o pedido "pode ser encaminhado ao prestador
segurado que atende a sua região". Se a lei exigir nomear o destinatário, ou no momento em que o
contrato for assinado, o nome legal precisa existir. O rodapé e o schema `Organization` também o
consomem.

**O que verifiquei:** na Sunbiz (2026-09-10) existe **GCM BEST SERVICES CORP, P22000086622, Active**.
**Não existe** nenhuma entidade "Lakewood Ranch Concrete" — a LLC que o prompt 05 dizia que seria
registrada continua inexistente. Também não existe entidade ativa chamada exatamente "Sarasota
Concrete" (há `SARASOTA CONCRETE CO` inativa, `SARASOTA CONCRETE LIFTING LLC` inativa e
`SARASOTA CONCRETE SOLUTIONS LLC.` ativa desde 2024, que é outro nome e outra empresa).

**Escolha uma:**

| Opção | Consequência |
|---|---|
| GCM Best Services Corp (P22000086622) | Funciona hoje. Empresa de Orlando faturando no Suncoast; nenhum problema legal, mas o DBA "Sarasota Concrete" precisa ser registrado sob ela |
| Registrar "Sarasota Concrete LLC" | Mais limpo para a marca e para um GBP próprio; custa taxa de registro e tempo |
| Registrar "Lakewood Ranch Concrete LLC" e usar para os dois hubs | Consolida Manatee + Sarasota numa entidade; o nome legal não aparece no branding deste site de qualquer forma |

### 1.2 `{{FICTITIOUS_NAME_STATUS}}` — registrar "Sarasota Concrete" como nome fictício

**Recomendação: registre.** É barato, resolve a questão de usar o nome publicamente e evita
conflito com a "Sarasota Concrete Solutions LLC" que já opera na região.

**Pendência que não consegui fechar:** a busca de nome fictício da Sunbiz exige JavaScript
(desafio Cloudflare) e ficou **BLOCKED** na automação. Antes de registrar, confirme à mão em
`dos.sunbiz.org/ficinam.html` que "SARASOTA CONCRETE" está livre como nome fictício.
A F.S. 865.09 exige também a publicação do anúncio legal em jornal do condado.

### 1.3 `{{LICENSE_TYPE_AND_NUMBER}}` — existe licença? qual?

**Estado atual do site:** o rodapé diz **"Insured"** e nada mais. Não há número de licença em
nenhuma página, e a palavra "Licensed" não aparece no site (verificado: 0 ocorrências).

**O que verifiquei nas fontes:**

- **Estado:** instalação de driveways e pavers está na lista do DBPR de serviços que **não** exigem
  licença estadual de construção. Ressalva explícita de que município/condado pode exigir licença local.
- **Sarasota County:** Código Cap. 22 Art. V § 22-122 — é ilegal contratar ou executar obra nas
  *trades* reguladas sem **Operating Certificate** do condado **mais** o **Certificate of Competency**
  aplicável. A categoria local "Masonry/Concrete" cobre footers, slabs, floors e paredes de alvenaria
  até um andar.
- **Charlotte County:** aceita, entre outras, a licença local **"Concrete Masonry"** para permits de
  driveway e slab.
- **F.S. 489.119(5)(b):** quem **tem** registro ou certificação estadual é obrigado a colocar o número
  em toda publicidade, em qualquer meio.

**O que preciso:** ou (a) o número da licença/certificate of competency e a jurisdição que o emitiu,
e eu coloco no rodapé, no About e no schema; ou (b) a confirmação de que não há, e o site continua
dizendo apenas "Insured" — que é o estado atual e é honesto.

### 1.4 `{{INSURANCE_PROOF}}` — comprovante de seguro

O site afirma "Insured". Preciso do certificado (COI) em arquivo para que a afirmação tenha respaldo
documental, mesmo sem publicar os limites. Se **não** houver seguro vigente, a palavra "Insured" sai
do rodapé imediatamente.

### 1.5 `{{AUTHOR_NAME}}` e `{{AUTHOR_TITLE}}` — quem assina o conteúdo

**Estado atual:** as 178 páginas terminam com "Last reviewed September 10, 2026 by the Sarasota
Concrete editorial team (author name pending owner input)". Nenhuma página reivindica autor nomeado,
e o schema `Article` aponta para a `Organization` em vez de uma `Person`.

**Por que importa:** autor verificável é um dos poucos controles de E-E-A-T que está sob nosso
domínio, e o prompt exige autor real com bio, foto e credencial. Preciso de nome, cargo, uma bio de
3 a 5 linhas, uma foto e qualquer credencial verificável (anos no ofício, certificações ICPI/ACI,
licença). Com isso as páginas passam a emitir `Person` com `sameAs`.

### 1.6 Escolha do logo — **única parada obrigatória do prompt**

Dez direções estão em `brand/logos.html` (abra no navegador), com SVG individual de cada uma em
`brand/svg/` (50 arquivos: horizontal claro, horizontal escuro, quadrado, favicon 32 e favicon 16).

O site está em produção com a direção **1 · Bayline** como wordmark provisório.

| # | Nome | Conceito | Recomendação |
|---|---|---|---|
| 1 | Bayline | Três linhas batimétricas da baía de Sarasota | **Recomendada.** Em uso provisório |
| 2 | Terrazzo | Chip de terrazzo da Sarasota School of Architecture | Boa alternativa editorial |
| 3 | Coquina | Selo redondo em pedra de concha | **Evitar:** terracota muito perto do Ocoee |
| 4 | Seawall Grid | Quatro painéis de seawall em grade | Boa, técnica |
| 5 | Pool Edge | Planta de piscina com o deck em volta | **Recomendada.** Risco: parecer pool builder |
| 6 | Mangrove | Raízes de mangue sobre laje | **Evitar:** verde colide com o Windermere |
| 7 | Benchmark | Marco de nivelamento | Boa, combina com a voz "de dados" |
| 8 | Ringling | Listras verticais | Vibrante; risco de parecer marca de evento |
| 9 | Horizon | Quatro barras que desvanecem | **Recomendada.** A mais sóbria |
| 10 | Conch | Espiral de concha em traço único | Checar contra logos de resorts de Siesta Key |

Depois da escolha eu gero SVG limpo, PNG transparente, versões clara/escura, favicon.ico, ícone
social 512 e um guia de marca de uma página.

---

## 2. Bloqueantes para gerar lead

### 2.1 `{{SARASOTA_TWILIO_NUMBER}}` — número 941

**Estado atual:** o site **não mostra telefone**. O cabeçalho traz "Get an estimate" em vez de
"Call ...", e nenhum link `tel:` existe, porque o `_data.py` está com o placeholder e os templates
esconderam o bloco em vez de imprimir `{{...}}`.

**O que fazer**, seguindo o padrão que já existe na sua conta Twilio (um número por site, serviço
Functions `<site>-voice`, `FORWARD_TO` para o seu telefone):

1. Comprar um número com DDD **941**.
2. Criar o serviço Functions `sarasota-voice`, com `FORWARD_TO` = seu telefone.
3. Me passar o número em dois formatos: exibição `(941) XXX-XXXX` e E.164 `+1941XXXXXXX`.

Preencho `BUSINESS["phone_display"]` e `["phone_tel"]` e os links `tel:`/`sms:` com tracking
aparecem em todas as 178 páginas automaticamente.

### 2.2 `{{MAIN_DESTINATION_EMAIL}}` — onde os leads chegam

O Worker `sarasotaconcrete-contact` já está escrito e envia por Cloudflare Email Workers a partir de
`hello@sarasotaconcrete.com`. Preciso do e-mail de destino final, que entra como secret:

```
cd site/workers/contact-email
wrangler secret put DESTINATION_EMAIL
```

### 2.3 Cloudflare — o que falta configurar

| Item | Comando ou local | Estado |
|---|---|---|
| Repositório GitHub `sarasotaconcrete` | — | a criar |
| Pages ligado ao repo, pasta `site`, output `dist` | Dashboard | a criar |
| Email Routing `hello@sarasotaconcrete.com` | Dashboard | a criar |
| Worker de contato publicado | `cd site/workers/contact-email && wrangler deploy` | a fazer |
| Service binding `CONTACT_EMAIL` → Worker | `site/wrangler.jsonc` (já declarado) | a ligar |
| KV `RATE_LIMIT_KV` | `wrangler kv namespace create RATE_LIMIT_KV`, depois preencher o id em `site/wrangler.jsonc` | a fazer |
| `TURNSTILE_SITE_KEY` e `TURNSTILE_SECRET_KEY` | Turnstile + variáveis do Pages | a fazer |
| Redirect Rule www → apex | Dashboard (não dá em `_redirects`) | a fazer |
| Desativar o bloqueio padrão de bots de IA no WAF para os bots de busca | Dashboard | a fazer |

O formulário **degrada com elegância**: sem Turnstile configurado a verificação é ignorada (o código
trata `secret` ausente como "ok, skipped") e sem KV o rate limit é ignorado. Ou seja, o site publica
e funciona antes de tudo isso estar pronto, mas publique com Turnstile se quiser evitar spam.

### 2.4 `{{GBP_DECISION}}` — **decisão de negócio urgente**

Esta é a decisão com maior impacto e a que menos depende de código.

Os estudos citados no prompt (BrightLocal, 60.970 checagens; análise de 28 milhões de respostas de
IA) apontam **Google Business Profile como fonte nº 1 para AI Overviews / AI Mode** e **Yelp como
fonte nº 1 para o ChatGPT** em buscas locais. Sem GBP e Yelp reais para o nome "Sarasota Concrete",
o site pode rankear organicamente e ainda assim não ser citado por IA em consultas locais.

| Opção | O que acontece |
|---|---|
| GBP próprio como *service-area business* para "Sarasota Concrete" | Melhor cenário. Sem endereço publicado, área de atendimento declarada. Exige verificação do Google e entidade legal (item 1.1) |
| Usar um perfil existente (GCM) | Nome no perfil ≠ nome no site, o que enfraquece a consistência de entidade que o prompt exige |
| Nenhum dos dois | O site funciona para SEO orgânico; assuma que não haverá citação local por IA |

A página `/directories/` está construída e **hoje não lista nenhum perfil**, porque listar um perfil
de outra marca seria apresentar credibilidade emprestada. Ela passa a listar assim que existirem.

### 2.5 `{{REVIEWS_SOURCE}}` — posso exibir avaliações?

A página `/reviews/` está publicada e **vazia**, explicando por quê. Para preenchê-la preciso de:

1. confirmação de que a entidade do perfil é a mesma que executa aqui (item 1.1);
2. autorização para citar;
3. o perfil de origem, que será **nomeado na página** ("avaliação deixada no perfil X em DD/MM").

`AggregateRating` só entra se o perfil pertencer exatamente a esta empresa. Verificado no build
atual: **0 ocorrências** de `aggregateRating`, `ratingValue` e `review` no schema.

---

## 3. Melhoram o site, não impedem a publicação

### 3.1 Catálogo — três itens em aberto

| Item | Situação | Decisão necessária |
|---|---|---|
| **Epoxy / polyaspartic garage floors** | No Ocoee legado, **não** no catálogo da GCM. O `network-registry.json` não o confirma. Cluster local ocupado por franquias (GarageExperts, Granite Garage Floors, Paradigm) | Executa (própria ou subcontratado identificado)? Se sim, crio `/coatings/garage-floors/`. Hoje: **sem página** |
| **Commercial concrete / parking lots** | No Ocoee legado, **não** na GCM | Idem. Hoje: **sem página** |
| **Architectural concrete** | Está no catálogo real da GCM (Orlando). **Página construída** em `/concrete/architectural/` com aviso visível de que a capacidade no Suncoast é confirmada no orçamento | Confirma que faz honed/board-formed em Sarasota? Se não, removo a página |
| **Stucco** | `not_confirmed_do_not_use` no registry | **Excluído**, sem menção. Nenhuma ação |
| **Foundations, footings, seawall caps, muros estruturais** | Exigem licença não confirmada | **Excluídos**, sem menção. Nenhuma ação |

### 3.2 Duas fronteiras de território que conflitam entre prompts

| Localidade | Conflito | O que fiz | Confirme |
|---|---|---|---|
| **Longboat Key** | O prompt 06 (Bradenton) lista como seed; o prompt 09 (este) dá a ilha inteira para Sarasota | Segui o 09, que é posterior: ilha inteira, incluindo a metade em Manatee | OK? |
| **Fruitville** | O prompt 05 (Lakewood Ranch) lista como seed; o 09 coloca Sarasota County inteiro aqui | Segui o 09: Fruitville é deste hub | OK? |

### 3.3 Dados que não consegui obter (o site está desenhado para recebê-los)

| Dado | Por que ficou BLOCKED | Impacto | Como destravar |
|---|---|---|---|
| **Keyword Planner** (export bruto por família × localização) | Sem sessão autenticada do Chrome nesta execução | A arquitetura já foi desenhada para as famílias genéricas geolocalizadas; o CSV em `research/03-keywords.csv` tem a coluna `volume_geo` marcada BLOCKED em cada linha, pronta para preencher | Exporte de `ads.google.com/aw/keywordplanner`, ou me libere a sessão |
| **Search Console do lakewoodranchconcretefl.com** (16 meses) | A propriedade não existe no Windsor.ai (só brazacleaning, triangle-floor, napasflooring, ocoeeconcrete) | **É o que decide a canibalização.** O mapa de 301 está escrito e não pode ser executado sem estes dados | Adicione `sc-domain:lakewoodranchconcretefl.com` ao Windsor, ou exporte o CSV |
| **Twilio — chamadas por origem** | O MCP do Twilio nesta sessão é só documentação | Perderíamos as perguntas reais dos leads como fonte de conteúdo | Export do console |
| **Testes em AI Mode, ChatGPT Search, Copilot, Perplexity, Gemini** | Sem acesso a essas interfaces | Nenhuma das 150 perguntas recebeu o rótulo `AI-CITED` | Roteiro de 10 prompts × 6 mecanismos pronto em `research/05-ai-citation-e-perguntas.md`, seção 1.1 |
| **Reddit, Nextdoor, Quora** | Buscas `site:reddit.com` não retornaram threads locais | Nenhuma pergunta rotulada `REDDIT` | Busca manual em r/sarasota, r/Venice_FL, r/NorthPort |
| **USPTO** | TSDR/TESS bloqueiam acesso automatizado (HTTP 401) | Marca geográfica descritiva raramente é registrável; o risco real é uso local, não registro federal | Busca manual em `tmsearch.uspto.gov` por "Sarasota Concrete" |
| **Páginas scgov.net, venicegov.com, sarasotafl.gov** | Akamai devolve 403 a acesso automatizado | Usei o Código de Posturas (eLaws), o Property Appraiser, o Charlotte County e fontes secundárias. Onde a fonte é secundária, **a página diz isso** | Confirme na fonte oficial os itens marcados com aviso nas páginas de permit |
| **Google Safe Browsing** para o domínio | Interface exige JavaScript | Histórico do domínio é benigno (ver `research/07`), mas a checagem formal falta | `transparencyreport.google.com/safe-browsing/search?url=sarasotaconcrete.com` |
| **Backlinks do domínio** | Sem conta Ahrefs/Bing Webmaster | Sem indício de histórico tóxico nas capturas do Wayback | Verifique após validar o site no Bing Webmaster Tools |

### 3.4 Fotos e projetos

**Hoje:** 26 imagens processadas (18 fotos reais de obra + 8 renderings rotulados), todas de obras da
**Flórida Central**, com metadados removidos e alt text que descreve o que se vê **sem afirmar cidade**.

**Preciso de:**
- 20 a 30 fotos reais de obras no **Suncoast** (Sarasota, Venice, North Port, as ilhas);
- 5 a 10 projetos documentados com cidade, serviço, metragem, material, desafio do lote, solução,
  prazo e faixa de preço, mais autorização do proprietário do imóvel para publicar.

A página `/projects/` está publicada e explica exatamente esse formato; ela se preenche com esses dados.

### 3.5 Os dois datasets próprios

Ambos estão publicados **com metodologia e sem números inventados**:

| Dataset | Estado | O que falta |
|---|---|---|
| **Sarasota Pool Deck Surface Temperature Study** (`/coastal/pool-deck-surface-temperature-study/`) | Protocolo completo publicado: 9 superfícies, termômetro infravermelho calibrado, 3 horários (10h, 14h, 17h), um dia claro de julho e um de janeiro, mediana de 3 leituras | Medir. Datas previstas: **janeiro/2027 e julho/2027**. Preciso das amostras das 9 superfícies na mesma base e de um termômetro IV com data de calibração |
| **Sarasota Concrete Cost Index** (`/pricing/sarasota-concrete-cost-index/`) | Schema do registro, método das releases trimestrais e limitações publicados. Baseline v0.1 = preços publicados do mercado, rotulado como tal | Dados de obras concluídas: serviço, material, localidade, metragem, preço instalado. A partir de n ≥ 3 por célula a release passa a ser dado próprio. Primeira release prevista: **1º trimestre de 2027** |

Os endpoints `/api/surface-temperatures.json` e `/api/cost-index.json` já existem e servem a
metodologia; passam a servir os dados quando existirem.

### 3.6 `{{WARRANTY_TERMS}}` e `{{FINANCING_PARTNER}}`

- `/warranty/` explica o que uma garantia de workmanship deve cobrir e excluir por serviço, **sem
  afirmar prazo**. Preciso dos períodos e exclusões reais por serviço.
- `/financing/` diz que financiamento existe quando houver parceiro confirmado. Preciso do nome do
  parceiro, termos e link de aplicação, ou a confirmação de que não há.

### 3.7 Indexação e monitoramento (depois de publicar)

Search Console (propriedade de domínio), Bing Webmaster Tools, IndexNow, Cloudflare Web Analytics,
GA4 (só após a revisão de privacidade) e monitoramento dos referrals `utm_source=chatgpt.com`,
`perplexity.ai` e `copilot`.

---

## 4. Resumo: o que impede a publicação hoje

1. **Escolha do logo** (item 1.6) — parada obrigatória do prompt.
2. **Entidade legal** (1.1) e decisão sobre licença (1.3), porque definem o rodapé e o contrato.
3. **Número Twilio** (2.1) e **e-mail de destino** (2.2), sem os quais o site não captura lead.
4. **Infra Cloudflare** (2.3).

Não impedem a publicação, mas decidem o resultado: **GBP e Yelp** (2.4) e os **dados do Search
Console do Lakewood Ranch** (3.3), que são o gatilho dos 301 e da resolução de canibalização.
