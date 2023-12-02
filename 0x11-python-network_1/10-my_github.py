#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""


import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)

    try:
        response = requests.get(url, auth=auth)
        json_data = response.json()
        print(json_data.get('id'))
    except ValueError:
        print(None)
