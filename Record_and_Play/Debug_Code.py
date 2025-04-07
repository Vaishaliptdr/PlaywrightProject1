# *******How to run the program in debug mode
# Copy recorded program in pycharm>> add pause at any place>>run the code
# Debugger will get open with our code>>Click on step over button to navigate through the code

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

#Add this statement
    page.pause()
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
