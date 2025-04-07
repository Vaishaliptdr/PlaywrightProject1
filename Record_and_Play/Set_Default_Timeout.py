#Setting default timeout for entire page
#Expect function does not accept default timeout: its timeout is set to 5 seconds
#But we can set customized timeout for expect function as,
#    expect(page.get_by_text("My Actions")).to_be_visible(timeout=8000)


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:

#Adding "slo_mo" for 500 milliseconds to run code in slow manner
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    context = browser.new_context()
    page = context.new_page()
    # page.pause()

#Setting default timeouts for entire page
    page.set_default_timeout(5000)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Adding wait condition
    page.wait_for_load_state("networkidle")

#Adding Timeouts
    page.get_by_role("textbox", name="Username").click()

    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()

#Adding Timeouts
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
