from locust import TaskSet, task
import random

class CartTask(TaskSet):
    @task
    def view_cart(self):
        user_id = random.randint(1, 10)
        self.client.get(f"/carts/user/{user_id}", name="/carts/user/:id")

    @task
    def add_cart(self):
        product_id = random.randint(1, 100)
        payload = {"userId": 1, "products": [{"id": product_id, "quantity": 1}]}
        self.client.post("/carts/add", json=payload, name="/carts/add")
