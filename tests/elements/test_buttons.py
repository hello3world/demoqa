import logging
from pages.elements.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.buttons_page import ButtonPage

def test_buttons(page):
    try:
        logging.info("Navigating to the home page")
        home_page = HomePage(page)
        home_page.open("https://demoqa.com/")
        home_page.page_verify()
        
        logging.info("Navigating to the buttons page")
        home_page.click_elements_button()
        element_page = ElementsPage(page)
        element_page.page_verify()
        element_page.click_buttons()

        buttons_page = ButtonPage(page)
        buttons_page.page_verify()

        logging.info("Performing button clicks")
        buttons_page.single_click_button()
        buttons_page.double_click_button()  
        buttons_page.right_click_button()
    except Exception as e:
        base_page = ButtonPage(page)
        base_page.take_screenshot_on_error(f"Error in test_buttons: {e}")
        raise
