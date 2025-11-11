import logging
import allure
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.text_box_page import TextBoxPage
from playwright.sync_api import expect


@allure.title("Text Box: invalid email should not be accepted")
@allure.severity(allure.severity_level.CRITICAL)
def test_text_box_rejects_invalid_email_format(page):
    home = HomePage(page)
    logging.info("Open DemoQA home page")
    home.open("https://demoqa.com/")
    home.page_verify()

    logging.info("Navigate to Elements -> Text Box")
    home.click_elements_button()
    elements = ElementsPage(page)
    elements.page_verify()
    elements.click_text_box()

    text_box = TextBoxPage(page)
    text_box.page_verify()

    logging.info("Fill form with invalid email and submit")
    text_box.fill_form(
        name="QA User",
        email="invalid-email",
        current_address="Addr 1",
        permanent_address="Addr 2",
    )

    logging.info("Verify that email input is marked as invalid")
    email_input = page.locator("#userEmail")
    old_classes = email_input.get_attribute("class")
    logging.debug(f"Email input classes after invalid submission: {old_classes}")
    text_box.click_submit_button()
    new_classes = email_input.get_attribute("class")
    logging.debug(f"Email input classes after clicking submit: {new_classes}")
    assert "field-error" in new_classes, \
        "Email input was not marked as invalid after submitting invalid email"
    logging.info("Test completed: invalid email format correctly rejected")
