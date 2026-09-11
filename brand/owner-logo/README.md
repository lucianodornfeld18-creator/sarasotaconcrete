# Logo fornecida pelo proprietário — 2026-09-11

O proprietário forneceu a logo definitiva: monograma hexagonal em **dourado/latão com grafite
escuro**, wordmark **SARASOTA** em grotesca pesada quase preta, **CONCRETE** em dourado com
letter-spacing, e a tagline **"SOLID FOUNDATIONS. BEAUTIFUL SPACES."**

Isso substitui as dez direções de `brand/logos.html`, que ficam como histórico.

## Coloque o arquivo original aqui

O PNG anexado no chat **não chega ao disco**. Salve o original nesta pasta com o nome
`logo-full.png` e rode:

```
cd site
python make_brand_assets.py
python build.py
```

O script detecta `brand/owner-logo/logo-full.png` e passa a usá-lo para o `og:image` (1200×630),
o ícone social 512 e a assinatura de e-mail. Sem o arquivo, ele gera esses assets a partir do SVG
plano descrito abaixo, e o site funciona normalmente.

## Por que existe um SVG plano além da logo original

A logo original é um monograma isométrico com gradiente de latão e textura de pedra. Isso é ótimo
em material impresso, num cartão e numa assinatura de e-mail. Não funciona em três lugares onde o
site precisa da marca:

| Uso | Problema com a arte original | O que o SVG plano resolve |
|---|---|---|
| Favicon 16 e 32 px | O gradiente e a textura viram uma mancha ilegível | Duas cores planas, silhueta reconhecível |
| Header fixo em 34 px | Idem, e o peso do arquivo entra no LCP | 1,2 KB inline, zero requisição |
| Modo escuro do navegador | O grafite desaparece no fundo escuro | Variante com o grafite trocado por creme |

Então a marca do site usa: **SVG plano** no header, favicon e ícone; **arte original** no og:image,
no social e no e-mail. É o padrão normal de um sistema de identidade, não um substituto da sua logo.

## Paleta extraída da logo

| Token | HEX | Onde |
|---|---|---|
| `--gold` | `#C1922E` | Cor primária: "CONCRETE" no wordmark, botões, links, metade clara do monograma |
| `--gold-lt` | `#E0BC63` | Realce do latão; texto dourado sobre fundo escuro |
| `--gold-dk` | `#8F6B1E` | Hover e estados ativos |
| `--ink` | `#1F1F1F` | "SARASOTA" no wordmark e texto corrido |
| `--graphite` | `#2E2E30` | Metade escura do monograma, seções escuras |
| `--paper` | `#FFFFFF` | Fundo, igual ao da arte original |
| `--sand` | `#F4F1EA` | Seções alternadas |

## Nota de compliance registrada

A tagline diz "Solid foundations". O site **não** oferece fundações, footings, seawall caps nem
muros estruturais — estão excluídos por falta de licença confirmada, conforme o prompt. A tagline é
linguagem figurativa de marca e o site não tem nenhuma página, menção ou schema de fundação, então
o risco é baixo. Mas se você preferir eliminá-lo por completo, a alternativa é usar a tagline só no
material impresso e manter no site apenas "Concrete, pavers and pool decks", que é o que a empresa
efetivamente vende. Diga qual prefere.
