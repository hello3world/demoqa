import logging
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.dynamic_properties_page import DynamicPropertiesPage


def navigate_to_dynamic_properties(page) -> DynamicPropertiesPage:
    logging.info("Navigating to the home page")
    home_page = HomePage(page)
    home_page.open("https://demoqa.com/")
    home_page.page_verify()

    logging.info("Navigating to the dynamic properties page")
    home_page.click_elements_button()
    element_page = ElementsPage(page)
    element_page.page_verify()
    element_page.click_dynamic_properties()

    dynamic_properties_page = DynamicPropertiesPage(page)
    dynamic_properties_page.page_verify()
    return dynamic_properties_page


def test_enable_after_5_seconds(page):
    dp = navigate_to_dynamic_properties(page)
    logging.info("Testing button enable after ~5 seconds")
    assert dp.wait_for_button_to_enable(), "Button did not enable after 5-7 seconds"


def test_color_changes(page):
    dp = navigate_to_dynamic_properties(page)
    logging.info("Testing color class change")
    initial_class, new_class = dp.wait_for_color_change()
    assert initial_class != new_class, "Color class did not change"


def test_button_appears(page):
    dp = navigate_to_dynamic_properties(page)
    logging.info("Testing appear after ~5 seconds")
    assert dp.wait_for_button_to_appear(), "Button did not appear after 5-7 seconds"
