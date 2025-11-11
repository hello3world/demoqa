from typing import Dict
from playwright.sync_api import expect
from pages.base_page import BasePage
import logging

class FormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    # region Getters (Locators)
    def get_header(self):
        return self.page.locator("h1")

    def get_first_name_input(self):
        return self.page.locator("#firstName")

    def get_last_name_input(self):
        return self.page.locator("#lastName")

    def get_email_input(self):
        return self.page.locator("#userEmail")

    def get_gender_option(self, gender: str):
        logging.info(f"Selecting gender: {gender}")
        print(gender)
        return self.page.locator(f'input[name="gender"][value="{gender}"]')

    def get_mobile_input(self):
        return self.page.locator("#userNumber")

    def get_dob_input(self):
        return self.page.locator("#dateOfBirthInput")

    def get_month_select(self):
        return self.page.locator(".react-datepicker__month-select")

    def get_year_select(self):
        return self.page.locator(".react-datepicker__year-select")

    def get_day_cell(self, day: int):
        return self.page.locator(f".react-datepicker__day--0{int(day):02d}").first

    def get_subjects_input(self):
        return self.page.locator("#subjectsInput")

    def get_hobby_checkbox(self, name: str):
        return self.page.get_by_text(name, exact=True)

    def get_upload_input(self):
        return self.page.locator("#uploadPicture")

    def get_address_input(self):
        return self.page.locator("#currentAddress")

    def get_state_control(self):
        return self.page.locator("#state")

    def get_state_option(self, state: str):
        return self.page.get_by_text(state, exact=True)

    def get_city_control(self):
        return self.page.locator("#city")

    def get_city_option(self, city: str):
        return self.page.get_by_text(city, exact=True)

    def get_submit_button(self):
        return self.page.get_by_role("button", name="Submit")

    def get_modal_title_locator(self):
        return self.page.locator("#example-modal-sizes-title-lg")

    def get_result_rows(self):
        return self.page.locator(".table-responsive tbody tr")
    # endregion

    # region Page verification
    def page_verify(self):
        expect(self.get_header().filter(has_text="Practice Form")).to_be_visible()
    # endregion

    # region Actions
    def set_name(self, first_name: str, last_name: str) -> None:
        self.get_first_name_input().fill(first_name)
        self.get_last_name_input().fill(last_name)

    def set_email(self, email: str) -> None:
        self.get_email_input().fill(email)

    def choose_gender(self, gender: str) -> None:
        radio = self.get_gender_option(gender)
        input_id = radio.get_attribute("id")
        if input_id:
            # Click the label associated with the input to avoid overlay intercepts
            self.page.locator(f'label[for="{input_id}"]').click()
        else:
            # Fallback
            radio.check(force=True)

    def set_mobile(self, mobile: str) -> None:
        self.get_mobile_input().fill(mobile)

    def set_date_of_birth(self, day: int, month: str | None, year: str | int | None) -> None:
        self.get_dob_input().click()
        if month is not None:
            self.get_month_select().select_option(label=str(month))
        if year is not None:
            self.get_year_select().select_option(label=str(year))
        self.get_day_cell(int(day)).click()

    def add_subject(self, subject: str) -> None:
        if subject:
            self.get_subjects_input().fill(subject)
            self.page.keyboard.press("Enter")

    def select_hobbies(self, hobbies: list[str]) -> None:
        for h in hobbies:
            self.get_hobby_checkbox(h).click()

    def upload_picture(self, path: str) -> None:
        if path:
            self.get_upload_input().set_input_files(path)

    def set_address(self, address: str) -> None:
        self.get_address_input().fill(address)

    def select_state_city(self, state: str, city: str) -> None:
        self.get_state_control().click()
        self.get_state_option(state).click()
        self.get_city_control().click()
        self.get_city_option(city).click()

    def submit_form(self) -> None:
        self.get_submit_button().click()
        expect(self.get_modal_title_locator()).to_be_visible()
    # endregion

    # region Orchestrators
    def fill_form(self, data: Dict[str, str]) -> None:
        self.set_name(data.get("first_name", ""), data.get("last_name", ""))
        self.set_email(data.get("email", ""))
        self.choose_gender(data.get("gender", ""))
        self.set_mobile(data.get("mobile", ""))
        self.set_date_of_birth(int(data.get("dob_day", 12)), data.get("dob_month"), data.get("dob_year"))
        self.add_subject(data.get("subject", ""))
        # As per test expectation
        self.select_hobbies(["Sports", "Music"]) 
        self.upload_picture(data.get("picture_path", ""))
        self.set_address(data.get("address", ""))
        self.select_state_city(data.get("state", ""), data.get("city", ""))


    def get_modal_title(self) -> str:
        return self.get_modal_title_locator().inner_text()

    def get_modal_data(self) -> Dict[str, str]:
        rows = self.get_result_rows()
        result: Dict[str, str] = {}
        count = rows.count()
        for i in range(count):
            key = rows.nth(i).locator("td").nth(0).inner_text().strip()
            val = rows.nth(i).locator("td").nth(1).inner_text().strip()
            result[key] = val
        return result
