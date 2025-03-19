import logging
from pages.elements.radio_button_page import RadioButtonPage
from pages.elements.home_page import HomePage
from pages.elements.elements_page import ElementsPage

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

        logging.info("Selecting 'Impressive'")
        radio_button_page.select_impressive()

        logging.info("Selecting 'No'")
        try:
            radio_button_page.select_no()
        except Exception as error:
            logging.error(f"Error exception = {error}")
            no_radio_button = page.locator('label[for="noRadio"]')
            if no_radio_button.is_enabled():
                no_radio_button.click()
                assert page.text_content(".mt-3") == "You have selected No"
            else:
                logging.info("The 'No' radio button is disabled and cannot be selected.")
    except Exception as e:
        base_page = RadioButtonPage(page)
        base_page.take_screenshot_on_error(f"Error in test_radio_button: {e}")
        raise
