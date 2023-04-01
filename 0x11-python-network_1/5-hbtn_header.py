#!/usr/bin/python3
"""  displays the value of the X-Request-Id variable in the header """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers['X-Request-Id'])
