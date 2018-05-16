#!/usr/bin/python3
"""
7-base_geometry
"""


class BaseGeometry:
    """
    Class of BaseGeometry
    """
    def __init___(self):
        """
        method initialize
        """
        pass

    def area(self):
        """
        method area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
