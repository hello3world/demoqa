from pages.base_page import BasePage
from playwright.sync_api import expect


class LinksPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_verify(self):
        expect(self.page.get_by_role("heading", name="Links")).to_be_visible()

    def open(self):
        self.page.goto("https://demoqa.com/links")
        self.page_verify()

    def open_new_tab_link(self, which: str = "simple") -> tuple[str, str]:
        if which == "simple":
            link = self.page.get_by_role("link", name="Home")
        elif which == "dynamic":
            link = self.page.locator("#dynamicLink")
        else:
            raise ValueError("which must be 'simple' or 'dynamic'")
        href = link.get_attribute("href")
        with self.page.context.expect_page() as new_page_info:
            link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return href.rstrip('/'), new_page.url.rstrip('/')

    def click_api_link(self, locator_name: str) -> str:
        mapping = {
            "CREATED": "#created",
            "NO_CONTENT": "#no-content",
            "MOVED": "#moved",
            "BAD_REQUEST": "#bad-request",
            "UNAUTHORIZED": "#unauthorized",
            "FORBIDDEN": "#forbidden",
            "NOT_FOUND": "#invalid-url",
        }
        selector = mapping.get(locator_name)
        if not selector:
            raise ValueError(f"Unknown locator_name: {locator_name}")
        self.page.locator(selector).click()
        resp = self.page.locator("#linkResponse")
        expect(resp).to_be_visible()
        return resp.inner_text()
