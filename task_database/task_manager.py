from datetime import datetime

# This function validates if the due date is today or in the future
def validate_due_date(due_date_str):
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    if due_date.date() < datetime.now().date():
        raise ValueError("Due date must be today or in the future.")
    return due_date_str

def create_task(title, due_date, priority):
    # Assume you have code to insert the task into the database
    print(f"Task '{title}' with due date {due_date} and priority {priority} created.")

def get_all_tasks():
    # Assume this function fetches all tasks from the database
    return [
        (1, "Task A", "2025-05-10", "Low", "pending"),
        (2, "Task B", "2025-05-15", "High", "completed")
    ]

def update_task(task_id, title, due_date, priority, status):
    # Assume code to update the task in the database
    print(f"Task {task_id} updated: {title}, {due_date}, {priority}, {status}")

def delete_task(task_id):
    # Assume code to delete the task from the database
    print(f"Task {task_id} deleted.")

def get_stats():
    # Assume code to fetch statistics of tasks, such as pending and completed tasks
    return [("pending", 5), ("completed", 3)]
