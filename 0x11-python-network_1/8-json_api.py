#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) == 1):
        values = {"q": ''}
    else:
        values = {"q": sys.argv[1]}

    res = requests.post(url, data=values)
    try:
        res_json = res.json()
        if (res_json):
            print("[{}] {}".format(res_json.get('id'), res_json.get('name')))
        else:
            print("No result")
    except TypeError:
        print("Not a valid JSON")
