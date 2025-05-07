import pytest
from datetime import datetime
from task_manager import validate_due_date, get_all_tasks, create_task, update_task, delete_task, get_stats

# --- TESTS ---

def test_validate_due_date_valid():
    """Test that validate_due_date function works with valid future and today's dates."""
    try:
        assert validate_due_date("2025-05-10") == "2025-05-10"  # Future date
        assert validate_due_date(datetime.now().strftime('%Y-%m-%d')) == datetime.now().strftime('%Y-%m-%d')  # Today's date
    except Exception as e:
        print(f"test_validate_due_date_valid: FAILED - {e}")
        raise
    else:
        print("test_validate_due_date_valid: PASSES")

def test_validate_due_date_invalid():
    """Test that validate_due_date function raises ValueError for past dates."""
    try:
        with pytest.raises(ValueError):
            validate_due_date("2020-05-10")  # Past date
    except Exception as e:
        print(f"test_validate_due_date_invalid: FAILED - {e}")
        raise
    else:
        print("test_validate_due_date_invalid: PASSES")

def test_create_task():
    """Test that create_task adds a task successfully."""
    try:
        create_task("Test Task", "2025-05-10", "Medium")  # Simulating task creation
    except Exception as e:
        print(f"test_create_task: FAILED - {e}")
        raise
    else:
        print("test_create_task: PASSES")

def test_get_all_tasks():
    """Test that get_all_tasks retrieves the tasks correctly."""
    try:
        tasks = get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0][1] == "Task A"
        assert tasks[1][3] == "High"
    except Exception as e:
        print(f"test_get_all_tasks: FAILED - {e}")
        raise
    else:
        print("test_get_all_tasks: PASSES")

def test_update_task():
    """Test that update_task updates a task's details."""
    try:
        update_task(1, "Updated Task", "2025-06-01", "High", "completed")
    except Exception as e:
        print(f"test_update_task: FAILED - {e}")
        raise
    else:
        print("test_update_task: PASSES")

def test_delete_task():
    """Test that delete_task removes a task successfully."""
    try:
        delete_task(1)
    except Exception as e:
        print(f"test_delete_task: FAILED - {e}")
        raise
    else:
        print("test_delete_task: PASSES")

def test_get_stats():
    """Test that get_stats returns the correct task statistics."""
    try:
        stats = get_stats()
        assert stats == [("pending", 5), ("completed", 3)]  # Expected task stats
    except Exception as e:
        print(f"test_get_stats: FAILED - {e}")
        raise
    else:
        print("test_get_stats: PASSES")
