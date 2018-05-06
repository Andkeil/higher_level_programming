#!/usr/bin/python3
"""
Module to print new lines after delimiters are found
Raise TypeError if not a string
"""


def text_indentation(text):
    """
    text_indentation: take in text and find delimiter to print new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    try:
        text = text.replace('.', ".\n\n")
        text = text.replace('?', "?\n\n")
        text = text.replace(':', ":\n\n")
        text = text.split("\n")
        for i in range(0, len(text)):
            print("{:s}".format(text[i].strip()),
                  end=("" if (i == len(text) - 1) else "\n"))
    except TypeError:
        raise TypeError("text must be a string")
