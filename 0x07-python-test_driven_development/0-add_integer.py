#!/usr/bin/python3
"""
Module to add two ints and return their sum
Only take ints and floats, raise TypeError otherwise
Converts floats to ints
"""


def add_integer(a, b=98):
    """
    add_integer: check for correct input, return sum
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)
