#!/usr/bin/python3
"""
function converts a json file to a python object
"""
from json import load


def load_from_json_file(filename):
    """
    opening the file in read mode
    """
    with open(filename, 'r', encoding="utf-8") as f:
        obj = load(f)
        return obj
