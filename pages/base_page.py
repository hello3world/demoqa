from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def page_verify(self, locator):
        expect(self.page.locator(locator)).to_visible(timeout=10)