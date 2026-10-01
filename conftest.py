import logging

import pytest
from playwright.sync_api import sync_playwright

from config.settings import BASE_URL, HEADLESS

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage


logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser():
    """Create one Chromium browser for the complete test session."""

    logger.info("Starting Playwright Chromium browser")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=HEADLESS
        )

        yield browser

        logger.info("Closing Playwright browser")
        browser.close()


@pytest.fixture
def page(browser):
    """
    Create an isolated browser context and page for every test.
    """

    context = browser.new_context()
    page = context.new_page()

    logger.info("Opening application: %s", BASE_URL)

    page.goto(BASE_URL)

    yield page

    logger.info("Closing test browser context")
    context.close()


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def order_page(page):
    return OrderPage(page)