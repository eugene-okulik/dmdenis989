from playwright.sync_api import Page, expect, Route
import re
import json


def test_change_response(page: Page):
    new_title = 'яблокофон 17 про'

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = new_title
        body["body"]["digitalMat"][0]["familyTypes"][0]["tabTitle"] = new_title
        body["body"]["digitalMat"][0]["familyTypes"][0]["exploreLink"]["text"] = f'Исследуйте {new_title} дальше'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('digitalmat&fae=true'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    button = page.locator('[data-autom="DigitalMat-1"]')
    button.click()
    label = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(label).to_have_text(new_title)
    tab = page.get_by_role('radio').nth(0)
    expect(tab).to_have_text(new_title)
    link = page.locator('[data-autom="DigitalMat-explorelink-0-0"]')
    expect(link).to_have_text(f'Исследуйте {new_title} дальше')
