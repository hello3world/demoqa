import time  # Импортируем модуль time для добавления задержек в скрипт.

from selenium.webdriver import Keys  # Импортируем Keys для имитации действий клавиатуры.
from selenium.webdriver.common.by import By  # Импортируем By для поиска элементов на странице.

from selenium.webdriver.support.select import Select


def test_form(driver):
    # Открываем веб-страницу с формой.
    driver.get("https://demoqa.com/automation-practice-form")
    # Разворачиваем окно браузера на весь экран для удобства.
    # driver.maximize_window()
    start_time = time.time()
    # Находим поле ввода "Имя" по его ID и вводим значение.
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Yana")

    # Находим поле ввода "Фамилия" по его ID и вводим значение.
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Nazarova")

    # Находим поле ввода "Email" по его ID и вводим значение.
    user_email = driver.find_element(By.ID, "userEmail")
    user_email.send_keys("test@ya.ru")

    # Находим опцию "Мужской" (Male) по тексту в метке (label), прокручиваем к ней и кликаем.
    gender_male = driver.find_element(By.XPATH, "//label[text()='Male']")
    driver.execute_script("arguments[0].scrollIntoView(true);", gender_male)
    gender_male.click()

    # Находим поле ввода "Номер телефона" по его ID и вводим значение.
    user_number = driver.find_element(By.ID, "userNumber")
    user_number.send_keys("89993452467")

    date_of_birth = driver.find_element(By.ID, "dateOfBirthInput")
    date_of_birth.click()
    month_select = Select(driver.find_element(By.CLASS_NAME, "react"
                                                             "-datepicker__month"
                                                             "-select"))
    month_select.select_by_visible_text('March')
    year_select = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year_select.select_by_visible_text("2005")
    day = driver.find_element(By.XPATH, '//div[text() = 12]')
    day.click()

    # Находим поле "Предметы" по его ID, вводим значение и выбираем его с помощью клавиши RETURN.
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("History")
    subjects.send_keys(Keys.RETURN)

    # Находим опцию "Спорт" (Sports) по тексту в метке, прокручиваем к ней и кликаем.
    hobby_sports = driver.find_element(By.XPATH, "//label[text()='Sports']")
    driver.execute_script("arguments[0].scrollIntoView(true);", hobby_sports)
    hobby_sports.click()

    # Находим опцию "Музыка" (Music) по тексту в метке, прокручиваем к ней и кликаем.
    hobby_music = driver.find_element(By.XPATH, "//label[text()='Music']")
    driver.execute_script("arguments[0].scrollIntoView(true);", hobby_music)
    hobby_music.click()

    # Загружаем изображение, находя элемент загрузки файла по ID и отправляя ему путь к файлу.
    import os  # Импортируем модуль os для получения абсолютного пути к файлу.
    picture = driver.find_element(By.ID, "uploadPicture")
    path_to_picture = os.path.abspath("pictures/cat.jpg")  # Укажите правильный путь к изображению.
    picture.send_keys(path_to_picture)

    # Находим поле ввода "Текущий адрес" по его ID и вводим значение.
    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("ул. Линейная, 8")  # Вводим адрес на русском.

    # Находим поле "Штат" (State) в выпадающем списке, вводим значение и выбираем его.
    state = driver.find_element(By.ID, "react-select-3-input")
    state.send_keys("Uttar Pradesh")
    state.send_keys(Keys.RETURN)

    # Находим поле "Город" (City) в выпадающем списке, вводим значение и выбираем его.
    city = driver.find_element(By.ID, "react-select-4-input")
    city.send_keys("Agra")
    city.send_keys(Keys.RETURN)

    # Прокручиваем к кнопке "Отправить" (Submit), делаем ее видимой и кликаем.
    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)
    submit.click()

    # создание имени скрина
    time_mark = time.strftime("%Y-%m-%d_%H-%M-%S")
    name_screen = 'Screenshot_' + time_mark + ".png"
    # здесь появляется форма - подтверждение
    path_to_file = os.path.abspath(f"screens/{name_screen}")
    driver.save_screenshot(path_to_file)

    # Находим заголовок модального окна, которое появляется после отправки формы.
    header_modal_window = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    header_modal_window_text = header_modal_window.text

    assert header_modal_window.text == "Thanks for submitting the form"
    end_time = time.time()
    full_time = end_time - start_time
    print(f"Время выполнения теста {full_time:.2f}")
    print("Test passed")
