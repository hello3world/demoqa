import allure
from pages.interactions.sortable_page import SortablePage

pytestmark = allure.suite('Interactions')

@allure.feature('Sortable Page')
class TestSortablePage:
    @allure.title('Check changed sortable list or grid')
    def test_sortable_list(self, page):
        sortable_page = SortablePage(page)
        sortable_page.open()
        before, after = sortable_page.change_order('list')
        assert before != after

    @allure.title('Check changed sortable grid')
    def test_sortable_grid(self, page):
        sortable_page = SortablePage(page)
        sortable_page.open()
        before, after = sortable_page.change_order('grid')
        assert before != after
