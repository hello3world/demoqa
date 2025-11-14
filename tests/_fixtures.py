from __future__ import annotations
import os
import pytest
from typing import Generator
from playwright.sync_api import (
    Playwright,
    expect as pw_expect,
    Page,
    Browser,
    BrowserContext,
)
from config import BROWSER_CONFIG, VIEWPORT


def _launch_browser(playwright: Playwright, name: str) -> Browser:
    name = name.lower()
    if name == "chromium":
        return playwright.chromium.launch(**BROWSER_CONFIG)
    if name == "firefox":
        return playwright.firefox.launch(**BROWSER_CONFIG)
    if name == "webkit":
        return playwright.webkit.launch(**BROWSER_CONFIG)
    raise ValueError(f"Unsupported browser: {name}")


@pytest.fixture(scope="function")
def page(
    request: pytest.FixtureRequest, playwright: Playwright
) -> Generator[Page, None, None]:
    """Provide an isolated Playwright Page per test with tracing and video enabled.
    Uses the `playwright` fixture provided by pytest-playwright to avoid starting sync_playwright
    inside an active asyncio event loop.
    Browser is selected via --browser option or BROWSER env var (default: chromium).
    """
    browser_name = request.config.getoption("--pw-browser", default=None) or os.getenv(
        "BROWSER", "chromium"
    )

    browser = _launch_browser(playwright, browser_name)
    os.makedirs("videos", exist_ok=True)
    context: BrowserContext = browser.new_context(
        viewport=VIEWPORT,
        accept_downloads=True,
        record_video_dir="videos",
    )
    # Start tracing for debug
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    pg = context.new_page()
    try:
        yield pg
    finally:
        # Stop tracing and save per-test trace file
        test_name = request.node.name.replace("/", "_")
        traces_dir = os.path.join("allure-results")
        os.makedirs(traces_dir, exist_ok=True)
        trace_path = os.path.join(traces_dir, f"trace_{test_name}.zip")
        try:
            context.tracing.stop(path=trace_path)
        except Exception:
            pass
        try:
            pg.close()
        except Exception:
            pass
        try:
            context.close()
        except Exception:
            pass
        try:
            browser.close()
        except Exception:
            pass


@pytest.fixture(scope="function")
def expect() -> Generator:
    """Expose Playwright expect assertions."""
    yield pw_expect
