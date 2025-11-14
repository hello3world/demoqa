import random
import allure
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    MULTI_INPUT = '#autoCompleteMultipleInput'
    MULTI_VALUES = '.auto-complete__multi-value__label'
    MULTI_CLEAR_CHIP = '.auto-complete__multi-value__remove'

    SINGLE_INPUT = '#autoCompleteSingleInput'
    SINGLE_VALUE = '.auto-complete__single-value'

    COLORS = [
        'Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Violet', 'Indigo'
    ]

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/auto-complete', wait_until='domcontentloaded')

    @allure.step('Fill multi auto-complete with random 2 colors')
    def fill_input_multi(self) -> list[str]:
        choices = random.sample(self.COLORS, k=2)
        input_el = self.page.locator(self.MULTI_INPUT)
        for color in choices:
            input_el.fill(color)
            self.page.keyboard.press('Enter')
        return choices

    def check_color_in_multi(self) -> list[str]:
        chips = self.page.locator(self.MULTI_VALUES)
        return [chips.nth(i).inner_text() for i in range(chips.count())]

    @allure.step('Remove one value from multi')
    def remove_value_from_multi(self) -> tuple[int, int]:
        chips = self.page.locator(self.MULTI_VALUES)
        before = chips.count()
        if before > 0:
            self.page.locator(self.MULTI_CLEAR_CHIP).first.click()
        after = chips.count()
        return before, after

    @allure.step('Remove all values from multi via cross')
    def remove_all_values_from_multi(self) -> int:
        removes = self.page.locator(self.MULTI_CLEAR_CHIP)
        for i in range(removes.count()):
            removes.first.click()
        return self.page.locator(self.MULTI_VALUES).count()

    @allure.step('Fill single auto-complete with one color')
    def fill_input_single(self) -> str:
        color = random.choice(self.COLORS)
        self.page.locator(self.SINGLE_INPUT).fill(color)
        self.page.keyboard.press('Enter')
        return color

    def check_color_in_single(self) -> str:
        val = self.page.locator(self.SINGLE_VALUE)
        return val.inner_text()
