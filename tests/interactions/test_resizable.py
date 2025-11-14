import allure
from pages.interactions.resizable_page import ResizablePage

pytestmark = allure.suite('Interactions')

@allure.feature('Resizable Page')
class TestResizablePage:
    @allure.title('Check changed "Resizable box"')
    def test_resizable_box(self, page):
        resizable_page = ResizablePage(page)
        resizable_page.open()
        max_box, min_box = resizable_page.change_size_resizable_box()
        assert ('500px', '300px') == max_box
        assert ('150px', '150px') == min_box

    @allure.title('Check changed "Resizable"')
    def test_resizable(self, page):
        resizable_page = ResizablePage(page)
        resizable_page.open()
        max_resize, min_resize = resizable_page.change_size_resizable()
        assert min_resize != max_resize
