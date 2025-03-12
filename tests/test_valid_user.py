"""This is a test script to test flask application"""
import pytest
from app import app

@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_valid_user_content(client):
        """Test valid user route"""
        response = client.get("/user/jack")
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data["message"] == "Valid User"
