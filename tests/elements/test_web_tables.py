import allure
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.web_table_page import WebTablePage


def _go_to_web_tables(page) -> WebTablePage:
    home = HomePage(page)
    home.open("https://demoqa.com/")
    home.page_verify()

    elements = ElementsPage(page)
    home.click_elements_button()
    elements.page_verify()
    elements.click_web_tables()

    wt = WebTablePage(page)
    wt.page_verify()
    return wt


@allure.title("Web Tables: add person shows in last row")
def test_web_tables_add_person(page):
    wt = _go_to_web_tables(page)
    wt.open_reg_form()
    wt.verify_reg_form()
    wt.fill_form("John", "Doe", "john.doe@example.com", "30", "50000", "Engineering")
    wt.submit_form()
    expect(page.locator(wt.table_rows).last).to_be_visible()
    assert wt.get_last_row_values() == [
        "John",
        "Doe",
        "john.doe@example.com",
        "30",
        "50000",
        "Engineering",
    ]


@allure.title("Web Tables: search by last name returns correct row")
def test_web_tables_search_person(page):
    wt = _go_to_web_tables(page)
    # add a unique user then search
    wt.open_add_form()
    wt.fill_form("Alice", "Zephyr", "alice.z@example.com", "28", "70000", "QA")
    wt.submit_form()
    wt.search_some_person("Zephyr")
    row_text = wt.check_search_person()
    assert "Zephyr" in row_text and "Alice" in row_text


@allure.title("Web Tables: edit first result updates age")
def test_web_tables_update_age(page):
    wt = _go_to_web_tables(page)
    wt.search_some_person("")
    wt.edit_first_result()
    new_age = wt.update_age("45")
    first_row_text = wt.check_search_person()
    assert new_age in first_row_text


@allure.title(
    "Web Tables: delete first result shows 'No rows found' when last record is removed"
)
def test_web_tables_delete_first(page):
    wt = _go_to_web_tables(page)
    # narrow to a unique row by adding, then delete it
    wt.open_add_form()
    wt.fill_form("Temp", "UserDel", "tmp.del@example.com", "31", "40000", "Tmp")
    wt.submit_form()
    wt.search_some_person("UserDel")
    wt.delete_first_result()
    # if search filter remains, table shows no data
    txt = wt.check_deleted_person()
    assert txt.strip().lower() == "no rows found"


@allure.title("Web Tables: change rows per page supports [5,10,20,50,100]")
def test_web_tables_change_row_count(page):
    wt = _go_to_web_tables(page)
    counts = wt.select_rows_count()
    assert counts == [5, 10, 20, 50, 100]
