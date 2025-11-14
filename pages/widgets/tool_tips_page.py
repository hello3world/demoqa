import allure
from playwright.sync_api import expect
from pages.base_page import BasePage


class ToolTipsPage(BasePage):
    MAP = {
        'button': {'trigger': '#toolTipButton', 'tip': '#buttonToolTip'},
        'field': {'trigger': '#toolTipTextField', 'tip': '#textFieldToolTip'},
        'contrary': {'trigger': "//a[text()='Contrary']", 'tip': '#contraryTexToolTip'},
        'section': {'trigger': "//a[text()='1.10.32']", 'tip': '#sectionToolTip'},
    }

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/tool-tips', wait_until='domcontentloaded')

    @allure.step('Check tool tips')
    def check_tool_tips(self, key: str) -> str:
        data = self.MAP[key]
        trigger = self.page.locator(data['trigger'])
        trigger.hover()
        tip = self.page.locator(data['tip']).locator('.tooltip-inner')
        expect(tip).to_be_visible()
        return tip.inner_text()
