from pages.base_page import BasePage

class TextBoxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def fill_full_name_input(self, name):
        full_name_input = self.page.get_by_placeholder("Full Name")
        full_name_input.fill(name)

    def fill_email_input(self, email):
        email_input = self.page.get_by_placeholder("name@example.com")
        email_input.fill(email)

    def fill_current_address_input(self, current_address):
        current_address_input = self.page.get_by_placeholder("Current Address")
        current_address_input.fill(current_address)

    def fill_permanent_address_input(self, permanent_address):
        permanent_address_input = self.page.locator("#permanentAddress")
        permanent_address_input.fill(permanent_address)
        
    def click_submit_button(self):
        submit_button = self.page.get_by_role("button", name="Submit")
        submit_button.click()

    def fill_form(self, name, email, current_address, permanent_address):
        self.fill_full_name_input(name)
        self.fill_email_input(email)
        self.fill_current_address_input(current_address)
        self.fill_permanent_address_input(permanent_address)
        self.click_submit_button()
