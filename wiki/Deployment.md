# Deployment

## Dev stack (Docker / Podman)

MongoDB + the RedPilot CLI in one command:

```bash
docker-compose up -d
docker-compose run redpilot recon target.com
docker-compose run redpilot shell
```

Podman works with the same file: `podman compose up -d`. On SELinux hosts add
`:z` to bind mounts if you hit "permission denied".

## Hardened API stack

Run the API behind a **Caddy** TLS gateway, with the API in a hardened container
(non-root, read-only root FS, `cap_drop: ALL`). Only the gateway is exposed.

```bash
cd deploy
cp .env.example .env            # set REDPILOT_API_KEYS (and REDPILOT_DOMAIN for real TLS)
docker compose up -d --build    # Caddy gateway + API (SQLite, zero-setup)
curl -k https://localhost/health
```

Add MongoDB: `docker compose --profile mongo up -d --build`.

### Through the gateway

| URL | Auth | What |
|---|---|---|
| `https://localhost/` | open | dashboard |
| `/health`, `/version`, `/metrics`, `/schema`, `/docs` | open | ops / contract |
| everything else | `X-API-Key` | scans, agent, scope, engagements, audit |

### Podman specifics

- **Ports 80/443 rootless** — run rootful (`sudo podman compose …`), lower the
  threshold (`sysctl net.ipv4.ip_unprivileged_port_start=80`), or publish high ports.
- **SELinux** — relabel the Caddyfile mount with `:ro,Z`, or
  `--security-opt label=disable`.

## Hardening

- **Gateway** — automatic TLS, HSTS + security headers, request-body cap; opt-in
  mTLS and rate-limiting.
- **API container** — non-root (uid 10001), read-only root FS with state only on
  the `/data` volume, `cap_drop: ALL`, `no-new-privileges`, resource limits,
  healthcheck.
- **CI** — Trivy (filesystem + image), pip-audit, and a CycloneDX SBOM.

Full guide: `SECURITY_HARDENING.md` (mTLS, rate-limiting, sops+age secrets,
authorized-egress note, pre-exposure checklist).

## Cloudflare (landing page only)

The Python backend does not run on Cloudflare's Workers runtime. The repo's
`wrangler.toml` publishes only the static landing page under `public/`
(`npx wrangler deploy`).
