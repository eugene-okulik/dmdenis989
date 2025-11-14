import pytest


TEST_DATA = [
    {"name": "New_object_1", "data": {"color": "blue", "size": "small"}},
    {"name": "New_object_2", "data": {"color": "red", "size": "medium"}},
    {"name": "New_object_3", "data": {"color": "green", "size": "large"}}
]


@pytest.mark.parametrize("data", TEST_DATA)
def test_create_object(create_post_endpoint, data):
    create_post_endpoint.create_new_post(body=data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_all(data)


def test_put_a_post(create_put_endpoint, create_object_id):
    body = {
        "name": "New_object2",
        "data": {
            "color": "green",
            "size": "big"
        }
    }
    create_put_endpoint.make_changes_in_post(create_object_id, body=body)
    create_put_endpoint.check_that_status_is_200()
    create_put_endpoint.check_all(body)


def test_patch_a_post(create_patch_endpoint, create_object_id):
    body = {
        "name": "My_object2",
    }
    create_patch_endpoint.make_patch_in_post(create_object_id, body=body)
    create_patch_endpoint.check_that_status_is_200()
    create_patch_endpoint.check_all(body)


def test_delete_a_post(delete_post_endpoint, create_object_id):
    delete_post_endpoint.delete_post(create_object_id)
    delete_post_endpoint.check_that_status_is_200()


def test_get_post(get_endpoint, create_object_id):
    get_endpoint.get_post(create_object_id)
    get_endpoint.check_that_status_is_200()
