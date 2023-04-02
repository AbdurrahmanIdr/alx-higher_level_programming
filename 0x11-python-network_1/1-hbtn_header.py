#!/usr/bin/python3
"""
After an intense search, I came to discover that the
X-request-Id is found in the .header of opened request
"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
