#!/usr/bin/env bash
#
# RedPilot demo walkthrough — records a short, deterministic tour of the CLI.
#
# Produce a GIF for the README:
#   1. Install recorder + renderer:
#        pip install asciinema
#        # and one of: https://github.com/asciinema/agg  (asciinema -> gif)
#   2. Record:   asciinema rec docs/demo.cast -c "bash scripts/demo.sh"
#   3. Render:   agg docs/demo.cast docs/demo.gif
#   4. Commit docs/demo.gif — the README already references it.
#
# The demo runs offline (--no-db --no-ai) and against example.com so it is safe
# and reproducible. Install the recon suite first (`redpilot tools --install`) to see
# real toolkit output.

set -e

TARGET="${1:-example.com}"
PAUSE="${PAUSE:-1.4}"

run() {
  echo
  echo "\$ $*"
  sleep "$PAUSE"
  "$@" || true
  sleep "$PAUSE"
}

clear
echo "=== RedPilot — AI-orchestrated offensive security automation ==="
sleep "$PAUSE"

run redpilot --help
run redpilot tools
run redpilot scope add "$TARGET"
run redpilot toolkit "$TARGET" --no-db --no-ai --no-crawl --no-urls
run redpilot recon "$TARGET" --passive --no-db --no-ai

echo
echo "=== Generate a shareable HTML report (add --with-ai for AI analysis) ==="
sleep "$PAUSE"
run redpilot report "$TARGET" --from-file /dev/stdin --format html --output-dir ./reports <<'JSON' || true
[{"target":"example.com","vuln_type":"missing_hsts","detail":"No HSTS header","severity":"High","severity_order":2,"recommendation":"Add Strict-Transport-Security","scan_type":"webscan","discovered_at":"2026-01-01"}]
JSON

echo
echo "Done. See ./reports for the generated report."
