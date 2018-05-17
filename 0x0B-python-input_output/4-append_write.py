#!/usr/bin/python3
"""
append_write
"""


def append_write(filename="", text=""):
    """
    method append string to file
    """
    with open(filename, 'a', encoding='utf8') as f:
        s = str(text)
        return(f.write(s))
