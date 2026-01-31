from playwright.sync_api import Page, expect


def test_login_invalid_user(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    form_button = page.get_by_role('link', name='Form Authentication')
    form_button.click()
    username = page.get_by_role('textbox', name='Username')
    username.fill('username')
    password = page.get_by_role('textbox', name='Password')
    password.fill('password')
    button = page.get_by_role('button')
    button.click()
    alert = page.get_by_text('Your username is invalid!')
    expect(alert).to_be_visible()
