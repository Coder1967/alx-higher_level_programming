#!/usr/bin/python3
""" module to check if an object is an instance of a subclass
of a particular class"""
def inherits_from(obj, a_class):
    """checks if obj is an object of a subclass of a_class"""
    if (issubclass(type(obj), a_class)):
        return True
    return False
