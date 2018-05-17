#!/usr/bin/python3
import sys
import json
"""
add_item
"""


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    new = load_json(filename)
except (ValueError, FileNotFoundError):
    new = []

new = new + sys.argv[1:]
save_to_json_file(new, filename)
