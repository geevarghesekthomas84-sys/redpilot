## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.
## 2024-05-18 - Async Action Button States
**Learning:** In plain HTML/JS interfaces without robust state management, users frequently double-submit forms or trigger multiple parallel API requests if buttons remain enabled during long-running asynchronous operations (like network scans or websocket streams).
**Action:** Always explicitly disable action buttons programmatically via JS (`element.disabled = true`) and visually via CSS (`opacity`, `cursor: not-allowed`) during asynchronous operations, ensuring they are re-enabled in all resolution paths (success `finally` blocks, `catch` blocks, and websocket `onmessage`/`onerror` handlers).
