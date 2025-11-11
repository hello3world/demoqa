from __future__ import annotations
import os
import time
from pathlib import Path
from typing import Optional, Union

from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str, wait_until: str = "domcontentloaded") -> None:
        self.page.goto(url, wait_until=wait_until)

    def wait_for_url(
        self, url_or_pattern: Union[str, re.Pattern], timeout: int = 10000
    ) -> None:
        self.page.wait_for_url(url_or_pattern, timeout=timeout)

    def expect_visible(
        self, target: Union[str, Locator], timeout: int = 10000
    ) -> Locator:
        locator = self.page.locator(target) if isinstance(target, str) else target
        expect(locator).to_be_visible(timeout=timeout)
        return locator

    def expect_hidden(
        self, target: Union[str, Locator], timeout: int = 10000
    ) -> Locator:
        locator = self.page.locator(target) if isinstance(target, str) else target
        expect(locator).to_be_hidden(timeout=timeout)
        return locator

    def get_by_test_id(self, test_id: str) -> Locator:
        return self.page.get_by_test_id(test_id)

    def screenshot(self, path: Optional[str] = None, full_page: bool = True) -> str:
        if path is None:
            ts = time.strftime("%Y%m%d_%H%M%S")
            path = f"screenshots/{ts}.png"
        Path(os.path.dirname(path) or ".").mkdir(parents=True, exist_ok=True)
        self.page.screenshot(path=path, full_page=full_page)
        return path

    def take_screenshot_on_error(self, message: str = "") -> str:
        ts = time.strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{ts}.png"
        return self.screenshot(filename, full_page=True)
