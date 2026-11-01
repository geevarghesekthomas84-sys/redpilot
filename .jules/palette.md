## 2024-11-01 - Explicit disabled state on vanilla JS actions
**Learning:** Vanilla JS apps lack built-in disabled/loading state bindings found in modern frameworks. Unprotected async actions (fetch requests, websocket streams) allowed duplicate submissions.
**Action:** Always explicitly disable action buttons programmatically (`btn.disabled = true`), update their text (e.g., "running..."), and include corresponding CSS (`:disabled` state styles) during long-running operations. Restore state in `finally` or `onclose`/`onerror` handlers.
## 2024-11-01 - Explicit disabled state on vanilla JS actions
**Learning:** Vanilla JS apps lack built-in disabled/loading state bindings found in modern frameworks. Unprotected async actions (fetch requests, websocket streams) allowed duplicate submissions.
**Action:** Always explicitly disable action buttons programmatically (`btn.disabled = true`), update their text (e.g., "running..."), and include corresponding CSS (`:disabled` state styles) during long-running operations. Restore state in `finally` or `onclose`/`onerror` handlers.
## 2026-11-01 - Cloudflare CI fixes for wrangler.toml
**Learning:** `compatibility_date` in `wrangler.toml` expects a real-world date. The CI might fail if this is set in the past relative to Cloudflare but not valid with local sandbox testing using mock future dates. The instructions specify to use a valid past/present date relative to real-world time to avoid CI deployment failure.
**Action:** Always verify `compatibility_date` on `wrangler.toml` is set correctly for deployments using `npx wrangler` if changes cause CI deployment test failures.
