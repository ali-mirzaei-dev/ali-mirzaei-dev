#!/usr/bin/env python3

import os
import requests
USERNAME = "ali-mirzaei-dev"
TOKEN = os.getenv("GH_TOKEN")
API = "https://api.github.com/graphql"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}