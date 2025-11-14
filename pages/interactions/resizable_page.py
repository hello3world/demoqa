import random
import allure
from pages.base_page import BasePage


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
        handle.hover(); self.page.mouse.down()
        self.page.mouse.move(self.page.mouse.position['x'] + 400, self.page.mouse.position['y'] + 200)
        self.page.mouse.up()
        max_size = self._get_px_from_width_height(self._get_max_min_size(self.RESIZABLE_BOX))
        handle.hover(); self.page.mouse.down()
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

    def _get_px_from_width_height(self, value_of_size: str) -> tuple[str, str]:
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def _get_max_min_size(self, selector: str) -> str:
        el = self.page.locator(selector)
        return el.get_attribute('style') or ''
