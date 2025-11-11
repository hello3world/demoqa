from pages.base_page import BasePage
from playwright.sync_api import expect


class ButtonPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        expect(self.page.get_by_role("heading", name="Buttons")).to_be_visible()

    def double_click_button(self):
        self.page.get_by_role("button", name="Double Click Me").dblclick()
        self.assert_message("#doubleClickMessage", "You have done a double click")

    def right_click_button(self):
        self.page.get_by_role("button", name="Right Click Me").click(button="right")
        self.assert_message("#rightClickMessage", "You have done a right click")

    def single_click_button(self):
        self.page.get_by_role("button", name="Click Me", exact=True).click()
        self.assert_message("#dynamicClickMessage", "You have done a dynamic click")

    def assert_message(self, selector, expected_message):
        expect(self.page.locator(selector)).to_have_text(expected_message)
