# RedPilot Demo

A short tour of the RedPilot CLI. The commands below are safe to run offline
(`--no-db --no-ai`) against `example.com`.

## Quick tour

```bash
redpilot tools                      # what's installed
redpilot tools --install            # install the Go recon suite (needs Go)
redpilot scope add example.com      # define engagement scope
redpilot toolkit example.com        # subfinder → httpx → katana → nuclei
redpilot recon example.com --passive
redpilot report example.com --format html --with-ai   # shareable HTML report
```

## Recording the GIF for the README

The README references `docs/demo.gif`. To (re)generate it:

```bash
pip install asciinema
# install agg (asciinema -> gif): https://github.com/asciinema/agg

asciinema rec docs/demo.cast -c "bash scripts/demo.sh"
agg docs/demo.cast docs/demo.gif
```

Then commit `docs/demo.gif`. Keep it short (~15–20s) and run it after
`redpilot tools --install` so the toolkit stages show real output.
