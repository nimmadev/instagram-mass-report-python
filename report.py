from playwright.sync_api import Playwright, sync_playwright, expect
import time
import pickle
from pathlib import Path
from files.helper import illeagl, scam, pretend_me, pretend_someone
#types of reports and choosing one
reports = {"illeagl": illeagl, "scam": scam, "pretend_me": pretend_me, "pretend_someone": pretend_someone}
report_username = input("Enter a report username : ")
for x in reports:
    print(x)
report_type = input("enter one of the report types : ").lower().strip()
report_function = reports[report_type]

#function to automate the report
def run(playwright: Playwright, session) -> None:
    # making pake user_agent and launching context
    iphone_12 = playwright.devices['iPhone 12']
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(**iphone_12)
    # make new page and load session
    page = context.new_page()

    page.goto("https://www.instagram.com/")
    context.add_cookies(cookies=session)
    time.sleep(2)
    page.goto("https://www.instagram.com/")
    # just for safety
    try:
        page.get_by_role("button", name="Turn On").click()
    except Exception:
        pass
    page.goto("https://www.instagram.com/%s/" % report_username)
    page.wait_for_url(f"https://www.instagram.com/{report_username}/")

    page.get_by_role("button", name="Options").click()

    page.get_by_role("button", name="Report").click()

    page.get_by_role("button", name="Report account chevron").click()
    # using one of two report types
    if report_type == "illeagl" or "scam":
        page.get_by_role("button", name="It's posting content that shouldn't be on Instagram chevron").click()
        report_function(page)
    else:
        page.get_by_role("button", name="It's pretending to be someone else chevron").click()
        report_function(page)
    # ---------------------
    # closeing and exiting the brower
    context.close()
    browser.close()

#start the script
with sync_playwright() as playwright:
    file_path = Path().cwd() / 'files' / "accounts"
    all_sessions =  [str(x) for x in file_path.iterdir()]
    for session_ in all_sessions:
        session = pickle.load(session_)
        run(playwright, session)
    # session = pickle.load(open("cookies.pickle", "rb"))
    # run(playwright, session)
