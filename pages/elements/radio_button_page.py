from pages.base_page import BasePage
from playwright.sync_api import expect

class RadioButtonPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    # actions
    def page_verify(self):
        expect(self.page.locator("h1").filter(has_text="Radio Button")).to_be_visible()

    def select_yes(self):
        self.page.locator("label[for='yesRadio']").click()

    def select_impressive(self):
        self.page.locator("label[for='impressiveRadio']").click()

    def no_option_is_disabled(self):
        expect(self.page.locator("label[for='noRadio']")).to_be_disabled()

