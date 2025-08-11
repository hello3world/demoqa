# Import pytest to work with fixture
import pytest
# Import Playwright for browser automation
from playwright.sync_api import sync_playwright, expect
from config import BROWSER_CONFIG, VIEWPORT

@pytest.fixture(scope='function')
def page():
    """Fixture for creating browser page"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(**BROWSER_CONFIG)
        context = browser.new_context(
            viewport=VIEWPORT,
            accept_downloads=True
        )
        page = context.new_page()
        
        yield page
        
        # Clean up resources
        page.close()
        context.close()
        browser.close()

@pytest.fixture(scope='function')
def expect(page):
    """Fixture for convenient expect usage"""
    return expect
