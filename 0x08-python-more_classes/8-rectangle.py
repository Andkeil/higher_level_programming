#!/usr/bin/python3
"""
module: 8-rectangle
"""


class Rectangle:
    """
    class: Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        init: self, width, height
        """
        self.__width = width
        self.__height = height
        self.__class__.number_of_instances += 1

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
        if self.__width or self.__height:
            return self.__width * self.__height

    def perimeter(self):
        """
        public instance method: perimeter
        """
        if self.__width or self.__height:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        __str__
        """
        s = ""
        a = str(self.print_symbol)
        for i in range(self.__height):
            for j in range(self.__width):
                s = s + a
            if i != int(self.__height) - 1:
                s = s + "\n"
        return s

    def __repr__(self):
        """
        __repr__
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        __del__
        """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method: bigger_or_equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        else:
            return rect_1
