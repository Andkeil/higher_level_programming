#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("Inside result: {}".format(a/b))
        result = a/b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        result = None
    finally:
        return result
