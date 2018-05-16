#!/usr/bin/python3
"""
my_int
"""


class MyInt(int):
    """
    class MyInt
    """
    def __init__(self, value):
        """
        method inialization
        """
        self.__value = value

    def __eq__(self, other):
        """
        overrides '=='
        """
        if type(self.__value) is int:
            return False

    def __ne__(self, other):
        """
        overrides '!='
        """
        if type(self.__value) is int:
            return True
