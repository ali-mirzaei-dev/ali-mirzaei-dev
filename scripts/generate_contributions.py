#!/usr/bin/env python3
from github_api import fetch_contributions
from svg import create_contributions_svg

contributions = fetch_contributions()

svg = create_contributions_svg(contributions)

with open("assets/contributions.svg", "w", encoding="utf-8") as file:
    file.write(svg)

print("Contributions SVG generated!")