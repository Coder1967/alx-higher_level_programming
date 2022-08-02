#!/usr/bin/python3
"""
function to convert a json string
into a python object
"""
from json import loads


def from_json_string(my_str):
    """
    returns the python object
    """
    return(loads(my_str))
