#!/usr/bin/python3
"""
function converts python object into
json and stores it in a file
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    opening file in write mode
    """
    with open(filename, 'w', encoding="utf-8") as f:
        dump(my_obj, f)
