import logging
import allure
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage


@allure.title("Elements section shows key menu items")
@allure.severity(allure.severity_level.NORMAL)
def test_elements_section_navigation_displays_menu(page):
    home = HomePage(page)
    logging.info("Open DemoQA home page")
    home.open("https://demoqa.com/")
    home.page_verify()

    logging.info("Navigate to Elements section")
    home.click_elements_button()

    elements = ElementsPage(page)
    elements.page_verify()

    # Verify key menu items are visible using recommended locators
    page.get_by_text("Text Box").wait_for()
    page.get_by_text("Buttons").wait_for()
    page.get_by_text("Radio Button").wait_for()
