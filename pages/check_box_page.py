from pages.base_page import BasePage
from playwright.sync_api import expect

class CheckBoxPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def page_verify(self):
        expect(self.page.locator("h1").filter(has_text="Check Box")).to_be_visible()

    def expand_all_nodes(self):
        self.page.locator("button[aria-label='Toggle']").click()

    def select_desktop(self):
        self.page.locator("label[for='tree-node-desktop']").click()

    def select_documents(self):
        self.page.locator("label[for='tree-node-documents']").click()

    def select_downloads(self):
        self.page.locator("label[for='tree-node-downloads']").click()

    def selected_result_text(self) -> str:
        return self.page.locator("#result").inner_text().lower()
