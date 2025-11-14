import allure
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    PARENT_FRAME = '#frame1'
    PARENT_TEXT = 'body'
    CHILD_FRAME = 'iframe[srcdoc="<p>Child Iframe</p>"]'
    CHILD_TEXT = 'p'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/nestedframes', wait_until='domcontentloaded')

    @allure.step('Check nested frame')
    def check_nested_frame(self) -> tuple[str, str]:
        parent_text = self.page.frame_locator(self.PARENT_FRAME).locator(self.PARENT_TEXT).inner_text()
        child_text = self.page.frame_locator(self.PARENT_FRAME).frame_locator(self.CHILD_FRAME).locator(self.CHILD_TEXT).inner_text()
        return parent_text, child_text
