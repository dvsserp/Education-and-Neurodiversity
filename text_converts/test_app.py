import pytest
from flask_server import create_app  # Import the create_app function

# Fixture to create a test client
@pytest.fixture
def client():
    """Fixture to set up a Flask test client."""
    # Create the app using the refactored create_app function
    app = create_app()
    app.config['TESTING'] = True  # Enable testing mode (disables CSRF, provides better error output)
    
    # Use Flask's test_client to simulate requests
    with app.test_client() as client:
        yield client  # This allows the test client to be used in the tests

# Test the home route
def test_home(client):
    """Test the home route '/'."""
    rv = client.get('/')  # Simulate a GET request to the home route
    assert rv.status_code == 200  # Check if the response is OK (status 200)
    assert b"web" in rv.data  # Check if the response contains content from web.html

# Test the chat route
def test_chat(client):
    """Test the chat route '/chat'."""
    rv = client.get('/chat')  # Simulate a GET request to the chat route
    assert rv.status_code == 200  # Ensure the route returns a successful status code
    assert b"chat" in rv.data  # Check if the response contains content from chat.html

# Test the geometry route
def test_geometry(client):
    """Test the geometry route '/geometry'."""
    rv = client.get('/geometry')  # Simulate a GET request to the geometry route
    assert rv.status_code == 200  # Ensure the route returns a successful status code
    assert b"geometry" in rv.data  # Adjust this based on the actual content in geometry.html

# Test the computer science route
def test_compsci(client):
    """Test the computer science route '/compsci'."""
    rv = client.get('/compsci')  # Simulate a GET request to the compsci route
    assert rv.status_code == 200  # Ensure the route returns a successful status code
    assert b"compsci" in rv.data  # Adjust this based on the actual content in compsci.html

# Test the astronomy route
def test_astro(client):
    """Test the astronomy route '/astro'."""
    rv = client.get('/astro')  # Simulate a GET request to the astro route
    assert rv.status_code == 200  # Ensure the route returns a successful status code
    assert b"astro" in rv.data  # Adjust this based on the actual content in astro.html
