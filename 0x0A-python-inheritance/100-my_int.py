#!/usr/bin/python3
""" initializing a 'MyInt' class """

class MyInt(int):
    def __eq__(self, value):
        if (self - value == 0):
            return False
        return True

    def __ne__(self, value):
        if self - value != 0:
            return False
        return True
