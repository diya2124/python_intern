import os
from sample import analyze_markdown
from html_report_generate import generate_chart, generate_html_report

# Paths
MD_PATH = 'sample.md'
CHART_PATH = 'test_chart.png'
REPORT_PATH = 'test_report.html'

def test_file_exists():
    """Ensure the Markdown file exists."""
    assert os.path.exists(MD_PATH), "sample.md file not found!"

def test_analyze_markdown_returns_report():
    """Ensure analyze_markdown returns a valid report dictionary."""
    report = analyze_markdown(MD_PATH)
    assert isinstance(report, dict)
    assert "Total Words" in report
    assert "Headings" in report
    assert "Links Found" in report
    assert "Valid Links" in report
    
    assert "Broken Links" in report
    assert "Images" in report

def test_headings_count():
    """Check that headings are correctly counted."""
    report = analyze_markdown(MD_PATH)
    assert report["Headings"] == 2, "Expected 2 headings in sample.md"

def test_link_validation_counts():
    """Check if valid and broken links are identified correctly."""
    report = analyze_markdown(MD_PATH)
    assert report["Links Found"] >= 3
    assert report["Valid Links"] >= 1
    assert isinstance(report["Broken Links"], list)

def test_generate_chart_creates_file():
    """Ensure chart is generated successfully."""
    report = analyze_markdown(MD_PATH)
    generate_chart(report, output_path=CHART_PATH)
    assert os.path.exists(CHART_PATH)
    os.remove(CHART_PATH)  # Clean up

def test_generate_html_report_content():
    """Check if HTML report is generated and contains key data."""
    report = analyze_markdown(MD_PATH)
    generate_chart(report, output_path=CHART_PATH)
    generate_html_report(report, chart_path=CHART_PATH, output_file=REPORT_PATH)

    assert os.path.exists(REPORT_PATH)

    with open(REPORT_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "Markdown Analysis Report" in content
        assert "<td>Total Words</td>" in content
        assert "<img src=\"" in content

    os.remove(CHART_PATH)
    os.remove(REPORT_PATH)
