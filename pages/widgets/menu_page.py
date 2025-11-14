import allure
from pages.base_page import BasePage


class MenuPage(BasePage):
    MENU = '#nav'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/menu', wait_until='domcontentloaded')

    @allure.step('Check all menu items')
    def check_menu(self) -> list[str]:
        items = self.page.locator(f"{self.MENU} li a")
        result: list[str] = []
        for i in range(items.count()):
            txt = items.nth(i).inner_text().strip()
            if txt:
                result.append(txt)
        return result
