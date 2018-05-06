#!/usr/bin/python3
"""
Module divides two lists from a matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: Divides list, raise TypeError on wrong input
    """
    new_list = []
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the "
                            "matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    try:
        for row in matrix:
            row = list(map(lambda x: round(x/div, 2), row))
            new_list.append(row)
        return new_list
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
