# Configuration

RedPilot is configured through environment variables (a `.env` in your working
directory is auto-loaded). All variables use the `REDPILOT_` prefix.

> **Back-compat:** legacy `SPAF_*` variables are still honored — at startup
> RedPilot mirrors any set `SPAF_*` onto the matching `REDPILOT_*` when the new
> one is unset. Prefer `REDPILOT_*` going forward.

## Core

| Variable | Default | Purpose |
|---|---|---|
| `REDPILOT_DB_BACKEND` | `mongo` | `mongo` or `sqlite` (zero-setup local file) |
| `REDPILOT_SQLITE_PATH` | `redpilot.db` | SQLite file path |
| `REDPILOT_MONGO_URI` | `mongodb://localhost:27017` | MongoDB connection |
| `REDPILOT_LOG_DIR` | `./logs` | log directory |
| `REDPILOT_LOG_LEVEL` | `INFO` | log level |
| `REDPILOT_AUDIT_LOG` | `logs/audit.jsonl` | audit trail path |

## AI providers & orchestration

| Variable | Purpose |
|---|---|
| `AI_PROVIDER` | `google` \| `claude` \| `ollama` \| `lmstudio` |
| `GOOGLE_API_KEY` / `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` | provider keys |
| `REDPILOT_MODEL_PLAN` / `_ANALYZE` / `_CODEGEN` / `_DEFAULT` | route each task to a model; comma-separate for fallbacks |
| `REDPILOT_CACHE` | `off` to disable the response cache |
| `REDPILOT_CACHE_PATH` | cache DB path |
| `REDPILOT_BUDGET_CALLS` / `REDPILOT_BUDGET_SECONDS` | bound each agent run |

Local models (Ollama / LM Studio) keep engagement data on your host.

## API, RBAC & engagements

| Variable | Purpose |
|---|---|
| `REDPILOT_API_KEYS` / `REDPILOT_API_KEY` | API keys (comma-separated); one is generated if unset |
| `REDPILOT_PRINCIPALS` / `REDPILOT_PRINCIPALS_FILE` | map keys → roles + engagements (RBAC) |
| `REDPILOT_AUTH_SIGNING_KEY` | mint/verify signed engagement authorizations |
| `REDPILOT_ENGAGEMENTS_DIR` | engagement workspaces root (default `engagements`) |
| `REDPILOT_RATE_LIMIT` / `REDPILOT_RATE_BURST` | API rate limit (req/min, burst) |

## Safety & stealth

| Variable | Purpose |
|---|---|
| `REDPILOT_MOCK` | `1` = synthetic findings, no target contacted |
| `USE_TOR=true` | route through TOR (`socks5://127.0.0.1:9050`) |
| `PROXY_FILE=./proxies.txt` | rotating proxy chain |
| `RANDOM_USER_AGENT=true` | randomize User-Agent per request |
| `NIST_API_KEY` / `SHODAN_API_KEY` | faster CVE lookups / passive intel |

## Passive intel

`SHODAN_API_KEY` enables Shodan recon (`redpilot[intel]`). A full `.env.example`
ships in the repo.
