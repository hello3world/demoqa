import os
from typing import Dict
import logging
import json
from pages.forms.form_page import FormPage
from pages.home_page import HomePage

def test_form(page):
    try:
        home_page = HomePage(page)
        home_page.open("https://demoqa.com/")
        home_page.page_verify()
        home_page.open_forms_button()

        form_page = FormPage(page)
        form_page.page_verify()
        
        # Load test data from JSON file
        with open(os.path.abspath("tests/forms/assets/data/test_data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
        data["picture_path"] = os.path.abspath(data["picture_path"])  # Resolve picture path

        form_page.fill_form(data)
        form_page.submit_form()

        assert form_page.get_modal_title() == "Thanks for submitting the form"

        # Assertions to verify entered data
        modal_data = form_page.get_modal_data()
        assert modal_data["Student Name"] == f"{data['first_name']} {data['last_name']}"
        assert modal_data["Student Email"] == data["email"]
        assert modal_data["Gender"] == "Male"  # Assuming gender is hardcoded in the test
        assert modal_data["Mobile"] == data["mobile"]
        assert modal_data["Date of Birth"] == f"12 {data['dob_month']},{data['dob_year']}"
        assert modal_data["Subjects"] == data["subject"]
        assert modal_data["Hobbies"] == "Sports, Music"
        assert modal_data["Picture"] == os.path.basename(data["picture_path"])
        assert modal_data["Address"] == data["address"]
        assert modal_data["State and City"] == f"{data['state']} {data['city']}"

    except Exception as e:
        logging.error("Error in test_form: {e}")
        form_page = FormPage(page)
        form_page.take_screenshot_on_error()  
        raise
