import allure
from pages.alerts_frames.nested_frames_page import NestedFramesPage

pytestmark = allure.suite('Alerts/Frames')

@allure.title('Verify parent and child nested frames text')
def test_nested(page):
    nf = NestedFramesPage(page)
    nf.open()
    parent, child = nf.check_nested_frame()
    assert 'Parent' in parent
    assert 'Child Iframe' in child
