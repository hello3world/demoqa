import random
import re
import time
import allure
from playwright.sync_api import expect

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
        count = items.count()
        if count >= 2:
            what = items.nth(0)
            where = items.nth(1)
            what.drag_to(where)
        order_after = self._get_sortable_items(tabs[tab_name]['item'])
        return order_before, order_after

    @allure.step('Get sortable items')
    def _get_sortable_items(self, selector: str) -> list[str]:
        items = self.page.locator(selector)
        return [items.nth(i).inner_text() for i in range(items.count())]


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


class ResizablePage(BasePage):
    RESIZABLE_BOX_HANDLE = 'div.constraint-area .react-resizable-handle-se'
    RESIZABLE_BOX = '#resizableBoxWithRestriction'
    RESIZABLE_HANDLE = '#resizable .react-resizable-handle-se'
    RESIZABLE = '#resizable'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/resizable', wait_until='domcontentloaded')

    @allure.step('Change size resizable box')
    def change_size_resizable_box(self) -> tuple[tuple[str, str], tuple[str, str]]:
        handle = self.page.locator(self.RESIZABLE_BOX_HANDLE)
        handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] + 400, self.page.mouse.position['y'] + 200)
        self.page.mouse.up()
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE_BOX))
        handle.hover()
        self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] - 500, self.page.mouse.position['y'] - 300)
        self.page.mouse.up()
        min_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step('Change size resizable')
    def change_size_resizable(self) -> tuple[tuple[str, str], tuple[str, str]]:
        h = self.page.locator(self.RESIZABLE_HANDLE)
        h.hover(); self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] + random.randint(1,300), self.page.mouse.position['y'] + random.randint(1,300))
        self.page.mouse.up()
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE))
        h.hover(); self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] + random.randint(-200,-1), self.page.mouse.position['y'] + random.randint(-200,-1))
        self.page.mouse.up()
        min_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE))
        return max_size, min_size

    @allure.step('Get pixel from width and height')
    def _get_px_from_width_height(self, value_of_size: str) -> tuple[str, str]:
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step('Get max and min size')
    def _get_max_min_size(self, selector: str) -> str:
        el = self.page.locator(selector)
        return el.get_attribute('style') or ''


class DroppablePage(BasePage):
    # simple
    SIMPLE_TAB = '#droppableExample-tab-simple'
    DRAG_ME_SIMPLE = '#draggable'
    DROP_HERE_SIMPLE = '#simpleDropContainer #droppable'

    # accept
    ACCEPT_TAB = '#droppableExample-tab-accept'
    ACCEPTABLE = '#acceptable'
    NOT_ACCEPTABLE = '#notAcceptable'
    DROP_HERE_ACCEPT = '#acceptDropContainer #droppable'

    # prevent Propogation
    PREVENT_TAB = '#droppableExample-tab-preventPropogation'
    NOT_GREEDY_DROP_BOX_TEXT = 'div#notGreedyDropBox p:nth-child(1)'
    NOT_GREEDY_INNER_BOX = '#notGreedyInnerDropBox'
    GREEDY_DROP_BOX_TEXT = 'div#greedyDropBox p:nth-child(1)'
    GREEDY_INNER_BOX = '#greedyDropBoxInner'
    DRAG_ME_PREVENT = '#ppDropContainer #dragBox'

    # revert Draggable
    REVERT_TAB = '#droppableExample-tab-revertable'
    WILL_REVERT = '#revertable'
    NOT_REVERT = '#notRevertable'
    DROP_HERE_REVERT = '#revertableDropContainer #droppable'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/droppable', wait_until='domcontentloaded')

    @allure.step('Drop simple div')
    def drop_simple(self) -> str:
        self.page.locator(self.SIMPLE_TAB).click()
        drag_div = self.page.locator(self.DRAG_ME_SIMPLE)
        drop_div = self.page.locator(self.DROP_HERE_SIMPLE)
        drag_div.drag_to(drop_div)
        return drop_div.inner_text()

    @allure.step('Drop accept div')
    def drop_accept(self, accept: str) -> str:
        accepts = {
            'acceptable': self.ACCEPTABLE,
            'not_acceptable': self.NOT_ACCEPTABLE,
        }
        self.page.locator(self.ACCEPT_TAB).click()
        accept_div = self.page.locator(accepts[accept])
        drop_div = self.page.locator(self.DROP_HERE_ACCEPT)
        accept_div.drag_to(drop_div)
        drop_text = drop_div.inner_text()
        return drop_text

    @allure.step('Drop prevent propogation div')
    def drop_prevent_propogation(self, propogation: str) -> tuple[str, str]:
        propogations = {
            'greedy': {
                'box': self.GREEDY_INNER_BOX,
                'text': self.GREEDY_DROP_BOX_TEXT,
            },
            'not_greedy': {
                'box': self.NOT_GREEDY_INNER_BOX,
                'text': self.NOT_GREEDY_DROP_BOX_TEXT,
            },
        }
        self.page.locator(self.PREVENT_TAB).click()
        drag_div = self.page.locator(self.DRAG_ME_PREVENT)
        inner_box = self.page.locator(propogations[propogation]['box'])
        drag_div.drag_to(inner_box)
        outer_box_text = self.page.locator(propogations[propogation]['text']).inner_text()
        inner_box_text = inner_box.inner_text()
        return outer_box_text, inner_box_text

    @allure.step('Drag revert draggable div')
    def drop_revert_draggable(self, type_drag: str) -> tuple[str, str]:
        drags = {'will': self.WILL_REVERT, 'not_will': self.NOT_REVERT}
        self.page.locator(self.REVERT_TAB).click()
        revert = self.page.locator(drags[type_drag])
        drop_div = self.page.locator(self.DROP_HERE_REVERT)
        revert.drag_to(drop_div)
        position_after_move = revert.get_attribute('style') or ''
        time.sleep(1)
        position_after_revert = revert.get_attribute('style') or ''
        return position_after_move, position_after_revert


