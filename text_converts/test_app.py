import pytest
from flask_server import create_app  # Import the create_app function, not app

@pytest.fixture
def client():
    app = create_app()  # Call create_app to initialize the Flask app
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"web" in rv.data  # Adjust this based on actual content in web.html
