#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(username, token))
    try:
        print(response.json().get('id'))
        #print(response.json())
    except ValueError:
        print('Not a valid JSON')
