#!/usr/bin/python3
""" function adds another attribute to an object """


def add_attribute(obj, name, value):
    """ we can't add attributes to classes with no dicts like
    the native classes eg int, float etc"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
