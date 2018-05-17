#!/usr/bin/python3
"""
append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    method append new string after search string found
    """
    string = ""
    with open(filename, encoding='utf8') as f:
        for line in f:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, 'w') as f:
        f.write(string)
