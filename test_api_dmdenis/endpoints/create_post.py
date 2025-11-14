import requests
import allure
from test_api_dmdenis.endpoints.endpoint import EndPoint


class CreatePost(EndPoint):

    @allure.step('Create new post')
    def create_new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(self.url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response

    def check_response_name_is_correct(self, name):
        with allure.step(f'Check response name == {name}'):
            assert self.json["name"] == name, 'name не совпадает'

    def check_response_size_is_correct(self, size):
        with allure.step(f'Check response size == {size}'):
            assert self.json["data"]["size"] == size, 'size не совпадает'

    def check_response_color_is_correct(self, color):
        with allure.step(f'Check response color == {color}'):
            assert self.json["data"]["color"] == color, 'color не совпадает'

    def check_all(self, data):
        self.check_response_name_is_correct(data["name"])
        self.check_response_size_is_correct(data["data"]["size"])
        self.check_response_color_is_correct(data["data"]["color"])
