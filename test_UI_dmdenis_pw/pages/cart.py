from test_UI_dmdenis_pw.locators import cart_locators as cart_loc
from test_UI_dmdenis_pw.pages.tables import Table
from playwright.sync_api import expect


class CartPage(Table):
    page_url = '/shop/cart'

    def check_empty_message(self, text):
        empty_message = self.find(cart_loc.empty_message_loc)
        expect(empty_message).to_have_text(text)

    def clear(self, text):

        remove_button = self.find(cart_loc.remove_button_loc)
        remove_button.click()
        empty_message = self.find(cart_loc.empty_message_loc)
        expect(empty_message).to_have_text(text)

    def open_cart(self):
        cart_button = self.find(cart_loc.cart_button_loc)
        cart_button.first.click()

    def discount_code(self, code, text):
        discount_field = self.find(cart_loc.discount_field_loc)
        discount_field.fill(code)
        apply_button = self.find(cart_loc.apply_button_loc)
        apply_button.click()
        alert = self.find(cart_loc.alert_loc)
        expect(alert).to_have_text(text)

    def continue_purchase(self):
        continue_button = self.find(cart_loc.continue_button_loc)
        continue_button.click()
        expect(self.find(cart_loc.cart_quantity_loc).first).to_have_text('1')

    def check_price_in_basket(self, price):
        cart_price = self.find(cart_loc.cart_price_loc)
        expect(cart_price).to_have_text(price)
