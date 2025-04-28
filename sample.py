import json
import re
import os
import requests

def load_config(path="config.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def analyze_markdown(filepath, config):
    report = {
        "Total Words": 0,
        "Headings": 0,
        "Links Found": 0,
        "Valid Links": 0,
        "Broken Links": [],
        "Images": 0
    }

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    words = [w for w in re.findall(r'\b\w+\b', content) if len(w) >= config["analysis"]["min_word_length"]]
    report["Total Words"] = len(words)

    if config["analysis"]["include_headings"]:
        report["Headings"] = len(re.findall(r'^#+ ', content, re.MULTILINE))

    if config["analysis"]["include_links"]:
        links = re.findall(r'\[(.*?)\]\((https?://[^\s)]+)\)', content)
        report["Links Found"] = len(links)

        if config["link_validation"]["validate_links"]:
            headers = {"User-Agent": config["link_validation"]["user_agent"]}
            for text, url in links:
                try:
                    res = requests.head(url, timeout=config["link_validation"]["timeout"], allow_redirects=config["link_validation"]["allow_redirects"], headers=headers)
                    if res.status_code < 400:
                        report["Valid Links"] += 1
                    else:
                        report["Broken Links"].append(url)
                except:
                    report["Broken Links"].append(url)

    if config["analysis"]["include_images"]:
        report["Images"] = len(re.findall(r'!\[.*?\]\((.*?)\)', content))

    return report
