import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    NEW_TAB_BUTTON = '#tabButton'
    NEW_WINDOW_BUTTON = '#windowButton'
    TITLE_NEW = '#sampleHeading'

    def __init__(self, page) -> None:
        super().__init__(page)

    @allure.step('Check opened new tab or window')
    def check_opened_interface(self, interface: str) -> str:
        btn_selector = self.NEW_TAB_BUTTON if interface == 'tab' else self.NEW_WINDOW_BUTTON
        with self.page.expect_popup() as popup_info:
            self.page.locator(btn_selector).click()
        new_page = popup_info.value
        expect(new_page.locator(self.TITLE_NEW)).to_be_visible()
        text_title = new_page.locator(self.TITLE_NEW).inner_text()
        new_page.close()
        return text_title
 
