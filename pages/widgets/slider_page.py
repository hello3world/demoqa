import allure
from pages.base_page import BasePage


class SliderPage(BasePage):
    SLIDER = 'input[type="range"]'
    VALUE_INPUT = '#sliderValue'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/slider', wait_until='domcontentloaded')

    @allure.step('Change slider value')
    def change_slider_value(self) -> tuple[str, str]:
        before = self.page.locator(self.VALUE_INPUT).input_value()
        slider = self.page.locator(self.SLIDER)
        slider.focus()
        for _ in range(10):
            slider.press('ArrowRight')
        after = self.page.locator(self.VALUE_INPUT).input_value()
        return before, after
