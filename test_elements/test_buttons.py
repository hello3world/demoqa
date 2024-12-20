def test_buttons(page):
    page = page
    page.goto('https://demoqa.com/buttons')

    # Double click button
    page.dblclick("#doubleClickBtn")
    assert page.text_content("#doubleClickMessage") == "You have done a double click"

    # Right click button
    page.click("#rightClickBtn", button="right")
    assert page.text_content("#rightClickMessage") == "You have done a right click"

    # Single click button
    page.click("//button[text()='Click Me']")
    assert page.text_content("#dynamicClickMessage") == "You have done a dynamic click"
