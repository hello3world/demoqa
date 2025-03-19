from playwright.sync_api import expect
import time
import logging

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def page_verify(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=10000)

    def take_screenshot_on_error(self, error_message: str):
        screenshot_path = f"assets/screenshots/error_{int(time.time())}.png"
        self.page.screenshot(path=screenshot_path)
        logging.error(f"{error_message}. Screenshot saved at {screenshot_path}")