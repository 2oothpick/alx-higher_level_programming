#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    repos = "https://api.github.com/repos"
    URL = f"{repos}/{argv[2]}/{argv[1]}/commits"
    resp = requests.get(URL)
    commits = resp.json()
    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get("commit").get("author").get("name"))
