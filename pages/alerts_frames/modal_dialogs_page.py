import allure
from pages.base_page import BasePage


class ModalDialogsPage(BasePage):
    SMALL_MODAL_BUTTON = '#showSmallModal'
    SMALL_MODAL_CLOSE_BUTTON = '#closeSmallModal'
    BODY_SMALL_MODAL = 'div.modal-body'
    TITLE_SMALL_MODAL = '#example-modal-sizes-title-sm'

    LARGE_MODAL_BUTTON = '#showLargeModal'
    LARGE_MODAL_CLOSE_BUTTON = '#closeLargeModal'
    BODY_LARGE_MODAL = 'div.modal-body p'
    TITLE_LARGE_MODAL = '#example-modal-sizes-title-lg'

    MODAL_CLOSE_CROSS = 'button.close span[aria-hidden="true"]'
    CLOSE_OVERLAY = 'div[role="dialog"]'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/modal-dialogs', wait_until='domcontentloaded')

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self, size: str, method: str) -> tuple[str, str]:
        if size == 'small':
            self.page.locator(self.SMALL_MODAL_BUTTON).click()
            title_text = self.page.locator(self.TITLE_SMALL_MODAL).inner_text()
            body_text = self.page.locator(self.BODY_SMALL_MODAL).inner_text()
            self._closing_method(method, 'SMALL_MODAL_CLOSE_BUTTON')
            return title_text, body_text
        else:
            self.page.locator(self.LARGE_MODAL_BUTTON).click()
            title_text = self.page.locator(self.TITLE_LARGE_MODAL).inner_text()
            body_text = self.page.locator(self.BODY_LARGE_MODAL).inner_text()
            self._closing_method(method, 'LARGE_MODAL_CLOSE_BUTTON')
            return title_text, body_text

    def _closing_method(self, method: str, locator_name: str) -> None:
        locator_selector = getattr(self, locator_name)
        if method == 'button':
            self.page.locator(locator_selector).click()
        elif method == 'cross':
            self.page.locator(self.MODAL_CLOSE_CROSS).click()
        else:
            self.page.locator(self.CLOSE_OVERLAY).click()
