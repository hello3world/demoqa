import time
import allure
from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    START_STOP = '#startStopButton'
    RESET = '#resetButton'
    BAR = '#progressBar'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/progress-bar', wait_until='domcontentloaded')

    def _value(self) -> str:
        # The bar text content is like "25%"
        return (self.page.locator(self.BAR).inner_text() or '0%').strip().replace('%', '')

    @allure.step('Change progress bar value by starting and stopping')
    def change_progress_bar_value(self) -> tuple[str, str]:
        before = self._value()
        self.page.locator(self.START_STOP).click()
        # Wait some time then stop
        self.page.wait_for_timeout(1500)
        self.page.locator(self.START_STOP).click()
        after = self._value()
        return before, after

    @allure.step('Fill progress bar to 100 or reset')
    def change_full_progress_bar(self, action: str | None = None) -> tuple[str, str]:
        before = self._value()
        self.page.locator(self.START_STOP).click()
        # Wait until 100% text appears
        self.page.locator(self.BAR).get_by_text('100%').wait_for(timeout=10000)
        self.page.locator(self.START_STOP).click()
        after = self._value()
        if action == 'reset':
            self.page.locator(self.RESET).click()
            after = self._value()
        return before, after
