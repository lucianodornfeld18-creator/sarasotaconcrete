# -*- coding: utf-8 -*-
"""Remove os registros de estacionamento de um dominio recem-transferido para a Cloudflare e liga o
Email Routing com o encaminhamento padrao da rede.

Existe porque a importacao de zona da Cloudflare copia os registros do registrador, e nos dominios
comprados via GoDaddy/Afternic isso significa um null MX (`MX 0 .`), um `TXT "v=spf1 -all"` e dezenas
de delegacoes NS de subdominio para ns1/ns2.afternic.com. Enquanto o null MX existir, tanto
`POST /zones/{id}/email/routing/dns` quanto `/enable` falham com o erro 2008 "Non-Cloudflare MX
records exist", e o alias hello@ nunca entrega.

Seguro por desenho:

  * nao apaga nada sem `--apply` (o padrao e so relatar);
  * grava um backup JSON restauravel de TODOS os registros antes de tocar em qualquer coisa;
  * so apaga o que casa com o padrao de parking reconhecido. Qualquer outro registro e listado e
    preservado, inclusive verificacoes de dominio (google-site-verification e afins). Os registros
    `_acme-challenge` que a Cloudflare gerencia sozinha nao aparecem na API e nao sao tocados.

O token vem do ambiente (CLOUDFLARE_API_TOKEN) e nunca e escrito em disco. Precisa de Zone:DNS:Edit
e Zone:Email Routing:Edit na zona.

Uso:

    # PowerShell
    $env:CLOUDFLARE_API_TOKEN='cfut_...'
    python tools/cleanup-parking-dns.py --domain sarasotaconcrete.com            # relatorio
    python tools/cleanup-parking-dns.py --domain sarasotaconcrete.com --apply    # executa

    # restaurar, se precisar
    python tools/cleanup-parking-dns.py --restore dns-backup-<dominio>-<data>.json
"""
import argparse
import datetime
import json
import os
import pathlib
import sys
import time

import requests

API = "https://api.cloudflare.com/client/v4"
DEFAULT_DEST = "opusdigitalmarketingflorida@gmail.com"

# Anycast da Afternic/GoDaddy usado nas paginas de venda, verificado em 2026-09-11.
PARK_IPS = {"13.248.169.48", "76.223.54.146"}
PARK_NS = {"ns1.afternic.com", "ns2.afternic.com"}
PARK_TXT = {"v=spf1 -all"}


def headers():
    tok = os.environ.get("CLOUDFLARE_API_TOKEN") or os.environ.get("CFT")
    if not tok:
        sys.exit("Defina CLOUDFLARE_API_TOKEN no ambiente (nao passe o token por argumento: "
                 "argumentos ficam no historico do shell).")
    return {"Authorization": "Bearer " + tok, "Content-Type": "application/json"}


def call(method, path, H, **kw):
    r = requests.request(method, API + path, headers=H, timeout=45, **kw)
    try:
        return r.json()
    except ValueError:
        return {"success": False, "errors": [{"message": "resposta nao-JSON: HTTP %s" % r.status_code}]}


def die(res, what):
    print("ERRO %s -> %s" % (what, json.dumps(res.get("errors"))[:300]))
    sys.exit(1)


def is_parking(r):
    t = r["type"]
    c = (r.get("content") or "").strip()
    if t == "A":
        return c in PARK_IPS
    if t == "MX":
        return c in (".", "")                      # null MX
    if t == "TXT":
        return c.strip('"').strip() in PARK_TXT
    if t == "NS":
        return c.rstrip(".").lower() in PARK_NS
    return False


def list_records(H, zone):
    out, page = [], 1
    while True:
        r = call("GET", "/zones/%s/dns_records" % zone, H, params={"per_page": 100, "page": page})
        if not r.get("success"):
            die(r, "listar registros")
        out += r["result"]
        if page >= r["result_info"]["total_pages"]:
            return out
        page += 1


def find_zone(H, domain):
    r = call("GET", "/zones", H, params={"name": domain})
    if not r.get("success"):
        die(r, "buscar a zona")
    if not r["result"]:
        sys.exit("A zona %s nao existe nesta conta (ou o token nao a alcanca)." % domain)
    z = r["result"][0]
    print("zona %s  id=%s  status=%s" % (z["name"], z["id"], z["status"]))
    if z["status"] != "active":
        print("  aviso: a zona ainda nao esta ativa; os nameservers atuais sao %s"
              % z.get("original_name_servers"))
    return z["id"]


