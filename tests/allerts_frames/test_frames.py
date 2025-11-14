import allure
from pages.alerts_frames.frames_page import FramesPage

pytestmark = allure.suite('Alerts/Frames')

@allure.title('Verify frame1 content and dimensions')
def test_frame1(page):
    frames = FramesPage(page)
    frames.open()
    text, width, height = frames.check_frame('frame1')
    assert text == 'This is a sample page'
    assert width and height

@allure.title('Verify frame2 content and dimensions')
def test_frame2(page):
    frames = FramesPage(page)
    frames.open()
    text, width, height = frames.check_frame('frame2')
    assert text == 'This is a sample page'
    assert width and height
