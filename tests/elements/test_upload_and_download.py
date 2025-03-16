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
    download_folder = "downloaded_files"
    download_path = upload_download_page.download_file(download_folder)
    logging.info(f"Downloaded file path: {download_path}")

def test_upload_file(page):
    ''' It's checked ability to upload the file from system folder'''

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
    path_to_picture = os.path.abspath("../pictures/cat.jpg")
    upload_download_page.upload_file(path_to_picture)

    logging.info("Verifying the upload")
    expect(upload_download_page.uploaded_file_name).to_have_text("cat.jpg")