class DragabblePage(BasePage):
    # simple
    SIMPLE_TAB = '#draggableExample-tab-simple'
    DRAG_ME = 'div#draggableExample-tabpane-simple #dragBox'

    # axis Restricted
    AXIS_TAB = '#draggableExample-tab-axisRestriction'
    ONLY_X = '#restrictedX'
    ONLY_Y = '#restrictedY'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/dragabble', wait_until='domcontentloaded')

    @allure.step('Simple drag and drop')
    def simple_drag_box(self) -> tuple[str, str]:
        self.page.locator(self.SIMPLE_TAB).click()
        drag_div = self.page.locator(self.DRAG_ME)
        position_before, position_after = self._get_before_and_after_position(drag_div)
        return position_before, position_after

    @allure.step('Drag axis restricted element')
    def drag_axis_restricted(self, type_only: str) -> tuple[str, str, str, str]:
        only = {'only_x': self.ONLY_X, 'only_y': self.ONLY_Y}
        self.page.locator(self.AXIS_TAB).click()
        only_element = self.page.locator(only[type_only])
        position_before, position_after = self._get_before_and_after_position(only_element)
        top_before = self._get_top_position(position_before)
        top_after = self._get_top_position(position_after)
        left_before = self._get_left_position(position_before)
        left_after = self._get_left_position(position_after)
        return top_before[0], top_after[0], left_before[0], left_after[0]

    @allure.step('Get before and after positions')
    def _get_before_and_after_position(self, drag_element) -> tuple[str, str]:
        # drag small random offsets twice and read style before/after
        self.page.mouse.move(1, 1)
        drag_element.hover(); self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] + random.randint(0, 50), self.page.mouse.position['y'] + random.randint(0, 50))
        self.page.mouse.up()
        before_position = drag_element.get_attribute('style') or ''
        drag_element.hover(); self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] + random.randint(0, 50), self.page.mouse.position['y'] + random.randint(0, 50))
        self.page.mouse.up()
        after_position = drag_element.get_attribute('style') or ''
        return before_position, after_position

    @allure.step('Get top position')
    def _get_top_position(self, positions: str) -> list[str]:
        return re.findall(r'[0-9]+', positions.split(';')[2])

    @allure.step('Get left position')
    def _get_left_position(self, positions: str) -> list[str]:
        return re.findall(r'[0-9]+', positions.split(';')[1])
