from pages.base_page import BasePage
from playwright.sync_api import expect
import os

class UploadDownloadPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def page_verify(self):
        expect(self.page.locator("h1:has-text('Upload and Download')")).to_be_visible(timeout=10000)

    def download_file(self):
        download_folder = "assets/downloads"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Download").click()
        download = download_info.value
        download_path = os.path.join(download_folder, download.suggested_filename)
        download.save_as(download_path)

    def upload_file(self, file_path):
        self.page.locator("#uploadFile").set_input_files(file_path)
        
