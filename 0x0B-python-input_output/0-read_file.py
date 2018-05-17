#!/usr/bin/python3
"""
read_file
"""


def read_file(filename=""):
    """
    metehod read file
    """
    with open(filename, 'r', encoding='ut8') as f:
        output = f.read()
    print("{}".format(output), end="")
