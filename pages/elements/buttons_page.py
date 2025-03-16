from pages.base_page import BasePage

class ButtonPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        self.page.wait_for_selector("h1:has-text('Buttons')")

    def double_click_button(self):
        self.page.get_by_role("button", name="Double Click Me").dblclick()
        self._assert_message("#doubleClickMessage", "You have done a double click")

    def right_click_button(self):
        self.page.get_by_role("button", name="Right Click Me").click(button="right")
        self._assert_message("#rightClickMessage", "You have done a right click")

    def single_click_button(self):
        self.page.locator('//button[text()="Click Me"]').click()
        self._assert_message("#dynamicClickMessage", "You have done a dynamic click")

    def _assert_message(self, selector, expected_message):
        assert self.page.text_content(selector) == expected_message

