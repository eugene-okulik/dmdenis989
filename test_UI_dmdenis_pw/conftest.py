import pytest
from playwright.sync_api import Page
from test_UI_dmdenis_pw.pages.cart import CartPage
from test_UI_dmdenis_pw.pages.tables import Table
from test_UI_dmdenis_pw.pages.good import Good


@pytest.fixture()
def table(page: Page):
    return Table(page)


@pytest.fixture()
def goods(page: Page):
    return Good(page)


@pytest.fixture()
def cart(page: Page):
    return CartPage(page)
