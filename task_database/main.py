from db_setup import create_tasks_table
from task_manager import create_task, get_all_tasks, update_task, delete_task, get_stats

def display_menu():
    """Display the main menu options for the task manager."""
    print("\n==== Personal Task Manager ====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. View Task Stats")
    print("6. Exit")

def add_task_flow():
    """Prompt user to input task details and add the task to the database."""
    title = input("Enter task title: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low, Medium, High): ")
    create_task(title, due_date, priority)
    print("Task added successfully!")

def view_tasks():
    """Retrieve and display all tasks from the database."""
    tasks = get_all_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"ID: {task[0]} | Title: {task[1]} | Due: {task[2]} | Priority: {task[3]} | Status: {task[4]}")

def update_task_flow():
    """Prompt user to select and update an existing task."""
    view_tasks()  # Display existing tasks to help select ID
    task_id = int(input("Enter the ID of the task to update: "))
    title = input("New title: ")
    due_date = input("New due date (YYYY-MM-DD): ")
    priority = input("New priority (Low, Medium, High): ")
    status = input("Status (pending/completed): ")
    update_task(task_id, title, due_date, priority, status)
    print("Task updated!")

def delete_task_flow():
    """Prompt user to delete a task by ID."""
    view_tasks()  # Show current tasks
    task_id = int(input("Enter the ID of the task to delete: "))
    delete_task(task_id)
    print("Task deleted!")

def view_stats():
    """Display statistics of completed vs pending tasks."""
    stats = get_stats()
    print("\n=== Task Stats ===")
    for status, count in stats:
        print(f"{status.capitalize()}: {count} task(s)")

def main():
    """
    Main driver function for the task manager.
    It displays the menu and routes user input to the appropriate functions.
    """
    create_tasks_table()  # Ensure the table exists before any operations

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Entry point for the script
if __name__ == "__main__":
    main()
