import requests
import allure

from test_api_dmdenis.endpoints.endpoint import EndPoint


class DeletePost(EndPoint):
    @allure.step('Delete post')
    def delete_post(self, create_object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{create_object_id}',
                                        headers=headers)
        return self.response
