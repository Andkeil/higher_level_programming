#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
10-square
"""


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        method initialization
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        method area
        """
        return self.__size**2
