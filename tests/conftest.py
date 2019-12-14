import pytest
from demo_app.app import create_app


@pytest.fixture
def client():
    # Yields a test client.
    app = create_app()
    flask_client = app.test_client()
    yield flask_client
