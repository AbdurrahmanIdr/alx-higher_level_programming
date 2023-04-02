#!/usr/bin/python3
"""My Comments come here and must be edited"""

import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    headers = {
              'Accept': 'Accept: application/vnd.github+json'
              }

    login = requests.get(url, headers=headers, params={'per_page': 10})
    whldict = login.json()
    for count in whldict:
        dict1 = count
        sha = dict1['sha']
        commit = dict1['commit']
        author = commit['author']
        print("{}: {}".format(sha, author['name']))
