from playwright.sync_api import Playwright, sync_playwright, expect

def illeagl(page):
    page.get_by_role("button", name="Sale of illegal or regulated goods chevron").click()
    page.get_by_text("Firearms").click()
    page.get_by_role("button", name="Submit Report").click()
    page.get_by_role("button", name="Close").click()

def scam(page):
    page.get_by_role("button", name="Scam or fraud chevron").click()
    page.get_by_role("button", name="Close").click()

def pretend_me(page):
    page.get_by_text("Someone I know").click()
    page.get_by_role("button", name="Submit Report").click()
    page.get_by_role("button", name="Close").click()

def pretend_someone(page):
    page.get_by_role("group").get_by_text("Me").first.click()
    page.get_by_role("button", name="Submit Report").click()
    page.get_by_role("button", name="Close").click()
