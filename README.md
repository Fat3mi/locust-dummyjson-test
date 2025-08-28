# Locust DummyJSON Load Testing

This project demonstrates **real-world load testing** using [Locust](https://locust.io) and the public [DummyJSON API](https://dummyjson.com).  
It simulates e-commerce user behavior: browsing products, managing carts, and logging in.

---

## Features
- **Product Browsing**: list products, view details, search queries.
- **Cart Actions**: view a user’s cart, add products to cart.
- **User Flows**: fetch users, view profiles, perform login.
- **Data-Driven Randomness**: randomized user IDs, product IDs, and queries for realism.
- **Custom Load Shape**: simulate ramp-up, steady load, and ramp-down (peak hours).
- **CI/CD Ready**: includes a GitHub Actions workflow that runs smoke tests automatically.

## Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
***Caution : strongly recommended to create & activate a virtual environment before installing dependencies.***

### 2. Run Locust in Web Mode
```bash
locust -f locustfile.py
```
Then open 👉 http://localhost:8089 to control the test.

### 3. Run Headless Mode
```bash
locust -f locustfile.py --headless -u 50 -r 5 -t 2m
```
- `-u 50` → 50 concurrent users  
- `-r 5`  → spawn rate 5 users/sec  
- `-t 2m` → test duration: 2 minutes  


## Endpoints Covered
- **Products**: `/products`, `/products/:id`, `/products/search`
- **Carts**: `/carts/user/:id`, `/carts/add`
- **Users**: `/users`, `/users/:id`, `/auth/login`


## Continuous Integration
A **GitHub Actions workflow** runs smoke tests (`5 users, 30s`) on every push to ensure scripts always work.


## 🔗 Resources
- [Locust Documentation](https://docs.locust.io/)
- [DummyJSON API](https://dummyjson.com)