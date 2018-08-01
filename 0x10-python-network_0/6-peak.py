#!/usr/bin/python3
"""
Find a peak in a list of unsorted
Integers
"""


def find_peak(list_of_integers):
    """
    Method to find a peak
    """
    length = len(list_of_integers)
    if length == 0:
        return
    mid = length // 2
    if (mid == length - 1 or list_of_integers[mid] >=
        list_of_integers[mid + 1]) and (mid == 0 or list_of_integers[mid] >=
                                         list_of_integers[mid - 1]):
        return (list_of_integers[mid])
    elif mid != length - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
        return (find_peak(list_of_integers[mid + 1:]))
    return (find_peak(list_of_integers[:mid]))
