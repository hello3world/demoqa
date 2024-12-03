def test_web_table_add_and_search(browser):
    page = browser
    page.goto('https://demoqa.com/webtables')

    # Verify the presence of the "Add" button
    add_button = page.locator('button#addNewRecordButton')
    assert add_button.is_visible(), "Add button is not visible"

    # Click the "Add" button to open the form
    add_button.click()

    # Fill in the form to add a new row
    first_name = "John"
    last_name = "Doe"
    email = "john.doe@example.com"
    age = "30"
    salary = "$100,000"
    department = "HR"

    page.locator('input#firstName').fill(first_name)
    page.locator('input#lastName').fill(last_name)
    page.locator('input#userEmail').fill(email)
    page.locator('input#age').fill(age)
    page.locator('input#salary').fill(salary)
    page.locator('input#department').fill(department)

    # Submit the form to add the new row
    page.locator('button#submit').click()

    # Verify that the new row appears in the table
    new_row_locator = page.locator(".rt-tr-group:nth-child(4)")
    assert new_row_locator.is_visible(), f"New row for {first_name} {last_name} not found"

    # Verify the added row contains correct data

    assert first_name in new_row_locator.text_content()
    assert last_name in new_row_locator.text_content()
    assert email in new_row_locator.text_content()
    assert age in new_row_locator.text_content()
    assert salary in new_row_locator.text_content()
    assert department in new_row_locator.text_content()

    # Verify the search functionality
    search_field = page.locator('input#searchBox')
    search_value = "John"
    search_field.fill(search_value)

    # Wait for the table to filter results
    page.wait_for_selector(f'div.rt-tbody div:has-text("{first_name}")')

    # Verify that the correct row appears in the filtered table
    filtered_row_locator = page.locator(
        f'//div[@class="rt-tbody"]//div[div[contains(text(), "{first_name}")]]')
    assert filtered_row_locator.is_visible(), f"Row with search value '{search_value}' not found"

    # Ensure that no rows outside of the search result are visible
    all_rows = page.locator('div.rt-tbody div')
    all_rows_count = all_rows.count()
    assert all_rows_count == 1, f"Expected 1 row, but found {all_rows_count} rows"

