from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.product_locators import ProductLocators


class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.product_title = page.locator(
            ProductLocators.PRODUCT_TITLE
        )

        self.product_price = page.locator(
            ProductLocators.PRODUCT_PRICE
        )

        self.product_description = page.locator(
            ProductLocators.PRODUCT_DESCRIPTION
        )

        self.add_to_cart = page.get_by_role(
            "link",
            name="Add to cart",
            exact=True
        )

    def verify_product_name(self, product_name: str):

        expect(
            self.product_title
        ).to_have_text(product_name)

    def add_product_to_cart(self):

        expect(
            self.add_to_cart
        ).to_be_visible()

        self.add_to_cart.click()

    def get_product_name(self):

        return self.product_title.inner_text()

    def get_product_price(self):

        return self.product_price.inner_text()