# 07 — Domínio, entidade, nome e licença

Data das verificações: 2026-09-10.

## 1. sarasotaconcrete.com — histórico

| Fonte | Resultado |
|---|---|
| RDAP Verisign (rdap.verisign.com/com/v1/domain/sarasotaconcrete.com) | Registration 2025-10-28; expiration 2027-10-28; last changed 2026-09-10; registrar GoDaddy.com, LLC; status clientDeleteProhibited/clientRenewProhibited/clientTransferProhibited/clientUpdateProhibited; nameservers NS1/NS2.AFTERNIC.COM (ainda apontando para o parking do vendedor no momento da leitura) |
| Wayback CDX (web.archive.org/cdx, via curl) | 20 capturas 2011-01-28 → 2025-07-13. 2011–2019: página "Home" de uma empresa local chamada "Sarasota Concrete" (© 2005, e-mail `info@saraotaconconcrete.com` com erro de digitação, imagens de menu "About Us", "Contact", "Curbing" — provavelmente landscape curbing); 2021-12: 301; 2022-02: página de venda da Epik ("Buy This Domain For $9,700"); 2023-04: página comprimida ilegível; 2024: 301/302; 2025-07: página de 292 bytes (parking) |
| Google Safe Browsing (transparencyreport) | interface exige JavaScript; **verificar à mão** em transparencyreport.google.com/safe-browsing/search?url=sarasotaconcrete.com |
| Backlinks (Bing Webmaster / Ahrefs free) | BLOCKED (sem conta); fazer após verificação do site no Bing Webmaster |

Conclusão: histórico benigno (empresa local + parking). Sem disavow. O nome anterior do domínio reforça a leitura "descritivo/municipal" da marca.

## 2. Sunbiz (search.sunbiz.org, via curl)

| Busca | Resultado |
|---|---|
| Entidade "Sarasota Concrete" | SARASOTA CONCRETE CO (160713, INACT); SARASOTA CONCRETE & BLOCK CO (160713, NAME HS — histórico); SARASOTA CONCRETE LIFTING, LLC (L03000005511, INACT); **SARASOTA CONCRETE SOLUTIONS LLC.** (L24000328771, **Active**) |
| Entidade "Lakewood Ranch Concrete" | nenhum registro (confirma a nota do prompt: a LLC ainda não existe) |
| Entidade "GCM Best Services" | GCM BEST SERVICES CORP — P22000086622 — Active |
| Nome fictício "Sarasota Concrete" | página protegida por challenge JavaScript — **BLOCKED**; checar à mão em dos.sunbiz.org/ficinam.html |

Leitura: "Sarasota Concrete" é descritivo + nome de município; não há entidade ativa idêntica. "Sarasota Concrete Solutions LLC" (2024) e "Sarasota Concrete Systems" (marca usada por concrete-sarasotafl.com) coexistem no mercado; distinção depende do logo/identidade e de não usar "Solutions"/"Systems"/"Contractors" no nome (o prompt já proíbe sufixos). Recomendação: registrar o DBA "Sarasota Concrete" na Sunbiz em nome de `{{LEGAL_ENTITY}}` e publicar o anúncio legal exigido pela F.S. 865.09.

## 3. USPTO

TESS/TSDR bloqueiam consulta automatizada (401). Um resultado de busca apontou para o serial 90226068 no tmsearch.uspto.gov, sem confirmação de que seja "Sarasota Concrete". **Verificar à mão** (tmsearch.uspto.gov → "Sarasota Concrete"). Marca geográfica descritiva dificilmente registrável no Principal Register sem secondary meaning; o risco relevante é conflito com marcas locais em uso, não registro federal.

## 4. Licenciamento

| Nível | Fonte | Achado |
|---|---|---|
| Estado (DBPR) | myfloridalicense.com lista "does not require a license" (bloqueada para fetch; snippets Levelset/Benchmark Pavers) | instalação de driveways e pavers está entre os serviços que **não** exigem licença estadual de construção; ressalva explícita de que cidades/condados podem exigir licença local |
| F.S. 489.119(5)(b) (flsenate.gov, texto 2025 lido) | "Each registrant or certificateholder shall affix the certificate or registration number to each application for a building permit and shall cause such number to be included in every offer of services, business proposal, bid, contract, or advertisement, regardless of medium, as defined by board rule, used by that person in the practice of contracting" — vale para quem **tem** registro/certificação estadual |
| Sarasota County — Código Cap. 22 Art. V § 22-122 (eLaws) | "It shall be unlawful … to contract for, or do any construction work in the trade or trades designated under the authority of this Article unless said person, firm or corporation holds an active Sarasota County Operating Certificate in addition to an applicable Sarasota County Certificate of Competency"; owner-contractor exemption para residência própria; General Contractors Licensing and Examining Board examina specialty contractors; categoria local "Masonry/Concrete" limitada a footers, slabs, floors e paredes de alvenaria até 1 andar (snippet do Cap. 22 — confirmar texto no showdocument 13022) |
| Charlotte County (charlottecountyfl.gov, lido integralmente) | permit de driveway/slab pode ser puxado por Owner-Builder, Certified/Registered Building, General, Residential ou **Local Concrete Masonry** |
| City of Sarasota / Venice / North Port / Longboat Key | registram contratantes com licença estadual ou competency card do condado; North Port exige desenhos selados por engenheiro FL quando aplicável |

Decisão de texto público: "Insured" (com `{{INSURANCE_PROOF}}`), nunca "Licensed", até `{{LICENSE_TYPE_AND_NUMBER}}` ser informado. Se a entidade tiver Certificate of Competency do condado, o número vai para footer, About e schema; se tiver licença estadual (CBC/CGC/CRC), o número vai para toda publicidade (489.119(5)(b)).

## 5. Entidade que executa em Sarasota

Hipótese do prompt: a mesma do Lakewood Ranch. Fatos: Lakewood Ranch Concrete LLC não existe na Sunbiz; GCM Best Services Corp existe (Orlando). Logo, hoje a única pessoa jurídica ativa é a GCM. O site trata isso como `{{LEGAL_ENTITY}}` em OWNER-INPUTS e a divulgação de consentimento do formulário diz que o pedido "may be forwarded to the licensed or insured provider that serves your area" sem nomear a GCM até decisão do proprietário (regra 6 do prompt mestre).
