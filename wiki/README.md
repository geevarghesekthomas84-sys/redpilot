# RedPilot wiki (source)

These Markdown files are the source for the project's GitHub wiki. The GitHub
wiki is a **separate git repository**, so these pages must be copied into it —
GitHub does not read them from the main repo automatically.

## Option A — web UI (quickest for the first page)

1. On GitHub: repo → **Wiki** → **Create the first page**.
2. Paste the contents of `Home.md`, save.
3. For each other page, **New Page**, name it exactly as the filename (without
   `.md`, keep the hyphens — e.g. `HTTP-API`, `Engagements-and-RBAC`), paste, save.
4. `_Sidebar.md` controls the sidebar nav.

## Option B — git (bulk, recommended once the wiki exists)

```bash
# after creating the first page once in the UI, the wiki repo exists:
git clone https://github.com/geevarghesekthomas84-sys/redpilot.wiki.git
cp wiki/*.md redpilot.wiki/
cd redpilot.wiki && git add -A && git commit -m "Populate wiki" && git push
```

Page names map from filenames: `Home.md` is the landing page; `_Sidebar.md` is the
sidebar; multi-word pages use hyphens and render with spaces.
