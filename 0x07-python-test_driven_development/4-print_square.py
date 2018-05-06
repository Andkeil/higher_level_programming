#!/usr/bin/python3
"""
Module to print out a square based on input size
Raise TypeError if size is not number
"""


def print_square(size):
    """
    print_square: Prints out a square visual with '#'
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#".format(), end="")
        print()
