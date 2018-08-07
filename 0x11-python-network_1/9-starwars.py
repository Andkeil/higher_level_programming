#!/usr/bin/python3
"""
Take string and send request to Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    info = {'search': sys.argv[1]}
    r = requests.get('https://swapi.co/api/people/', params=info)
    print("Number of result: {}".format(r.json()['count']))
    for i in range(0, r.json()['count']):
        try:
            print(r.json()['results'][i]['name'])
        except:
            continue
