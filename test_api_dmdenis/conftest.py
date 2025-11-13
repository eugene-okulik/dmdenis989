import pytest
import allure
import requests

from test_api_dmdenis.endpoints.create_post import CreatePost
from test_api_dmdenis.endpoints.put_post import PutPost
from test_api_dmdenis.endpoints.patch_post import CreatePatch
from test_api_dmdenis.endpoints.delete_post import DeletePost
from test_api_dmdenis.endpoints.get_post import GetPost


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def create_put_endpoint():
    return PutPost()


@pytest.fixture()
def delete_post_endpoint():
    return DeletePost()


@pytest.fixture()
def get_endpoint():
    return GetPost()


@pytest.fixture()
def create_patch_endpoint():
    return CreatePatch()


@pytest.fixture()
def create_object_id():
    body = {
        "name": "New_object",
        "data": {
            "color": "blue",
            "size": "small"
        }
    }
    headers = {'Content-Type': 'application/json'}
    with allure.step('Create new object'):
        response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    obj_id = response.json()['id']
    yield obj_id
    with allure.step('Delete object'):
        requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
