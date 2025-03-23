import subprocess

# File with test paths
test_file = "utils/tests.txt"

# Read test paths from file
try:
    with open(test_file, "r") as f:
        test_paths = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print(f"Error: File {test_file} not found.")
    exit(1)

# Check if there are tests to run
if not test_paths:
    print("The tests.txt file is empty or contains no valid paths.")
    exit(1)

# Ensure Playwright is installed
try:
    subprocess.run(["playwright", "install"], check=True)
except subprocess.CalledProcessError:
    print("Error: Failed to install Playwright browsers.")
    exit(1)

# Form the pytest command
command = ["pytest", "--browser=chromium"] + test_paths

# Run the command
print(f"Running tests: {', '.join(test_paths)}")
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Test execution error: {e}")
    print("Check the test paths, dependencies, and logs for more details.")
    exit(1)
