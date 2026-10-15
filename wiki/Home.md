# RedPilot

**AI-orchestrated offensive security** — one target in, a written assessment out.
Point RedPilot at an authorized target and the AI plans the recon, RedPilot runs
the tools on your machine, and you get the findings plus a written assessment.
Built for Kali, bug bounty, and red-team work.

> ⚠️ **Authorized testing only.** Engagement-scope enforcement, signed
> authorizations, and an append-only audit trail run across every surface — they
> are safety controls, **not** authorization. You are responsible for written
> permission for every target.

```bash
pip install "redpilot[ai]"     # RedPilot + AI providers
redpilot setup                 # pick your AI + database (SQLite = zero setup)
redpilot agent target.com      # the AI plans → runs → reports, end to end
```

## Contents

- **[[Installation]]** — pip extras, requirements, external recon tools
- **[[Quickstart]]** — agent, pipeline, single modules, mock mode
- **[[Configuration]]** — environment variables, AI providers, database
- **[[CLI Reference|CLI-Reference]]** — every command
- **[[HTTP API & Dashboard|HTTP-API]]** — REST + WebSocket, metrics, web console
- **[[MCP]]** — expose RedPilot to Claude Desktop; consume external MCP servers
- **[[Staged Pipeline|Staged-Pipeline]]** — discovery → validation → remediation → report
- **[[Engagements & RBAC|Engagements-and-RBAC]]** — multi-tenant workspaces + roles
- **[[Deployment]]** — hardened Docker / Podman / Caddy
- **[[Security & Threat Model|Security-and-Threat-Model]]** — controls & risk classes
- **[[FAQ]]**

## One engine, many surfaces

Reach RedPilot from the **CLI**, the **HTTP API**, the **web dashboard**, or an
**MCP host** — they all drive the same service engine. Every active step is
scope-gated and audit-logged, runs the modules on your machine, and the AI writes
it up.

| Surface | Entry |
|---|---|
| CLI | `redpilot <command>` |
| HTTP API + dashboard | `redpilot serve` → `http://127.0.0.1:8000` |
| MCP server | `redpilot mcp` (for Claude Desktop / MCP hosts) |

- PyPI: https://pypi.org/project/redpilot/
- Source: https://github.com/geevarghesekthomas84-sys/redpilot
- License: MIT
