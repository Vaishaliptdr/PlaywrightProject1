###
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.pause()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Adding wait condition
    page.wait_for_load_state("networkidle")

    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.wait_for_load_state("networkidle")

#Adding assertions
    expect(page.get_by_text("My Actions")).to_be_visible()
    print('Profile displayed')


    print('Success')
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
