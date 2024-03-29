#!/usr/bin/python3
"""module prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """ensuring a string is passed"""
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
