import sys
import os
import tempfile
import pytest

# Ensure app is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.models import get_db_connection, init_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    db_fd, db_path = tempfile.mkstemp()
    app.config['DATABASE_PATH'] = db_path

    # Override DB connection
    def fake_get_db_connection():
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    import app.models
    app.models.get_db_connection = fake_get_db_connection

    with app.app_context():
        init_db()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Upload Document" in response.data
