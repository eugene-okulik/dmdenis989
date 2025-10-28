import requests


def clear(created_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{created_id}')


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
    return response.json()['id']


def create_object():
    body = {
            "name": "New_object",
            "data": {
                     "color": "blue",
                     "size": "small"
            }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()["name"] == "New_object", 'name не совпадает'
    assert response.json()["data"]["size"] == "small", 'size не совпадает'
    assert response.json()["data"]["color"] == "blue", 'color не совпадает'
    print(response.json())


def change_object():
    obj_id = create_object_id()
    body = {
            "name": "New_object2",
            "data": {
                     "color": "green",
                     "size": "big"
            }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{obj_id}',
                            json=body, headers=headers)
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()["name"] == "New_object2", 'name не изменился'
    assert response.json()["data"]["color"] == "green", 'color не изменился'
    assert response.json()["data"]["size"] == "big", 'size не изменился'
    print(response.json())
    clear(obj_id)


def patch_object():
    obj_id = create_object_id()
    body = {
            "name": "My_object",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{obj_id}',
                              json=body, headers=headers)
    assert response.status_code == 200, 'Код ответа не 200'
    assert response.json()["name"] == 'My_object', 'name не изменился'
    assert response.json()["data"]["color"] == "blue", 'color изменился'
    assert response.json()["data"]["size"] == "small", 'size изменился'
    print(response.json())
    clear(obj_id)


def delete_object():
    obj_id = create_object_id()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    print(response.text)
    assert response.status_code == 200


create_object()
change_object()
patch_object()
delete_object()
