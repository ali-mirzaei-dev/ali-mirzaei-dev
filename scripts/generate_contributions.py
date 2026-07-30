#!/usr/bin/env python3
from svg import create_svg
import os
import requests
USERNAME = "ali-mirzaei-dev"
TOKEN = os.getenv("GH_TOKEN")
API = "https://api.github.com/graphql"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

query = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions

        weeks {
          contributionDays {
            contributionCount
          }
        }
      }
    }
  }
}
"""

response = requests.post(
    API,
    headers=headers,
    json={
        "query": query,
        "variables": {
            "login": USERNAME
        }
    }
)
data = response.json()

contributions = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]

svg = create_svg(contributions)

with open("assets/contributions.svg", "w", encoding="utf-8") as file:
    file.write(svg)


print("SVG generated!")