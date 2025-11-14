import allure
from pages.widgets.tabs_page import TabsPage

pytestmark = allure.suite('Widgets')

@allure.feature('Tabs Page')
class TestTabsPage:
    @allure.title('Check switched tabs')
    def test_tabs_what(self, page):
        tabs = TabsPage(page)
        tabs.open()
        button_text, content = tabs.check_tabs('what')
        assert button_text.lower() == 'what' and content != 0

    @allure.title('Check switched tabs - origin')
    def test_tabs_origin(self, page):
        tabs = TabsPage(page)
        tabs.open()
        button_text, content = tabs.check_tabs('origin')
        assert button_text.lower() == 'origin' and content != 0

    @allure.title('Check switched tabs - use')
    def test_tabs_use(self, page):
        tabs = TabsPage(page)
        tabs.open()
        button_text, content = tabs.check_tabs('use')
        assert button_text.lower() == 'use' and content != 0
