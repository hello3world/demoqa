import allure
from pages.alerts_frames.modal_dialogs_page import ModalDialogsPage

pytestmark = allure.suite('Alerts/Frames')

@allure.title('Verify small modal title and body text')
def test_small_modal_dialogs(page):
    modal_dialogs_page = ModalDialogsPage(page)
    modal_dialogs_page.open()
    title_small, body_small_text = modal_dialogs_page.check_modal_dialogs('small', 'button')
    assert title_small == 'Small Modal'
    assert 'This is a small modal.' in body_small_text

@allure.title('Verify large modal title and body includes Lorem Ipsum')
def test_large_modal_dialogs(page):
    modal_dialogs_page = ModalDialogsPage(page)
    modal_dialogs_page.open()
    title_large, body_large_text = modal_dialogs_page.check_modal_dialogs('large', 'button')
    assert title_large == 'Large Modal'
    assert 'Lorem Ipsum' in body_large_text
