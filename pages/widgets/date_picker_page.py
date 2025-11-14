import allure
from pages.base_page import BasePage


class DatePickerPage(BasePage):
    DATE_INPUT = '#datePickerMonthYearInput'
    DATE_TIME_INPUT = '#dateAndTimePickerInput'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/date-picker', wait_until='domcontentloaded')

    @allure.step('Select date')
    def select_date(self) -> tuple[str, str]:
        before = self.page.locator(self.DATE_INPUT).input_value()
        self.page.locator(self.DATE_INPUT).click()
        # pick 15th of current month
        self.page.locator('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').first.click()
        after = self.page.locator(self.DATE_INPUT).input_value()
        return before, after

    @allure.step('Select date and time')
    def select_date_and_time(self) -> tuple[str, str]:
        before = self.page.locator(self.DATE_TIME_INPUT).input_value()
        self.page.locator(self.DATE_TIME_INPUT).click()
        self.page.locator('.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').first.click()
        # select time 12:00
        self.page.get_by_text('12:00').first.click()
        after = self.page.locator(self.DATE_TIME_INPUT).input_value()
        return before, after
