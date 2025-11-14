import allure
from pages.alerts_frames.alerts_frame_windows_page import BrowserWindowsPage

pytestmark = allure.suite('Alerts/Frames')

@allure.title('Open new tab and verify title')
def test_new_tab(page):
    p = BrowserWindowsPage(page)
    page.goto('https://demoqa.com/browser-windows', wait_until='domcontentloaded')
    title = p.check_opened_interface('tab')
    assert title == 'This is a sample page'

@allure.title('Open new window and verify title')
def test_new_window(page):
    p = BrowserWindowsPage(page)
    page.goto('https://demoqa.com/browser-windows', wait_until='domcontentloaded')
    title = p.check_opened_interface('window')
    assert title == 'This is a sample page'
