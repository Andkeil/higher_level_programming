#!/usr/bin/python3
""" 6-square """


class Square:
    """ Class: Square """
    def __init__(self, size=0, position=(0, 0)):
        """ init """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

    def area(self):
        """ area """
        return (self.size ** 2)

    @property
    def size(self):
        """ size """
        return (self.__size)

    @property
    def position(self):
        """ position """
        return (self.__position)

    @size.setter
    def size(self, value):
        """ size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ position """
        if self._tuple_(value):
            self.__position = value
        elif not self._tuple_(value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def _tuple_(self, position):
        """ _tuple """
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def my_print(self):
        """ my_print """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print ("{}{}".format(" " * self.position[0], '#' * self.size))
