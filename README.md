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

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

**Author**: QA Team  
**Version**: 1.0.0  
**Last Updated**: 2024