def test_(browser):
    page = browser
    page.goto('https://demoqa.com/radio-button')

    # Select "Yes"
    # page.click("label[for='yesRadio']")
    # assert page.text_content(".mt-3 > .text-success") == "Yes"

    # Select "Impressive"
    page.click("label[for='impressiveRadio']")
    assert page.text_content(".mt-3 > .text-success") == "Impressive"

    # Select "No"
    try:
        page.click('label[for="noRadio"]')
        assert page.text_content(".mt-3 > .text-success") == "No"
    except Exception as error:
        print("Error exception = ", error)

    no_radio_button = page.locator('label[for="noRadio"]')
    if no_radio_button.is_enabled():
        no_radio_button.click()
        assert page.text_content(".mt-3") == "You have selected No"
    else:
        print("The 'No' radio button is disabled and cannot be selected.")
