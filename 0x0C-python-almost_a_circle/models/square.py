#!/usr/bin/python3
"""
Class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherited from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        method str rep of obj
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        method size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        method size setter and validation
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        method to assign attributes from arguments
        """
        if len(args) != 0:
            i = 0
            attrs = ["id", "size", "x", "y"]
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
        sq_dict = {}
        attrs = ["size", "x", "id", "y"]
        for attribute in attrs:
            sq_dict[attribute] = getattr(self, attribute)
        return sq_dict
