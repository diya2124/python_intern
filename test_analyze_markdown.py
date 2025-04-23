import pytest
from unittest.mock import patch, mock_open
from sample import analyze_markdown
  # Replace with your actual file name
import requests

mock_md = """
# Title

Some content with a [valid link](https://example.com) and an ![image](img.png)

## Subtitle
More text.
"""

def test_analyze_markdown_basic():
    with patch("builtins.open", mock_open(read_data=mock_md)):
        with patch("os.path.exists", return_value=True):
            with patch("requests.head") as mock_head:
                mock_head.return_value.status_code = 200
                
                result = analyze_markdown("fake.md")

    assert result["Total Words"] == 17
    assert result["Headings"] == 2
    assert result["Links Found"] == 1
    assert result["Valid Links"] == 1
    assert result["Broken Links"] == []
    assert result["Images"] == 1

def test_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = analyze_markdown("missing.md")
        assert result is None
