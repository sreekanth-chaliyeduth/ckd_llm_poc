import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
import subprocess
import time
import os
from playwright.sync_api import Page

@pytest.fixture(scope="session", autouse=True)
def start_server():
    """Start the FastAPI server before running tests"""
    server = subprocess.Popen(
        ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(2)
    yield
    server.terminate()
    server.wait()

@pytest.fixture
def mock_llm_client():
    """Fixture to mock LLM client responses"""
    with patch('backend.llm_client.LLMClient') as mock:
        mock_instance = Mock()
        mock_instance.predict.return_value = {
            "prediction": 0.85,
            "confidence": 0.85,
            "explanation": "Based on the provided data, there is a high risk of CKD progression. The patient shows multiple risk factors including age, albumin levels, and presence of anemia."
        }
        mock.return_value = mock_instance
        yield mock_instance

@pytest.fixture
def test_client(mock_llm_client):
    """Fixture to create a test client with mocked dependencies"""
    from backend.main import app
    return TestClient(app)

@pytest.fixture
def browser_context_args(browser_context_args):
    """Configure browser context for tests"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
        "ignore_https_errors": True,
    } 