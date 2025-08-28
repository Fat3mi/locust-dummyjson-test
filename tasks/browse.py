from locust import TaskSet, task
import random

class BrowseTask(TaskSet):
    @task(3)
    def list_products(self):
        self.client.get("/products", name="/products")

    @task(2)
    def view_product(self):
        product_id = random.randint(1, 100)
        self.client.get(f"/products/{product_id}", name="/products/:id")

    @task(1)
    def search_product(self):
        query = random.choice(["phone", "laptop", "fragrance", "shoes"])
        self.client.get(f"/products/search?q={query}", name="/products/search")
