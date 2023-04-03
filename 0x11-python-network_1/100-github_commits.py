#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest) """
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]  # Repository name
    owner = sys.argv[2]  # Owner name
    url = "https://api.github.com/repos/{}/{}/commits?\
            author=rails&per_page=10".format(
        owner, repo
    )

    response = requests.get(url)
    commits = response.json()

    for commit in commits:
        print(
            "{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")
            )
        )
