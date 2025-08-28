from locust import TaskSet, task
import random

class UserTask(TaskSet):
    @task(2)
    def list_users(self):
        self.client.get("/users", name="/users")

    @task(1)
    def single_user(self):
        user_id = random.randint(1, 30)
        self.client.get(f"/users/{user_id}", name="/users/:id")

    @task(1)
    def login(self):
        # DummyJSON fake login (always same user/password)
        payload = {"username": "chloem", "password": "chloempass"}
        self.client.post("/auth/login", json=payload, name="/auth/login")
