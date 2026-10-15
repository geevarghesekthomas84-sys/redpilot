# HTTP API & Dashboard

Run RedPilot as a service — everything the CLI does, over REST + WebSocket, with
a built-in web dashboard and Prometheus metrics.

```bash
pip install "redpilot[api]"
export REDPILOT_API_KEYS="your-secret-key"   # or let it print a generated one
redpilot serve                               # http://127.0.0.1:8000  (docs at /docs)
```

Secure by default: every endpoint except health/version/metrics/`/schema` and the
dashboard needs an API key (`X-API-Key`), active scans are scope-gated, and
requests are rate-limited.

## Async job model

```bash
# start a scan → job id, then stream it
curl -s -XPOST localhost:8000/scans -H "X-API-Key: $KEY" \
     -H 'content-type: application/json' \
     -d '{"module":"toolkit","target":"example.com"}'
# → {"job_id":"…","status":"running"}
#   GET /jobs/{id}       → status + typed findings
#   WS  /ws/jobs/{id}    → live step/finding events
```

## Endpoints

| Endpoint | Auth | What |
|---|---|---|
| `GET /health`, `GET /version` | open | liveness / version |
| `GET /metrics` | open | Prometheus metrics (aggregate only) |
| `GET /schema` | open | JSON Schema of result models |
| `GET /`, `GET /dashboard` | open | built-in web console |
| `GET /docs` | open | OpenAPI explorer |
| `GET /whoami` | key | your principal (role + engagements) |
| `GET /engagements`, `POST /engagements` | key / lead | list / create engagements |
| `GET /scope`, `POST /scope` | key / lead | view / add scope |
| `GET /tools` | key | external-tool install status |
| `GET /audit` | key | recent active-action audit entries |
| `POST /scans` | operator | start a scan job (202 + job id) |
| `POST /agent` | operator | start an agent job |
| `POST /pipeline` | operator | start a staged-pipeline job |
| `GET /jobs/{id}` | key | job status + typed result |
| `WS /ws/jobs/{id}` | key | live progress & findings |
| `GET /scans/recent`, `GET /findings/{id}` | key | history / findings |

Select an engagement per request with the `X-Engagement: <id>` header (see
**[[Engagements & RBAC|Engagements-and-RBAC]]**). Roles gate who can do what.

## Dashboard & metrics

- **Dashboard** (`/`) — connect with your `X-API-Key`, see scope/tools, launch
  scans or the agent, watch live events over WebSocket, read findings + audit.
- **Metrics** (`/metrics`) — scans started/completed/failed by module, findings
  by severity, agent runs by mode, auth failures, rate-limited requests. Labels
  are aggregate only (no target names), so it's safe to scrape.

## Production

Bind `--host 0.0.0.0` **only** behind the hardened reverse-proxy gateway — see
**[[Deployment]]**.
