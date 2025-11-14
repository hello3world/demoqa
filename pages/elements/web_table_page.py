from pages.base_page import BasePage
from playwright.sync_api import expect


class WebTablePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.add_button = "#addNewRecordButton"
        self.first_name = "#firstName"
        self.last_name = "#lastName"
        self.email = "#userEmail"
        self.age = "#age"
        self.salary = "#salary"
        self.department = "#department"
        self.submit_button = "#submit"
        self.table_rows = "div.rt-tbody div.rt-tr-group"
        self.search_box = "#searchBox"
        self.reg_form_heading = "#registration-form-modal"

    def open_page(self):
        self.page.goto("https://demoqa.com/webtables")

    def page_verify(self):
        expect(self.page.locator("h1").filter(has="Web Tables")).to_be_visible()

    def open_reg_form(self):
        self.page.locator(self.add_button).click()

    # Backwards-compatible alias used by some tests
    def open_add_form(self):
        self.open_reg_form()

    def verify_reg_form(self):
        expect(self.page.locator(self.reg_form_heading)).to_be_visible()

    # Backwards-compatible alias
    def verify_add_form(self):
        self.verify_reg_form()

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        email: str,
        age: str,
        salary: str,
        department: str,
    ):
        self.page.locator(self.first_name).fill(first_name)
        self.page.locator(self.last_name).fill(last_name)
        self.page.locator(self.email).fill(email)
        self.page.locator(self.age).fill(age)
        self.page.locator(self.salary).fill(salary)
        self.page.locator(self.department).fill(department)

    def submit_form(self):
        self.page.locator(self.submit_button).click()

    def get_last_row_values(self):
        last_row = self.page.locator(self.table_rows).last
        return [last_row.locator("div.rt-td").nth(i).inner_text() for i in range(6)]

    def search_some_person(self, keyword: str):
        self.page.locator(self.search_box).fill(keyword)

    def check_search_person(self) -> str:
        row = self.page.locator(self.table_rows).first
        return " ".join(
            [row.locator("div.rt-td").nth(i).inner_text() for i in range(6)]
        )

    def edit_first_result(self):
        self.page.locator(self.table_rows).first.locator("span[title='Edit']").click()

    def update_age(self, new_age: str) -> str:
        self.page.locator(self.age).fill(new_age)
        self.submit_form()
        return new_age

    def delete_first_result(self):
        self.page.locator(self.table_rows).first.locator("span[title='Delete']").click()

    def check_deleted_person(self) -> str:
        return self.page.locator("div.rt-noData").inner_text()

    def select_rows_count(self) -> list[int]:
        # Control is a select element labeled Rows per page
        control = self.page.locator("select[aria-label='rows per page']")
        options = ["5", "10", "20", "50", "100"]
        seen = []
        for opt in options:
            control.select_option(opt)
            seen.append(int(opt))
        return seen
