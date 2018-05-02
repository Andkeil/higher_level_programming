#!/usr/bin/python3
"""
 6-square module
"""


class Square:
    """
    Class: Square with private attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """Arguments:
                     size: size of square
                     position: position of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

    def area(self):
        """
        return size squared
        """
        return (self.size ** 2)

    @property
    def size(self):
        """
        return size
        """
        return (self.__size)

    @property
    def position(self):
        """
        return position
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """size: size of square
        sets value if passes validation
        raise error otherwise
        arguments: value: int
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ position

        arguments: value: int
        """

        if type(value) is tuple and len(value) == 2 and type(value[0]) is int\
           and type(value[1]) is int and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ print visual representation
        Arguments: none
        """


        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print ("{}{}".format(" " * self.position[0], '#' * self.size))
