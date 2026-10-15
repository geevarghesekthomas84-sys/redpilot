# RedPilot deploy

Run the RedPilot API hardened, behind a **Caddy** TLS gateway. Only the gateway is
exposed to the network; the API listens on an internal network and is reached
only through Caddy. State (SQLite DB, audit logs, AI cache, engagements) lives on
the `redpilot_data` volume under `/data`, so the container itself runs **read-only**.

```
          ┌─────────────┐        internal         ┌───────────────┐
  :443 ──▶│   Caddy      │ ─────────────────────▶ │  RedPilot API      │
  :80  ──▶│  TLS·headers │   http://api:8000       │  (read-only,   │
          │  (opt mTLS)  │                         │   non-root)    │──▶ /data
          └─────────────┘                         └───────────────┘    volume
```

## Quick start

```bash
cd deploy
cp .env.example .env          # set REDPILOT_API_KEYS (and REDPILOT_DOMAIN for real TLS)
docker compose up -d --build  # gateway + API (SQLite, zero-setup)
curl -k https://localhost/health
```

Add MongoDB instead of SQLite:

```bash
docker compose --profile mongo up -d --build
```

### Podman

The stack runs on Podman with the same files — it's Docker-API compatible:

```bash
podman compose up -d --build         # Podman 4.4+ (compose provider)
# or: podman-compose up -d --build
```

Two Podman specifics for this hardened stack:

- **Ports 80/443 (rootless).** Binding privileged ports rootless is blocked by
  default. Either run rootful (`sudo podman compose up -d --build`), lower the
  threshold once (`sudo sysctl net.ipv4.ip_unprivileged_port_start=80`), or
  publish high ports instead (edit the gateway `ports:` to `8080:80`,`8443:443`).
- **SELinux (Fedora/RHEL).** The gateway bind-mounts `./Caddyfile`. If it reports
  "permission denied", relabel it with a `:Z` suffix —
  `./Caddyfile:/etc/caddy/Caddyfile:ro,Z` — or add `--security-opt label=disable`.

Everything else (read-only root FS, `cap_drop`, `no-new-privileges`, the `/data`
volume, the `mongo` profile) behaves identically under Podman.

## What you get

Through the gateway (replace `localhost` with your `REDPILOT_DOMAIN`):

| URL | Auth | What |
|---|---|---|
| `https://localhost/` | open | built-in web **dashboard** |
| `https://localhost/health`, `/version` | open | liveness / version |
| `https://localhost/metrics` | open | Prometheus metrics (aggregate only) |
| `https://localhost/docs` | open | OpenAPI explorer |
| everything else | `X-API-Key` | scans, agent, scope, engagements, audit |

## Configuration (`.env`)

| Variable | Default | Purpose |
|---|---|---|
| `REDPILOT_API_KEYS` | — (required) | comma-separated API keys |
| `REDPILOT_DOMAIN` | `localhost` | public domain for automatic Let's Encrypt TLS |
| `REDPILOT_ACME_EMAIL` | — | contact e-mail for real-domain ACME |
| `REDPILOT_DB_BACKEND` | `sqlite` | `sqlite` (zero-setup) or `mongo` (`--profile mongo`) |
| `AI_PROVIDER`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY` | — | optional AI assessment |
| `REDPILOT_PRINCIPALS` | — | map keys → roles + engagements (RBAC; unset = all-access lead) |
| `REDPILOT_AUTH_SIGNING_KEY` | — | mint tamper-evident engagement authorizations |

Inside the container, all writable state is pinned under `/data`
(`REDPILOT_SQLITE_PATH`, `REDPILOT_AUDIT_LOG`, `REDPILOT_CACHE_PATH`, `REDPILOT_ENGAGEMENTS_DIR`),
which is the only writable path — the root filesystem is read-only.

## Hardening at a glance

- **Gateway** — automatic TLS, HSTS + security headers, request-body cap; opt-in
  **mTLS** and rate-limiting (see the Caddyfile). Drops all caps except
  `NET_BIND_SERVICE`, `no-new-privileges`.
- **API container** — non-root (uid 10001), **read-only root FS** with state only
  on the `/data` volume, `cap_drop: ALL`, `no-new-privileges`, CPU/memory limits,
  and a `/health` healthcheck.
- **Exposure** — only the gateway publishes ports (80/443); the API and Mongo are
  internal-only.

Full guide — mTLS, rate-limiting, sops+age secrets, the authorized-egress note,
and a pre-exposure checklist — in
[`../SECURITY_HARDENING.md`](../SECURITY_HARDENING.md).

## Cloudflare (landing page only)

RedPilot's FastAPI backend is Python and **does not run on Cloudflare's Workers
runtime** — run it via the Docker/Caddy stack above. The repo's `wrangler.toml`
only publishes the static project **landing page** under `../public`
(`npx wrangler deploy`). It is a marketing/docs page, not the app.
