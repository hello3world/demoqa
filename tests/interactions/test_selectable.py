import allure
from pages.interactions.selectable_page import SelectablePage

pytestmark = allure.suite('Interactions')

@allure.feature('Selectable Page')
class TestSelectablePage:
    @allure.title('Check changed selectable list or grid of a one item')
    def test_selectable_one_item_list(self, page):
        selectable_page = SelectablePage(page)
        selectable_page.open()
        count = selectable_page.select_item('list', 'one')
        assert count == 1

    @allure.title('Check changed selectable list or grid of all items')
    def test_selectable_all_items_grid(self, page):
        selectable_page = SelectablePage(page)
        selectable_page.open()
        count = selectable_page.select_item('grid', 'all')
        assert count == 9
