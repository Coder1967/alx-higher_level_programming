#!/usr/bin/python3
""" module to check if obj is an object of a class or an object of its subclass"""
def is_kind_of_class(obj, a_class):
    """ checks if an object is a class or subclass of a class"""
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    return False
