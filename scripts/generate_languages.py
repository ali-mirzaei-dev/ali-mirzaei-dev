#!/usr/bin/env python3
from github_api import fetch_repositories
from svg import create_languages_svg

repos = fetch_repositories()

# Calculate language stats
lang_bytes = {}
lang_repos = {}

for repo in repos:
    if not repo["languages"]:
        continue
    
    for edge in repo["languages"]["edges"]:
        name = edge["node"]["name"]
        size = edge["size"]
        color = edge["node"]["color"]
        
        if name not in lang_bytes:
            lang_bytes[name] = {"size": 0, "color": color}
        lang_bytes[name]["size"] += size
        
        if name not in lang_repos:
            lang_repos[name] = 0
        lang_repos[name] += 1

# Sort by bytes
sorted_langs = sorted(lang_bytes.items(), key=lambda x: x[1]["size"], reverse=True)
total_bytes = sum(v["size"] for v in lang_bytes.values())

svg = create_languages_svg(sorted_langs, total_bytes, lang_repos)

with open("assets/languages.svg", "w", encoding="utf-8") as file:
    file.write(svg)

print("Languages SVG generated!")