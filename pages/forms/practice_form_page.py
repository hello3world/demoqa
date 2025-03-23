import os
from pages.base_page import BasePage 

class PracticeFormPage(BasePage):
    def __init__(self, page):
        self.page = page
        self.first_name = "#firstName"
        self.last_name = "#lastName"
        self.email = "#userEmail"
        self.gender = "label[for='gender-radio-1']"
        self.mobile = "#userNumber"
        self.dob_input = "#dateOfBirthInput"
        self.month_select = ".react-datepicker__month-select"
        self.year_select = ".react-datepicker__year-select"
        self.day_select = "div.react-datepicker__day--012"
        self.subjects_input = "#subjectsInput"
        self.hobby_sports = "label[for='hobbies-checkbox-1']"
        self.hobby_music = "label[for='hobbies-checkbox-3']"
        self.upload_picture = "#uploadPicture"
        self.current_address = "#currentAddress"
        self.state_input = "#react-select-3-input"
        self.city_input = "#react-select-4-input"
        self.submit_button = "#submit"
        self.modal_title = "#example-modal-sizes-title-lg"

    def fill_form(self, data):
        self.page.fill(self.first_name, data["first_name"])
        self.page.fill(self.last_name, data["last_name"])
        self.page.fill(self.email, data["email"])
        self.page.click(self.gender)
        self.page.fill(self.mobile, data["mobile"])
        self.page.click(self.dob_input)
        self.page.select_option(self.month_select, label=data["dob_month"])
        self.page.select_option(self.year_select, label=data["dob_year"])
        self.page.click(self.day_select)
        self.page.fill(self.subjects_input, data["subject"])
        self.page.press(self.subjects_input, "Enter")
        self.page.click(self.hobby_sports)
        self.page.click(self.hobby_music)
        self.page.set_input_files(self.upload_picture, data["picture_path"])
        self.page.fill(self.current_address, data["address"])
        self.page.fill(self.state_input, data["state"])
        self.page.press(self.state_input, "Enter")
        self.page.fill(self.city_input, data["city"])
        self.page.press(self.city_input, "Enter")

    def submit_form(self):
        self.page.click(self.submit_button)

    def get_modal_title(self):
        return self.page.text_content(self.modal_title)

    def get_modal_data(self):
        rows = self.page.locator("tbody tr")
        modal_data = {}
        for row in rows.all():
            key = row.locator("td").nth(0).text_content().strip()
            value = row.locator("td").nth(1).text_content().strip()
            modal_data[key] = value
        return modal_data
