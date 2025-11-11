import allure
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.elements.elements_page import ElementsPage
from pages.elements.links_page import LinksPage
import pytest


def _go_to_links(page) -> LinksPage:
    home = HomePage(page)
    home.open("https://demoqa.com/")
    home.page_verify()

    elements = ElementsPage(page)
    home.click_elements_button()
    elements.page_verify()
    elements.click_links()

    links = LinksPage(page)
    links.page_verify()
    return links


@allure.title("Links: new tab link opens correct URL")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("which", ["simple", "dynamic"]) 
def test_links_new_tab(page, which: str):
    links = _go_to_links(page)
    link_href, opened_url = links.open_new_tab_link(which)
    assert link_href == opened_url, f"The link is broken or URL incorrect. Expected: {link_href}. Actual: {opened_url}"


@allure.title("Links: API response text contains expected status word")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "locator_name",
    ["CREATED", "NO_CONTENT", "MOVED", "BAD_REQUEST", "UNAUTHORIZED", "FORBIDDEN", "NOT_FOUND"],
)
def test_links_api_status_text(page, locator_name: str):
    links = _go_to_links(page)
    response_text = links.click_api_link(locator_name)
    expected_word = locator_name.replace("_", " ").title()
    assert expected_word in response_text, (
        f"The expected word is missing from the response field. Expected: {expected_word}. Actual: {response_text}"
    )
