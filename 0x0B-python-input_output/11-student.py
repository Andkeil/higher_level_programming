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

    def to_json(self):
        """
        method dict rep of student
        """
        return self.__dict__
