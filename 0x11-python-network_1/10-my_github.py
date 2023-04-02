#!/usr/bin/python3
"""My Comments come here and must be edited"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    patoken = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {
              'Authorization': 'token {}'.format(patoken),
              'Accept': 'application/vnd.github.v3+json',
              }

    login = requests.get(url, headers=headers)
    print(login.json().get('id', 'None'))
