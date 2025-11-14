import allure
from pages.interactions.droppable_page import DroppablePage

pytestmark = allure.suite('Interactions')

@allure.feature('Droppable Page')
class TestDroppablePage:
    @allure.title('Check "Simple" droppable')
    def test_simple_droppable(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!'

    @allure.title('Check acceptable div in "Accept" droppable')
    def test_accept_droppable_acceptable(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        accept_result = droppable_page.drop_accept('acceptable')
        assert accept_result == 'Dropped!'

    @allure.title('Check not acceptable div in "Accept" droppable')
    def test_accept_droppable_not_acceptable(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        accept_result = droppable_page.drop_accept('not_acceptable')
        assert accept_result == 'Drop here'

    @allure.title('Check not greedy box in "Prevent Propogation" droppable')
    def test_prevent_propogation_droppable_not_greedy(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        outer_box_text, inner_box_text = droppable_page.drop_prevent_propogation('not_greedy')
        assert outer_box_text == 'Dropped!'
        assert inner_box_text == 'Dropped!'

    @allure.title('Check greedy box in "Prevent Propogation" droppable')
    def test_prevent_propogation_droppable_greedy(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        outer_box_text, inner_box_text = droppable_page.drop_prevent_propogation('greedy')
        assert outer_box_text == 'Outer droppable'
        assert inner_box_text == 'Dropped!'

    @allure.title('Check will revert in "Revert draggable" droppable')
    def test_will_revert_draggable_droppable(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_draggable('will')
        assert position_after_move != position_after_revert

    @allure.title('Check not will revert in "Revert draggable" droppable')
    def test_not_will_revert_draggable_droppable(self, page):
        droppable_page = DroppablePage(page)
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_revert_draggable('not_will')
        assert position_after_move == position_after_revert
