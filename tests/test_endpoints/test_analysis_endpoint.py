from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

# Initialize TestClient with the FastAPI app
client = TestClient(app)

def test_analysis_endpoint_basic():
    # Send GET request to analysis endpoint
    response = client.get("/analysis")

    # Assert that the response status code is 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Extract JSON data from the response
    data = response.json()

    # Ensure the response contains the expected structure and data types
    assert isinstance(data["user_with_most_posts"], str), "user_with_most_posts should be a string"
    assert isinstance(data["average_title_length"], float), "average_title_length should be a float"
    assert isinstance(data["common_words"], list), "common_words should be a list"
    assert len(data["common_words"]) > 0, "common_words list should not be empty"


# Test case for error handling in the analysis endpoint
@patch('app.routers.analysis.fetch_users_posts')
def test_analysis_endpoint_error(mock_fetch):
    # Mock the fetch_users_posts function to raise an exception
    mock_fetch.side_effect = Exception("Failed to fetch data")
    # Send GET request to analysis endpoint
    response = client.get("/analysis")
    # Assert that the response status code is 500
    assert response.status_code == 500
    # Assert the JSON response content for the error message
    assert response.json() == {"message": "Failed to fetch data from the external API."}
