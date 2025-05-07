from db_connection import get_connection
import queries
import logging

logging.basicConfig(level=logging.INFO)

def create_task(title, due_date, priority):
    conn = get_connection()
    c = conn.cursor()
    c.execute(queries.CREATE_TASK, (title, due_date, priority))
    conn.commit()
    conn.close()
    logging.info(f"Task '{title}' created")

def get_all_tasks():
    conn = get_connection()
    c = conn.cursor()
    c.execute(queries.GET_ALL_TASKS)
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_task(task_id, title, due_date, priority, status):
    conn = get_connection()
    c = conn.cursor()
    c.execute(queries.UPDATE_TASK, (title, due_date, priority, status, task_id))
    conn.commit()
    conn.close()
    logging.info(f"Task ID {task_id} updated")

def delete_task(task_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()
    logging.info(f"Task ID {task_id} deleted")

def get_stats():
    conn = get_connection()
    c = conn.cursor()
    c.execute(queries.GET_STATS)
    stats = c.fetchall()
    conn.close()
    return stats
