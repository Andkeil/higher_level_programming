#!/usr/bin/python3
"""
read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    method read number of lines indicated
    """
    with open(filename, encoding='utf8') as f:
        numl = sum(1 for line in open(filename))
        if nb_lines <= 0 or nb_lines > numl:
            print(f.read(), end="")
        else:
            for line in range(0, nb_lines):
                print(f.readline(), end="")
    f.closed
