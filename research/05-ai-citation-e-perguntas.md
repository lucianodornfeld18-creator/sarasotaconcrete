# 05 — Fontes citadas por IA e as 150 perguntas

Data: 2026-09-10.

## 1. Testes em mecanismos de IA — status

Google AI Mode / AI Overviews, ChatGPT Search, Bing Copilot, Perplexity, Gemini e Claude (interface de busca) **não** foram acessados nesta execução (BLOCKED). Nenhuma pergunta recebeu o rótulo `AI-CITED`. O roteiro abaixo está pronto para ser rodado à mão em janela anônima com localização Sarasota; registrar resposta, fontes citadas, formato e o que a fonte tem que nós não temos, na planilha `06-150-questions.csv` (colunas `ai_engine`, `ai_sources`).

### 1.1 Roteiro de 60 prompts (10 por mecanismo, os mesmos 10 em cada)

1. how much does a pool deck cost in Sarasota
2. best concrete contractor Sarasota FL
3. do I need a permit to replace my driveway in Sarasota County
4. what pool deck material stays coolest in Florida
5. travertine vs pavers pool deck salt water pool Florida
6. how often should I seal pavers on Siesta Key
7. does a new pool deck count toward the FEMA 50% rule
8. sea turtle lighting rules for my pool deck on Longboat Key
9. what to do with pavers after storm surge in Venice FL
10. concrete driveway cost per square foot North Port FL

O que as fontes de 2026 dizem sobre onde as IAs buscam resposta local (citadas no prompt: BrightLocal, 60.970 checagens; análise de 28 milhões de respostas): Google Business Profile é a fonte nº 1 para AI Overviews/AI Mode e Yelp é a nº 1 para ChatGPT em buscas locais. Sem GBP e Yelp reais para "Sarasota Concrete" não há citação local; decisão `{{GBP_DECISION}}` em OWNER-INPUTS.

### 1.2 Tipos de fonte com mais chance de citação (inferência a partir das buscas desta sessão)

Para perguntas de permit/flood/tartaruga, as fontes que dominam a busca são páginas .gov (scgov.net, charlottecountyfl.gov, longboatkey.org, sarasotapropertyappraiser.gov, FEMA, FWC/FDEP) e blogs de expediters/advogados locais (sarasotapermits.com, sarasotalaw.org). Para custo, blogs de contractors de Tampa/Sarasota com tabelas por material (decocreteservices.com, handys.now, wellbuiltflorida.com, buildpriced.com). Para calor de superfície, blogs de pavers do sul da Flórida com números não medidos ("20–30°F cooler"). Implicação: as páginas deste hub linkam a fonte primária em toda afirmação regulatória e publicam método + dados próprios em vez de repetir números de terceiros.

## 2. Método de classificação das 150 perguntas

Rótulos usados: `VOLUME` (família com volume medido na planilha EMD), `COMPETITOR` (a pergunta aparece em FAQ/heading de concorrente auditado ou em blog local com a mesma dúvida), `EXPERT-GAP` (lacuna editorial identificada na auditoria, sem volume observado), `OWNER-CALLS` (reservado — Twilio/formulários do Lakewood Ranch BLOCKED). Não usados por falta de acesso: `PAA`, `AUTOCOMPLETE`, `TRENDS`, `AI-CITED`, `REDDIT`, `GSC`.

Dedupe global: as perguntas canônicas já respondidas pelo Lakewood Ranch (auditoria de 2026-08-20) não foram repetidas: "How much should a 20x20 paver patio cost in Florida?", "How much do 1,000 square feet of driveway pavers cost?", "How deep should the base be under driveway pavers?", "Can pavers be installed over an existing concrete patio or lanai?", "What is the coolest pool deck material for Florida?", "Are travertine pavers good around a pool?", "How often should pavers be sealed in Florida?", "Why did my paver sealer turn white or cloudy?", "Is it cheaper to resurface or replace a concrete pool deck?", "Do stamped concrete surfaces need to be sealed in Florida?", "Do I need a permit or HOA approval for a concrete driveway?", "Can you replace a cracked or uneven concrete garage floor?". As perguntas deste hub têm âmbito Sarasota/costeiro explícito e respondem coisas diferentes (medição, jurisdição, sal, surge, ilha-barreira).

Distribuição das 150: páginas de serviço 34, city×service 6, cost guides/pricing 14, permits/flood/turtle 24, HOA 10, comparações 12, coastal 12, ferramentas 3, guias 22, FAQ contextual/institucional 13. Tabela completa em `06-150-questions.csv`.
