from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.name = page.locator(
            OrderLocators.NAME
        )

        self.country = page.locator(
            OrderLocators.COUNTRY
        )

        self.city = page.locator(
            OrderLocators.CITY
        )

        self.card = page.locator(
            OrderLocators.CARD
        )

        self.month = page.locator(
            OrderLocators.MONTH
        )

        self.year = page.locator(
            OrderLocators.YEAR
        )

        self.purchase_button = page.get_by_role(
            "button",
            name="Purchase",
            exact=True
        )

    def fill_order_details(
        self,
        name: str,
        country: str,
        city: str,
        card: str,
        month: str,
        year: str
    ):

        self.name.fill(name)
        self.country.fill(country)
        self.city.fill(city)
        self.card.fill(card)
        self.month.fill(month)
        self.year.fill(year)

    def purchase(self):

        expect(
            self.purchase_button
        ).to_be_visible()

        expect(
            self.purchase_button
        ).to_be_enabled()

        self.purchase_button.click()

    def verify_order_success(self):

        expect(
            self.page.get_by_text(
                "Thank you for your purchase!"
            )
        ).to_be_visible()