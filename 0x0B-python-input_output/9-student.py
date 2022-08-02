#!/usr/bin/python3
"""
defining 'Student' class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        initializing class object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary of the instance
        """
        return self.__dict__
