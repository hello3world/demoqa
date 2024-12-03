def test_links(browser):
    page = browser
    page.goto('https://demoqa.com/radio-button')
    page.click("text=Links")
    page.click("#simpleLink")  # Click on the "Home" link

    # Ensure a new tab was opened with the correct URL
    page.wait_for_timeout(2000)  # Wait for tab load
    assert page.url == "https://demoqa.com/"