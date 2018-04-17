#!/usr/bin/python3
def no_c(my_string):
    cena_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            cena_str += i
    return cena_str
