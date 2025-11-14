import allure
from pages.base_page import BasePage


class FramesPage(BasePage):
    FIRST_FRAME = '#frame1'
    SECOND_FRAME = '#frame2'
    TITLE_FRAME = '#sampleHeading'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/frames', wait_until='domcontentloaded')

    @allure.step('Check frame')
    def check_frame(self, frame_number: str) -> list[str]:
        if frame_number == 'frame1':
            iframe = self.page.locator(self.FIRST_FRAME)
            width = iframe.get_attribute('width') or ''
            height = iframe.get_attribute('height') or ''
            text = self.page.frame_locator(self.FIRST_FRAME).locator(self.TITLE_FRAME).inner_text()
            return [text, width, height]
        elif frame_number == 'frame2':
            iframe = self.page.locator(self.SECOND_FRAME)
            width = iframe.get_attribute('width') or ''
            height = iframe.get_attribute('height') or ''
            text = self.page.frame_locator(self.SECOND_FRAME).locator(self.TITLE_FRAME).inner_text()
            return [text, width, height]
        else:
            raise ValueError('Unsupported frame_number: use "frame1" or "frame2"')
