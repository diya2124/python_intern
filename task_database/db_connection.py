import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")

def get_connection():
    return sqlite3.connect(DB_NAME)
