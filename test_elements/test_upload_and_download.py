# Import the os module for working with files
import os
# Import function expect for making assertions
from playwright.sync_api import expect

def test_download_file(page):
    """
    It's checked the ability to download the file by clicking the Download button
    :param page: The page object representing the browser page
    :return: None
    """
    # Navigate to the specified page
    page.goto('https://demoqa.com/upload-download')

    # Check that the "Download" link is visible on the page
    expect(page.get_by_role("link", name="Download")).to_be_visible()

    # Specify the folder where you want the file to be downloaded
    download_folder = "download"

    # Ensure the folder exists or create if it doesn't
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Wait for the download to start
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download").click()  # Replace with your selector

    # Get the download object after it starts
    download = download_info.value

    # Get the suggested filename
    suggested_filename = download.suggested_filename

    # Define the path where the file should be saved
    download_path = os.path.join(download_folder, suggested_filename)

    # Save file to a desired location
    download.save_as(download_path)

    print(f"Downloaded file path: {download_path}")




    def test_upload_file(page):
        path_to_picture = os.path.abspath("../pictures/cat.jpg")
        page.set_input_files("#uploadFile", path_to_picture)
