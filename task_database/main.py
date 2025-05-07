from db_setup import create_tasks_table
from task_manager import create_task, get_all_tasks, update_task, delete_task, get_stats
from datetime import datetime

def display_menu():
    print("\n==== Personal Task Manager ====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. View Task Stats")
    print("6. Exit")

def validate_due_date(due_date_str):
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
    if due_date.date() < datetime.now().date():
        raise ValueError("Due date must be today or in the future.")
    return due_date_str

def get_valid_task_id():
    tasks = get_all_tasks()
    if not tasks:
        raise ValueError("No tasks available.")
    view_tasks()
    task_ids = [str(task[0]) for task in tasks]
    task_id = input("Enter the task ID: ").strip()
    if task_id not in task_ids:
        raise ValueError("Invalid task ID.")
    return int(task_id)

def add_task_flow():
    try:
        title = input("Enter task title: ").strip()
        if not title:
            raise ValueError("Title cannot be empty.")

        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        due_date = validate_due_date(due_date)

        priority = input("Enter priority (Low, Medium, High): ").strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            raise ValueError("Priority must be Low, Medium, or High.")

        create_task(title, due_date, priority)
        print(" Task added successfully!")
    except ValueError as ve:
        print(f" Input Error: {ve}")
    except Exception as e:
        print(f" Error: {e}")

def view_tasks():
    try:
        tasks = get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(f"ID: {task[0]} | Title: {task[1]} | Due: {task[2]} | Priority: {task[3]} | Status: {task[4]}")
    except Exception as e:
        print(f" Error retrieving tasks: {e}")

def update_task_flow():
    try:
        task_id = get_valid_task_id()

        title = input("New title: ").strip()
        if not title:
            raise ValueError("Title cannot be empty.")

        due_date = input("New due date (YYYY-MM-DD): ").strip()
        due_date = validate_due_date(due_date)

        priority = input("New priority (Low, Medium, High): ").strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            raise ValueError("Priority must be Low, Medium, or High.")

        status = input("Status (pending/completed): ").strip().lower()
        if status not in ["pending", "completed"]:
            raise ValueError("Status must be 'pending' or 'completed'.")

        update_task(task_id, title, due_date, priority, status)
        print(" Task updated!")
    except ValueError as ve:
        print(f" Input Error: {ve}")
    except Exception as e:
        print(f" Error updating task: {e}")

def delete_task_flow():
    try:
        task_id = get_valid_task_id()
        delete_task(task_id)
        print("✅ Task deleted!")
    except ValueError as ve:
        print(f" Input Error: {ve}")
    except Exception as e:
        print(f" Error deleting task: {e}")

def view_stats():
    try:
        stats = get_stats()
        print("\n=== Task Stats ===")
        for status, count in stats:
            print(f"{status.capitalize()}: {count} task(s)")
    except Exception as e:
        print(f" Error fetching stats: {e}")

def main():
    create_tasks_table()
    while True:
        display_menu()
        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_task_flow()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task_flow()
        elif choice == "4":
            delete_task_flow()
        elif choice == "5":
            view_stats()
        elif choice == "6":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
