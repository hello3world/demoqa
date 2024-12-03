from selenium.webdriver.chrome.options import Options
from selenium import webdriver  # Импортируем WebDriver для автоматизации действий браузера.
import pytest

# фикстура для инициализации драйвера на Selenium
@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Инициализируем сессию WebDriver с использованием браузера Chrome.
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()



