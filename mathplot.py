import matplotlib.pyplot as plt
from sample import analyze_markdown, load_config  # Import load_config to load the configuration

def generate_chart(report):
    """
    Generate and save a bar chart visualization of the Markdown analysis.
    """
    labels = ["Words", "Headings", "Links", "Valid Links", "Images"]
    values = [
        report["Total Words"],
        report["Headings"],
        report["Links Found"],
        report["Valid Links"],
        report["Images"]
    ]

    # Check if values are valid
    if not all(isinstance(value, (int, float)) for value in values):
        print("⚠️ Invalid data found in the report.")
        return

    plt.figure(figsize=(9, 6))
    bars = plt.bar(labels, values, color=['skyblue', 'orange', 'lightgreen', 'green', 'salmon'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, int(yval), ha='center', fontsize=12)

    plt.title("Markdown File Analysis")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("markdown_analysis_chart.png")
    print("Chart saved as markdown_analysis_chart.png")

if __name__ == "__main__":
    # Load the config
    config = load_config()

    # Define the path to your markdown file
    file_path = r'C:\Users\diyac\OneDrive\Desktop\internship\python_intern\sample.md'

    # Pass the file path and config to analyze_markdown
    report = analyze_markdown(file_path, config)

    # Debug: Check the report
    if report:
        print("✅ Report Generated:", report)
        generate_chart(report)
    else:
        print("❌ Report not generated. Please check the analysis function.")
