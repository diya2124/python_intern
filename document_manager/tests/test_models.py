import sys
import os
import tempfile
import sqlite3
import pytest

# Ensure app is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import insert_document, get_all_documents, init_db

@pytest.fixture
def test_db(monkeypatch):
    # Use a temporary file as the database
    db_fd, db_path = tempfile.mkstemp()
    monkeypatch.setenv("FLASK_ENV", "testing")

    def fake_get_db_connection():
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    # Patch get_db_connection in app.models
    import app.models
    app.models.get_db_connection = fake_get_db_connection

    # Initialize temp DB schema
    init_db()

    yield db_path  # test runs here

    os.close(db_fd)
    os.unlink(db_path)

def test_insert_and_get_document(test_db):
    insert_document("sample.pdf", "test", "Sample content", "/path/to/sample.pdf")
    docs = get_all_documents()
    assert len(docs) == 1
    assert docs[0]["filename"] == "sample.pdf"
    assert docs[0]["category"] == "test"
    assert docs[0]["content"] == "Sample content"
