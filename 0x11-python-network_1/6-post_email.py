#!/usr/bin/python3
"""Using request to send a post request and print"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    post = {"email": sys.argv[2]}
    reply = requests.post(url, post)
    print(reply.text)
