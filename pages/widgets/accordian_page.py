import allure
from pages.base_page import BasePage


class AccordianPage(BasePage):
    SECTION_MAP = {
        'first': {'btn': '#section1Heading', 'panel': '#section1Content'},
        'second': {'btn': '#section2Heading', 'panel': '#section2Content'},
        'third': {'btn': '#section3Heading', 'panel': '#section3Content'},
    }

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/accordian', wait_until='domcontentloaded')

    @allure.step('Check accordian widget')
    def check_accordian(self, section: str) -> tuple[str, int]:
        data = self.SECTION_MAP[section]
        btn = self.page.locator(data['btn'])
        btn.click()
        panel = self.page.locator(data['panel'])
        text = panel.inner_text()
        return btn.inner_text(), len(text.strip())
