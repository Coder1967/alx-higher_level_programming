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

    def to_json(self, attr=None):
        """
        reurns the a dict of the attributes specified in
        the string 'attr
        """
        if attr is None:
            return self.__dict__
        my_dict = {}
        for key in self.__dict__:
            if key in attr:
                tmp = "self" + "." + key
                my_dict[key] = eval(tmp)
        return my_dict

    def reload_from_json(self, json):
        """
        replaces the attributes of the instance with
        the ones in the json string
        """
        for key in self.__dict__:
            if key in json:
                self.__dict__[key] = json[key]

        return self.__dict__
