from db_connection import get_connection
from datetime import datetime

def validate_due_date(date_str):
    """Validate and return a properly formatted due date or raise ValueError."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")

def create_task(title, due_date, priority):
    if not title.strip():
        raise ValueError("Task title cannot be empty.")
    if priority not in ["Low", "Medium", "High"]:
        raise ValueError("Priority must be 'Low', 'Medium', or 'High'.")
    due_date = validate_due_date(due_date)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, due_date, priority) VALUES (?, ?, ?)",
            (title, due_date, priority),
        )
        conn.commit()

def get_all_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()

def update_task(task_id, title, due_date, priority, status):
    due_date = validate_due_date(due_date)
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET title = ?, due_date = ?, priority = ?, status = ?
            WHERE id = ?
        """, (title, due_date, priority, status, task_id))
        conn.commit()

def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def get_stats():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'")
        completed = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'pending'")
        pending = cursor.fetchone()[0]
        return completed, pending
