#!/usr/bin/python3
"""
number_of_lines
"""


def number_of_lines(filename=""):
    """
    Method # of lines in file
    """
    lines = 0
    with open(filename,  encoding='utf8') as f:
        for i in f:
            lines += 1
    f.closed
    return lines
