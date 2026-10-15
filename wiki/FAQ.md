# FAQ

**What is RedPilot?**
An AI-orchestrated offensive-security platform: point it at an authorized target
and the AI plans the recon, RedPilot runs the tools on your machine, and you get
findings plus a written assessment. Reach it from the CLI, HTTP API, web
dashboard, or an MCP host — all driving one scope-gated, audited engine.

**Is it legal to use?**
RedPilot is for **authorized testing only**. Scope enforcement and signed
authorizations are safety controls, not permission. You must have written
authorization for every target.

**Was this project called something else?**
Yes — it was formerly `spaf`. It is now `redpilot` (RedPilot). Legacy `SPAF_*`
environment variables are still honored for backward compatibility.

**Do I need MongoDB?**
No. Use the zero-setup SQLite backend: `REDPILOT_DB_BACKEND=sqlite` (or pick it in
`redpilot setup`).

**Which AI providers are supported?**
Google Gemini, Anthropic Claude, and OpenAI-compatible local servers (Ollama,
LM Studio). Use local models to keep engagement data on your host. See
**[[Configuration]]**.

**Can I try it without touching a real target?**
Yes — mock mode: `REDPILOT_MOCK=1 redpilot webscan target.com` or
`redpilot pipeline target.com --mock`. Synthetic findings, no network.

**How do I run it as a service / for a team?**
`redpilot serve` for the API + dashboard; see **[[HTTP API & Dashboard|HTTP-API]]**,
**[[Engagements & RBAC|Engagements-and-RBAC]]**, and **[[Deployment]]**.

**Can I add my own scanner?**
Yes. Subclass `PluginModule` and advertise it on the `redpilot.modules`
entry-point group, or register it in-process. It then runs through CLI/API/MCP.
Plugins are not auto-added to the agent's curated action set.

**Is the output machine-readable?**
Yes — `redpilot schema` (or `GET /schema`) emits JSON Schema for every result
model; checked-in schemas live in `docs/schemas/`.

**How do I report a security issue?**
See `SECURITY.md` in the repo.
