# CLI Reference

Run `redpilot --help` for the authoritative list; `redpilot <command> --help` for
each command's options.

## Assessment

| Command | What it does |
|---|---|
| `redpilot agent <target>` | autonomous AI agent: plan → run → assess (`--dry-run`, `-y`, `--aggressive`, `--no-ai`, `--no-db`, `--scope-file`, `--output`) |
| `redpilot pipeline <target>` | staged discovery → validation → remediation → report (`--mock`, `--report-dir`, `--no-db`) |

## Modules

| Command | What it does |
|---|---|
| `redpilot recon <target>` | subdomains, DNS, WHOIS |
| `redpilot toolkit <target>` | external recon chain (subfinder → … → nuclei) |
| `redpilot webscan <url>` | HTTP headers, TLS, path checks |
| `redpilot scan <target>` | network + CVE mapping (nmap; `--scanner`, `--ports`) |
| `redpilot crawl <url>` | site crawler |

## Engagements & scope

| Command | What it does |
|---|---|
| `redpilot scope add\|remove\|show [value]` | manage the engagement scope (`--file`) |
| `redpilot engagements [--create NAME]` | list / create isolated engagements (`--scope`, `--authorized-by`, `--retention-days`) |

## Data & reports

| Command | What it does |
|---|---|
| `redpilot report [target]` | HTML/JSON report (`--format`, `--from-file`, `--with-ai`) |
| `redpilot diff <old_id> <new_id>` | compare two scans |
| `redpilot export <target>` | export findings (`--format csv\|json`) |
| `redpilot schema` | emit the JSON Schema of result models (`--write DIR`, `--model NAME`) |

## Services & integration

| Command | What it does |
|---|---|
| `redpilot serve` | HTTP API + dashboard (`--host`, `--port`, `--scope-file`) |
| `redpilot mcp` | MCP server (stdio) for Claude Desktop / MCP hosts |
| `redpilot mcp-tools` | list tools from configured external MCP servers |
| `redpilot plugins` | list registered scan-module plugins |

## Setup & utilities

| Command | What it does |
|---|---|
| `redpilot setup` | interactive configuration wizard |
| `redpilot test-ai` | verify the configured AI provider |
| `redpilot tools [--install]` | check / install the external recon binaries |

> A fuller command reference lives in `COMMANDS.md` in the repo.
