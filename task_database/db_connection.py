import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database name from the environment
DB_NAME = os.getenv("DB_NAME")

# Validate DB_NAME
if not DB_NAME:
    raise ValueError("Environment variable DB_NAME is missing. Please set it in your .env file.")

def get_connection():
    """
    Establish and return a connection to the SQLite database.
    """
    return sqlite3.connect(DB_NAME)
