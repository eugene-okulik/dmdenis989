from locust import task, HttpUser
import random


class ApiUser(HttpUser):
    obj_id = None
    temp_ids = []

    def on_start(self):
        body = {
            "name": "Test_object",
            "data": {
                "color": "blue",
                "size": "small"
            }
        }
        response = self.client.post('/object', json=body)
        self.obj_id = response.json()['id']

        for _ in range(5):
            self.create_temp_object()

    def create_temp_object(self):
        """Создает временный объект для удаления"""
        body = {
            "name": f"Temp_{random.randint(1000, 9999)}",
            "data": {
                "color": "green",
                "size": "medium"
            }
        }
        response = self.client.post('/object', json=body)
        self.temp_ids.append(response.json()['id'])

    @task(3)
    def get_object(self):
        self.client.get(f'/object/{self.obj_id}')

    @task(2)
    def update_object(self):
        body = {
            "name": f"Updated_{random.randint(1, 100)}",
            "data": {
                "color": "red",
                "size": "large"
            }
        }
        self.client.put(f'/object/{self.obj_id}', json=body)

    @task(2)
    def patch_object(self):
        body = {
            "name": f"Patched_{random.randint(1, 100)}",
        }
        self.client.patch(f'/object/{self.obj_id}', json=body)

    @task(1)  # редко создаем новые
    def create_object(self):
        colors = ["red", "blue", "green", "yellow"]
        sizes = ["small", "medium", "large"]
        body = {
            "name": f"New_{random.randint(100, 999)}",
            "data": {
                "color": random.choice(colors),
                "size": random.choice(sizes)
            }
        }
        self.client.post('/object', json=body)

    @task(1)
    def delete_object(self):
        if self.temp_ids:
            obj_id = self.temp_ids.pop()
            self.client.delete(f'/object/{obj_id}', name="DELETE /object")
            self.create_temp_object()
