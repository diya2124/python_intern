import pytest
from task_manager import (
    create_task, get_all_tasks, update_task,
    delete_task, get_stats, validate_due_date
)

def test_validate_due_date_valid():
    assert validate_due_date("2025-05-10") == "2025-05-10"

def test_validate_due_date_invalid():
    with pytest.raises(ValueError):
        validate_due_date("invalid-date")

def test_create_task():
    create_task("Task A", "2025-05-11", "Low")
    tasks = get_all_tasks()
    assert any(task[1] == "Task A" for task in tasks)

def test_get_all_tasks():
    create_task("Task B", "2025-05-12", "Medium")
    tasks = get_all_tasks()
    assert len(tasks) >= 1
    assert any(task[1] == "Task B" for task in tasks)

def test_update_task():
    create_task("Update Me", "2025-05-13", "High")
    tasks = get_all_tasks()
    task_id = next(task[0] for task in tasks if task[1] == "Update Me")
    update_task(task_id, "Updated", "2025-06-01", "Low", "completed")
    updated_tasks = get_all_tasks()
    updated = next(task for task in updated_tasks if task[0] == task_id)
    assert updated[1] == "Updated"
    assert updated[4] == "completed"

def test_delete_task():
    create_task("Delete Me", "2025-05-20", "Low")
    tasks = get_all_tasks()
    task_id = next(task[0] for task in tasks if task[1] == "Delete Me")
    delete_task(task_id)
    remaining = get_all_tasks()
    assert not any(task[0] == task_id for task in remaining)

def test_get_stats():
    create_task("Stat Task 1", "2025-08-01", "Low")
    create_task("Complete Me", "2025-05-20", "Medium")
    tasks = get_all_tasks()
    task_id = next(task[0] for task in tasks if task[1] == "Complete Me")
    update_task(task_id, "Complete Me", "2025-05-20", "Medium", "completed")
    completed, pending = get_stats()
    assert isinstance(completed, int)
    assert isinstance(pending, int)
    assert completed >= 1

def test_create_task_empty_description():
    with pytest.raises(ValueError):
        create_task("   ", "2025-05-10", "Low")

def test_create_task_invalid_priority():
    with pytest.raises(ValueError):
        create_task("Test Task", "2025-05-10", "Urgent")

def test_create_task_invalid_date_format():
    with pytest.raises(ValueError):
        create_task("Test Task", "10-05-2025", "Low")
