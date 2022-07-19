#!/usr/bin/python3

""" creating a class """


class Square:
    """ initializung a squar """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        self._Square__size = size
