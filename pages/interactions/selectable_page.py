import allure
from pages.base_page import BasePage


class SelectablePage(BasePage):
    TAB_LIST = "a#demo-tab-list"
    LIST_ITEM = 'ul#verticalListContainer li.list-group-item'
    LIST_ITEM_ACTIVE = 'ul#verticalListContainer li.list-group-item.active'

    TAB_GRID = 'a#demo-tab-grid'
    GRID_ITEM = 'div#gridContainer li.list-group-item'
    GRID_ITEM_ACTIVE = 'div#gridContainer li.list-group-item.active'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/selectable', wait_until='domcontentloaded')

    @allure.step('Select list or grid item')
    def select_item(self, tab_name: str, count: str) -> int:
        tabs = {
            'list': {'tab': self.TAB_LIST, 'item': self.LIST_ITEM, 'active': self.LIST_ITEM_ACTIVE},
            'grid': {'tab': self.TAB_GRID, 'item': self.GRID_ITEM, 'active': self.GRID_ITEM_ACTIVE},
        }
        self.page.locator(tabs[tab_name]['tab']).click()
        self._click_selectable_item(tabs[tab_name]['item'], count)
        active = self.page.locator(tabs[tab_name]['active'])
        return active.count()

    @allure.step('Click selectable item')
    def _click_selectable_item(self, selector: str, count: str) -> None:
        items = self.page.locator(selector)
        if count == 'one':
            items.first.click()
        else:
            for i in range(items.count()):
                items.nth(i).click()
