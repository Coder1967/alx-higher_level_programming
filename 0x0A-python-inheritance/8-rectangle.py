#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" defining 'Rectangle' class that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """ initializing class """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
