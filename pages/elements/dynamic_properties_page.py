from pages.base_page import BasePage
from playwright.sync_api import expect


class DynamicPropertiesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        expect(
            self.page.get_by_role("heading", name="Dynamic Properties")
        ).to_be_visible(timeout=10000)

    def wait_for_button_to_enable(self) -> bool:
        button = self.page.locator("#enableAfter")
        expect(button).to_be_enabled(timeout=7000)
        return True

    def wait_for_color_change(self) -> tuple[str, str]:
        button = self.page.locator("#colorChange")
        old_class = button.get_attribute("class") or ""
        expect(button).to_have_class("text-danger", timeout=7000)
        new_class = button.get_attribute("class") or ""
        return old_class, new_class


    def wait_for_button_to_appear(self) -> bool:
        appear_btn = self.page.locator("#visibleAfter")
        expect(appear_btn).to_be_visible(timeout=7000)
        return True
