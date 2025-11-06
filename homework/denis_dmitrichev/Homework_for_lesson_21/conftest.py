import requests
import pytest
import allure


@pytest.fixture(scope='session')
def print_start_completed():
    print("\nStart testing")
    yield
    print("Testing completed")


@pytest.fixture(scope='function')
def print_before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


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
