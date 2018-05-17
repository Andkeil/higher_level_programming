#!/usr/bin/python3
import json
"""
save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    method writes an object to json txt file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
    f.closed
