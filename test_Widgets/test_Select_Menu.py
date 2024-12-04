def test_select_option(page):
    # Откройте страницу, содержащую select элемент
    page = page
    page.goto("https://demoqa.com/select-menu")

    # Выбор опции из выпадающего списка
    page.select_option("#oldSelectMenu", "Yellow")  # выбираем значение по value

    # Проверка выбранного значения
    selected_value = page.locator("#oldSelectMenu").input_value()  # Получение выбранного значения
    assert selected_value == "3", f"Ожидалось 'Yellow', но получено '{selected_value}'"
