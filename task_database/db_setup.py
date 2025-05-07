from db_connection import get_connection

def create_tasks_table():
    """Create the tasks table in the database if it does not already exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                due_date TEXT,
                priority TEXT,
                status TEXT DEFAULT 'pending'
            )
        """)
        conn.commit()

# Optional direct execution
if __name__ == "__main__":
    create_tasks_table()
