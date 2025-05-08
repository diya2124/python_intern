import pandas as pd
import matplotlib.pyplot as plt

def show_chart():
    """
    This function reads the benchmark results from 'results.csv' and generates
    a horizontal bar chart to visualize the average execution time of each SQL query.
    The chart is saved as 'performance_chart.png' and also displayed.

    The CSV file is expected to have columns: "Query" and "Avg Time (s)".
    """

    # Read the benchmark results from the CSV file into a DataFrame
    df = pd.read_csv("results.csv")

    # Plotting
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.barh(df["Query"], df["Avg Time (s)"], color="skyblue")  # Create horizontal bar chart
    plt.xlabel("Average Time (s)")  # Label for the x-axis
    plt.title("Query Performance Benchmark")  # Title for the chart
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.savefig("performance_chart.png")  # Save the chart as a PNG file
    plt.show()  # Display the chart

# Main function to trigger the chart generation
if __name__ == "__main__":
    show_chart()  # Run the show_chart function when the script is executed
