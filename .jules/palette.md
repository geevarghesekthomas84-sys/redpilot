## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.

## 2024-11-08 - Safe Async Button States in Vanilla JS
**Learning:** When using plain JavaScript to handle async form submissions, failing to explicitly disable buttons and handle re-enabling within a `try/finally` block leads to duplicate submissions and broken UI states when errors occur.
**Action:** Always programmatically disable buttons during await calls and strictly wrap the operation in a try/finally block to guarantee restoration of the original state and text.
