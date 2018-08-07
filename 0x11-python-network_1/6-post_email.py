#!/usr/bin/python3
"""
Take URL, send POST req
"""
import requests
import sys


if __name__ == "__main__":
    reply = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(reply.text)
