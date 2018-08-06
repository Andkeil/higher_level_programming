#!/usr/bin/python3
"""
Python script to fetch hbtn status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        info = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(info)))
        print("\t- content: {}".format(info))
        print("\t- utf8 content: {}".format(info.decode(encoding="utf-8")))
