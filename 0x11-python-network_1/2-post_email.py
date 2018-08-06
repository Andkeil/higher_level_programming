#!/usr/bin/python3
"""
Script take URL, POST req, display body
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    info = {'email': sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(info)
    data = data.encode('ascii')
    reply = urllib.request.Request(url, data)
    with urllib.request.urlopen(reply) as response:
        body = response.read()
    print(body.decode(encoding="utf-8"))
