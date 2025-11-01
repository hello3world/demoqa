import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import pytest

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