def restore(path):
    H = headers()
    recs = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    if not recs:
        sys.exit("backup vazio")
    zone = recs[0]["zone_id"]
    print("restaurando %d registros na zona %s" % (len(recs), recs[0]["zone_name"]))
    ok = 0
    for r in recs:
        body = {k: r[k] for k in ("type", "name", "content", "ttl") if k in r}
        for k in ("priority", "proxied"):
            if r.get(k) is not None:
                body[k] = r[k]
        res = call("POST", "/zones/%s/dns_records" % zone, H, json=body)
        if res.get("success"):
            ok += 1
        else:
            print("  falhou %-5s %-38s %s" % (r["type"], r["name"], json.dumps(res.get("errors"))[:120]))
    print("restaurados: %d de %d" % (ok, len(recs)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", help="dominio da zona, ex. sarasotaconcrete.com")
    ap.add_argument("--dest", default=DEFAULT_DEST, help="destino do encaminhamento de email")
    ap.add_argument("--alias", default="hello", help="parte local do alias (padrao: hello)")
    ap.add_argument("--apply", action="store_true", help="executa; sem isso apenas relata")
    ap.add_argument("--no-email", action="store_true", help="so limpa o DNS, nao mexe no Email Routing")
    ap.add_argument("--restore", help="restaura a partir de um backup JSON e sai")
    a = ap.parse_args()

    if a.restore:
        return restore(a.restore)
    if not a.domain:
        sys.exit("--domain e obrigatorio")

    H = headers()
    v = call("GET", "/user/tokens/verify", H)
    print("token:", v.get("result", {}).get("status") if v.get("success") else "INVALIDO")
    zone = find_zone(H, a.domain)

    recs = list_records(H, zone)
    park = [r for r in recs if is_parking(r)]
    keep = [r for r in recs if not is_parking(r)]
    print("\n%d registros na zona: %d de parking, %d preservados" % (len(recs), len(park), len(keep)))

    by_type = {}
    for r in park:
        by_type.setdefault(r["type"], []).append(r)
    for t in sorted(by_type):
        print("  %-4s x%-3d %s" % (t, len(by_type[t]),
                                   ", ".join(sorted({str(x.get("content"))[:28] for x in by_type[t]}))))
    if keep:
        print("  PRESERVADOS:")
        for r in keep:
            print("    %-5s %-40s %s" % (r["type"], r["name"], str(r.get("content"))[:60]))

    if not a.apply:
        print("\n(relatorio apenas; rode de novo com --apply para executar)")
        return

    stamp = datetime.date.today().isoformat()
    backup = pathlib.Path("dns-backup-%s-%s.json" % (a.domain, stamp))
    backup.write_text(json.dumps(recs, indent=2), encoding="utf-8")
    print("\nbackup de %d registros -> %s" % (len(recs), backup))

    print("\n== apagando")
    gone = 0
    for r in park:
        res = call("DELETE", "/zones/%s/dns_records/%s" % (zone, r["id"]), H)
        if res.get("success"):
            gone += 1
        else:
            print("  FALHOU %-5s %-38s %s" % (r["type"], r["name"], json.dumps(res.get("errors"))[:120]))
    print("  apagados %d de %d; restam %d registros" % (gone, len(park), len(list_records(H, zone))))

    if a.no_email:
        return

    print("\n== Email Routing")
    res = call("POST", "/zones/%s/email/routing/dns" % zone, H, json={})
    if not res.get("success"):
        print("  /dns ->", json.dumps(res.get("errors"))[:220])
        res = call("POST", "/zones/%s/email/routing/enable" % zone, H, json={})
        print("  /enable ->", "OK" if res.get("success") else json.dumps(res.get("errors"))[:220])
    else:
        print("  OK")

    alias = "%s@%s" % (a.alias, a.domain)
    rules = (call("GET", "/zones/%s/email/routing/rules" % zone, H).get("result") or [])
    if not any(m.get("value") == alias for ru in rules for m in (ru.get("matchers") or [])):
        payload = {"name": "%s -> forward" % a.alias, "enabled": True, "priority": 0,
                   "matchers": [{"type": "literal", "field": "to", "value": alias}],
                   "actions": [{"type": "forward", "value": [a.dest]}]}
        print("  regra %s:" % alias,
              "OK" if call("POST", "/zones/%s/email/routing/rules" % zone, H, json=payload).get("success") else "falhou")
    if not any((ru.get("matchers") or [{}])[0].get("type") == "all" and ru.get("enabled") for ru in rules):
        payload = {"name": "Forward all", "enabled": True, "matchers": [{"type": "all"}],
                   "actions": [{"type": "forward", "value": [a.dest]}]}
        print("  catch-all:",
              "OK" if call("PUT", "/zones/%s/email/routing/rules/catch_all" % zone, H, json=payload).get("success") else "falhou")

    time.sleep(3)
    s = call("GET", "/zones/%s/email/routing" % zone, H).get("result") or {}
    print("\n== resultado: routing enabled=%s status=%s" % (s.get("enabled"), s.get("status")))
    for ru in (call("GET", "/zones/%s/email/routing/rules" % zone, H).get("result") or []):
        m = ", ".join("%s=%s" % (x.get("type"), x.get("value")) for x in (ru.get("matchers") or []))
        act = ", ".join("%s=%s" % (x.get("type"), x.get("value")) for x in (ru.get("actions") or []))
        print("   regra on=%-5s %-38s -> %s" % (ru.get("enabled"), m, act))
    for r in list_records(H, zone):
        print("   %-5s %-32s %-46s prio=%s" % (r["type"], r["name"], str(r.get("content"))[:46], r.get("priority")))


if __name__ == "__main__":
    main()
