import sqlite3
import time
import csv
import os  # Import os for file existence check

from db_connection import get_connection

# List of queries to benchmark (including INSERT, UPDATE, DELETE)
QUERIES = [
    "SELECT * FROM tasks",
    "SELECT COUNT(*) FROM tasks",
    "SELECT * FROM tasks WHERE priority='High'",
    "SELECT * FROM tasks ORDER BY due_date",
    "INSERT INTO tasks (title, priority, due_date) VALUES ('New Task', 'Medium', '2025-12-31')",
    "UPDATE tasks SET priority='Low' WHERE priority='High'",
    "DELETE FROM tasks WHERE priority='Low'"
]

def benchmark_queries():
    """
    Benchmarks the performance of various SQL queries on the 'tasks' table.
    Executes each query 100 times, records execution time, and appends results to a CSV file.
    """

    results = []
    
    try:
        # Open database connection once
        conn = get_connection()
        cursor = conn.cursor()

        for query in QUERIES:
            start_time = time.time()

            for _ in range(100):
                try:
                    cursor.execute(query)
                    if query.startswith("SELECT"):
                        cursor.fetchall()  # Ensure SELECT queries are fully executed
                    else:
                        conn.commit()  # Commit changes for INSERT/UPDATE/DELETE
                except sqlite3.Error as e:
                    print(f"Error executing query: {query} - {e}")

            end_time = time.time()
            avg_time = round((end_time - start_time) / 100, 6)

            results.append({"Query": query, "Avg Time (s)": avg_time})

        conn.close()  # Close connection after all queries

        # Check if file exists, append results if it does
        file_exists = os.path.exists("results.csv")
        with open("results.csv", "a" if file_exists else "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Query", "Avg Time (s)"])
            if not file_exists:
                writer.writeheader()  # Write header only if file is new
            writer.writerows(results)  # Append results

    except sqlite3.Error as e:
        print(f"Database connection error: {e}")

# Run the benchmarking process
if __name__ == "__main__":
    benchmark_queries()
