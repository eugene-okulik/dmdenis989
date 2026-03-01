def test_terms(goods):
    goods.open_page()
    goods.term_and_conditions("STANDARD TERMS AND CONDITIONS OF SALE")


def test_check_price(goods):
    goods.open_page()
    goods.check_price('295.00')


def test_add_to_cart(goods, cart):
    goods.open_page()
    goods.add_some_goods_into_card()
    goods.open_good_in_card()
    goods.check_card_header("Order overview")
    cart.check_price_in_basket('590.00')
