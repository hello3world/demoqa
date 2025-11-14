import allure
from pages.widgets.accordian_page import AccordianPage

pytestmark = allure.suite('Widgets')

@allure.feature('Accordian Page')
class TestAccordianPage:
    @allure.title('Check accordian widget')
    def test_accordian(self, page):
        accordian_page = AccordianPage(page)
        accordian_page.open()
        first_title, first_content = accordian_page.check_accordian('first')
        second_title, second_content = accordian_page.check_accordian('second')
        third_title, third_content = accordian_page.check_accordian('third')
        assert first_title == 'What is Lorem Ipsum?' and first_content > 0
        assert second_title == 'Where does it come from?' and second_content > 0
        assert third_title == 'Why do we use it?' and third_content > 0
