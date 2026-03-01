from test_UI_dmdenis_pw.pages.base_page import BasePage
from test_UI_dmdenis_pw.locators import tables_locators as loc, cart_locators as card_loc
from playwright.sync_api import expect


class Table(BasePage):
    page_url = '/shop/category/desks-1'

    def check_found_good(self, price_value, good_name):
        goods_names = self.find(loc.goods_name_loc)
        expect(goods_names).to_have_text(good_name)
        price = self.find(loc.price_loc)
        expect(price).to_have_text(price_value)

    def click_search_button(self):
        search_button = self.find(loc.search_button_loc)
        search_button.first.click()
        self.page.wait_for_timeout(10000)

    def send_query_in_search_field(self, query):
        search_field = self.find(loc.search_loc)
        search_field.nth(1).click()
        search_field.nth(1).fill(query)

    def sort_by_name(self, good1_name):
        goods_names = self.find(loc.goods_name_loc)
        expect(goods_names.first).to_have_text(good1_name)
        dropdown_element = self.find(loc.dropdown_element_loc)
        dropdown_element.click()
        alphabet_filtration = self.find(loc.alphabet_filtration_loc)
        alphabet_filtration.click()

    def check_good_name(self, good2_name):
        goods_names = self.find(loc.goods_name_loc)
        expect(goods_names.first).to_have_text(good2_name)

    def put_into_basket(self, good_name):
        goods = self.find(loc.goods_loc)
        goods.first.hover()
        button = self.find(loc.add_basket_button_loc)
        button.first.click()
        good_in_card = self.find(card_loc.card_good_name_loc)
        expect(good_in_card.first).to_have_text(good_name)
