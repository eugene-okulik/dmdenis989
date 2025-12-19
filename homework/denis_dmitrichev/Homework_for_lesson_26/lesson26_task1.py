from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    chrome_driver.maximize_window()
    return chrome_driver


def test_new_window(driver):
    driver.get("http://testshop.qa-practice.com/")
    good = driver.find_element(By.LINK_TEXT, "Customizable Desk")
    ActionChains(driver).key_down(Keys.CONTROL).click(good).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    add_button = driver.find_element(By.ID, "add_to_cart")
    add_button.click()
    continue_button = driver.find_element(By.CSS_SELECTOR, '.btn-secondary')
    continue_button.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "sup.my_cart_quantity"),
            "1"
        )
    )
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    cart_button = driver.find_element(By.CSS_SELECTOR,
                                      '[class="o_navlink_background btn position-relative '
                                      'rounded-circle p-1 text-center text-reset"]')
    cart_button.click()
    good_in_card = driver.find_element(By.CSS_SELECTOR, '[class="d-inline align-top h6 fw-bold"]')
    assert good_in_card.text == "Customizable Desk (Steel, White)"


def test_add_to_cart(driver):
    driver.get("http://testshop.qa-practice.com/")
    goods = driver.find_elements(By.CSS_SELECTOR, '[itemprop="image"]')
    ActionChains(driver).move_to_element(goods[0]).perform()
    button = driver.find_element(By.CSS_SELECTOR, '[class="o_wsale_product_btn"]')
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="o_wsale_product_btn"]'))
    )
    button.click()
    good_in_cart = driver.find_element(By.CSS_SELECTOR, '[class="product-name product_display_name"]')
    assert good_in_cart.text == "[FURN_0096] Customizable Desk (Steel, White)"
