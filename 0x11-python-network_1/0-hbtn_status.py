#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        body = response.read()
    print(
        "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(body), body, body.decode("utf-8")
        )
    )
