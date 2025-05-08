import pandas as pd
import matplotlib.pyplot as plt

def show_chart():
    """
    This function reads the benchmark results from 'results.csv' and generates
    a vertical bar chart to visualize the average execution time of each SQL query.
    The chart is saved as 'performance_chart.png' and also displayed.

    The CSV file is expected to have columns: "Query" and "Avg Time (s)".
    """

    # Read the benchmark results from the CSV file into a DataFrame
    df = pd.read_csv("results.csv")

    # Generate unique colors for each bar
    colors = plt.cm.get_cmap("tab10", len(df))  # Using 'tab10' colormap

    # Plotting
    plt.figure(figsize=(12, 6))  # Set the figure size
    plt.bar(df["Query"], df["Avg Time (s)"], color=[colors(i) for i in range(len(df))])  # Vertical bar chart
    plt.ylabel("Average Time (s)")  # Label for the y-axis
    plt.xlabel("Query")  # Label for the x-axis
    plt.title("Query Performance Benchmark")  # Title for the chart
    plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability

    # Apply logarithmic scaling to y-axis for better visualization
    plt.yscale("log")

    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.savefig("performance_chart.png")  # Save the chart as a PNG file
    plt.show()  # Display the chart

# Main function to trigger the chart generation
if __name__ == "__main__":
    show_chart()  # Run the show_chart function when the script is executed
