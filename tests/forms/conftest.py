# Import pytest to work with fixture
import pytest
# Import Playwright for browser automation
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    # Initialize Playwright in synchronous mode and create a context to
    # interact with the browser
    with sync_playwright() as p:
        # The following three lines are responsible for launching the browser
        # and creating a context within it
        # Launch Chrome browser headless = False launches the browser in
        # graphical mode
        browser = p.chromium.launch(headless=False)
        # Create an isolated browser session
        context = browser.new_context()
        # Opens a new page (tab) in the browser
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
