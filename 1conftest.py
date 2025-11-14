from __future__ import annotations
import os
import io
import pytest
import allure
from typing import Any
from playwright.sync_api import Page

# Reuse shared fixtures
from tests._fixtures import page as _page_fixture, expect as _expect_fixture


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--pw-browser",
        action="store",
        default=os.getenv("BROWSER", "chromium"),
        help="Browser to use: chromium|firefox|webkit",
    )


@pytest.fixture(scope="function", autouse=True)
def _attach_artifacts_on_failure(request: pytest.FixtureRequest, page: Page):
    yield
    outcome = getattr(request.node, "rep_call", None)
    if outcome and outcome.failed:
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass
        try:
            html = page.content()
            allure.attach(html, name="page_source", attachment_type=allure.attachment_type.HTML)
        except Exception:
            pass
        try:
            test_name = request.node.name.replace("/", "_")
            trace_path = os.path.join("allure-results", f"trace_{test_name}.zip")
            if os.path.exists(trace_path):
                with open(trace_path, "rb") as f:
                    allure.attach(f.read(), name="trace.zip", attachment_type=allure.attachment_type.ZIP)
        except Exception:
            pass

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: Any):
    # yield to get the report object from pytest
    outcome = yield
    rep = outcome.get_result()
    # store report on the item for access in fixture above
    setattr(item, "rep_" + rep.when, rep)


# Expose shared fixtures
@pytest.fixture(scope="function")
def page(_page_fixture):  # type: ignore[override]
    return _page_fixture


@pytest.fixture(scope="function")
def expect(_expect_fixture):  # type: ignore[override]
    return _expect_fixture
