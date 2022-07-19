#!/usr/bin/python3

""" creating a class """


class Square:
    """ initializung a squar """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        i = 0

        if self.__size == 0:
            print()
        else:
            while i < self.__size:
                print(self.__size * '#')
                i += 1
