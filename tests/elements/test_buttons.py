import logging
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.buttons_page import ButtonPage


def navigate_to_buttons(page):
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
    return buttons_page


def test_single_click_button(page):
    try:
        buttons_page = navigate_to_buttons(page)
        logging.info("Performing single click")
        buttons_page.single_click_button()
    except Exception as e:
        buttons_page.take_screenshot_on_error(f"Error in test_single_click_button: {e}")
        raise


def test_double_click_button(page):
    try:
        buttons_page = navigate_to_buttons(page)
        logging.info("Performing double click")
        buttons_page.double_click_button()
    except Exception as e:
        buttons_page.take_screenshot_on_error(f"Error in test_double_click_button: {e}")
        raise


def test_right_click_button(page):
    try:
        buttons_page = navigate_to_buttons(page)
        logging.info("Performing right click")
        buttons_page.right_click_button()
    except Exception as e:
        buttons_page.take_screenshot_on_error(f"Error in test_right_click_button: {e}")
        raise
