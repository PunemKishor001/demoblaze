from playwright.sync_api import expect

from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator(
            LoginLocators.USERNAME
        )

        self.password = page.locator(
            LoginLocators.PASSWORD
        )

        self.login_button = page.locator(
            LoginLocators.LOGIN_BUTTON
        )

        self.welcome_user = page.locator(
            LoginLocators.WELCOME_USER
        )

    def login(
        self,
        username: str,
        password: str
    ):

        self.username.fill(username)
        self.password.fill(password)

        self.login_button.click()

    def verify_logged_in(self, username: str):

        expect(
            self.welcome_user
        ).to_contain_text(username)