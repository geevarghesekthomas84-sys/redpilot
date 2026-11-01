## 2024-11-01 - Explicit disabled state on vanilla JS actions
**Learning:** Vanilla JS apps lack built-in disabled/loading state bindings found in modern frameworks. Unprotected async actions (fetch requests, websocket streams) allowed duplicate submissions.
**Action:** Always explicitly disable action buttons programmatically (`btn.disabled = true`), update their text (e.g., "running..."), and include corresponding CSS (`:disabled` state styles) during long-running operations. Restore state in `finally` or `onclose`/`onerror` handlers.
## 2024-11-01 - Explicit disabled state on vanilla JS actions
**Learning:** Vanilla JS apps lack built-in disabled/loading state bindings found in modern frameworks. Unprotected async actions (fetch requests, websocket streams) allowed duplicate submissions.
**Action:** Always explicitly disable action buttons programmatically (`btn.disabled = true`), update their text (e.g., "running..."), and include corresponding CSS (`:disabled` state styles) during long-running operations. Restore state in `finally` or `onclose`/`onerror` handlers.
