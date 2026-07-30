#!/usr/bin/env python3
import os
import requests

USERNAME = "ali-mirzaei-dev"
TOKEN = os.getenv("GH_TOKEN")
API = "https://api.github.com/graphql"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


def run_query(query, variables=None):
    """Run a GraphQL query against GitHub API."""
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    
    response = requests.post(API, headers=headers, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Query failed: {response.status_code}\n{response.text}")
    
    data = response.json()
    if "errors" in data:
        raise Exception(f"GraphQL errors: {data['errors']}")
    
    return data


def fetch_contributions():
    """Fetch contribution calendar data."""
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
    data = run_query(query, {"login": USERNAME})
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def fetch_contribution_days():
    """Fetch all contribution days for streak calculation."""
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """
    data = run_query(query, {"login": USERNAME})
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    
    all_days = []
    for week in weeks:
        for day in week["contributionDays"]:
            all_days.append(day)
    
    return all_days


def fetch_repositories():
    """Fetch repository data with languages."""
    query = """
    query($login: String!) {
      user(login: $login) {
        repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
          nodes {
            name
            languages(first: 10) {
              edges {
                size
                node {
                  name
                  color
                }
              }
            }
          }
        }
      }
    }
    """
    data = run_query(query, {"login": USERNAME})
    return data["data"]["user"]["repositories"]["nodes"]