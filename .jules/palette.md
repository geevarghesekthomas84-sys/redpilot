## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.

## 2024-10-26 - Async WebSocket Double-Submission Prevention
**Learning:** In dashboards connecting to async endpoints (like WebSockets for job streaming), users tend to double-click submission buttons if visual feedback is not immediate or distinct enough, leading to duplicate jobs or confusing UI states.
**Action:** Always immediately disable submission buttons upon click, provide intermediary text states (e.g. "starting...", "running..."), and use CSS to distinguish the disabled state before the asynchronous operation fully connects or completes.
