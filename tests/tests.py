import json
import pytest
import app
from fastapi.testclient import TestClient
from app.controllers import ReverseController, MediumLengthController, MatrixController

client = TestClient(app)

class TestReverseController:
    def test_reverse_positive_number(self):
        response = client.get("/reverse?number=12345")
        assert response.status_code == 200
        assert response.json() == {"number": 54321}

    def test_reverse_negative_number(self):
        response = client.get("/reverse?number=-12345")
        assert response.status_code == 200
        assert response.json() == {"number": -54321}

    def test_reverse_zero(self):
        response = client.get("/reverse?number=0")
        assert response.status_code == 200
        assert response.json() == {"number": 0}


class TestMediumLengthController:
    def test_medium_length(self):
        response = client.post("/medium-length", json={"phrase": "hello world"})
        assert response.status_code == 200
        assert response.json() == {"medium_length": 5.0}


class TestMatrixController:
    def test_matrix(self):
        response = client.post("/matrix", json={
            "phrase1": "hello world",
            "phrase2": "goodbye world"
        })
        
        assert response.status_code == 200
        assert response.json() == {
            "common_words": ["world"],
            "different_words": [["hello"], ["goodbye"]]
        }
