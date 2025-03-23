import pytest
from playwright.sync_api import sync_playwright
import logging
from pages.elements.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.dynamic_properties_page import DynamicPropertiesPage

URL = "https://demoqa.com/dynamic-properties"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Можно поставить True для фона
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    yield page
    page.close()

def navigate_to_dynamic_properties(page):
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

# 1. Проверка, что кнопка становится активной через 5 секунд
def test_enable_after_5_seconds(page):
    dynamic_properties_page = navigate_to_dynamic_properties(page)
    logging.info("Testing button enable after 5 seconds")
    assert dynamic_properties_page.wait_for_button_to_enable(), "Button did not enable after 5 seconds"

# 2. Проверка, что текст кнопки изменяется
def test_text_changes(page):
    dynamic_properties_page = navigate_to_dynamic_properties(page)
    logging.info("Testing text change")
    initial_text, new_text = dynamic_properties_page.wait_for_text_change()
    assert initial_text != new_text, "Text did not change"

# 3. Проверка, что кнопка меняет цвет
def test_color_changes(page):
    dynamic_properties_page = navigate_to_dynamic_properties(page)
    logging.info("Testing color change")
    initial_color, new_color = dynamic_properties_page.wait_for_color_change()
    assert initial_color != new_color, "Color did not change"

if __name__ == "__main__":
    pytest.main()
