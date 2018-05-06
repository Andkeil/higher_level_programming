#!/usr/bin/python3
def text_indentation(text):
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
