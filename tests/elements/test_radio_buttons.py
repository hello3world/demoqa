import logging
from pages.elements.radio_button_page import RadioButtonPage
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from playwright.sync_api import expect

def test_radio_button(page):
    try:
        logging.info("Navigating to the home page")
        home_page = HomePage(page)
        home_page.open("https://demoqa.com/")
        home_page.page_verify()
        
        logging.info("Navigating to the radio button page")
        home_page.click_elements_button()
        element_page = ElementsPage(page)
        element_page.page_verify()
        element_page.click_radio_buttons()

        radio_button_page = RadioButtonPage(page)
        radio_button_page.page_verify()

        logging.info("Selecting 'Yes'")
        radio_button_page.select_yes()
        expect(page.locator(".text-success")).to_have_text("Yes")

        logging.info("Selecting 'Impressive'")
        radio_button_page.select_impressive()
        expect(page.locator(".text-success")).to_have_text("Impressive")

        logging.info("Selecting 'No'")
        radio_button_page.no_option_is_disabled()

    except Exception as e:
        logging.error(f"Error in test_radio_button: {e}")
        base_page = RadioButtonPage(page)
        base_page.take_screenshot_on_error()
        raise
