#!/usr/bin/python3
"""
creating function to append to a txt file
"""


def append_write(filename="", text=""):
    """
    opening the file in append mode
    """
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
