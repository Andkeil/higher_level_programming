#!/usr/bin/python3
"""
Auth for github with provided user/pass
"""
import requests
import sys


if __name__ == "__main__":
    info = {'login': sys.argv[1]}
    r = requests.get('https://api.github.com/user', params=info, auth=(
            sys.argv[1], sys.argv[2])).json()
    try:
        print(r['id'])
    except KeyError:
        print("None")
