#!/usr/bin/python3
import json
"""
load_from_json_file
"""


def load_from_json_file(filename):
    """
    method create object from JSON file
    """
    with open(filename) as f:
        obj = json.load(f)
    f.closed
    return obj
