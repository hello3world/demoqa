import allure
from pages.base_page import BasePage


class SortablePage(BasePage):
    TAB_LIST = '#demo-tab-list'
    LIST_ITEM = 'div#demo-tabpane-list .list-group-item'

    TAB_GRID = '#demo-tab-grid'
    GRID_ITEM = 'div#demo-tabpane-grid .list-group-item'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/sortable', wait_until='domcontentloaded')

    @allure.step('Change list or grid order')
    def change_order(self, tab_name: str) -> tuple[list[str], list[str]]:
        tabs = {
            'list': {'tab': self.TAB_LIST, 'item': self.LIST_ITEM},
            'grid': {'tab': self.TAB_GRID, 'item': self.GRID_ITEM},
        }
        self.page.locator(tabs[tab_name]['tab']).click()
        order_before = self._get_sortable_items(tabs[tab_name]['item'])
        items = self.page.locator(tabs[tab_name]['item'])
        if items.count() >= 2:
            items.nth(0).drag_to(items.nth(1))
        order_after = self._get_sortable_items(tabs[tab_name]['item'])
        return order_before, order_after

    @allure.step('Get sortable items')
    def _get_sortable_items(self, selector: str) -> list[str]:
        items = self.page.locator(selector)
        return [items.nth(i).inner_text() for i in range(items.count())]
