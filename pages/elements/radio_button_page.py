from ..base_page import BasePage

class RadioButtonPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        self.page.wait_for_selector("h1:has-text('Radio Button')")

    def select_yes(self):
        self.page.locator("#yesRadio").check()
        self._assert_message("Yes")

    def select_impressive(self):
        self.page.locator("#impressiveRadio").check()
        self._assert_message("Impressive")

    def select_no(self):
        self.page.locator("#noRadio").check()


    def _assert_message(self, expected_message):
        assert self.page.locator(".text-success").text_content() == expected_message
