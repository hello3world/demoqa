
# 1. Test Text Box
def test_text_box(browser):
    page = browser
    page.goto('https://demoqa.com/text-box')
    page.locator('#userName').fill('Ivan Petrov')
    page.locator('#userEmail').fill('ivan_petrov@gmail.com')
    page.locator('#currentAddress').fill('Minsk City, Main Street, 1-1')
    page.locator('#permanentAddress').fill('Minsk City, Secondary Street, 1-2')
    page.locator('#submit').click()

    # Validate results
    assert 'Ivan Petrov' in page.locator('#name').text_content()
    assert 'ivan_petrov@gmail.com' in page.locator('#email').text_content()
    assert 'Minsk City, Main Street, 1-1' in page.locator(
        'p#currentAddress').text_content()
    assert 'Minsk City, Secondary Street, 1-2' in page.locator(
        'p#permanentAddress').text_content()
