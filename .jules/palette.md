## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.
## 2024-05-17 - Button Disabled States on Async Actions
**Learning:** In plain HTML/JS setups without state frameworks, dynamically changing text (e.g. to "loading...") and disabling a button can lead to a permanently stuck disabled button if an asynchronous error occurs and the reset logic isn't strictly executed.
**Action:** Always wrap the async `await` operation in a `try/finally` block when disabling buttons in vanilla JS event handlers to guarantee the button is re-enabled and its original text (ideally stored in a dataset attribute rather than hardcoded) is restored even if the operation throws an error.
