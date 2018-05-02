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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return square of size
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        return size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """size: size of square
        sets value if passes validation
        raise error otherwise
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
