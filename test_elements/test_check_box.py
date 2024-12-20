def test_check_box(page):
    page = page
    page.goto('https://demoqa.com/checkbox')
    page.locator("//button[@title='Toggle']").click()
    page.locator("text=Desktop").click()  # Select the main checkbox

    assert page.locator("#tree-node-desktop").is_checked()
