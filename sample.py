import re
import requests
from bs4 import BeautifulSoup

def analyze_markdown(file_path):
    """
    Analyze a Markdown (.md) file to count words, headings, links, and images.
    validates all hyperlinks and classifies them as valid or broken.

    Parameters:
    file_path

    Returns:
    dict: A dictionary containing the analysis report with the following keys:
          - Total Words
          - Headings
          - Links Found
          - Valid Links
          - Broken Links
          - Images
    """
    with open(file_path, 'r',) as f:
        content = f.read()

    word_count = len(content.split())
    headings = len(re.findall(r'^#{1,6} ', content, re.MULTILINE))
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    images = re.findall(r'!\[.*?\]\((.*?)\)', content)

    valid_links = 0
    broken_links = []

    for url in links:
        try:
            r = requests.head(url, allow_redirects=True, timeout=5)
            if r.status_code == 200:
                valid_links += 1
            else:
                broken_links.append(url)
        except requests.RequestException:
            broken_links.append(url)

    report = {
        "Total Words": word_count,
        "Headings": headings,
        "Links Found": len(links),
        "Valid Links": valid_links,
        "Broken Links": broken_links,
        "Images": len(images)
    }

    return report

if __name__ == "__main__":
    """
    Main execution block.
    Set the file path to a Markdown file and print its analysis report.
    """
    file_path = r'C:\Users\diyac\OneDrive\Desktop\internship\python_intern\sample.md'
    report = analyze_markdown(file_path)
    print(report)
