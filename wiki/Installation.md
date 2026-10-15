# Installation

RedPilot needs **Python 3.11+**. Install from PyPI:

```bash
pip install redpilot             # CLI + core
pip install "redpilot[ai]"       # + AI providers (Gemini / Claude / OpenAI-compatible)
pip install "redpilot[api]"      # + HTTP API, dashboard, metrics
pip install "redpilot[mcp]"      # + MCP server / client
pip install "redpilot[intel]"    # + Shodan passive intel
pip install "redpilot[dev]"      # + test/dev tooling
```

Extras combine: `pip install "redpilot[ai,api,mcp]"`.

## First run

```bash
cp .env.example .env             # configure providers / database / stealth
redpilot --install-completion    # shell tab-completion (optional)
redpilot tools --install         # install the external recon toolkit (needs Go)
redpilot setup                   # interactive configuration wizard
```

## Requirements

- **Python 3.11+**
- **[Nmap](https://nmap.org)** — network scanning
- **MongoDB** (optional) — or the zero-setup local SQLite backend
- **Optional:** [RustScan](https://github.com/RustScan/RustScan) for fast port discovery

## External recon toolkit

RedPilot's `toolkit` module orchestrates these Go binaries — check/install with
`redpilot tools` / `redpilot tools --install`:

`subfinder` · `httpx` · `nuclei` · `katana` · `dnsx` · `assetfinder` ·
`waybackurls` · `gau` · `ffuf` · `hakrawler`

## Docker / Podman

No local Python needed — see **[[Deployment]]** for the dev stack and the
hardened API container.

## From source

```bash
git clone https://github.com/geevarghesekthomas84-sys/redpilot
cd redpilot
pip install -e ".[dev,api,mcp]"
pytest -q
```
