import random
import allure
from pages.base_page import BasePage


class SelectMenuPage(BasePage):
    # React Selects
    SELECT_VALUE = '#withOptGroup'
    SELECT_ONE = '#selectOne'
    REACT_OPTION = 'div[role="option"]'

    # Old style select
    OLD_SELECT = '#oldSelectMenu'

    # React multiselect
    MULTI_INPUT = '#react-select-4-input'
    MULTI_VALUE = '.css-12jo7m5, .auto-complete__multi-value__label, .css-1rhbuit-multiValue'
    MULTI_CLEAR = '.css-xb97g8 .css-1hwfws3, .css-12jo7m5 ~ .css-xb97g8'

    # Standard multi select
    STANDARD_MULTI = '#cars'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/select-menu', wait_until='domcontentloaded')

    @allure.step('Check dropdown by key')
    def check_dropdown(self, key: str) -> tuple[str, str]:
        if key == 'select_value':
            container = self.page.locator(self.SELECT_VALUE)
            container.click()
            option_text = 'Group 1, option 1'
            self.page.get_by_role('option', name=option_text, exact=True).click()
            actual = container.locator('.css-1uccc91-singleValue, .css-1wa3eu0-placeholder').inner_text()
            return option_text, actual
        elif key == 'select_one':
            container = self.page.locator(self.SELECT_ONE)
            container.click()
            option_text = 'Mr.'
            self.page.get_by_role('option', name=option_text, exact=True).click()
            actual = container.locator('.css-1uccc91-singleValue, .css-1wa3eu0-placeholder').inner_text()
            return option_text, actual
        else:
            raise ValueError('Unsupported dropdown key')

    @allure.step('Check old style select dropdown')
    def check_old_select(self) -> tuple[str, str]:
        select = self.page.locator(self.OLD_SELECT)
        # choose a fixed visible label for determinism
        label = 'Purple'
        select.select_option(label=label)
        # read selected option text
        actual = select.input_value()
        # input_value returns the value attribute; map Purple->4 in demo site; we can read selected option text instead
        selected_text = select.locator('option:checked').inner_text()
        return label, selected_text

    @allure.step('Fill react multiselect with two colors')
    def fill_multi_dropdown(self) -> list[str]:
        choices = ['Green', 'Blue']
        for c in choices:
            self.page.locator(self.MULTI_INPUT).fill(c)
            self.page.keyboard.press('Enter')
        return choices

    def check_color_in_multi_dropdown(self) -> list[str]:
        chips = self.page.locator(self.MULTI_VALUE)
        return [chips.nth(i).inner_text() for i in range(chips.count())]

    @allure.step('Remove one value from multiselect')
    def remove_value_from_multi_dropdown(self) -> tuple[int, int]:
        chips = self.page.locator(self.MULTI_VALUE)
        before = chips.count()
        if before:
            # Remove last chip by pressing Backspace in input
            self.page.locator(self.MULTI_INPUT).press('Backspace')
        after = chips.count()
        return before, after

    @allure.step('Remove all values from multiselect')
    def remove_all_values_from_multi_dropdown(self) -> int:
        # Clear by focusing input and pressing Ctrl+A then Backspace
        inp = self.page.locator(self.MULTI_INPUT)
        inp.focus()
        self.page.keyboard.press('Control+A')
        self.page.keyboard.press('Backspace')
        return self.page.locator(self.MULTI_VALUE).count()

    @allure.step('Select some options in standard multi select')
    def select_standart_multi(self) -> list[str]:
        select = self.page.locator(self.STANDARD_MULTI)
        values = ['volvo', 'saab']
        select.select_option(value=values)
        return [select.locator('option[value="volvo"]').inner_text(), select.locator('option[value="saab"]').inner_text()]

    def select_all_standart_multi(self) -> None:
        select = self.page.locator(self.STANDARD_MULTI)
        all_values = [opt.get_attribute('value') for opt in select.locator('option').all() if opt.get_attribute('value')]
        select.select_option(value=all_values)

    def check_standart_multi(self) -> list[str] | int:
        select = self.page.locator(self.STANDARD_MULTI)
        selected = select.locator('option:checked')
        # return count for "select all" assertion
        count = selected.count()
        if count == 4:
            return 4
        return [selected.nth(i).inner_text() for i in range(count)]
