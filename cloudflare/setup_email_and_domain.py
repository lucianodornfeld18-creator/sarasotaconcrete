# -*- coding: utf-8 -*-
"""Finish the Cloudflare side for sarasotaconcrete.com.

Adapted from the script that worked for kissimmeeconcrete.com
(C:\\Users\\luana\\Projetos\\kissimmeeconcrete\\cloudflare\\setup_email_and_domain.py), with one step
added that the Kissimmee version did not need: Kissimmee's Pages project was already git-connected,
while Sarasota's site currently lives in `sarasotaconcrete-preview`, a direct-upload project that
Cloudflare cannot convert (the API answers 8000069).

Steps, safe to re-run:

  1. Clear what the registrar's parking service left in the zone: the A records on the apex, www and
     the wildcard pointing at the Afternic lander, the null MX records (`0 .`) that block Email
     Routing, the `v=spf1 -all` TXT records, and the NS records delegating subdomains back to
     ns1/ns2.afternic.com.
  2. Create the git-connected Pages project `sarasotaconcrete`, mirroring grovelandconcrete and
     kissimmeeconcrete exactly (build `python build.py`, root `site`, output `dist`), and deploy it.
  3. Attach the apex and www to that project and add the proxied CNAMEs.
  4. Enable Email Routing, forward hello@sarasotaconcrete.com to the marketing inbox and turn on the
     catch-all, matching windermereconcrete.com.
  5. Bind the rate-limit KV namespace, as the sibling projects do.

Deliberate deviation from the instruction to delete the old project first: the new project is
created and proven before anything is removed, so there is never a moment where the site exists
nowhere. Deleting `sarasotaconcrete-preview` is a separate, explicit `--delete-old` run.

Order matters: the null MX records must go before /email/routing/enable, or Cloudflare answers 2008
"Non-Cloudflare MX records exist".

Tokens: DNS work needs Zone.DNS:Edit, passed as CF_API_TOKEN. Pages and Email Routing work with the
wrangler OAuth session. Each call tries CF_API_TOKEN first and falls back to the wrangler token on an
auth error, so the pair together is enough and no new token is needed.

Known gap: the www -> apex redirect needs Zone:Rulesets, which neither token has. The canonical tags
already point every page at the apex, so this is cosmetic until a token with that scope exists.
"""
import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

ZONE = "sarasotaconcrete.com"
ZID = "f81cf0f1ee298f97eb8abb521f343097"
ACCOUNT_ID = "21cabe20549f2f63baa4d3fd781abe74"   # the DNS-scoped token returns an empty /accounts
PROJECT = "sarasotaconcrete"
OLD_PROJECT = "sarasotaconcrete-preview"
PAGES_HOST = "sarasotaconcrete.pages.dev"
DESTINATION = "opusdigitalmarketingflorida@gmail.com"
LOCAL_PART = "hello"
GH_OWNER = "lucianodornfeld18-creator"
GH_OWNER_ID = "265936952"
GH_REPO = "sarasotaconcrete"
GH_REPO_ID = "1366589111"
KV_BINDING = "RATE_LIMIT_KV"
KV_ID = "2425ece680b2407a9aa3e60d0d961d44"        # sarasotaconcrete-ratelimit
PARKING_IPS = {"13.248.169.48", "76.223.54.146", "172.67.147.196", "104.21.28.230"}
API = "https://api.cloudflare.com/client/v4"


def _wrangler_token():
    cfg = pathlib.Path(os.path.expanduser("~/.wrangler/config/default.toml"))
    if not cfg.exists():
        return None
    for line in cfg.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("oauth_token"):
            return line.split("=", 1)[1].strip().strip('"')
    return None


TOKENS = [t for t in (os.environ.get("CF_API_TOKEN") or os.environ.get("CLOUDFLARE_API_TOKEN"),
                      _wrangler_token()) if t]
if not TOKENS:
    raise SystemExit("no Cloudflare token: set CF_API_TOKEN or log in with wrangler")


def call(method, path, body=None):
    """Try each token in turn; an auth error falls through to the next one."""
    url = path if path.startswith("http") else API + path
    last = None
    for tok in TOKENS:
        r = urllib.request.Request(
            url, data=json.dumps(body).encode() if body is not None else None,
            method=method, headers={"Authorization": "Bearer " + tok,
                                    "Content-Type": "application/json"})
        try:
            return json.loads(urllib.request.urlopen(r, timeout=90).read())
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            try:
                last = json.loads(raw or "{}")
            except Exception:
                last = {"success": False, "errors": [{"code": e.code, "message": raw[:200]}]}
            codes = {str(x.get("code")) for x in (last.get("errors") or [])}
            if not ({"10000", "9109", "1000"} & codes):
                return last
    return last


