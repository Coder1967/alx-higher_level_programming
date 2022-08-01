#!/usr/bin/python3
""" module to check check if an object is an instance of a particular class"""


def is_same_class(obj, a_class):
    """ function checks if obj is an instance/object of a_class"""
    if type(obj) == a_class:
        return True
    return False
