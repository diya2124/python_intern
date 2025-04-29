import pytest
import os
from pathlib import Path
from sample import generate_html_report  # Adjust the import if necessary
from unittest.mock import MagicMock

def test_generate_html_report_creates_file(tmp_path):
    """
    Test that `generate_html_report` successfully creates an HTML report file.

    This test verifies:
    - An HTML file is created at the specified path.
    - The report includes expected content such as headers and data entries.
    - The chart image reference is correctly embedded.
    """

    # Create a mock markdown analysis report
    report = {
        "Total Words": 42,
        "Headings": 2,
        "Links Found": 1,
        "Valid Links": 1,
        "Broken Links": [],
        "Images": 1
    }

    # Define basic visual configuration for the report styling
    config = {
        "visual_report": {
            "font_family": "Arial, sans-serif",
            "margin": "20px",
            "content_color": "black"
        }
    }

    # Define a temporary output path for the HTML report
    output_path = tmp_path / "report.html"
    
    # Call the function to generate the HTML report
    generate_html_report(report, config, chart_path="chart.png", output_file=str(output_path))
    
    # Assert the HTML report file was created
    assert os.path.exists(output_path)

    # Open and read the contents of the generated HTML file
    with open(output_path, 'r', encoding='utf-8') as f:
        content = f.read()

        # Assert that key elements are included in the HTML
        assert "<h1>Markdown Analysis Report</h1>" in content
        assert "<td>Total Words</td><td>42</td>" in content
        assert "<td>Headings</td><td>2</td>" in content
        assert "<td>Links Found</td><td>1</td>" in content
        assert "<td>Images</td><td>1</td>" in content
        assert "<img src=\"chart.png\"" in content  # Check that chart image is embedded
