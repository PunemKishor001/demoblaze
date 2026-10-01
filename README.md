# DemoBlaze Web Automation Framework

## Overview

This project is a UI automation framework developed for the DemoBlaze Product Store assessment.

The framework uses **Python, Playwright and Pytest** and follows the **Page Object Model (POM)** design pattern.

The objective is to provide reliable, maintainable and reusable automated tests covering high-value web application scenarios.

## Technology Stack

- Python 3.13
- Playwright
- Pytest
- Pytest-Rerunfailures
- Pytest-HTML
- Allure Pytest
- Page Object Model
- JSON-based test data

## Application Under Test

DemoBlaze Product Store:

https://www.demoblaze.com/

## Framework Structure

```text
demoblaze_playwright/
│
├── config/
│   └── settings.py
│
├── locators/
│   ├── home_locators.py
│   ├── login_locators.py
│   ├── product_locators.py
│   ├── cart_locators.py
│   ├── order_locators.py
│   └── signup_locators.py
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── order_page.py
│
├── tests/
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_signup.py
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_order.py
│
├── test_data/
│   ├── users.json
│   ├── products.json
│   └── order_data.json
│
├── utils/
│   ├── config_reader.py
│   ├── helpers.py
│   └── logger.py
│
├── reports/
├── screenshots/
├── traces/
├── logs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Design Approach

### Page Object Model

Each application page has a dedicated Page Object.

For example:

```text
test_product.py
       |
       v
ProductPage
       |
       v
product_locators.py
       |
       v
Playwright
```

Tests contain business scenarios while Page Objects contain UI interaction logic.

### Locator Separation

Locators are maintained separately from Page Objects.

This provides:

- Reusability
- Easier maintenance
- Reduced duplication
- Cleaner Page Objects
- Easier locator updates when the UI changes

### Test Isolation

A new Playwright browser context is created for each test.

This prevents state and cookies from one test affecting another test.

## Automated Scenarios

### Login

- Valid login
- Invalid login

### Product

- Select Samsung Galaxy S6
- Verify product details
- Add product to cart

### Cart

- Verify selected product appears in cart

### Order

- Open Place Order dialog
- Enter customer information
- Submit order
- Verify successful purchase

## Synchronization Strategy

The framework uses Playwright's built-in synchronization mechanisms and web-first assertions.

Examples:

```python
expect(locator).to_be_visible()
```

and:

```python
expect(locator).to_have_text(expected_text)
```

Fixed waits such as `wait_for_timeout()` are intentionally avoided because they introduce unnecessary timing dependencies.

## Retry Strategy

The framework is configured to retry failed tests three times.

Configuration:

```ini
--reruns 3
```

This helps handle transient failures while still reporting a test as failed after the configured retry attempts.

## Reporting

HTML reports are generated automatically:

```text
reports/report.html
```

The framework is also configured to retain diagnostic artifacts when failures occur.

### Failure Diagnostics

- Screenshot on failure
- Playwright trace on failure
- Video on failure

These artifacts help investigate intermittent and environment-specific failures.

## Running the Tests

### Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Install Chromium

```powershell
python -m playwright install chromium
```

### Run all tests

```powershell
python -m pytest
```

### Run in headed mode

```powershell
python -m pytest --headed
```

### Run a specific test file

```powershell
python -m pytest tests/test_product.py
```

### Run with detailed output

```powershell
python -m pytest -v
```

## Test Result

The current implementation validates the complete automated suite successfully.

Example:

```text
5 passed
```

## Coding Practices

The framework follows these practices:

- Page Object Model
- Separate locator modules
- Reusable page methods
- Meaningful assertions
- Playwright auto-waiting
- Independent tests
- Test data separation
- Three retries for failed tests
- Failure diagnostics
- Minimal useful comments
- Avoidance of unnecessary hard waits

## Interview Discussion Points

The implementation can be explained through the following design decisions:

1. Why Page Object Model was selected
2. Why locators are separated from Page Objects
3. How Playwright synchronization works
4. Why fixed waits are avoided
5. How test isolation is achieved
6. How retries are configured
7. How failures are diagnosed
8. How test data is maintained
9. How the framework can be extended for additional pages and scenarios
10. How the framework could be integrated into CI/CD

## Future Enhancements

Potential future improvements include:

- CI/CD integration
- Parallel test execution
- Environment-specific configuration
- Allure reporting
- API-based test data setup
- Additional negative and boundary scenarios
- Cross-browser execution
- AI-assisted test generation and failure analysis