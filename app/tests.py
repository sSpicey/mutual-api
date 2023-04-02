import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestReverseIntegers:
    path = "/reverse_integer"

    def test_reverse_positive_number(self):
        response = client.get(f"{self.path}/12345")
        assert response.status_code == 200
        assert response.json() == {"reverse integer": 54321}

    def test_reverse_negative_number(self):
        response = client.get(f"{self.path}/-12345")
        assert response.status_code == 200
        assert response.json() == {"reverse integer": -54321}

    def test_reverse_zero(self):
        response = client.get(f"{self.path}/0")
        assert response.status_code == 200
        assert response.json() == {"reverse integer": 0}

    def test_reverse_single_digit_number(self):
        response = client.get(f"{self.path}/5")
        assert response.status_code == 200
        assert response.json() == {"reverse integer": 5}

    def test_reverse_multiple_zeros(self):
        response = client.get(f"{self.path}/000")
        assert response.status_code == 200
        assert response.json() == {"reverse integer": 0}

class TestAverageWordsLength:
    path = "/average_length"

    def test_equal_words_length(self):
        response = client.post(self.path, json={"phrase": "hello world"})
        assert response.status_code == 200
        assert response.json() == {"average length": 5.0}
    
    def test_standard_phrase(self):
        response = client.post(self.path, json={"phrase": "Hi all, my name is Tom...I am originally from Brazil."})
        assert response.status_code == 200
        assert response.json()["average length"] == pytest.approx(3.54, abs=0.01)

    def test_empty_phrase(self):
        response = client.post(self.path, json={"phrase": ""})
        assert response.status_code == 200
        assert response.json() == {"average length": 0}

class TestMatchedAndMismatchedWords:
    path = "/matched_mismatched_words"

    def test_matched_and_mismatched(self):
        response = client.post(self.path, json={
            "phrase1": "We are really pleased to meet you in our city",
            "phrase2": "The city was hit by a really heavy storm"
        })

        assert response.status_code == 200

        response = response.json()
        assert set(response["mismatched words"]) == set(["We", "to", "heavy", "The", "storm", "meet", "hit", "pleased", "are", "by", "a", "in", "was", "you", "our"])
        assert set(response["matched words"]) == set(["really", "city"])

    def test_identical_phrases(self):
        response = client.post(self.path, json={
            "phrase1": "Hello world",
            "phrase2": "Hello world"
        })

        assert response.status_code == 200

        response = response.json()
        assert set(response["mismatched words"]) == set()
        assert set(response["matched words"]) == set(["Hello", "world"])

    def test_empty_phrase(self):
        response = client.post(self.path, json={
            "phrase1": "",
            "phrase2": ""
        })

        assert response.status_code == 200

        response = response.json()
        assert set(response["mismatched words"]) == set()
        assert set(response["matched words"]) == set()
