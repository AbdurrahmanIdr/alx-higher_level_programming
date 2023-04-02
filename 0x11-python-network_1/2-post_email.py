#!/usr/bin/python3
"""
So what I Basically did here was parse, Post with data
"""

import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode("utf-8")
    with urllib.request.urlopen(url, data) as response:
        reply = response.read()
        print(reply.decode("utf-8"))
