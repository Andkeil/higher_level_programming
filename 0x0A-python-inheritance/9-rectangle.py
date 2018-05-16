#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
9-rectangle
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        """
        method initialization
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        method area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method str
        """
        s = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return s
