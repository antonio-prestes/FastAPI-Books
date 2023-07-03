import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestBooksAPI(unittest.TestCase):
    def test_root_endpoint(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World Books API"})

    def test_get_books_endpoint(self):
        response = client.get("/books")
        self.assertEqual(response.status_code, 200)

    def test_store_books_endpoint(self):
        book_data = {
            "titulo": "Livro de Teste",
            "autor": "Autor de Teste",
            "ano": 2023
        }
        response = client.post("/books", json=book_data)
        self.assertEqual(response.status_code, 200)