#!/usr/bin/python3
"""
Module to print first and last name from input
Raise TypeError when input is not strings
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: take up to two strings and print name
    """
    if not isinstance(first_name, str) and not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s}".format(first_name + " " + last_name))
