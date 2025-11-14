import allure
from pages.interactions.dragabble_page import DragabblePage

pytestmark = allure.suite('Interactions')

@allure.feature('Dragabble Page')
class TestDragabblePage:
    @allure.title('Check "Simple" dragabble')
    def test_simple_dragabble(self, page):
        dragabble_page = DragabblePage(page)
        dragabble_page.open()
        before, after = dragabble_page.simple_drag_box()
        assert before != after

    @allure.title('Check Only X in "Axis Restricted" dragabble')
    def test_axis_restricted_dragabble_only_x(self, page):
        dragabble_page = DragabblePage(page)
        dragabble_page.open()
        top_before, top_after, left_before, left_after = dragabble_page.drag_axis_restricted('only_x')
        assert top_before == top_after and int(top_after) == 0
        assert left_before != left_after and int(left_before) != 0

    @allure.title('Check Only Y in "Axis Restricted" dragabble')
    def test_axis_restricted_dragabble_only_y(self, page):
        dragabble_page = DragabblePage(page)
        dragabble_page.open()
        top_before, top_after, left_before, left_after = dragabble_page.drag_axis_restricted('only_y')
        assert top_before != top_after and top_after != 0
        assert left_before == left_after and int(left_after) == 0
