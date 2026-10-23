from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Don't try to mock fetch this deeply for local file URLs, just trigger the DOM changes directly for testing visual states
    page.goto("file:///app/redpilot/api/static/dashboard.html")
    page.wait_for_timeout(500)

    # Note the button has id "save" but text is "connect"
    page.locator("#key").fill("invalid_key_for_test")
    # Take screenshot right after clicking to catch the disabled/loading state
    # We will trigger the states via JS since fetch errors out immediately for file://
    page.evaluate("""
        const btn = document.querySelector('#save');
        btn.disabled = true;
        btn.textContent = 'connecting...';

        const btn2 = document.querySelector('#addScope');
        btn2.disabled = true;
        btn2.textContent = 'adding...';

        const btn3 = document.querySelector('#go');
        btn3.disabled = true;
        btn3.textContent = 'starting...';
    """)

    page.wait_for_timeout(200) # Give it time for JS to execute and DOM to update
    page.screenshot(path="/tmp/verification_disabled.png")
    page.wait_for_timeout(500)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/tmp/videos2"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
