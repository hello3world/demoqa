import pytest
from playwright.sync_api import sync_playwright
from ...pages.elements.web_table_page import WebTablePage

URL = "https://demoqa.com/webtables"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    yield page
    page.close()

def test_add_row(page):
    web_table = WebTablePage(page)
    web_table.open_add_form()
    web_table.fill_form("John", "Doe", "john.doe@example.com", "30", "50000", "Engineering")
    web_table.submit_form()
    page.wait_for_selector(web_table.table_rows)
    assert web_table.get_last_row_values() == ["John", "Doe", "john.doe@example.com", "30", "50000", "Engineering"]

if __name__ == "__main__":
    pytest.main()