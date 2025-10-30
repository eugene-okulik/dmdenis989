import requests
import pytest


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
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')


def test_get_object(create_object_id, print_start_completed, print_before_after):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{create_object_id}')
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()['id'] == create_object_id, 'Вернулся не тот ID'


@pytest.mark.parametrize('name,color,size', [
    ("New_object_1", "blue", "small"),
    ("New_object_2", "red", "medium"),
    ("New_object_3", "green", "large")
])
def test_create_object(print_before_after, name, color, size):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()["name"] == name, 'name не совпадает'
    assert response.json()["data"]["size"] == size, 'size не совпадает'
    assert response.json()["data"]["color"] == color, 'color не совпадает'


def test_change_object(create_object_id, print_before_after):
    body = {
        "name": "New_object2",
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{create_object_id}',
                            json=body, headers=headers)
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()["name"] == "New_object2", 'name не изменился'
    assert response.json()["data"]["color"] == "green", 'color не изменился'
    assert response.json()["data"]["size"] == "big", 'size не изменился'


@pytest.mark.medium
def test_patch_object(create_object_id, print_before_after):
    body = {
        "name": "My_object",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{create_object_id}',
                              json=body, headers=headers)
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()["name"] == 'My_object', 'name не изменился'
    assert response.json()["data"]["color"] == "blue", 'color изменился'
    assert response.json()["data"]["size"] == "small", 'size изменился'


@pytest.mark.critical
def test_delete_object(create_object_id, print_before_after):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{create_object_id}')
    assert response.status_code == 200
