# Project name: Demoqa.com Test Automation

## Overview

## Technologies Used
- *Python*: Programming language used for writing test scripts
- *Playwright*: Tool for automating web browsers and interacting with the pages.
- *Pytest*: Testing framework for running and managing tests
- *Page Object Model (POM)*: A design pattern used to model web paes as objects for better maintainability

## Installation
1. Clone the repository:
2. Create virtual environment
Windows:
python -m venv venv
Activate the virtual environment
venv\scripts\activate
macOS and Linux
python3 -m venv venv
Activate
source venv/bin/activate
3. Install the required dependencies:
pip install -r requirements.txt

 ## Running Tests
Choose needed test and complete command
pytest -v test_box.py
Generate HTM Reports
pytest --html=report.html

