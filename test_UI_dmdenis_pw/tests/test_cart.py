good1_name = "[FURN_0096] Customizable Desk (Steel, White)"


def test_check_empty_massage(cart):
    cart.open_page()
    cart.check_empty_message("Your cart is empty!")


def test_clear_cart(cart):
    cart.open_main_page()
    cart.put_into_basket(good1_name)
    cart.continue_purchase()
    cart.open_cart()
    cart.clear("Your cart is empty!")


def test_check_invalid_promo(cart):
    cart.open_main_page()
    cart.put_into_basket(good1_name)
    cart.continue_purchase()
    cart.open_cart()
    cart.discount_code('sdgdfghdfshdfhdf', "This promo code is not available.")
