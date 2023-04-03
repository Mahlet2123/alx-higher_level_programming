#!/usr/bin/python3
""" displays the value of the X-Request-Id variable in the header """
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.headers['X-Request-Id']:
        print(req.headers['X-Request-Id'])
    else:
        print('None')