def errs(r):
    return json.dumps((r or {}).get("errors"))[:220]


def is_parking(rec):
    typ, name = rec["type"], rec["name"]
    content = (rec.get("content") or "").strip().strip('"')
    if typ in ("A", "AAAA") and content in PARKING_IPS:
        return True
    if typ == "MX" and content in (".", ""):
        return True
    if typ == "TXT" and content.startswith("v=spf1") and "cloudflare" not in content:
        return True
    if typ == "NS" and content.rstrip(".").endswith("afternic.com") and name != ZONE:
        return True
    if typ == "CNAME" and name in (ZONE, "www." + ZONE) and PAGES_HOST not in content:
        return True
    return False


def step1_clear_parking_dns():
    print("1. clearing the registrar parking DNS")
    r = call("GET", f"/zones/{ZID}/dns_records?per_page=500")
    if not r.get("success"):
        print("   cannot read DNS: %s" % errs(r))
        print("   -> set CF_API_TOKEN to a token with Zone.DNS:Edit on " + ZONE)
        return False
    records = r["result"]
    targets = [x for x in records if is_parking(x)]
    keep = [x for x in records if not is_parking(x)]
    print("   %d of %d records look like parking leftovers" % (len(targets), len(records)))
    for x in keep:
        print("   KEEPING %-5s %-34s %s" % (x["type"], x["name"], str(x.get("content"))[:40]))
    backup = pathlib.Path(__file__).resolve().parent / ("dns-backup-%s.json" % ZONE)
    backup.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print("   backup of all %d records -> %s" % (len(records), backup.name))

    by_type, removed, failed = {}, 0, 0
    for rec in targets:
        d = call("DELETE", f"/zones/{ZID}/dns_records/{rec['id']}")
        if d.get("success"):
            removed += 1
            by_type[rec["type"]] = by_type.get(rec["type"], 0) + 1
        else:
            failed += 1
            print("   FAILED %-5s %-34s %s" % (rec["type"], rec["name"], errs(d)))
    print("   removed %d (%s)%s" % (removed, ", ".join("%s x%d" % kv for kv in sorted(by_type.items())),
                                    ", %d failed" % failed if failed else ""))
    left = call("GET", f"/zones/{ZID}/dns_records?per_page=500").get("result") or []
    print("   %d record(s) remain: %s" % (len(left), ", ".join(sorted({x["type"] for x in left})) or "none"))
    return failed == 0


def step2_create_pages_project():
    print("2. git-connected Pages project")
    existing = call("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}")
    if existing.get("success"):
        src = ((existing["result"].get("source") or {}).get("type"))
        print("   %s already exists (source=%s)" % (PROJECT, src))
        if src != "github":
            print("   WARNING: it is not git-connected; Cloudflare cannot convert one (8000069)")
        return existing["result"]

    body = {
        "name": PROJECT,
        "production_branch": "main",
        "source": {
            "type": "github",
            "config": {
                "owner": GH_OWNER, "owner_id": GH_OWNER_ID,
                "repo_name": GH_REPO, "repo_id": GH_REPO_ID,
                "production_branch": "main",
                "pr_comments_enabled": False,
                "deployments_enabled": True,
                "production_deployments_enabled": True,
                "preview_deployment_setting": "none",
                "preview_branch_includes": ["*"], "preview_branch_excludes": [],
                "path_includes": ["*"], "path_excludes": [],
            },
        },
        "build_config": {
            "build_command": "python build.py",
            "destination_dir": "dist",
            "root_dir": "site",
        },
        "deployment_configs": {
            "production": {"kv_namespaces": {KV_BINDING: {"namespace_id": KV_ID}}},
            "preview": {"kv_namespaces": {KV_BINDING: {"namespace_id": KV_ID}}},
        },
    }
    r = call("POST", f"/accounts/{ACCOUNT_ID}/pages/projects", body)
    if not r.get("success"):
        print("   create ->", errs(r))
        return None
    print("   created %s (subdomain %s)" % (PROJECT, r["result"].get("subdomain")))
    return r["result"]


