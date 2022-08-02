#!/usr/bin/python3
"""
changes a python object to a list of its
attribute
"""


def class_to_json(obj):
    """
    returns a dict of the object and
    its attribute
    """
    return obj.__dict__
