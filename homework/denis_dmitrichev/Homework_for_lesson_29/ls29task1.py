from playwright.sync_api import Page, expect


def test_visible(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    button = page.locator(".a-button")
    button.click()
    result_box = page.locator(".result-text")
    expect(result_box).to_have_text('Ok')
