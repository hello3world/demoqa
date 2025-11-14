import sys
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

# Ensure repository root is importable (so 'pages' package resolves)
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Reuse shared fixtures from tests._fixtures to avoid duplicate Playwright startup
from tests._fixtures import page as _page_fixture


@pytest.fixture
def page(_page_fixture):  # type: ignore[override]
    return _page_fixture
