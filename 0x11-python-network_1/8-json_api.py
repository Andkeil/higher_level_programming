#!/usr/bin/python3
"""
Take in letter, send POST req to search server
letter must be in variable 'q'
"""
import requests
import sys


if __name__ == "__main__":
    try:
        info = {'q': sys.argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', info)
    except:
        r = requests.post('http://0.0.0.0:5000/search_user')
    try:
        if r:
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
        else:
            print("No result")
    except KeyError:
        print("Not a valid JSON")
