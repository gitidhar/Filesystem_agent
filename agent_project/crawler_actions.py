from playwright.sync_api import Playwright, Browser, sync_playwright, expect
from crawler import activate_crawler, shutdown

def run(browser: Browser) -> None:
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://soundcloud.com/")
    page.locator("#content").get_by_role("searchbox", name="Search").click()
    page.locator("#content").get_by_role("searchbox", name="Search").fill("unreleased travis scott snippets")
    page.locator("#content").get_by_role("searchbox", name="Search").press("Enter")
    # page.get_by_role("button", name="Pause", exact=True).click()


