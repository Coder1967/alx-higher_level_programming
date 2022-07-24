#!/usr/bin/python3
" a module to add two integers"


def add_integer(a, b=98):
    "ensuring a number was passed"
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
