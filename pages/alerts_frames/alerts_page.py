import random
import allure
from pages.base_page import BasePage


class AlertsPage(BasePage):
    SEE_ALERT_BUTTON = '#alertButton'
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = '#timerAlertButton'
    CONFIRM_BOX_ALERT_BUTTON = '#confirmButton'
    CONFIRM_RESULT = '#confirmResult'
    PROMPT_BOX_ALERT_BUTTON = '#promtButton'
    PROMPT_RESULT = '#promptResult'

    def __init__(self, page) -> None:
        super().__init__(page)

    def open(self) -> None:
        self.page.goto('https://demoqa.com/alerts', wait_until='domcontentloaded')

    @allure.step('Get text from alert')
    def check_see_alert(self) -> str:
        with self.page.expect_event('dialog') as dialog_info:
            self.page.locator(self.SEE_ALERT_BUTTON).click()
        dialog = dialog_info.value
        message = dialog.message
        dialog.accept()
        return message

    @allure.step('Check alert appear after 5 sec')
    def check_alert_appear_after_5_sec(self) -> str:
        with self.page.expect_event('dialog') as dialog_info:
            self.page.locator(self.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        dialog = dialog_info.value
        message = dialog.message
        dialog.accept()
        return message

    @allure.step('Check action with alert')
    def check_action_alert(self, action: str) -> str:
        with self.page.expect_event('dialog') as dialog_info:
            self.page.locator(self.CONFIRM_BOX_ALERT_BUTTON).click()
        dialog = dialog_info.value
        if action == 'accept':
            dialog.accept()
        else:
            dialog.dismiss()
        return self.page.locator(self.CONFIRM_RESULT).inner_text()

    @allure.step('Check prompt alert')
    def check_prompt_alert(self) -> tuple[str, str]:
        text = f'autotest{random.randint(0, 999)}'
        with self.page.expect_event('dialog') as dialog_info:
            self.page.locator(self.PROMPT_BOX_ALERT_BUTTON).click()
        dialog = dialog_info.value
        dialog.accept(prompt=text)
        text_result = self.page.locator(self.PROMPT_RESULT).inner_text()
        return text, text_result
