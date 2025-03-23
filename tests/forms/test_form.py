import os
import time
import json
from playwright.sync_api import sync_playwright
from pages.forms.practice_form_page import PracticeFormPage

def test_form(page):
    try:
        page.goto("https://demoqa.com/automation-practice-form")
        
        # Load test data from JSON file
        with open(os.path.abspath("tests/forms/test_data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
        data["picture_path"] = os.path.abspath(data["picture_path"])  # Resolve picture path

        form_page = PracticeFormPage(page)
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

        os.makedirs("assets/screenshots", exist_ok=True)
        time_mark = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.abspath(f"assets/screenshots/screenshot_form_OK_{time_mark}.png")
        page.screenshot(path=screenshot_path)
        
        
    except Exception as e:
        form_page.take_screenshot_on_error(f"Error in test_form: {e}")  
        raise
