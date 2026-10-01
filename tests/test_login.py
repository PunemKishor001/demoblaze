import json

from playwright.sync_api import expect


with open(
    "test_data/users.json",
    encoding="utf-8"
) as file:

    USERS = json.load(file)


def test_valid_login(
    page,
    home_page,
    login_page
):

    home_page.open_login()

    login_page.login(
        USERS["valid_user"]["username"],
        USERS["valid_user"]["password"]
    )

    login_page.verify_logged_in(
        USERS["valid_user"]["username"]
    )


def test_invalid_login(
    page,
    home_page,
    login_page
):

    home_page.open_login()

    page.once(
        "dialog",
        lambda dialog: dialog.accept()
    )

    login_page.login(
        USERS["invalid_user"]["username"],
        USERS["invalid_user"]["password"]
    )