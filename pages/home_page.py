from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.home_locators import HomeLocators


class HomePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_link = page.locator(
            HomeLocators.LOGIN_LINK
        )

        self.signup_link = page.locator(
            HomeLocators.SIGNUP_LINK
        )

        self.cart_link = page.locator(
            HomeLocators.CART_LINK
        )

    def open_login(self):
        self.login_link.click()

    def open_signup(self):
        self.signup_link.click()

    def open_cart(self):
        self.cart_link.click()

    def select_product(self, product_name: str):

        product = self.page.get_by_role(
            "link",
            name=product_name,
            exact=True
        )

        expect(product).to_be_visible()

        product.click()

    def select_category(self, category: str):

        self.page.get_by_text(
            category,
            exact=True
        ).click()