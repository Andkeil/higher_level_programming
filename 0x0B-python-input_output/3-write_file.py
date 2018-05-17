#!/usr/bin/python3
"""
write_file
"""


def write_file(filename="", text=""):
    """
    method write file
    """
    with open(filename, 'w') as f:
        output = f.write(text)
    f.closed
    return output
