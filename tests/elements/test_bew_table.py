import pytest
import allure
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.web_table_page import WebTablePage


@allure.title("Web Tables: add person shows in last row")
def test_add_row(page):
    home = HomePage(page)
    home.open("https://demoqa.com/")
    home.page_verify()

    elements = ElementsPage(page)
    home.click_elements_button()
    elements.page_verify()
    elements.click_web_tables()

    wt = WebTablePage(page)
    wt.page_verify()
    wt.open_reg_form()
    wt.verify_reg_form()
    wt.fill_form("John", "Doe", "john.doe@example.com", "30", "50000", "Engineering")
    wt.submit_form()

    # Verify last row equals the entered values
    wt.page.locator(wt.table_rows).last.wait_for(state="visible")
    assert wt.get_last_row_values() == [
        "John",
        "Doe",
        "john.doe@example.com",
        "30",
        "50000",
        "Engineering",
    ]


if __name__ == "__main__":
    pytest.main()
