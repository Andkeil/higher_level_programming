#!/usr/bin/python3
"""
add_attribute
"""


def add_attribute(obj, attr, value):
    """
    method add attribute to object
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
