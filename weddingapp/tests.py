from django.test import TestCase
from .models import *
from rest_framework import status


class TestEndpoints(TestCase):
    fixtures = ["products_fixture.json"]

    def get(self, url):
        return self.client.get(url)

    def test_api_root(self):
        self.assertEqual(self.get("/api/").status_code, status.HTTP_200_OK)

    def test_products(self):
        self.assertEqual(self.get("/api/products/").status_code, status.HTTP_200_OK)

    def test_products_detail(self):
        response = self.get("/api/products/1/")
        json_data = response.json()
        product = Product.objects.get(pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product.stock, json_data["stock"])

    def test_products_search(self):
        response = self.get("/api/products/?search=5")
        json_data = response.json()
        product = Product.objects.get(id=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(product.brand, json_data["results"][0]["brand"])

        list_response = self.get("/api/products/")
        list_data = list_response.json()
        self.assertLess(json_data["count"], list_data["count"])

    def test_products_post(self):
        response = self.client.post(
            "/api/products/",
            {"name": "Usha Mango Wood Lamp Base", "brand": "NKUKU"},
        )
        json_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        instance_response = self.get(f"/api/products/{json_data['id']}/")
        instance_data = instance_response.json()
        self.assertEqual(json_data["brand"], instance_data["brand"])

    def test_products_post_without_req_params(self):
        response = self.client.post(
            "/api/products/", {"brand": "NKUKU"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_products_put(self):
        instance_response = self.get("/api/products/2/")
        instance_json_data = instance_response.json()

        payload = {
            "name": "Faux Tortoiseshell Lamp",
            "brand": "OKA",
            "price": 179.99,
            "stock": 2
        }
        response = self.client.put(
            "/api/products/2/", payload, content_type="application/json"
        )
        json_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(instance_json_data["name"], json_data["name"])

    def test_products_delete(self):
        response = self.client.delete("/api/products/6/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
