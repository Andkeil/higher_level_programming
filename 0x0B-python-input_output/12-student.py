#!/usr/bin/python3
"""
student
"""


class Student:
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        method initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method dict rep of student
        """
        a_dict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                a_dict[i] = getattr(self, i)
        return a_dict
