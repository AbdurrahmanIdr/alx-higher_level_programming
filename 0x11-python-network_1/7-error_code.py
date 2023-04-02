#!/usr/bin/python3
"""Requests and request code"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    reply = requests.get(url)
    if reply.status_code >= 400:
        print("Error code: ", end="")
        print(reply.status_code)
    else:
        print(reply.text)
