#!/usr/bin/python3
"""
module: 2-rectangle
"""


class Rectangle:
    """
    class: Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        init: self, width, height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter: width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        property: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter: height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        public instance method: area
        """
        if self.width or self.height:
            return self.width * self.height

    def perimeter(self):
        """
        public instance method: perimeter
        """
        if self.width or self.height:
            return (self.width * 2) + (self.height * 2)
