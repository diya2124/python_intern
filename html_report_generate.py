import os
import matplotlib.pyplot as plt
from sample import analyze_markdown, load_config

def generate_chart(report, config, output_path='chart.png'):
    visual = config.get("visual_report", {})
    width = visual.get("chart_width", 10)
    height = visual.get("chart_height", 20)
    colors = visual.get("link_colors", ['skyblue', 'purple', 'lightgreen', 'green', 'salmon'])

    labels = ["Words", "Headings", "Links", "Valid Links", "Images"]
    values = [
        report["Total Words"],
        report["Headings"],
        report["Links Found"],
        report["Valid Links"],
        report["Images"]
    ]

    # Guard against invalid values
    if not all(isinstance(v, (int, float)) for v in values):
        print("⚠️ Invalid data found in the report. Cannot generate chart.")
        return

    plt.figure(figsize=(width, height))
    bars = plt.bar(labels, values, color=colors)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 2, int(yval), ha='center')

    plt.title("Markdown File Analysis")
    plt.ylabel("Count")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"📊 Chart saved as {output_path}")

def generate_html_report(report, config, chart_path='chart.png', output_file='report.html'):
    visual = config.get("visual_report", {})
    font = visual.get("font_family", "Arial, sans-serif")
    margin = visual.get("margin", "20px")
    color = visual.get("content_color", "black")

    html_content = f"""
    <html>
    <head>
        <title>Markdown Analysis Report</title>
        <style>
            body {{ font-family: {font}; margin: {margin}; color: {color}; }}
            h1 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 50%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            img {{ margin-top: 20px; max-width: 600px; }}
        </style>
    </head>
    <body>
        <h1>Markdown Analysis Report</h1>
        <table>
            <tr><th>Metric</th><th>Value</th></tr>
            <tr><td>Total Words</td><td>{report["Total Words"]}</td></tr>
            <tr><td>Headings</td><td>{report["Headings"]}</td></tr>
            <tr><td>Links Found</td><td>{report["Links Found"]}</td></tr>
            <tr><td>Valid Links</td><td>{report["Valid Links"]}</td></tr>
            <tr><td>Broken Links</td><td>{len(report["Broken Links"])}</td></tr>
            <tr><td>Images</td><td>{report["Images"]}</td></tr>
        </table>
        <img src="{chart_path}" alt="Markdown Analysis Chart">
    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ HTML report saved as {output_file}")

if __name__ == "__main__":
    config = load_config()
    file_path = r'C:\Users\diyac\OneDrive\Desktop\internship\python_intern\sample.md'
    report = analyze_markdown(file_path, config)

    if report:
        print("✅ Report Generated:", report)
        generate_chart(report, config)
        generate_html_report(report, config)
    else:
        print("❌ Failed to generate report.")
