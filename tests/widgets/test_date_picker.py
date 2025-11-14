import allure
from pages.widgets.date_picker_page import DatePickerPage

pytestmark = allure.suite('Widgets')

@allure.feature('Date Picker Page')
class TestDatePickerPage:
    @allure.title('Check change date')
    def test_change_date(self, page):
        date_picker_page = DatePickerPage(page)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after

    @allure.title('Check change date and time')
    def test_change_date_and_time(self, page):
        date_picker_page = DatePickerPage(page)
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_before != value_date_after