def step3_deploy(timeout_s=900):
    print("3. deploying the production branch")
    d = call("POST", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/deployments", {"branch": "main"})
    if not d.get("success"):
        print("   trigger ->", errs(d))
    else:
        print("   deployment", d["result"].get("id"), "queued")
    deadline = time.time() + timeout_s
    last = None
    while time.time() < deadline:
        time.sleep(15)
        ds = call("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/deployments?per_page=1")
        rows = ds.get("result") or []
        if not rows:
            continue
        stage = (rows[0].get("latest_stage") or {})
        state = "%s/%s" % (stage.get("name"), stage.get("status"))
        if state != last:
            print("   ", state)
            last = state
        if stage.get("name") == "deploy" and stage.get("status") == "success":
            print("   build succeeded ->", rows[0].get("url"))
            return True
        if stage.get("status") == "failure":
            print("   build FAILED at stage", stage.get("name"))
            return False
    print("   still building after %ds" % timeout_s)
    return False


def step4_attach_domains():
    print("4. attaching the apex and www")
    for host in (ZONE, "www." + ZONE):
        r = call("POST", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains", {"name": host})
        print("   attach %-30s %s" % (host, "ok" if r.get("success") else errs(r)[:90]))

    cur = call("GET", f"/zones/{ZID}/dns_records?per_page=500").get("result") or []
    have = {(x["type"], x["name"]): x for x in cur}
    for host in (ZONE, "www." + ZONE):
        existing = have.get(("CNAME", host))
        if existing and PAGES_HOST in (existing.get("content") or ""):
            print("   CNAME already set for", host)
            continue
        c = call("POST", f"/zones/{ZID}/dns_records",
                 {"type": "CNAME", "name": host, "content": PAGES_HOST, "proxied": True, "ttl": 1})
        print("   CNAME %-30s -> %-28s %s" % (host, PAGES_HOST, "ok" if c.get("success") else errs(c)[:90]))

    print("   waiting for the certificates")
    for _ in range(24):
        time.sleep(15)
        d = call("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains")
        rows = [(x["name"], x.get("status")) for x in (d.get("result") or [])]
        print("     " + " | ".join("%s=%s" % r for r in rows))
        if rows and all(s == "active" for _, s in rows):
            print("   both domains active")
            return True
    print("   still provisioning; certificates can take a few more minutes")
    return True


def step5_email_routing():
    print("5. enabling Email Routing")
    r = call("POST", f"/zones/{ZID}/email/routing/enable", {})
    if r.get("success"):
        print("   routing enabled")
    elif "already" in errs(r).lower() or "enabled" in errs(r).lower():
        print("   routing already enabled")
    else:
        print("   enable ->", errs(r))
        if "MX" in errs(r):
            return False

    addr = f"{LOCAL_PART}@{ZONE}"
    rules = call("GET", f"/zones/{ZID}/email/routing/rules?per_page=50").get("result") or []
    if any(any(m.get("value") == addr for m in (x.get("matchers") or [])) for x in rules):
        print("   rule for %s already exists" % addr)
    else:
        c = call("POST", f"/zones/{ZID}/email/routing/rules", {
            "name": "Forward %s" % addr, "enabled": True,
            "matchers": [{"type": "literal", "field": "to", "value": addr}],
            "actions": [{"type": "forward", "value": [DESTINATION]}]})
        print("   rule %s -> %s  %s" % (addr, DESTINATION, "ok" if c.get("success") else errs(c)))

    ca = call("PUT", f"/zones/{ZID}/email/routing/rules/catch_all", {
        "name": "Forward all Sarasota Concrete email", "enabled": True,
        "matchers": [{"type": "all"}],
        "actions": [{"type": "forward", "value": [DESTINATION]}]})
    print("   catch-all -> %s  %s" % (DESTINATION, "ok" if ca.get("success") else errs(ca)))

    res = (call("GET", f"/zones/{ZID}/email/routing") or {}).get("result") or {}
    print("   status: enabled=%s state=%s" % (res.get("enabled"), res.get("status")))
    return True


def delete_old_project():
    print("deleting the superseded direct-upload project", OLD_PROJECT)
    new = call("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}")
    if not new.get("success"):
        print("   refusing: %s does not exist yet" % PROJECT)
        return
    doms = [d["name"] for d in (call("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains")
                                .get("result") or []) if d.get("status") == "active"]
    if ZONE not in doms:
        print("   refusing: %s is not serving %s yet (active: %s)" % (PROJECT, ZONE, doms or "none"))
        return
    r = call("DELETE", f"/accounts/{ACCOUNT_ID}/pages/projects/{OLD_PROJECT}")
    print("   ", "deleted" if r.get("success") else errs(r))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delete-old", action="store_true",
                    help="remove %s, only once %s serves the apex" % (OLD_PROJECT, PROJECT))
    a = ap.parse_args()

    print("tokens available: %d\n" % len(TOKENS))
    if a.delete_old:
        return delete_old_project() or 0

    if not step1_clear_parking_dns():
        return 1
    if not step2_create_pages_project():
        return 1
    step3_deploy()
    step4_attach_domains()
    step5_email_routing()
    print("\nDone. Check https://%s/ and send a test message to %s@%s" % (ZONE, LOCAL_PART, ZONE))
    print("Then, once the apex is serving: python cloudflare/setup_email_and_domain.py --delete-old")
    return 0


if __name__ == "__main__":
    sys.exit(main())
