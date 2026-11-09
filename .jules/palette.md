## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.

## 2024-05-18 - Vanilla JS Async Button States
**Learning:** In plain HTML/JS interfaces without reactive frameworks, long-running async operations can lead to duplicate submissions if action buttons aren't explicitly disabled.
**Action:** Always manually set `btn.disabled = true` and update loading text for async actions, and crucially wrap the `await` in a `try/finally` block to guarantee the button is re-enabled even if the operation throws an error.
