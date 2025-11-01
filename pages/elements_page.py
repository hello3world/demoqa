from playwright.sync_api import expect
from pages.base_page import BasePage

class ElementsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_verify(self):
        expect(self.page.get_by_text("Please select an item from left to start practice.")).to_be_visible(timeout=10000)

    def click_text_box(self):
        self.page.get_by_text("Text Box").click()

    def click_check_box(self):
        self.page.get_by_text("Check Box").click()
        
    def click_radio_buttons(self):
        self.page.get_by_text("Radio Button").click()

    def click_web_tables(self):
        self.page.get_by_text("Web Tables").click()

    def click_buttons(self):
        self.page.get_by_text("Buttons").click()
    
    def click_links(self):
        self.page.get_by_text("Links").click()

    def click_broken_links_images(self):
        self.page.get_by_text("Broken Links - Images").click()
    
    def click_upload_and_download(self):
        self.page.get_by_text("Upload and Download").click()

    def click_dynamic_properties(self):
        self.page.get_by_text("Dynamic Properties").click()