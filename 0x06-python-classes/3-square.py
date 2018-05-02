#!/usr/bin/python3
"""
Square class def
"""


class Square:
    """
    Square class with private attribute
    """
    def __init__(self, size=0):
        """
        Arguments:
        size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return area of square size
        """
        return (self.__size ** 2)
