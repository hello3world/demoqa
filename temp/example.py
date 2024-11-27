import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Для настройки headless-режима
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

# Настройка headless-режима
chrome_options = Options()
chrome_options.add_argument("--headless")  # Включение headless-режима
chrome_options.add_argument("--window-size=1920x1080")  # Установка разрешения окна

# Инициализация драйвера с опциями
driver = webdriver.Chrome(options=chrome_options)

# Запуск таймера
start_time = time.time()

driver.get("https://demoqa.com/automation-practice-form")

# Заполнение формы
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Yana")

last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Nazarova")

user_email = driver.find_element(By.ID, "userEmail")
user_email.send_keys("test@ya.ru")

gender_male = driver.find_element(By.XPATH, "//label[text()='Male']")
driver.execute_script("arguments[0].scrollIntoView(true);", gender_male)
gender_male.click()

user_number = driver.find_element(By.ID, "userNumber")
user_number.send_keys("89993452467")

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
subjects.send_keys("History")
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
current_address = driver.find_element(By.ID, "currentAddress")
current_address.send_keys("ул. Линейная, 8")

# Выбор штата
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Uttar Pradesh")
state.send_keys(Keys.RETURN)

# Выбор города
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Agra")
city.send_keys(Keys.RETURN)

# Клик по кнопке "Submit"
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit)
submit.click()

# Создание директории "screens", если она не существует
screens_dir = os.path.abspath("screens")
if not os.path.exists(screens_dir):
    os.makedirs(screens_dir)

# Генерация имени файла на основе текущего времени
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
screenshot_path = os.path.join(screens_dir, f"screenshot_{timestamp}.png")

# Уменьшение масштаба страницы
driver.execute_script("document.body.style.zoom='70%'")  # Установить масштаб на 50%
# Сделать скриншот перед assert
driver.save_screenshot(screenshot_path)

# Проверка текста в модальном окне
header_modal_window = driver.find_element(By.ID, "example-modal-sizes-title-lg")
header_modal_window_text = header_modal_window.text

# Проверка
assert header_modal_window_text == "Thanks for submitting the form"
print("Test passed")

# Завершение таймера
end_time = time.time()

# Вычисление времени выполнения теста
time_for_test = end_time - start_time
print(f"Test execution time: {time_for_test:.2f} seconds")

# Закрытие браузера
driver.quit()
