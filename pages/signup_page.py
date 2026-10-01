from pages.base_page import BasePage
from locators.signup_locators import SignupLocators


class SignupPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator(
            SignupLocators.USERNAME
        )

        self.password = page.locator(
            SignupLocators.PASSWORD
        )

        self.signup_button = page.locator(
            SignupLocators.SIGNUP_BUTTON
        )

    def signup(
        self,
        username: str,
        password: str
    ):

        self.username.fill(username)
        self.password.fill(password)

        self.signup_button.click()