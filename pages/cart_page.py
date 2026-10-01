from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.cart_items = page.locator(
            CartLocators.CART_ITEMS
        )

        self.total_price = page.locator(
            CartLocators.TOTAL_PRICE
        )

        self.place_order_button = page.locator(
            CartLocators.PLACE_ORDER
        )

    def get_cart_items(self):
        return self.cart_items

    def get_total_price(self):
        return self.total_price.inner_text()

    def place_order(self):
        self.place_order_button.click()

    def delete_product(self, product_row):
        product_row.locator(
            CartLocators.DELETE_BUTTON
        ).click()