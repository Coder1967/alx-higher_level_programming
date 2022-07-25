#!/usr/bin/python3
""" class for Rectangle """


class Rectangle:
    """ keeps count of current amount of instances """
    number_of_instances = 0
    """ determines representation of rectangle to be printed """
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
            shape += str(self.print_symbol) * self.__width
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
