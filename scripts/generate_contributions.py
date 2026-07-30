#!/usr/bin/env python3

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
print(data)
