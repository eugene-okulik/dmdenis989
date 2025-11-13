import requests
import allure

from test_api_dmdenis.endpoints.endpoint import EndPoint


class GetPost(EndPoint):
    @allure.step('Get post')
    def get_post(self, create_object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/{create_object_id}',
                                     headers=headers)
        return self.response
