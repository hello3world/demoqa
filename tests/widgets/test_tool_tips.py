import allure
from pages.widgets.tool_tips_page import ToolTipsPage

pytestmark = allure.suite('Widgets')

@allure.feature('Tool Tips')
class TestToolTips:
    @allure.title('Check tool tips - button')
    def test_tool_tip_button(self, page):
        p = ToolTipsPage(page)
        p.open()
        tip = p.check_tool_tips('button')
        assert tip == 'You hovered over the Button'

    @allure.title('Check tool tips - field')
    def test_tool_tip_field(self, page):
        p = ToolTipsPage(page)
        p.open()
        tip = p.check_tool_tips('field')
        assert tip == 'You hovered over the text field'

    @allure.title('Check tool tips - contrary')
    def test_tool_tip_contrary(self, page):
        p = ToolTipsPage(page)
        p.open()
        tip = p.check_tool_tips('contrary')
        assert tip == 'You hovered over the Contrary'

    @allure.title('Check tool tips - section')
    def test_tool_tip_section(self, page):
        p = ToolTipsPage(page)
        p.open()
        tip = p.check_tool_tips('section')
        assert tip == 'You hovered over the 1.10.32'
