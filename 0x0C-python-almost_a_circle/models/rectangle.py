#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherited from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        method width
        """
        return self.__width

    @property
    def height(self):
        """
        method height
        """
        return self.__height

    @property
    def x(self):
        """
        method rtrn x
        """
        return self.__x

    @property
    def y(self):
        """
        method rtrn y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        method width setter and valid verification
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        method height setter and valid verification
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        method x setter and validation
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        method y setter and validation
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        method rtrn area
        """
        return (self.__width * self.__height)

    def display(self):
        """
        method display the rectangle
        """
        print(("\n" * self.__y) + "\n".join(((" " * self.__x) +
                                             ("#" * self.__width))
                                            for i in range(self.__height)))

    def __str__(self):
        """
        method rtrn rectangle
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """
        method to assign args to attributes
        """
        if len(args) != 0:
            i = 0
            attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, attrs[i], args[i])
                i += 1

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        method rtrn dict representation of obj
        """
        rec_dict = {}
        attrs = ["height", "width", "x", "id", "y"]
        for attribute in attrs:
            rec_dict[attribute] = getattr(self, attribute)
        return rec_dict
