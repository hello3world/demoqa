from pages.base_page import BasePage
from playwright.sync_api import expect

class DynamicPropertiesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        expect(self.page.locator("h1:has-text('Dynamic Properties')")).to_be_visible(timeout=10000)

    def wait_for_button_to_enable(self):
        self.page.wait_for_selector("#enableAfter:enabled", timeout=6000)
        return self.page.locator("#enableAfter").is_enabled()

    def wait_for_text_change(self):
        button = self.page.locator("#colorChange")
        initial_text = button.inner_text()
        self.page.wait_for_timeout(6000)
        new_text = button.inner_text()
        return initial_text, new_text

    def wait_for_color_change(self):
        button = self.page.locator("#colorChange")
        initial_color = button.evaluate("el => getComputedStyle(el).color")
        self.page.wait_for_timeout(6000)
        new_color = button.evaluate("el => getComputedStyle(el).color")
        return initial_color, new_color
