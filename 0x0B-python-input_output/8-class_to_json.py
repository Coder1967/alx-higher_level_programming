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
    my_dict = {}
    for content in dir(obj):
        if content[0] != '_' and content[1] != '_':
            attr = "obj"
            attr += "."
            attr += content
            my_dict[content] = eval(attr)
    return my_dict
