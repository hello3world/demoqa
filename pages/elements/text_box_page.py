from pages.base_page import BasePage
from playwright.sync_api import expect

class TextBoxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        expect(self.page.locator("h1:has-text('Text Box')")).to_be_visible(timeout=10000)

    def fill_full_name_input(self, name):
        self.page.get_by_placeholder("Full Name").fill(name)

    def fill_email_input(self, email):
        self.page.get_by_placeholder("name@example.com").fill(email)

    def fill_current_address_input(self, current_address):
        self.page.get_by_placeholder("Current Address").fill(current_address)

    def fill_permanent_address_input(self, permanent_address):
        self.page.locator("#permanentAddress").fill(permanent_address)
        
    def click_submit_button(self):
        self.page.get_by_role("button", name="Submit").click()

    def fill_form(self, name, email, current_address, permanent_address):
        self.fill_full_name_input(name)
        self.fill_email_input(email)
        self.fill_current_address_input(current_address)
        self.fill_permanent_address_input(permanent_address)
        self.click_submit_button()
