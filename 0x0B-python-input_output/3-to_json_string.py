#!/usr/bin/python3
"""
writing a function to convert a python
object to a json string
"""
from json import dumps

def to_json_string(my_obj):
    return dumps(my_obj)
