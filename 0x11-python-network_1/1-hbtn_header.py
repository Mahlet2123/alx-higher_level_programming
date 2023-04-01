#!/usr/bin/python3
"""  displays the value of the X-Request-Id variable in the header """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers['X-Request-Id'])
