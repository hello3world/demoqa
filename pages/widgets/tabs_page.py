import allure
from pages.base_page import BasePage


class TabsPage(BasePage):
    TAB_BUTTONS = {
        'what': '#demo-tab-what',
        'origin': '#demo-tab-origin',
        'use': '#demo-tab-use',
        'more': '#demo-tab-more',
    }
    TAB_PANES = {
        'what': '#demo-tabpane-what',
        'origin': '#demo-tabpane-origin',
        'use': '#demo-tabpane-use',
        'more': '#demo-tabpane-more',
    }

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/tabs', wait_until='domcontentloaded')

    @allure.step('Switch tabs and return content length')
    def check_tabs(self, tab_name: str) -> tuple[str, int]:
        btn_sel = self.TAB_BUTTONS[tab_name]
        pane_sel = self.TAB_PANES[tab_name]
        btn = self.page.locator(btn_sel)
        btn.click()
        content = self.page.locator(pane_sel).inner_text()
        return btn.inner_text().strip(), len(content.strip())
