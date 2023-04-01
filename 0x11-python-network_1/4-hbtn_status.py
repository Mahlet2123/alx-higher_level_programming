#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        body = response.read()
    string = "Body response:\n\t- type: {}\n\t- content: {}"
    print(string.format(type(body.decode()), body.decode('utf-8')))
