from playwright.sync_api import Playwright, sync_playwright, expect

def illegal(page):
    page.locator("button").filter(has_text="Sale of illegal or regulated goodschevron").click()
    page.get_by_text("Firearms").click()
    page.get_by_role("button", name="Submit Report").click()
    page.get_by_role("button", name="Close").click()

def scam(page):
    page.locator("button").filter(has_text="Scam or fraudchevron").click()
    page.get_by_role("button", name="Close").click()

def pretend_me(page):
    page.get_by_text("Someone I follow").click()
    page.get_by_role("button", name="Submit Report").click()
    page.get_by_role("button", name="Close").click()

def pretend_someone(page):
    page.get_by_text("Me", exact=True).click()
    page.get_by_role("button", name="Submit Report").click()
    page.get_by_role("button", name="Close").click()
