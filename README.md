# DemoQA Playwright Tests

Automated testing project for DemoQA website using Playwright and Python.

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo>
cd demoqa
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Run Tests

```bash
python run_tests.py
```

## 📁 Project Structure

```
demoqa/
├── 📄 config.py                    # Project configuration
├── 📄 logger_config.py             # Logging configuration
├── 📄 run_tests.py                 # Test runner script
├── 📄 requirements.txt             # Python dependencies
├── 📄 pytest.ini                  # pytest configuration
├── 📄 .gitignore                  # Git exclusions
├── 📄 README.md                   # Project documentation
│
├── 📁 pages/                      # Page Object Model
│   ├── 📄 __init__.py
│   ├── 📄 base_page.py            # Base page class
│   ├── 📁 elements/               # Element pages
│   └── 📁 forms/                  # Form pages
│
├── 📁 models/                     # Pydantic data models (ported from Selenium)
│   └── 📄 models.py
│
├── 📁 utils/                      # Helpers & data generators (ported from Selenium)
│   ├── 📄 generator.py
│   └── 📄 routes.py
│
├── 📁 tests/                      # Tests
│   ├── 📁 elements/               # Element tests
│   └── 📁 forms/                  # Form tests
│
├── 📁 screenshots/                # Error screenshots
├── 📁 logs/                       # Execution logs
├── 📁 allure-results/             # Allure results
└── 📁 venv/                       # Virtual environment
```

## 🧪 Running Tests

### Basic Run

```bash
python run_tests.py
```

### Run Specific Category

```bash
python run_tests.py --category elements
python run_tests.py --category forms
```

### With Allure Report

```bash
python run_tests.py --allure
```

### With Visible Browser

```bash
python run_tests.py --headed
```

### Direct pytest Run

```bash
pytest tests/                    # All tests
pytest tests/elements/           # Elements only
pytest tests/forms/              # Forms only
pytest -n auto                   # Parallel run (requires pytest-xdist)
```

## ⚙️ Configuration

### config.py

- `BASE_URL`: Base website URL
- `BROWSER_TIMEOUT`: Element timeout
- `SCREENSHOT_TIMEOUT`: Screenshot timeout
- `BROWSER_CONFIG`: Browser settings

### pytest.ini

- Automatic Allure report generation
- Test discovery settings
- Default configuration

## 📊 Reports and Logs

### Allure Reports

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

Artifacts captured on failure (attached automatically):

- Screenshot (PNG)
- Page HTML
- Playwright trace ZIP
- Video per test (saved under videos/), where enabled in fixtures

### Logs

- Automatically created in `logs/` directory
- Include information about all actions
- Format: `demoqa_YYYYMMDD_HHMMSS.log`

### Screenshots

- Automatically created on errors
- Saved in `screenshots/` directory
- Filename: `error_timestamp.png`

## 🏗️ Architecture

### Page Object Model

- `BasePage`: Base class with common methods
- Specialized pages for each section
- Encapsulation of element interaction logic

### pytest Fixtures

- `page`: Browser page creation and management
- `expect`: Convenient access to Playwright assertions
- Automatic resource cleanup
- Per-test isolated contexts with tracing and video, suitable for parallelization

### Logging

- Centralized configuration
- Logs to files and console
- Various detail levels

## 🔧 Development

### Adding New Page

1. Create class in `pages/`
2. Inherit from `BasePage`
3. Implement specific methods

### Adding New Tests

1. Create `test_*.py` file in appropriate directory
2. Use fixtures from `conftest.py`
3. Follow naming convention

### Logging Configuration

- Change level in `logger_config.py`
- Add new handlers if needed

## 🚨 Troubleshooting

### "playwright not found" Error

```bash
pip install playwright
playwright install
```

### Browser Issues

```bash
playwright install --force
```

### Import Errors

```bash
pip install -r requirements.txt
```

## 📚 Additional Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)

## 🐳 Docker

### Build image

```bash
docker build -t demoqa-playwright .
```

### Run tests (default chromium, headless)

```bash
docker run --rm -v %CD%/allure-results:/app/allure-results demoqa-playwright
# Linux/macOS: docker run --rm -v "$(pwd)/allure-results:/app/allure-results" demoqa-playwright
```

### Select browser

```bash
docker run --rm -e BROWSER=firefox -v %CD%/allure-results:/app/allure-results demoqa-playwright
```

Artifacts will be available in `allure-results` (including trace zips on failure). Screenshots/videos/logs are saved under respective folders.

## 🌐 Browser selection

- CLI via runner:

```bash
python run_tests.py --pw-browser chromium
python run_tests.py --pw-browser firefox
python run_tests.py --pw-browser webkit
```

- Pytest directly:

```bash
pytest --pw-browser=firefox
```

- Environment variable:

```bash
set BROWSER=firefox  # Windows
export BROWSER=firefox  # Linux/macOS
```

For CI headless runs set `HEADLESS=true` (default). For local headed runs pass `--headed` to the runner or `pytest`.

Note: Custom CLI flag is `--pw-browser` (Chromium/Firefox/WebKit). The legacy `--browser` flag is not used to avoid conflicts.

This repository is fully Playwright-based. Legacy Selenium tests were migrated or superseded, and reusable data/models were ported into `utils/` and `models/`.

## 🏁 Getting Started for CI

- GitHub Actions workflow provided in `.github/workflows/tests.yml` runs a matrix on Chromium and Firefox.
- Artifacts: `allure-results` uploaded for each browser.
- Local dry-run of CI command:

```bash
pytest -v --pw-browser=chromium --alluredir=allure-results
pytest -v --pw-browser=firefox  --alluredir=allure-results
```

Set `HEADLESS=true` for CI environments (default), and avoid forcing `--headed`.

## 🧰 Common Commands

| Purpose | Command |
|---|---|
| Run all tests (Chromium) | `pytest -v --alluredir=allure-results` |
| Run Firefox | `pytest -v --pw-browser=firefox --alluredir=allure-results` |
| Run WebKit | `pytest -v --pw-browser=webkit --alluredir=allure-results` |
| Run in parallel | `pytest -n auto` |
| Run Elements only | `pytest tests/elements -v` |
| Serve Allure report | `allure serve allure-results` |
| Runner (Chromium) | `python run_tests.py --category elements` |
| Runner (Firefox) | `python run_tests.py --category elements --pw-browser firefox` |

## 📏 Conventions

- Naming
  - Tests: `test_<area>_<behavior>_<expectation>.py` (e.g., `test_links_new_tab_opens_correct_url.py`).
  - Test functions: clear scenario intent (e.g., `test_web_tables_add_person`).
  - Page objects: `<Area>Page` in `pages/<area>/`.
- Locators
  - Prefer Playwright-recommended APIs: `get_by_role`, `get_by_label`, `get_by_text`, `get_by_test_id`.
  - Avoid brittle XPath/CSS when a semantic locator exists.
  - Reuse locators by storing them in page objects.
- Assertions
  - Use web-first assertions: `expect(locator).to_be_visible()`, `to_have_text()`, etc.
  - Avoid hard-coded sleeps; rely on auto-wait and `expect`.
- Fixtures & Isolation
  - Use shared `page` and `expect` fixtures; each test gets an isolated context.
  - Keep tests parallel-safe (no shared mutable state).
- Allure
  - Add `@allure.title` and `@allure.severity` to important tests.
  - Artifacts (screenshot, HTML, trace) are auto-attached on failure.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request