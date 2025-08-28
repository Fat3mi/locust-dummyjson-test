from locust import HttpUser, between, LoadTestShape
from tasks.browse import BrowseTask
from tasks.cart import CartTask
from tasks.user import UserTask

class DummyJsonUser(HttpUser):
    host = "https://dummyjson.com"
    wait_time = between(1, 3)
    tasks = [BrowseTask, CartTask, UserTask]

class PeakLoadShape(LoadTestShape):
    stages = [
        {"duration": 60, "users": 20, "spawn_rate": 2},  
        {"duration": 180, "users": 100, "spawn_rate": 5},
        {"duration": 240, "users": 0, "spawn_rate": 10},
    ]

    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None
