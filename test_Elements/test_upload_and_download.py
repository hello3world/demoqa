import os  # Импортируем модуль os для работы с файлами.
def test_(page):
    page = page
    page.goto('https://demoqa.com/upload-download')

    # download file
    def test_file_download(page):
        page = page
        page.goto('https://demoqa.com/upload-download')
        with page.expect_download() as download_info:
            page.click("#downloadButton")  # Replace with your selector
        download = download_info.value

        # Save the downloaded file to a specific location
        download_path = download.path()
        print(f"Downloaded file path: {download_path}")

        # Optional: Save file to a desired location
        download.save_as("downloads/my_file.txt")


    # upload file
    def test_file_upload(page):
        path_to_picture = os.path.abspath("../pictures/cat.jpg")
        page.set_input_files("#uploadFile", path_to_picture)
