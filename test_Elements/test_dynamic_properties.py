def test_dynamic_properties(browser):
    page = browser
    page.goto('https://demoqa.com/radio-button')

    # Select "Yes"
    page.click("label[for='yesRadio']")
    assert page.text_content(".mt-3") == "You have selected Yes"

    # Select "Impressive"
    page.click("label[for='impressiveRadio']")
    assert page.text_content(".mt-3") == "You have selected Impressive"

