#!/usr/bin/python3
"""Trying to request url with request"""

import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    reply = requests.get(url)
    print("Body response:")
    print("\t- type: " + str(type(reply.text)))
    print("\t- content: " + str(reply.text))
