#!/usr/bin/python3
""" class for Rectangle """


class Rectangle:
    """ initializing function """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    """ getter and setter for width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ getter and setter for height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ returns the area of a rectangle """
    def area(self):
        return (self.__height * self.__width)

    """ returns the perimeter of a rectangle """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    """ str magical method """
    def __str__(self):
        i = 0
        shape = ""

        if self.__width == 0 or self.__height == 0:
            return ""
        while i < self.__height:
            shape += "#" * self.__width
            if i != self.__height - 1:
                shape += '\n'
            i += 1
        return shape

    def __repr__(self):
        tmp = "Rectangle("
        tmp += str(self.__width)
        tmp += ", "
        tmp += str(self.__height)
        tmp += ")"
        return tmp

    """ function to delete an instant/object """
    def __del__(self):
        print("Bye rectangle...")
