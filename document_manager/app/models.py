import sqlite3
import os
from flask import current_app

def get_db_connection():
    db_path = os.path.join(current_app.instance_path, 'documents.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            category TEXT NOT NULL,
            content TEXT,
            filepath TEXT NOT NULL,
            upload_time TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_document(filename, category, content, filepath):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO documents (filename, category, content, filepath) VALUES (?, ?, ?, ?)',
        (filename, category, content, filepath)
    )
    conn.commit()
    conn.close()

def get_all_documents():
    conn = get_db_connection()
    docs = conn.execute('SELECT * FROM documents ORDER BY upload_time DESC').fetchall()
    conn.close()
    return docs
