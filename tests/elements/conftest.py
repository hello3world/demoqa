import sys
from pathlib import Path
import pytest
import allure
from playwright.sync_api import sync_playwright

# Ensure repository root is importable (so 'pages' package resolves)
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

    
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.fixture(autouse=True)
def _allure_test_step(request: pytest.FixtureRequest):
    with allure.step(f"Test: {request.node.name}"):
        yield


@pytest.fixture(autouse=True)
def _attach_artifacts_on_failure(request: pytest.FixtureRequest, page):
    yield
    outcome = getattr(request.node, "rep_call", None)
    if outcome and outcome.failed:
        try:
            allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass
        try:
            html = page.content()
            allure.attach(html, name="page_source", attachment_type=allure.attachment_type.HTML)
        except Exception:
            pass
