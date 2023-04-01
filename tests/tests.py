import json
import pytest
from fastapi.testclient import TestClient
from app.controllers import ReverseController, MediumLengthController, MatrixController

client = TestClient(app)
