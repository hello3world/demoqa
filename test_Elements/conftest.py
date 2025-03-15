# Import pytest to work with fixture
import pytest
# Import Playwright for browser automation
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(scope='function')
def page():
    # Initialize Playwright in synchronous mode and create a context to
    # interact with the browser
    with sync_playwright() as playwright:
        # The following three lines are responsible for launching the browser
        # and creating a context within it
        # Launch Chrome browser headless = True launches the browser without
        # graphical mode
        browser = playwright.chromium.launch(headless=True)
        # Create an isolated browser session
        context = browser.new_context()
        # Opens a new page (tab) in the browser
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
