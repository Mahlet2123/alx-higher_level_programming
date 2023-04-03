#!/usr/bin/python3
""" displays the value of the X-Request-Id variable in the header """
import requests
import sys


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
