import pytest
import io
from flask import jsonify
from flask_server import create_app  # Assuming your Flask app is in app.py
from unittest.mock import patch

# Pytest fixture for setting up the Flask test client
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True  # Set the app to testing mode
    with app.test_client() as client:
        yield client

# Test the /test_my_ai route
def test_test_my_ai_success(client):
    # Mock chat_with_together_api function to avoid external API calls
    with patch('AI_Stuff.AI_MAIN.chat_with_together_api') as mock_chat:
        # Define the mock return value
        mock_chat.return_value = ("This is a test response from the AI.", [])
        
        # Send a POST request with a test query
        response = client.post('/test_my_ai', json={"query": "Tell me a fun fact"})
        
        # Verify the response status code
        assert response.status_code == 200
        
        # Verify the response JSON
        data = response.get_json()
        assert data["result"] == "This is a test response from the AI."
        assert data["history"][0]["content"] == "Tell me a fun fact"

# Test the /test_my_ai route when no query is provided
def test_test_my_ai_default_query(client):
    with patch('AI_Stuff.AI_MAIN.chat_with_together_api') as mock_chat:
        # Mock the AI response
        mock_chat.return_value = ("This is a test response from the AI.", [])

        # Send a POST request without a query (should use default)
        response = client.post('/test_my_ai', json={})
        
        # Verify the response status code
        assert response.status_code == 200
        
        # Verify the response content
        data = response.get_json()
        assert data["history"][0]["content"] == "Write a one sentence quote"  # Default query
