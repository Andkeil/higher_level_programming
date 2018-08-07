#!/usr/bin/python3
"""
Take string and send request to Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    info = {'search': sys.argv[1]}
    r = requests.get('https://swapi.co/api/people/', params=info).json()
    count = r['count']
    print("Number of results: {}".format(count))
    if count > 0:
        for thing in r['results']:
            print(thing['name'])
