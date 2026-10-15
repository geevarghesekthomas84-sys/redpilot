# RedPilot Command Reference

> **AI-orchestrated offensive security automation** — AI-Augmented Offensive Security  
> Every scan command automatically runs AI threat analysis after completion.  
> Add `--no-ai` to any command to skip. Add `--no-db` to run without MongoDB.

---

## 🗂️ Table of Contents

- [Scanning Commands](#-scanning-commands)
- [AI Commands](#-ai-commands)
- [Reporting & Operations](#-reporting--operations)
- [Engagement Scope](#-engagement-scope)
- [Global Options](#-global-options)
- [AI Provider Config](#-ai-providers--env-configuration)
- [Stealth / OpsSec](#-stealth--opsec-env)
- [Common Workflows](#-common-workflows)

---

## 🔍 Scanning Commands

### `redpilot recon <target>` — Domain Reconnaissance

Passive and active reconnaissance: subdomain enumeration, DNS audit, WHOIS, zone-transfer attempts, and **passive Shodan intelligence** (if `SHODAN_API_KEY` is set).

```bash
redpilot recon target.com                          # Full recon + AI + Shodan (if key set)
redpilot recon target.com --passive                # Passive OSINT only (stealthy)
redpilot recon target.com --no-ai                  # Skip AI analysis
redpilot recon target.com --output results.json    # Save findings to JSON
redpilot recon target.com --delay 1.5 --concurrency 3   # Slow + stealthy
```

| Flag | Default | Description |
|---|---|---|
| `--passive` / `--active` | passive | Passive OSINT only vs. active DNS brute-force |
| `--output <file>` | — | Save results as JSON |
| `--delay <seconds>` | `0.0` | Delay between DNS requests |
| `--concurrency <n>` | `5` | Max concurrent subdomain resolutions |
| `--no-ai` | off | Skip AI analysis after scan |
| `--no-db` | off | Run without MongoDB logging |

---

### `redpilot scan <target>` — Network Port Scan

High-speed port scanning using **Nmap** or **RustScan**, with service detection, OS fingerprinting, and automated CVE lookups via NIST NVD.

```bash
redpilot scan target.com                                       # Nmap standard scan + AI
redpilot scan target.com --intensity aggressive                # Deep scan (-sV -sC -O -A)
redpilot scan target.com --ports 1-65535                       # Full port range
redpilot scan target.com --scanner rustscan --ports 1-65535    # RustScan → Nmap pipeline
redpilot scan target.com --scanner rustscan --ulimit 8000      # Increase RustScan throughput
redpilot scan target.com --no-ai --output network.json        # Offline, save output
```

| Flag | Default | Description |
|---|---|---|
| `--scanner` | `nmap` | Scanner engine: `nmap` \| `rustscan` |
| `--ports` | `1-1024` | Port range (e.g., `1-65535`) |
| `--intensity` | `normal` | Nmap depth: `light` \| `normal` \| `aggressive` |
| `--ulimit` | `5000` | RustScan: open file descriptor limit |
| `--batch-size` | `2500` | RustScan: ports probed per batch |
| `--output <file>` | — | Save results as JSON |
| `--no-ai` | off | Skip AI analysis after scan |
| `--no-db` | off | Run without MongoDB logging |

> **RustScan + Nmap pipeline:** RustScan does async TCP mass-connect to find open ports, then hands them to Nmap for full service/OS/CVE detection.

---

### `redpilot webscan <url>` — Web Security Audit

Security headers, cookie flags, TLS/certificate checks, sensitive path probing, CORS, server disclosure.

```bash
redpilot webscan https://target.com                # Full web audit + AI analysis
redpilot webscan https://target.com --headers-only # Headers only (fast)
redpilot webscan https://target.com --no-ai        # Skip AI analysis
redpilot webscan https://target.com --output web.json
```

| Flag | Default | Description |
|---|---|---|
| `--headers-only` | off | Only check HTTP security headers |
| `--output <file>` | — | Save results as JSON |
| `--delay <seconds>` | `0.0` | Delay between path probe requests |
| `--concurrency <n>` | `5` | Max concurrent path probes |
| `--no-ai` | off | Skip AI analysis |
| `--no-db` | off | Run without MongoDB logging |

---

### `redpilot crawl <url>` — Web Application Spider

Recursively crawls a web application, discovers endpoints, forms, and flags sensitive keywords.

```bash
redpilot crawl https://target.com                  # Default crawl (depth 2, 50 pages)
redpilot crawl https://target.com --depth 4        # Deeper crawl
redpilot crawl https://target.com --max-pages 200  # Crawl more pages
redpilot crawl https://target.com --no-ai          # Skip AI analysis
```

| Flag | Default | Description |
|---|---|---|
| `--depth <n>` | `2` | Maximum crawl depth |
| `--max-pages <n>` | `50` | Maximum pages to crawl |
| `--output <file>` | — | Save results as JSON |
| `--no-ai` | off | Skip AI analysis |
| `--no-db` | off | Run without MongoDB logging |

---

### `redpilot agent <target>` — Autonomous Agent

The AI plans an ordered sequence of RedPilot modules, runs them on your host, and
writes one consolidated AI assessment at the end. The AI only chooses **which
built-in modules** to run (never arbitrary commands). Active steps are
scope-gated and ask for confirmation first.

```bash
redpilot agent example.com                         # plan → confirm → run → assess
redpilot agent example.com --goal "find web vulns" # steer the plan
redpilot agent example.com --dry-run               # show the plan only
redpilot agent example.com --aggressive -y         # deeper settings, no prompt
redpilot agent https://example.com --no-ai         # default playbook, no AI
redpilot agent example.com --output findings.json
```

| Flag | Default | Description |
|---|---|---|
| `--goal` / `-g` | — | Natural-language objective that steers planning |
| `--dry-run` | off | Show the plan and exit |
| `--yes` / `-y` | off | Skip the confirmation prompt |
| `--aggressive` | off | Aggressive nmap, nuclei DAST, active recon |
| `--scope-file` | `scope.json` | Engagement scope for active steps |
| `--ignore-scope` | off | Disable scope enforcement (dangerous) |
| `--output <file>` | — | Save all findings as JSON |
| `--no-ai` | off | Skip AI planning/assessment (default playbook) |
| `--no-db` | off | Run without database logging |

---

### `redpilot toolkit <target>` — External Recon Pipeline

Runs a chained pipeline of best-in-class open-source recon binaries, feeding each
stage's output into the next:

```
subfinder / assetfinder → dnsx → httpx → katana / hakrawler
                                       → waybackurls / gau → ffuf → nuclei
```

Each binary is **optional** — if it is not on `$PATH` the stage is skipped with a
warning, so the pipeline degrades gracefully on a partial install.

```bash
redpilot toolkit target.com                          # Full pipeline
redpilot toolkit target.com --no-nuclei --no-crawl   # Recon-only (no active scan)
redpilot toolkit target.com --fuzz --wordlist wl.txt # Add ffuf content fuzzing
redpilot toolkit target.com --nuclei-severity critical,high
redpilot toolkit target.com --output recon.json --no-ai
```

| Flag | Default | Description |
|---|---|---|
| `--no-subs` | off | Skip subdomain enumeration (subfinder/assetfinder) |
| `--no-probe` | off | Skip HTTP probing (httpx) |
| `--no-crawl` | off | Skip active crawling (katana/hakrawler) |
| `--no-urls` | off | Skip historical URL harvesting (waybackurls/gau) |
| `--no-nuclei` | off | Skip nuclei vulnerability scanning |
| `--fuzz` | off | Enable ffuf content fuzzing (requires `--wordlist`) |
| `--wordlist <file>` | — | Wordlist for ffuf |
| `--depth <n>` | `2` | Crawl depth for katana |
| `--nuclei-severity <list>` | `critical,high,medium` | Comma-separated nuclei severities |
| `--nuclei-dast` | off | Run nuclei DAST/fuzzing templates against the crawled URL corpus |
| `--scope-file <file>` | `scope.json` | Engagement scope consulted before active scanning |
| `--ignore-scope` | off | Disable scope enforcement (dangerous) |
| `--output <file>` | — | Save results as JSON |
| `--no-ai` | off | Skip AI analysis |
| `--no-db` | off | Run without MongoDB logging |

> **Scope safety:** if a scope file with in-scope entries exists, out-of-scope
> entry targets are refused and subdomains discovered outside the scope are
> dropped before any active stage (httpx/katana/ffuf/nuclei) runs. Manage scope
> with `redpilot scope add|remove|show`. Bypass with `--ignore-scope` only when you
> have authorization for every host in the target set.

---

### `redpilot tools` — Toolkit Installation Status

Lists every external recon binary RedPilot integrates and shows whether each is
installed on your system, with install sources for any that are missing.

```bash
redpilot tools                 # list install status
redpilot tools --install       # install missing Go-based tools via 'go install' (needs Go)
redpilot tools --install --force   # reinstall all tools
```

| Flag | Description |
|---|---|
| `--install` | Install missing recon tools via `go install` |
| `--force` | With `--install`, (re)install every tool, not just missing ones |

| Tool | Role |
|---|---|
| `subfinder` | Passive subdomain enumeration |
| `assetfinder` | Passive subdomain/asset discovery |
| `dnsx` | Fast DNS resolver / toolkit |
| `httpx` | HTTP(S) probing & fingerprinting |
| `katana` | Next-gen crawling & spidering |
| `hakrawler` | Fast endpoint crawler |
| `waybackurls` | Wayback Machine URL harvesting |
| `gau` | getallurls historical URL fetch |
| `ffuf` | Content / directory fuzzing |
| `nuclei` | Template-based vulnerability scanning |

> The Docker image installs the full suite automatically. For a local install,
> use `go install` for the Go-based tools and grab `ffuf` from its releases page.

---

## 🤖 AI Commands

### `redpilot test-ai` — AI Provider Health Check

Tests the configured AI provider's connectivity and prints a health report table.

```bash
redpilot test-ai
```

**Output example:**
```
┌──────────────────────────────────┐
│     AI Provider Health Check     │
├──────────────┬───────────────────┤
│ Provider     │ OLLAMA            │
│ Model        │ llama3.2          │
│ Status       │ ✅ OK             │
│ Response     │ OK                │
└──────────────┴───────────────────┘
```

---

### `redpilot chat <query>` — Direct AI Consultation

Free-form chat with the **configured** AI provider.

```bash
redpilot chat "How do I bypass a WAF?"
redpilot chat "Write a Python PoC for CVE-2024-xxxx"
```

---

### `redpilot gemini <query>` — Google Gemini Shortcut

Queries **Google Gemini** regardless of `AI_PROVIDER` setting.

```bash
redpilot gemini "Explain CVE-2024-1234"
redpilot gemini "Write an Nmap scan script for internal networks"
```

---

### `redpilot claude <query>` — Anthropic Claude Shortcut

Queries **Anthropic Claude** regardless of `AI_PROVIDER` setting.

```bash
redpilot claude "Write an Ansible remediation task for missing HSTS"
redpilot claude "Summarize this pentest report in executive language"
```

---

### `redpilot ollama <query>` — Ollama Shortcut *(streaming)*

Queries your **locally running Ollama** model. Tokens stream to the terminal in real-time.

```bash
redpilot ollama "List exploitation paths for open SMB ports"
redpilot ollama "Generate a Python reverse shell"
```

> **Requires:** `ollama serve` running locally (or `OLLAMA_URL` pointing to remote).

---

### `redpilot lmstudio <query>` — LM Studio Shortcut *(streaming)*

Queries the **model currently loaded in LM Studio**. Tokens stream in real-time.

```bash
redpilot lmstudio "Analyze these HTTP headers for security risks"
redpilot lmstudio "Summarize OWASP Top 10 attack techniques"
```

> **Requires:** LM Studio → Local Server tab → Start Server.

---

### `redpilot ai <scan_id>` — Re-Analyze a Past Scan

Re-runs AI analysis on any previous scan's findings **without re-scanning** the target.

```bash
redpilot ai <scan_id>                              # Re-analyze (module auto-detected)
redpilot ai <scan_id> --module network             # Force network prompt template
redpilot ai <scan_id> --provider ollama            # Use Ollama for this call only
redpilot ai <scan_id> --provider lmstudio          # Use LM Studio for this call only
redpilot ai <scan_id> --provider claude            # Use Claude for this call only
```

| Flag | Default | Description |
|---|---|---|
| `--module` | auto | Prompt template: `recon` \| `network` \| `webscan` \| `crawler` |
| `--provider` | `.env` | Override AI provider for this call only |

---

### `redpilot analyze` — Full AI Threat Report

Generic AI analysis by scan ID or local JSON file.

```bash
redpilot analyze --id <scan_id>
redpilot analyze --file findings.json
```

---

### `redpilot poc <finding_id>` — Generate Exploit Script

Generates a standalone Python Proof-of-Concept exploit script.

```bash
redpilot poc <finding_id>
redpilot poc <finding_id> --output exploit.py
```

---

### `redpilot remediate <finding_id>` — Generate Fix Code

Generates production-ready remediation code for a specific finding.

```bash
redpilot remediate <finding_id>                    # Default: Ansible
redpilot remediate <finding_id> --format terraform
redpilot remediate <finding_id> --format bash
```

| Flag | Default | Values | Description |
|---|---|---|---|
| `--format` | `ansible` | `ansible` \| `terraform` \| `bash` | Output format |

---

## 📊 Reporting & Operations

### `redpilot export <target>` — Export Findings

Exports all deduplicated findings for a target from MongoDB to CSV or JSON.

```bash
redpilot export target.com                         # Default: CSV
redpilot export target.com --format csv            # Explicit CSV (client spreadsheets)
redpilot export target.com --format json           # JSON (pipeline integration)
redpilot export target.com --format csv --output /tmp/client_report.csv
```

| Flag | Default | Description |
|---|---|---|
| `--format` | `csv` | Output format: `csv` \| `json` |
| `--output <file>` | `<target>_findings.<ext>` | Custom output file path |

---

### `redpilot diff <scan_id_1> <scan_id_2>` — Compare Scans

Compares two scans and shows what's new, fixed, and unchanged.

```bash
redpilot history                                   # Get scan IDs first
redpilot diff <older_scan_id> <newer_scan_id>
```

**Output:**
```
Scan Diff  2026-05-01 10:00 → 2026-05-04 14:30
Target: target.com

┌─ 🆕 New Findings (3) ──────┐    ┌─ ✅ Fixed / Resolved (2) ──┐
│ missing_hsts               │    │ exposed_git_repo           │
│ cors_misconfiguration      │    │ cookie_no_secure_flag      │
│ server_version_disclosure  │    └────────────────────────────┘
└────────────────────────────┘

Unchanged: 5 findings
```

---

### `redpilot report <target>` — Generate HTML/JSON Report

The HTML report includes a severity-distribution chart, a per-module breakdown,
and (with `--with-ai`) an embedded AI threat-intelligence analysis. All finding
data is HTML-escaped.

```bash
redpilot report target.com --format html           # Dark-mode HTML dashboard
redpilot report target.com --format json           # Structured JSON export
redpilot report target.com --format both           # Both simultaneously
redpilot report target.com --with-ai               # Embed AI threat analysis
redpilot report --from-file findings.json          # Report from a saved JSON file
```

| Flag | Default | Description |
|---|---|---|
| `--format` | `both` | Output: `html` \| `json` \| `both` |
| `--with-ai` | off | Embed an AI threat-intelligence analysis in the report |
| `--output-dir <dir>` | `./reports` | Directory to save reports |
| `--from-file <file>` | — | Build the report from a local JSON results file |

---

### `redpilot watch <target>` — Shadow Scan (24/7 Monitoring)

Continuously re-runs a module on a schedule. AI alerts when new findings are detected.

```bash
redpilot watch target.com                              # Recon every hour (default)
redpilot watch target.com --interval 1800              # Every 30 minutes
redpilot watch target.com --module webscan             # Monitor web security posture
redpilot watch target.com --module network             # Monitor open ports
redpilot watch target.com --no-ai                      # Monitoring only, no AI summaries
redpilot watch target.com --no-db                      # No database logging
```

| Flag | Default | Description |
|---|---|---|
| `--interval <seconds>` | `3600` | Seconds between scans |
| `--module` | `recon` | Module to run: `recon` \| `webscan` \| `network` \| `crawl` \| `toolkit` |
| `--no-ai` | off | Skip AI alert summaries |
| `--no-db` | off | Run without MongoDB logging |

---

### `redpilot history` — View Past Scans

```bash
redpilot history                                   # Show 20 most recent scans
redpilot history target.com                        # Filter by target
redpilot history --limit 50                        # Show more results
```

---

### `redpilot update` — Update RedPilot

```bash
redpilot update                                    # pip install --upgrade redpilot
```

---

### `redpilot shell` — Interactive AI Shell

```bash
redpilot shell
```

**Shell commands:**
| Command | Description |
|---|---|
| `chat <query>` | Talk to the configured AI |
| `analyze <scan_id>` | Run AI analysis on a past scan |
| `exit` / `quit` | Exit the shell |

---

### `redpilot setup` — Configuration Wizard

```bash
redpilot setup
```

---

### `redpilot login` — Cloud Authentication

```bash
redpilot login
```

---

## 🗂️ Engagement Scope

Manage which targets are in-scope for your engagement. Persisted to `scope.json`.

```bash
redpilot scope show                                # View current scope table
redpilot scope add target.com                      # Add to in-scope
redpilot scope add 10.0.0.0/24                     # CIDR ranges work too
redpilot scope remove target.com                   # Remove from scope
redpilot scope show --file engagement.json         # Use a custom scope file
```

| Argument | Description |
|---|---|
| `show` | Display scope as a rich table |
| `add <value>` | Add domain/IP/CIDR to in-scope list |
| `remove <value>` | Remove from in-scope list |
| `--file <path>` | Custom scope file (default: `scope.json`) |

---

## ⚙️ Global Options

| Flag | Description |
|---|---|
| `--no-ai` | Skip automatic AI analysis after any scan |
| `--no-db` | Run in offline mode (no MongoDB required) |
| `--install-completion` | Install shell tab-completion (bash/zsh/fish/PowerShell) |
| `--show-completion` | Show the completion script for your shell |
| `--help` | Show detailed help for any command |

---

## 🌍 AI Providers — `.env` Configuration

| Provider | `AI_PROVIDER` | Required Key | Model Var | Streaming |
|---|---|---|---|---|
| Google Gemini | `google` | `GOOGLE_API_KEY` | `GOOGLE_MODEL` (default: `gemini-2.0-flash`) | ❌ |
| Anthropic Claude | `claude` | `ANTHROPIC_API_KEY` | `ANTHROPIC_MODEL` | ❌ |
| Ollama (local) | `ollama` | — | `OLLAMA_MODEL` (auto-detected) | ✅ |
| LM Studio (local) | `lmstudio` | — | `LM_STUDIO_MODEL` (auto-detected) | ✅ |

> **Name variants all work:** `lmstudio` \| `lm-studio` \| `lm_studio`

**Quick local setup:**
```bash
# Ollama
AI_PROVIDER=ollama
OLLAMA_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.2           # optional, auto-detected

# LM Studio
AI_PROVIDER=lmstudio
LM_STUDIO_URL=http://localhost:1234/v1
LM_STUDIO_MODEL=your-model      # optional, auto-detected
```

---

## 🔒 Stealth / OpsSec (`.env`)

| Variable | Description |
|---|---|
| `USE_TOR=true` | Route all requests through TOR (`socks5://127.0.0.1:9050`) |
| `PROXY_FILE=./proxies.txt` | Rotating SOCKS5/HTTP proxy chain file |
| `RANDOM_USER_AGENT=true` | Randomise browser User-Agent per request |
| `NIST_API_KEY=<key>` | NIST NVD API key (10× CVE lookup rate — free signup) |
| `SHODAN_API_KEY=<key>` | Passive Shodan recon in `redpilot recon` (free tier available) |

---

## 💡 Common Workflows

```bash
# ── Full pentest engagement ───────────────────────────────────────
redpilot scope add target.com
redpilot recon target.com
redpilot webscan https://target.com
redpilot scan target.com --intensity aggressive --scanner rustscan --ports 1-65535
redpilot crawl https://target.com --depth 3
redpilot report target.com --format html
redpilot export target.com --format csv          # Client deliverable

# ── External recon toolkit pipeline ───────────────────────────────
redpilot tools                                   # Check which recon binaries are installed
redpilot toolkit target.com                      # subfinder→httpx→katana→nuclei chain
redpilot toolkit target.com --no-nuclei          # Attack-surface mapping only (no active scan)
redpilot toolkit target.com --fuzz --wordlist /usr/share/wordlists/common.txt

# ── Offline / air-gapped (Ollama, no DB) ─────────────────────────
AI_PROVIDER=ollama redpilot scan target.com --no-db

# ── Re-analyze an old scan with a different AI ───────────────────
redpilot ai <scan_id> --provider claude

# ── Compare weekly scans to see what changed ─────────────────────
redpilot diff <last_week_scan_id> <today_scan_id>

# ── 24/7 web monitoring with AI alerts ───────────────────────────
redpilot watch target.com --module webscan --interval 3600

# ── Generate exploit + fix for a finding ─────────────────────────
redpilot history                                 # find finding ID
redpilot poc <finding_id> --output exploit.py
redpilot remediate <finding_id> --format ansible

# ── Docker quick-start ────────────────────────────────────────────
docker-compose up -d
docker-compose run redpilot recon target.com
docker-compose run redpilot shell
```
