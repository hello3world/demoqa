# Base image with Playwright dependencies and browsers
FROM mcr.microsoft.com/playwright/python:v1.46.0-jammy

# Set workdir
WORKDIR /app

# Copy only dependency files first for layer caching
COPY requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps

# Copy project files
COPY . /app

# Environment defaults for CI
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    BROWSER=chromium \
    PYTEST_ADDOPTS="-v --alluredir=allure-results"

# Create result/artifact dirs
RUN mkdir -p allure-results screenshots videos logs

# Default command runs tests; override with docker run args if needed
CMD ["pytest", "tests"]
