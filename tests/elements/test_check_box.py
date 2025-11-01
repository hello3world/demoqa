import logging
import allure
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.elements_page import ElementsPage
from pages.check_box_page import CheckBoxPage

@allure.title("Check Box: selecting Desktop, Documents, Downloads shows in result")
@allure.severity(allure.severity_level.NORMAL)
def test_check_box_select_desktop_documents_downloads(page):
    home = HomePage(page)
    logging.info("Open DemoQA home page")
    home.open("https://demoqa.com/")
    home.page_verify()

    logging.info("Navigate to Elements -> Check Box")
    home.click_elements_button()
    elements = ElementsPage(page)
    elements.page_verify()
    elements.click_check_box()

    cb = CheckBoxPage(page)
    cb.page_verify()

    logging.info("Expand all and select Desktop, Documents, Downloads")
    cb.expand_all_nodes()
    cb.select_desktop()
    cb.select_documents()
    cb.select_downloads()

    result_text = page.locator("#result").inner_text()
    print(result_text)
    assert "desktop" in result_text and "documents" in result_text and "downloads" in result_text
