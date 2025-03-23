class WebTablePage:
    def __init__(self, page):
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

    def open_add_form(self):
        self.page.locator(self.add_button).click()

    def fill_form(self, first_name, last_name, email, age, salary, department):
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
        return [last_row.locator("div.rt-td").nth(i).text_content() for i in range(6)]
