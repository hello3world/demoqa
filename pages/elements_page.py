from playwright.sync_api import expect
from pages.base_page import BasePage

class ElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_verify(self):
        expect(self.page.get_by_text("Please select an item from left to start practice.")).to_be_visible(timeout=10)

    def click_text_box(self):
        text_box = self.page.get_by_text("Text Box")
        text_box.click()
