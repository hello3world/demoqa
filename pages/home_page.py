from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_verify(self):
        expect(self.page.get_by_alt_text("Selenium Online Training")).to_be_visible(timeout=10)
    
    def click_elements_button(self):
        elements_button = self.page.get_by_text("Elements")
        elements_button.click()