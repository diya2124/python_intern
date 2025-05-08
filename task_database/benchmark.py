import sqlite3
import time
import csv  # Add csv import to avoid any issues when writing to CSV

from db_connection import get_connection  # Importing the function to get database connection

# List of queries to benchmark
QUERIES = [
    "SELECT * FROM tasks",  # Select all tasks from the table
    "SELECT COUNT(*) FROM tasks",  # Get the total number of tasks
    "SELECT * FROM tasks WHERE priority='High'",  # Select tasks with 'High' priority
    "SELECT * FROM tasks ORDER BY due_date",  # Select tasks ordered by due date
]

def benchmark_queries():
    """
    This function benchmarks the performance of several SQL queries on the 'tasks' table.
    It executes each query 100 times, measures the average execution time, and writes
    the results to a CSV file.

    Queries are predefined in the QUERIES list, and the average execution time for each
    query is calculated by dividing the total time by the number of executions.
    """

    # Initialize a list to store the benchmark results
    results = []

    # Iterate through each query in the list
    for query in QUERIES:
        conn = get_connection()  # Establish a database connection
        cursor = conn.cursor()  # Create a cursor object to interact with the database

        # Record the start time for benchmarking
        start_time = time.time()

        # Execute the query 100 times to get an average execution time
        for _ in range(100):
            cursor.execute(query)
            cursor.fetchall()  # Fetch all results (to ensure query is fully executed)

        # Record the end time after the 100 executions
        end_time = time.time()

        # Calculate the average time per execution (rounded to 6 decimal places)
        avg_time = round((end_time - start_time) / 100, 6)

        # Append the results in dictionary format to the results list
        results.append({"Query": query, "Avg Time (s)": avg_time})

        # Close the database connection
        conn.close()

    # Write the benchmark results to a CSV file
    with open("results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Query", "Avg Time (s)"])
        writer.writeheader()  # Write the header row
        writer.writerows(results)  # Write all the benchmark results

# Main function to trigger the benchmarking process
if __name__ == "__main__":
    benchmark_queries()  # Run the benchmark queries when the script is executed
