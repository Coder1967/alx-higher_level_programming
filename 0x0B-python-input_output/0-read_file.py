#!/usr/bin/python3
"""
function reads a text file and prints it's content to
standard output
"""


def read_file(filename=""):
    """ acessing the file in read mode """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

read_file("0-readfile.txt")
