# Quickstart

> Set an engagement scope first so active steps are gated to authorized targets
> (see **[[Engagements & RBAC|Engagements-and-RBAC]]**):
>
> ```bash
> redpilot scope add target.com
> ```

## The autonomous agent

The AI plans which modules to run, chains them, and writes the assessment:

```bash
redpilot agent target.com                 # plan → confirm → run → assess
redpilot agent target.com --dry-run       # show the plan only; touch nothing
redpilot agent target.com -y --aggressive # no prompt; deeper/active settings
```

## The staged pipeline (deterministic)

Discovery → validation → remediation → report, with strict stage hand-offs:

```bash
redpilot pipeline target.com --report-dir ./reports
```

See **[[Staged Pipeline|Staged-Pipeline]]**.

## Single modules

```bash
redpilot recon    target.com      # subdomains · DNS · WHOIS
redpilot toolkit  target.com      # external recon chain (subfinder → … → nuclei)
redpilot webscan  https://target  # headers · TLS · paths
redpilot scan     target.com      # network + CVE mapping (nmap)
redpilot crawl    https://target  # crawler
```

## Mock mode (no target touched)

Dry-run the whole pipeline with synthetic findings — great for demos, dev, CI:

```bash
REDPILOT_MOCK=1 redpilot webscan target.com     # any module honors it
redpilot pipeline target.com --mock             # or options {"mock": true} via API
```

## Reports, diff, export

```bash
redpilot report target.com --format both        # HTML + JSON
redpilot diff <old_scan_id> <new_scan_id>        # what changed
redpilot export target.com --format csv          # client-friendly CSV
```

## Run it as a service

```bash
pip install "redpilot[api]"
redpilot serve                     # http://127.0.0.1:8000  (dashboard at /, docs at /docs)
```

See **[[HTTP API & Dashboard|HTTP-API]]**.
