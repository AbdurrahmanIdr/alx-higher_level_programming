#!/usr/bin/python3
"""Trying to request url header with request"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    reply = requests.get(url)
    if 'X-Request-Id' in reply.headers:
        print(reply.headers["X-Request-Id"])
