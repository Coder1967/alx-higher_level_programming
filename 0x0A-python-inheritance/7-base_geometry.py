#!/usr/bin/python3
""" creating BaseGeometry class """


class BaseGeometry:
    """ creating a method 'area' """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks if 'value' is a positive integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
