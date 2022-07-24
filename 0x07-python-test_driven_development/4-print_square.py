#!/usr/bin/python3
"module to print a square"


def print_square(size):
    i = 0
    "checks if size is an integr"
    if type(size) != int:
        raise TypeError("size must be an integer")
    "checks if size is a negative integer"
    if size < 0:
        raise ValueError("size must be >= 0")
    while i < size:
        print("#" * size)
        i += 1
