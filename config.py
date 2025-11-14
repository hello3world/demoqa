"""
DemoQA Project Configuration
"""
import os

# Basic settings
BASE_URL = "https://demoqa.com"
BROWSER_TIMEOUT = 10000
SCREENSHOT_TIMEOUT = 60000

# Browser settings
BROWSER_CONFIG = {
    "headless": os.getenv("HEADLESS", "true").lower() == "true",
    "args": [
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-web-security",
        "--disable-features=VizDisplayCompositor"
    ]
}

# Viewport settings
VIEWPORT = {
    "width": 1920,
    "height": 1080
}

# Paths
SCREENSHOT_DIR = "screenshots"
ALLURE_RESULTS_DIR = "allure-results"

# Create directories on import
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)