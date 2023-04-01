#!/usr/bin/python3
""" displays the body of the response (decoded in utf-8)."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
        print(body.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
