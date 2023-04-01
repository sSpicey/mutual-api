import json
import pytest
import app
from fastapi.testclient import TestClient
from app.controllers import ReverseController, MediumLengthController, MatrixController

client = TestClient(app)
