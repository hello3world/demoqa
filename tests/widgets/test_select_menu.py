import allure
from pages.widgets.select_menu_page import SelectMenuPage

pytestmark = allure.suite('Widgets')

@allure.feature('Select Menu Page')
class TestSelectMenuPage:
    @allure.title('Check "Select Value" dropdown')
    def test_check_select_value_dropdown(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        option_value, actual_value = select_menu_page.check_dropdown('select_value')
        assert option_value == actual_value

    @allure.title('Check "Select One" dropdown')
    def test_check_select_one_dropdown(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        option_value, actual_value = select_menu_page.check_dropdown('select_one')
        assert option_value == actual_value

    @allure.title('Check "Old Style Select Menu" dropdown')
    def test_check_old_style_select_dropdown(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        input_value, result_value = select_menu_page.check_old_select()
        assert input_value == result_value

    @allure.title('Check the "Multiselect drop down" is filled')
    def test_fill_multi_dropdown(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        colors = select_menu_page.fill_multi_dropdown()
        colors_result = select_menu_page.check_color_in_multi_dropdown()
        assert colors == colors_result

    @allure.title('Check deletions from the "Multiselect drop down"')
    def test_remove_value_from_multi_dropdown(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        select_menu_page.fill_multi_dropdown()
        count_value_before, count_value_after = select_menu_page.remove_value_from_multi_dropdown()
        assert count_value_before != count_value_after

    @allure.title('Check deletions from the "Multiselect drop down" by cross')
    def test_remove_all_values_from_multi_dropdown_by_cross(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        select_menu_page.fill_multi_dropdown()
        count_value = select_menu_page.remove_all_values_from_multi_dropdown()
        assert count_value == 0

    @allure.title('Check some parameters "Standart multi select" are selected')
    def test_select_values_in_standart_multi(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        cars = select_menu_page.select_standart_multi()
        selected_cars = select_menu_page.check_standart_multi()
        assert cars == selected_cars

    @allure.title('Check all "Standart multi select" parameters are selected')
    def test_select_all_values_in_standart_multi(self, page):
        select_menu_page = SelectMenuPage(page)
        select_menu_page.open()
        select_menu_page.select_all_standart_multi()
        selected_cars = select_menu_page.check_standart_multi()
        assert selected_cars == 4
