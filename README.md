# 🌐 Demoqa.com Test Automation

## 📝 Overview
This project provides comprehensive test automation for the Demoqa.com website using modern web testing technologies. It implements robust test scenarios with a focus on reliability, maintainability, and scalability.

## 🛠 Technologies Used
- **🐍 Python**: Core programming language for test script development
  - Provides powerful and readable test implementations
- **🎭 Playwright**: Advanced web browser automation framework
  - Enables cross-browser testing with high performance
- **🧪 Pytest**: Flexible testing framework
  - Supports detailed test discovery and execution

## 💻 Project Setup

### Prerequisites
- Python 3.8+

### Installation Steps

1. **Clone the Repository**
```powershell
git clone https://github.com/hello3world/demoqa.g it
cd demoqa
```

2. **Create Virtual Environment**

#### Windows:
```powershell
python -m venv venv
venv\scripts\activate
```

#### macOS and Linux:
```powershell
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```powershell
pip install -r requirements.txt
pip install pytest-playwright
playwright install
```

## 🚀 Running Tests

### Basic Test Execution
Run specific tests or entire test suites with flexible options:

```powershell
# Run a specific test file
pytest -v -s test_box.py

# Run with increased verbosity
pytest -v -s 

# Run specific test
pytest -v -s test_box.py::test_specific_scenario
```


### Reporting Options

#### HTML Report Generation
```powershell
pytest -v -s test_box.py --html=report.html
```

## 📊 Test Coverage

### Current Test Scenarios
- [ ] Text Box Interactions
- [ ] Checkbox Validations
- [ ] Radio Button Selections
- [ ] Button Clicks and Interactions

## 🔒 Best Practices
- Follow PEP 8 coding standards
- Implement comprehensive error handling
- Use meaningful test and variable names
- Maintain clear and concise test logic

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Project Link: [https://github.com/hello3world/demoqa](https://github.com/hello3world/demoqa)