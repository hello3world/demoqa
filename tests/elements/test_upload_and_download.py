# Import the os module for working with files
import os
import logging
# Import function expect for making assertions
from playwright.sync_api import expect
from pages.elements.upload_download_page import UploadDownloadPage
from pages.elements.home_page import HomePage
from pages.elements.elements_page import ElementsPage

def test_download_file(page):
    """
    It's checked the ability to download the file by clicking the Download button
    :param page: The page object representing the browser page
    :return: None
    """
    try:
        logging.info("Navigating to the home page")
        home_page = HomePage(page)
        home_page.open("https://demoqa.com/")
        home_page.page_verify()
        
        logging.info("Navigating to the text box page")
        home_page.click_elements_button()
        element_page = ElementsPage(page)
        element_page.page_verify()
        element_page.click_upload_and_download()
        
        logging.info("Navigating to the upload-download page")
        upload_download_page = UploadDownloadPage(page)
        upload_download_page.page_verify()

        logging.info("Downloading the file")
        upload_download_page.download_file()
    except Exception as e:
        base_page = UploadDownloadPage(page)
        base_page.take_screenshot_on_error(f"Error in test_download_file: {e}")
        raise

def test_upload_file(page):
    ''' It's checked ability to upload the file from system folder'''

    try:
        logging.info("Navigating to the home page")
        home_page = HomePage(page)
        home_page.open("https://demoqa.com/")
        home_page.page_verify()
        
        logging.info("Navigating to the text box page")
        home_page.click_elements_button()
        element_page = ElementsPage(page)
        element_page.page_verify()
        element_page.click_upload_and_download()
        
        logging.info("Navigating to the upload-download page")
        upload_download_page = UploadDownloadPage(page)
        upload_download_page.page_verify()

        logging.info("Uploading the file")
        path_to_picture = os.path.abspath("assets/pictures/cat.jpg")
        upload_download_page.upload_file(path_to_picture)

        logging.info("Verifying the upload")
    except Exception as e:
        base_page = UploadDownloadPage(page)
        base_page.take_screenshot_on_error(f"Error in test_upload_file: {e}")
        raise
