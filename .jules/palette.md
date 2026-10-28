## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.

## 2024-10-28 - Explicit visual disabled states
**Learning:** Pure HTML interfaces handling long-running websocket tasks lack inherent feedback for pending operations. Without explicit disabling of buttons, users might click multiple times, thinking the application is unresponsive, or trigger the action repeatedly.
**Action:** Implement explicit disabled visual styles (e.g. `opacity`, `cursor: not-allowed`) and programmatically disable action buttons during pending operations and websocket streams in vanilla JS/HTML applications.
