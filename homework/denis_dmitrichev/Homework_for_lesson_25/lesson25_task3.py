from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(20)
    chrome_driver.maximize_window()
    return chrome_driver


def test_choose_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    language_selector = driver.find_element(By.CSS_SELECTOR, '[id="id_choose_language"]')
    select_field = Select(language_selector)
    select_field.select_by_value('2')
    submit_button = driver.find_element(By.CSS_SELECTOR, '[id="submit-id-submit"]')
    submit_button.click()
    result_text = driver.find_element(By.CSS_SELECTOR, '[id="result-text"]')
    assert result_text.text == "Ruby"


def test_waiting_for_button(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    show_text = driver.find_element(By.CSS_SELECTOR, '[id="finish"]')
    assert show_text.text == "Hello World!"


def test_waiting_for_button2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    text_locator = (By.CSS_SELECTOR, '#finish')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(text_locator)
    )
    show_text = driver.find_element(By.CSS_SELECTOR, '#finish')
    assert show_text.text == "Hello World!"
