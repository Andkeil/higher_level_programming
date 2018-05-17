#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    method rtrn list of lists of ints repping triangle
    """
    if n <= 0:
        return ([])
    new_list = [[1]]
    if n == 1:
        return new_list
    for i in range(n - 1):
        new_list.append([j + n for j, n in zip(new_list[-1] + [0],
                                               [0] + new_list[-1])])
    return new_list
