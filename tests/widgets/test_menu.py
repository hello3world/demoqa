import allure
from pages.widgets.menu_page import MenuPage

pytestmark = allure.suite('Widgets')

@allure.feature('Menu Page')
class TestMenuPage:
    @allure.title('Check all of the menu items')
    def test_menu_items(self, page):
        menu_page = MenuPage(page)
        menu_page.open()
        data = menu_page.check_menu()
        assert data == [
            'Main Item 1',
            'Main Item 2',
            'Sub Item',
            'Sub Item',
            'SUB SUB LIST »',
            'Sub Sub Item 1',
            'Sub Sub Item 2',
            'Main Item 3',
        ]
