from playwright.sync_api import Page


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be openet for this page class')

    def find(self, locator):
        return self.page.locator(locator)

    # def find_all(self, locator: tuple):
    #     return self.driver.find_elements(*locator)

    def open_main_page(self):
        self.page.goto(self.base_url)

