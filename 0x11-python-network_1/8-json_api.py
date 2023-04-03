#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    values = {'q': sys.argv[1] if len(sys.argv) > 1 else ''}

    res = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        res_json = res.json()
        if res_json:
            print('[{}] {}'.format(res_json.get('id'), res_json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
