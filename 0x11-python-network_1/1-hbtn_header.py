#!/usr/bin/python3
"""
Script take URL and display X-Request-ID
of response header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        info = response.info()['X-Request-Id']
        print(info)
