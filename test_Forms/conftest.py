import pytest
# Импортируем Playwright для автоматизации браузера.
from playwright.sync_api import sync_playwright

@pytest.fixture(scope='function')
def page():
    # Синхронное использование Playwright.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # headless=False запускает браузер в графическом режиме.
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()