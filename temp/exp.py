import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys

# Фикстура для инициализации драйвера
@pytest.fixture(scope="function")
def driver():
    # Настройка headless-режима
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")

    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    # Закрытие драйвера после выполнения теста
    driver.quit()

# Фикстура для создания директории скриншотов
@pytest.fixture(scope="session")
def setuшp_screenshots_dir():
    screens_dir = os.path.abspath("screens")
    if not os.path.exists(screens_dir):
        os.makedirs(screens_dir)
    return screens_dir

# Фикстура для замера времени выполнения теста
@pytest.fixture(scope="function")
def track_time():
    start_time = time.time()
    yield
    end_time = time.time()
    time_for_test = end_time - start_time
    print(f"Test execution time: {time_for_test:.2f} seconds")


# Параметризация теста с разными наборами данных
@pytest.mark.parametrize(
    "first_name, last_name, email, phone, subject, state, city", [
        ("Yana", "Nazarova", "yana@test.com", "89993452467", "History", "Uttar Pradesh", "Agra"),
        ("Ivan", "Petrov", "ivan@test.com", "89999999999", "Maths", "Haryana", "Karnal"),
        ("Olga", "Sidorova", "olga@test.com", "89988888888", "Physics", "Delhi", "Delhi"),
    ]
)
def test_submit_form(driver, setup_screenshots_dir, track_time, first_name, last_name, email, phone, subject, state, city):
    # Открытие страницы
    driver.get("https://demoqa.com/automation-practice-form")

    # Заполнение формы
    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "userEmail").send_keys(email)

    # Выбор пола (фиксируем мужской пол для всех тестов)
    gender_male = driver.find_element(By.XPATH, "//label[text()='Male']")
    driver.execute_script("arguments[0].scrollIntoView(true);", gender_male)
    gender_male.click()

    # Заполнение номера телефона
    driver.find_element(By.ID, "userNumber").send_keys(phone)

    # Выбор даты рождения
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.click()
    month_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month_select.select_by_visible_text("March")
    year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year_select.select_by_visible_text("2015")
    day = driver.find_element(By.XPATH, "//div[text() = '13']")
    day.click()

    # Заполнение поля "Subjects"
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys(subject)
    subjects.send_keys(Keys.RETURN)

    # Выбор хобби
    hobby_sports = driver.find_element(By.XPATH, "//label[text()='Sports']")
    driver.execute_script("arguments[0].scrollIntoView(true);", hobby_sports)
    hobby_sports.click()

    hobby_music = driver.find_element(By.XPATH, "//label[text()='Music']")
    driver.execute_script("arguments[0].scrollIntoView(true);", hobby_music)
    hobby_music.click()

    # Загрузка изображения
    picture = driver.find_element(By.ID, "uploadPicture")
    path_to_picture = os.path.abspath("../pictures/cat.jpg")
    picture.send_keys(path_to_picture)

    # Ввод адреса
    driver.find_element(By.ID, "currentAddress").send_keys("ул. Линейная, 8")

    # Выбор штата и города
    state_input = driver.find_element(By.ID, "react-select-3-input")
    state_input.send_keys(state)
    state_input.send_keys(Keys.RETURN)

    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys(city)
    city_input.send_keys(Keys.RETURN)

    # Клик по кнопке "Submit"
    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    submit.click()

    # Генерация имени файла для скриншота
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = os.path.join(setup_screenshots_dir, f"screenshot_{timestamp}.png")

    # Уменьшение масштаба страницы и создание скриншота
    driver.execute_script("document.body.style.zoom='70%'")
    driver.save_screenshot(screenshot_path)

    # Проверка текста в модальном окне
    header_modal_window = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    header_modal_window_text = header_modal_window.text

    # Убедитесь, что форма успешно отправлена
    assert header_modal_window_text == "Thanks for submitting the form"
    print("Test passed")
