# Staged Pipeline

The staged pipeline is the **deterministic** counterpart to the agent: a fixed,
ordered workflow with strict stage hand-offs.

```
discovery → validation → remediation → report
```

Each stage receives **only** the previous stage's typed result — never another
stage's internals — so there is no cross-stage data leakage. Active module
execution goes through the same engine as everything else, so scope, RBAC, audit,
rate limiting, and mock mode all apply.

## Stages

| Stage | Runs | Produces |
|---|---|---|
| **discovery** | `recon`, `toolkit`, `crawl` | discovered assets/endpoints |
| **validation** | `webscan`, `scan` | confirmed + classified findings (incl. CVE mapping) |
| **remediation** | — (no target contact) | findings enriched with fix guidance |
| **report** | report generator | a JSON deliverable |

Each stage may only invoke its fixed module set, so (for example) discovery can
never launch a network scan. Findings are de-duplicated across stages; remediation
never mutates its inputs.

## Run it

```bash
redpilot pipeline target.com --report-dir ./reports      # CLI
redpilot pipeline target.com --mock                      # dry-run, no target touched
```

Over the API (operator role, scope-gated):

```bash
curl -s -XPOST localhost:8000/pipeline -H "X-API-Key: $KEY" \
     -H 'content-type: application/json' \
     -d '{"target":"target.com","options":{"mock":true}}'
# → job id; GET /jobs/{id} returns the per-stage results + final findings
```

## Output shape

The pipeline returns a typed `PipelineResult` — per-stage `StageResult`s plus the
final de-duplicated findings and severity counts. Both are in the JSON-Schema
export (`redpilot schema` / `GET /schema`).
