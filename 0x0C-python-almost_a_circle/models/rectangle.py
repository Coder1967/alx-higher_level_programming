#!/usr/bin/python3
""" definition of the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle imports from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    """ getter for height """
    @property
    def height(self):
        """ returns the value of __height """
        return self.__height

    """ setter for height """
    @height.setter
    def height(self, value):
        """ sets the value of the height private attribute """
        if type(self) == Rectangle:
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
        self.__height = value

    """ getter for width """
    @property
    def width(self):
        """ returns the value of width """
        return self.__width

    """ setter for width """
    @width.setter
    def width(self, value):
        """ sets the value of the width private attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ getter for x"""
    @property
    def x(self):
        """ returns value of x private attribute """
        return self.__x

    """ setter fo x"""
    @x.setter
    def x(self, value):
        """ sets private attribute x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ getter for y """
    @property
    def y(self):
        """ returns value of y private attribute """
        return self.__y

    """ setter for y private attribute"""
    @y.setter
    def y(self, value):
        """ sets private attribute y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ returns the area of the Rectangle instance """
    def area(self):
        """ returns the area """
        return self.height * self.width

    """prints the Rectangle instance to stdout"""
    def display(self):
        """ prints it out to stdout using # """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    """ str magical function """
    def __str__(self):
        return "[Rectangle]({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                self.x,
                                                                self.y,
                                                                self.width,
                                                                self.height)

    """ update the values of the attriutes """
    def update(self, *args, **kwargs):
        """ returns the update of the values of the attributes"""
        length = len(args)

        if args is not None and length > 0:
            if length == 1:
                self.id = args[0]
            elif length == 2:
                self.id, self.width = args
            elif length == 3:
                self.id, self.width, self.height = args
            elif length == 4:
                self.id, self.width, self.height, self.x = args
            elif length == 5:
                self.id, self.width, self.height, self.x, self.y = args
        else:
            for key in kwargs:
                if key == 'width':
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'id':
                    self.id = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    """ returns the rectangle attributes in dictionary form """
    def to_dictionary(self):
        """ creating dictionary """

        new_dict = dict()
        new_dict['id'] = self.id
        new_dict['width'] = self.width
        new_dict['height'] = self.height
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
