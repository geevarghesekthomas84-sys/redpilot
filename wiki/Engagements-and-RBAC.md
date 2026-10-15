# Engagements & RBAC

Run multiple **isolated engagements** with **role-based access control** — for
teams and concurrent client work. Each engagement has its own scope, audit trail,
and report storage; nothing leaks between them.

## Scope (the safety gate)

```bash
redpilot scope add target.com
redpilot scope add 10.0.0.0/24
redpilot scope show
redpilot scope remove 10.0.0.0/24
redpilot scope show --file engagement_scope.json
```

Out-of-scope targets are refused (fail-closed once a scope is set). Overly-broad
targets (wildcards, `0.0.0.0/0`, huge CIDRs) are rejected at the input boundary.

## Engagements

```bash
export REDPILOT_AUTH_SIGNING_KEY="…"      # key that mints authorizations
redpilot engagements --create "Acme Corp" --scope "acme.com,api.acme.com" \
                     --authorized-by "ciso@acme.com" --retention-days 90
redpilot engagements                       # list
```

Each engagement lives under `REDPILOT_ENGAGEMENTS_DIR` with its own `scope.json`,
`audit.jsonl`, and `reports/`.

## Roles

Map API keys to a role and the engagements they may touch via `REDPILOT_PRINCIPALS`
(or `REDPILOT_PRINCIPALS_FILE`):

```bash
export REDPILOT_PRINCIPALS='{
  "LEAD_KEY":  {"name":"lead","role":"lead","engagements":["*"]},
  "OP_KEY":    {"name":"op","role":"operator","engagements":["acme-corp"]},
  "VIEW_KEY":  {"name":"client","role":"viewer","engagements":["acme-corp"]}
}'
```

| Role | Can |
|---|---|
| **viewer** | read scope, tools, findings, audit |
| **operator** | + launch scans & active agent/pipeline runs (in allowed engagements) |
| **lead** | + manage scope, create engagements, sign authorizations |

**Backward-compatible:** with no principals configured, existing
`REDPILOT_API_KEYS` act as all-access leads — RBAC is strictly opt-in.

Over the API, send `X-API-Key` (→ your role) and `X-Engagement: <id>` to select
the workspace. A viewer gets `403` on active endpoints; access outside your
granted engagements is `403`; an unknown engagement is `404`.

## Signed authorizations

With `REDPILOT_AUTH_SIGNING_KEY` set, an engagement carries a tamper-evident HMAC
signature over its id, scope hash, authorizer, and expiry. Editing the stored
scope or expiry invalidates it, and active runs on a persisted engagement are
refused without a valid, unexpired signature.
