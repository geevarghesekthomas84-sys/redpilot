## 2024-05-17 - Pure HTML Dashboard Accessibility
**Learning:** Pure HTML forms often rely on visual layout rather than semantic association. Controls like inputs and selects without `<label>` elements are invisible to screen readers without `aria-label`s. In addition, pure HTML/CSS without an explicit focus indicator makes keyboard navigation difficult.
**Action:** Always verify explicit labels or `aria-label`s for inputs/selects, and add `:focus-visible` to form controls in custom CSS to ensure proper keyboard accessibility.

## 2024-10-22 - Action Buttons and Keyboard Accessibility
**Learning:** Implementing visual feedback (like 'disabled' styles and inline loading text changes) via a helper function inside native HTML interfaces prevents overlapping execution and greatly improves UX. Keyboard accessibility like mapping 'Enter' keystrokes on critical inputs enables smooth workflow navigation.
**Action:** Use a uniform wrapper around async UI handlers to handle disable/enable logic seamlessly and always add simple 'Enter' key listeners to text inputs that clearly correspond to primary actions.
