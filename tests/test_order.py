from playwright.sync_api import expect


def test_place_order(
    home_page,
    product_page,
    cart_page,
    order_page
):

    product_name = "Samsung galaxy s6"

    # Select product
    home_page.select_product(product_name)

    # Verify product
    product_page.verify_product_name(product_name)

    # Add product to cart
    product_page.add_product_to_cart()

    # Open cart
    home_page.open_cart()

    # Verify product exists in cart
    expect(
        cart_page.cart_items
    ).to_contain_text(product_name)

    # Open order dialog
    cart_page.place_order()

    # Fill order details
    order_page.fill_order_details(
        name="Kishor",
        country="India",
        city="Hyderabad",
        card="4111111111111111",
        month="10",
        year="2030"
    )

    # Purchase
    order_page.purchase()

    # Verify successful order
    order_page.verify_order_success()