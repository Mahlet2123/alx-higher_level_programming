#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
import requests
import sys


if __name__ == "__main__":
    url = http://0.0.0.0:5000/search_user
    values = {"q": sys.argv[1]}

    res = requests.post(url, data=values)
    print(res.text)
