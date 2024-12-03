import os  # Импортируем модуль os для работы с файлами.
import time  # Импортируем модуль time для замеров времени и создания меток.
from playwright.sync_api import sync_playwright  # Импортируем Playwright для автоматизации браузера.

def test_form():
    # Синхронное использование Playwright.
    with sync_playwright() as playwright:
        try:
            # Лог: Запуск браузера.
            print("Запуск браузера...")
            browser = playwright.chromium.launch(headless=False)  # headless=False запускает браузер в графическом режиме.
            context = browser.new_context()
            page = context.new_page()

            # Замеряем время начала теста.
            start_time = time.time()

            # Лог: Открываем тестовую страницу.
            print("Открываем тестовую страницу...")
            page.goto("https://demoqa.com/automation-practice-form")

            # Заполнение формы
            print("Вводим данные в форму...")
            page.fill("#firstName", "Yana")
            page.fill("#lastName", "Nazarova")
            page.fill("#userEmail", "test@ya.ru")
            page.click("label[for='gender-radio-1']")
            page.fill("#userNumber", "89993452467")

            # Выбор даты
            print("Выбираем дату рождения...")
            page.click("#dateOfBirthInput")
            page.select_option(".react-datepicker__month-select", label="March")
            page.select_option(".react-datepicker__year-select", label="2005")
            page.click("div.react-datepicker__day--012")

            # Ввод предмета
            print("Вводим предмет...")
            page.fill("#subjectsInput", "History")
            page.press("#subjectsInput", "Enter")

            # Выбор хобби
            print("Выбираем хобби...")
            page.click("label[for='hobbies-checkbox-1']")  # Sports
            page.click("label[for='hobbies-checkbox-3']")  # Music

            # Загрузка файла
            print("Загружаем файл...")
            path_to_picture = os.path.abspath("../pictures/cat.jpg")
            page.set_input_files("#uploadPicture", path_to_picture)

            # Текущий адрес
            print("Вводим текущий адрес...")
            page.fill("#currentAddress", "ул. Линейная, 8")

            # Выбор штата и города
            print("Выбираем штат и город...")
            page.fill("#react-select-3-input", "Uttar Pradesh")
            page.press("#react-select-3-input", "Enter")
            page.fill("#react-select-4-input", "Agra")
            page.press("#react-select-4-input", "Enter")

            # Отправка формы
            print("Отправляем форму...")
            page.click("#submit")

            # Скриншот результата
            print("Делаем скриншот результата...")
            os.makedirs("../screens", exist_ok=True)  # Убедимся, что папка существует.
            time_mark = time.strftime("%Y-%m-%d_%H-%M-%S")
            name_screen = f'Screenshot_{time_mark}.png'
            path_to_file = os.path.abspath(f"screens/{name_screen}")
            page.screenshot(path=path_to_file)

            # Проверка результата
            print("Проверяем результат...")
            header_modal_window = page.text_content("#example-modal-sizes-title-lg")
            assert header_modal_window == "Thanks for submitting the form", "Заголовок не совпадает"

            # Замер времени
            end_time = time.time()
            full_time = end_time - start_time
            print(f"Тест завершен. Время выполнения: {full_time:.2f} секунд")
            print("Test passed")

        except Exception as e:
            print(f"Ошибка во время выполнения теста: {e}")
        finally:
            # Закрываем браузер.
            print("Закрываем браузер...")
            browser.close()


# Запускаем тест
if __name__ == "__main__":
    test_form()
