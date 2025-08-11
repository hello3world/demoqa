from playwright.sync_api import expect
import time
from config import SCREENSHOT_DIR, BROWSER_TIMEOUT, SCREENSHOT_TIMEOUT
from logger_config import logger

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        """Opens the specified URL"""
        logger.info(f"Opening URL: {url}")
        self.page.goto(url)

    def page_verify(self, locator):
        """Verifies element visibility on the page"""
        logger.debug(f"Checking element visibility: {locator}")
        expect(self.page.locator(locator)).to_be_visible(timeout=BROWSER_TIMEOUT)

    def take_screenshot_on_error(self, error_message: str):
        """Takes a screenshot on error"""
        screenshot_path = f"{SCREENSHOT_DIR}/error_{int(time.time())}.png"
        self.page.screenshot(
            path=screenshot_path,
            timeout=SCREENSHOT_TIMEOUT,
            animations="disabled"
        )
        logger.error(f"{error_message}. Screenshot saved at {screenshot_path}")

    def wait_for_element(self, locator, timeout=None):
        """Waits for element to appear"""
        timeout = timeout or BROWSER_TIMEOUT
        logger.debug(f"Waiting for element: {locator}, timeout: {timeout}")
        return self.page.locator(locator).wait_for(timeout=timeout)

    def click_element(self, locator):
        """Clicks on element with waiting"""
        logger.debug(f"Clicking on element: {locator}")
        element = self.wait_for_element(locator)
        element.click()

    def fill_input(self, locator, text):
        """Fills input field"""
        logger.debug(f"Filling field {locator} with text: {text}")
        element = self.wait_for_element(locator)
        element.fill(text)