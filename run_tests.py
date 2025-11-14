#!/usr/bin/env python3
"""
DemoQA Test Runner Script
"""
import subprocess
import sys
import argparse
from pathlib import Path

def run_command(command):
    """Executes a command and returns the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command execution error: {e}")
        print(f"stderr: {e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(description='DemoQA Test Runner')
    parser.add_argument('--category', choices=['elements', 'forms', 'all'], 
                       default='all', help='Test category to run')
    parser.add_argument('--headed', action='store_true', 
                       help='Run with visible browser')
    parser.add_argument('--allure', action='store_true', 
                       help='Generate Allure report')
    parser.add_argument('--pw-browser', choices=['chromium', 'firefox', 'webkit'],
                       default=None, help='Select browser for execution')
    
    args = parser.parse_args()
    
    # Basic pytest options
    pytest_options = ['-v', '--tb=short']
    
    if args.headed:
        pytest_options.append('--headed')
    
    if args.allure:
        pytest_options.append('--alluredir=allure-results')

    if args.pw_browser:
        pytest_options.append(f'--pw-browser={args.pw_browser}')
    
    # Determine test path
    if args.category == 'all':
        test_path = 'tests'
    else:
        test_path = f'tests/{args.category}'
    
    # Check if test directory exists
    if not Path(test_path).exists():
        print(f"Directory {test_path} not found!")
        sys.exit(1)
    
    # Form command
    command = f"pytest {' '.join(pytest_options)} {test_path}"
    print(f"Running command: {command}")
    
    # Run tests
    success = run_command(command)
    
    if success and args.allure:
        print("\nGenerating Allure report...")
        run_command("allure serve allure-results")
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main() 