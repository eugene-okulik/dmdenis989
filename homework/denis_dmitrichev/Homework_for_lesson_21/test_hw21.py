import requests
import pytest
import allure


@allure.id('234')
@allure.title('Получение готового объекта')
@allure.feature('Posts')
@allure.story('Get posts')
def test_get_object(create_object_id, print_start_completed, print_before_after):
    with allure.step(f'Run get request for {create_object_id}'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{create_object_id}')
    with allure.step('Check response for request'):
        assert response.status_code == 200, 'Код ответа не 200'
    with allure.step(f'Check ID is {create_object_id}'):
        assert response.json()['id'] == create_object_id, 'Вернулся не тот ID'


@allure.id('235')
@allure.title('Создание нового объекта')
@allure.feature('Posts')
@allure.story('Change posts')
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
    with allure.step(f'Run post request for new object {name}'):
        response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    with allure.step('Run check status code'):
        assert response.status_code == 200, 'Код ответа не 200'
    with allure.step(f'Check response name == {name}'):
        assert response.json()["name"] == name, 'name не совпадает'
    with allure.step(f'Check response size == {size}'):
        assert response.json()["data"]["size"] == size, 'size не совпадает'
    with allure.step(f'Check response data == {color}'):
        assert response.json()["data"]["color"] == color, 'color не совпадает'


@allure.id('236')
@allure.title('Изменение объекта')
@allure.feature('Posts')
@allure.story('Change posts')
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
    with allure.step('Run check status code'):
        assert response.status_code == 200, 'Код ответа не 200'
    with allure.step('Check response name == New_object2'):
        assert response.json()["name"] == "New_object2", 'name не изменился'
    with allure.step('Check response color == green'):
        assert response.json()["data"]["color"] == "green", 'color не изменился'
    with allure.step('Check response size == big'):
        assert response.json()["data"]["size"] == "big", 'size не изменился'


@allure.id('237')
@allure.title('Изменение части объекта')
@allure.feature('Posts')
@allure.story('Change posts')
@pytest.mark.medium
def test_patch_object(create_object_id, print_before_after):
    body = {
        "name": "My_object",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{create_object_id}',
                              json=body, headers=headers)
    with allure.step('Run check status code'):
        assert response.status_code == 201, 'Код ответа не 200'
    with allure.step('Check response name == My_object'):
        assert response.json()["name"] == 'My_object', 'name не изменился'
    with allure.step('Check response color == blue'):
        assert response.json()["data"]["color"] == "blue", 'color изменился'
    with allure.step('Check response size == small'):
        assert response.json()["data"]["size"] == "small", 'size изменился'


@allure.id('238')
@allure.title('Удаление объекта')
@allure.feature('Example')
@allure.story('Delete Posts')
@pytest.mark.critical
def test_delete_object(create_object_id, print_before_after):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{create_object_id}')
    with allure.step('Run check status code'):
        assert response.status_code == 200, 'Код ответа не 200'
