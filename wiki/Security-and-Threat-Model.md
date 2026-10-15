# Security & Threat Model

RedPilot is offensive-security tooling: used correctly it tests systems you are
**authorized** to test; used incorrectly it can cause harm. Scope enforcement,
authorization signing, and the audit trail are safety controls — **not**
authorization. You are responsible for written permission for every target.

## Layered controls

| Threat | Control |
|---|---|
| Scanning out-of-scope hosts | engagement-scope enforcement (fail-closed when scope set) |
| Accidental mass / internet-wide scan | overly-broad-target rejection (wildcards, huge CIDRs) |
| Unauthorized active testing | signed engagement authorizations (HMAC + expiry) |
| Unauthenticated API access | API-key auth on every non-public endpoint |
| Privilege misuse | RBAC roles (viewer / operator / lead) |
| Request flooding / external-service abuse | per-principal rate limiting (429) |
| Command injection | subprocess **arg lists** only (never `shell=True`) + a destructive-command denylist |
| Prompt-injection via target/AI output | output sanitization, defanging, never-execute policy |
| Secret leakage in logs | redaction filter on all log sinks |
| Supply-chain CVEs | Trivy + pip-audit + CycloneDX SBOM in CI |
| Blast radius of the API container | non-root, read-only FS, cap_drop, TLS gateway |

## Out of scope (non-goals)

- RedPilot does **not** grant authorization or verify you have it.
- It does not sandbox the external recon binaries (`nmap`, `nuclei`, …) — run it
  on a host you control, ideally the hardened container.
- It does not defend against a malicious operator holding a valid lead key.
- AI providers see the prompts you send — use local models (Ollama / LM Studio)
  when engagement data must not leave the host.

## Risk by workflow

| Workflow | Touches target? | Risk |
|---|---|---|
| `scope` / `engagements` | no | Low |
| `recon` (passive) | indirect | Low–Med |
| `toolkit` / active recon | yes | Med |
| `webscan` / `crawl` | yes | Med |
| `scan` (network/nmap) | yes | Med–High |
| `agent` (dry-run) / `pipeline --mock` | no | Low |
| `agent` (active) / aggressive nuclei DAST | yes | High |

**Mock mode** (`REDPILOT_MOCK=1` / `--mock`) drops every workflow to Low — the
pipeline runs end-to-end with synthetic findings and no target is contacted.

## Reporting

Security issues: see `SECURITY.md`. Full threat model: `docs/THREAT_MODEL.md`.
Deploy hardening: `SECURITY_HARDENING.md`.
