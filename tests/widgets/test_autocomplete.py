import allure
from pages.widgets.autocomplete_page import AutoCompletePage

pytestmark = allure.suite('Widgets')

@allure.feature('Autocomplete Page')
class TestAutoCompletePage:
    @allure.title('Check the autocomplete is filled')
    def test_fill_multi_autocomplete(self, page):
        autocomplete_page = AutoCompletePage(page)
        autocomplete_page.open()
        colors = autocomplete_page.fill_input_multi()
        colors_result = autocomplete_page.check_color_in_multi()
        assert colors == colors_result

    @allure.title('Check deletions from the multi autocomplete')
    def test_remove_value_from_multi(self, page):
        autocomplete_page = AutoCompletePage(page)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
        assert count_value_before != count_value_after

    @allure.title('Check deletions from the multi autocomplete by cross')
    def test_remove_all_values_from_multi_by_cross(self, page):
        autocomplete_page = AutoCompletePage(page)
        autocomplete_page.open()
        autocomplete_page.fill_input_multi()
        count_value = autocomplete_page.remove_all_values_from_multi()
        assert count_value == 0

    @allure.title('Check deletions from the single autocomplete')
    def test_fill_single_autocomplete(self, page):
        autocomplete_page = AutoCompletePage(page)
        autocomplete_page.open()
        color = autocomplete_page.fill_input_single()
        color_result = autocomplete_page.check_color_in_single()
        assert color == color_result
