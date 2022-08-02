#!/usr/bin/python3
"""
function writes into a txt file
"""

def write_file(filename="", text=""):
    """
    opening the file in the write mode
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
