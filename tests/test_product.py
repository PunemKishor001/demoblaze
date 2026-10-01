from playwright.sync_api import expect


def test_add_product_to_cart(
    home_page,
    product_page
):

    product_name = "Samsung galaxy s6"

    home_page.select_product(product_name)

    product_page.verify_product_name(product_name)

    product_page.add_product_to_cart()