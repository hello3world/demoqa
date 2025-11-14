import random
import re
import allure
from pages.base_page import BasePage


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

    def _get_before_and_after_position(self, drag_element) -> tuple[str, str]:
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

    def _get_top_position(self, positions: str) -> list[str]:
        return re.findall(r'[0-9]+', positions.split(';')[2])

    def _get_left_position(self, positions: str) -> list[str]:
        return re.findall(r'[0-9]+', positions.split(';')[1])
