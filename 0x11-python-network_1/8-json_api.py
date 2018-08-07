#!/usr/bin/python3
"""
Take in letter, send POST req to search server
letter must be in variable 'q'
"""
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    info = {'q': q}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=info).json()
        if r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
