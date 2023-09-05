import contextlib
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pickle
import uuid
from pathlib import Path

username = input("Enter username: ")
password = input("Enter password: ")

#path for working dir
cwd = Path().cwd()
name = uuid.uuid4().int.__str__()[:8]
file_name = f"{name}.pickle"
# save cookies
def save_object(obj, filename):
    with open(filename, 'wb') as f:  # Overwrites any existing file.
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def run(playwright: Playwright) -> None:
    # make a browser and context 
    iphone_12 = playwright.devices['iPhone 12']
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(**iphone_12)
    # make a browser page is like a TAB
    page = context.new_page()

    page.goto("https://www.instagram.com/")

    page.get_by_role("button", name="Log in").click()

    page.get_by_label("username").click()

    page.get_by_label("username").fill(username)

    page.get_by_label("Password").click()

    page.get_by_label("Password").fill(password)

    page.get_by_role("button", name="Log in").click()
    time.sleep(30)
    try:
        # check if user is logged in
        with contextlib.suppress(Exception):
            page.get_by_text(text="Save Info").click()
            page.get_by_text(text="Not Now").click()
        # save cookies from context not page
        save_object(context.cookies("https://www.instagram.com/"), cwd / 'files' / "accounts" / file_name)
    except Exception:
        print("Failed to log in")
    time.sleep(10)
    # close context
    context.close()

    # close browser
    browser.close()
    


with sync_playwright() as playwright:
    run(playwright)
