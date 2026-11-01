import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.sheyda.com/")
    page.get_by_label("مرد عنکبوتی: روزگاری نو").click()
    page.get_by_role("link", name="تام هالند تام هالند بازیگر").click()

    # ---------------------
    # context.close()
    # browser.close()
    page.pause()


with sync_playwright() as playwright:
    run(playwright)
