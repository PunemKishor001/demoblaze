from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def refresh(self):
        self.page.reload()

    def go_back(self):
        self.page.go_back()

    def get_current_url(self):
        return self.page.url