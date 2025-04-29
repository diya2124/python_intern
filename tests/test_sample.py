import pytest
import os
from pathlib import Path
import json5  # JSON5 is used for reading the configuration file

from sample import load_config, analyze_markdown, generate_chart, generate_html_report

def test_load_config_valid(tmp_path):
    """
    Test whether a valid configuration file is correctly loaded by `load_config`.

    Steps:
    - Create a temporary JSON5 file with known settings.
    - Load it using the function.
    - Verify that key values match the original input.
    """
    # Create a sample configuration dictionary
    config_data = {
        "analysis": {
            "min_word_length": 3,
            "include_headings": True,
            "include_links": True,
            "include_images": True
        },
        "link_validation": {
            "validate_links": True,
            "timeout": 5,
            "allow_redirects": True,
            "user_agent": "TestAgent"
        },
        "visual_report": {
            "font_family": "Arial, sans-serif",
            "margin": "20px",
            "content_color": "black",
            "chart_width": 10,
            "chart_height": 6,
            "link_colors": ['skyblue', 'purple', 'lightgreen', 'green', 'salmon']
        }
    }

    # Save the config to a temporary file
    config_file = tmp_path / "config.json"
    with open(config_file, "w", encoding="utf-8") as f:
        json5.dump(config_data, f)

    # Load the config using the function under test
    config = load_config(str(config_file))

    # Assert that critical values are correctly loaded
    assert config["analysis"]["min_word_length"] == 3
    assert config["link_validation"]["timeout"] == 5
    assert config["visual_report"]["font_family"] == "Arial, sans-serif"


def test_analyze_markdown(tmp_path):
    """
    Test the `analyze_markdown` function using a temporary markdown file.

    Verifies:
    - Correct total word count based on minimum word length.
    - Accurate heading, link, and image detection.
    """
    # Markdown content includes headings, text, a link, and an image
    md_content = "# Title\n## Subtitle\nSome normal text with a link [Google](https://google.com).\n![Image](image.png)"
    
    # Write the markdown to a temporary file
    md_file = tmp_path / "test_file.md"
    md_file.write_text(md_content)

    # Minimal configuration enabling all features
    config = {
        "analysis": {
            "min_word_length": 3,
            "include_headings": True,
            "include_links": True,
            "include_images": True
        },
        "link_validation": {
            "validate_links": False,  # Disable real HTTP requests
            "timeout": 5,
            "allow_redirects": True,
            "user_agent": "TestAgent"
        },
        "visual_report": {}
    }

    # Analyze the file
    report = analyze_markdown(str(md_file), config)

    # Assertions for expected analysis outcomes
    assert report["Total Words"] == 14  # Count of words meeting length criteria
    assert report["Headings"] == 2  # 1x # and 1x ##
    assert report["Links Found"] == 1  # This seems too high — double-check logic in the main function
    assert report["Images"] == 1  # One image tag


def test_generate_chart(tmp_path):
    """
    Test if the `generate_chart` function runs successfully and creates a visual chart.

    Uses a fake report dictionary with dummy data to simulate analysis output.
    """
    # Simulated report data
    report = {
        "Total Words": 100,
        "Headings": 5,
        "Links Found": 3,
        "Valid Links": 1,
        "Broken Links": ["http://broken.link"],
        "Images": 2
    }

    # Basic config to pass styling info
    config = {
        "visual_report": {
            "font_family": "Arial, sans-serif",
            "margin": "20px",
            "content_color": "black"
        }
    }

    # Call function — it should produce a chart without error
    # You could extend this test to check that a PNG or SVG file was created
    generate_chart(report, config)
