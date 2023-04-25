from playwright.sync_api import Playwright, sync_playwright, expect
##

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.sbishinseibank.co.jp/")
    page.get_by_role("link", name="English", exact=True).click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Login", exact=True).click()
    page1 = page1_info.value
    page1.locator("input[name=\"nationalId\"]").fill("")
    page1.locator("#loginPassword").click()
    page1.locator("#loginPassword").fill("")
    page1.get_by_role("button", name="Login").click()
    page1.get_by_role("link", name="Logout").click()
    expect(page.get_by_text("Names"), "should be logged in").to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
