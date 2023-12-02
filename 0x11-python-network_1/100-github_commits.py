#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""


import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
        print(f"{sha}: {author_name}")
