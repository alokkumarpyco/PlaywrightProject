from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("-----")
    page.get_by_test_id("royal_pass").click()
    page.get_by_test_id("royal_pass").fill("-----")
    page.get_by_test_id("royal_login_button").click()
    page.get_by_role("button", name="Messenger").click()
    page.get_by_role("link", name="Shashank Shekhar").click()
    page.get_by_role("paragraph").click()
    page.get_by_role("textbox", name="Message").fill("munna ji")
    page.get_by_role("button", name="Press enter to send").click()
    page.get_by_role("button", name="Your profile").click()
    page.get_by_role("button", name="Log Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
