# plot_analysis.py

import matplotlib.pyplot as plt
from sample import analyze_markdown

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
    file_path = r'C:\Users\diyac\OneDrive\Desktop\internship\python_intern\sample.md'
    report = analyze_markdown(file_path)
    if report:
        print(report)
        generate_chart(report)
