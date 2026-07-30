#!/usr/bin/env python3
from github_api import fetch_repositories
from datetime import datetime

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

# Take top 5 languages
top_langs = sorted_langs[:5]

# Split into two columns
mid = min(3, len(top_langs))
left_langs = top_langs[:mid]
right_langs = top_langs[mid:]

# Font
font_pro = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"

# Build SVG
card_width = 620
card_height = 180

# Bar settings
bar_max_width = 200
bar_height = 6

# Build left column (By Bytes)
left_bars = ""
for i, (name, data) in enumerate(left_langs):
    y = 125 + i * 22
    pct = round(data["size"] / total_bytes * 100)
    bar_width = max(4, pct / 100 * bar_max_width)
    color = data["color"] or "#6e7781"
    
    left_bars += f'''
<text x="34" y="{y}" font-size="12" font-family="{font_pro}" fill="#424a53">{name.lower()}</text>
<rect x="100" y="{y - 8}" width="{bar_width}" height="{bar_height}" rx="3" fill="{color}"/>
<text x="{100 + bar_max_width + 10}" y="{y}" font-size="12" font-family="{font_pro}" fill="#8c959f">{pct}%</text>'''

# Build right column (By Repos)
right_bars = ""
for i, (name, data) in enumerate(right_langs):
    y = 125 + i * 22
    count = lang_repos.get(name, 0)
    max_repos = max(lang_repos.values()) if lang_repos else 1
    bar_width = max(4, count / max_repos * bar_max_width)
    color = data["color"] or "#6e7781"
    
    right_bars += f'''
<text x="344" y="{y}" font-size="12" font-family="{font_pro}" fill="#424a53">{name.lower()}</text>
<rect x="410" y="{y - 8}" width="{bar_width}" height="{bar_height}" rx="3" fill="{color}"/>
<text x="{410 + bar_max_width + 10}" y="{y}" font-size="12" font-family="{font_pro}" fill="#8c959f">{count}</text>'''

# Section headers
left_header = ""
right_header = ""
if left_langs:
    left_header = f'<text x="34" y="105" font-size="9" font-family="{font_pro}" fill="#8c959f" font-weight="600" letter-spacing="1">BY BYTES</text>'
if right_langs:
    right_header = f'<text x="344" y="105" font-size="9" font-family="{font_pro}" fill="#8c959f" font-weight="600" letter-spacing="1">BY REPOS</text>'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{card_width}" height="{card_height}" viewBox="0 0 {card_width} {card_height}" fill="none">
<rect x="1" y="1" width="{card_width - 2}" height="{card_height - 2}" rx="10" fill="#ffffff" stroke="#d0d7de"/>

<!-- Divider -->
<line x1="310" y1="16" x2="310" y2="164" stroke="#d8dee4" stroke-width="1"/>

{left_header}
{left_bars}
{right_header}
{right_bars}

</svg>'''

with open("assets/languages.svg", "w", encoding="utf-8") as file:
    file.write(svg)

print("Languages SVG generated!")