#!/usr/bin/python3
""" definition of 'Square' class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ initializing class """

    def __init__(self, size, x=0, y=0, id=None):
        """ passing to the super class """
        super().__init__(size, size, x, y, id)
        self.size = size

    """getter for size"""
    @property
    def size(self):
        return self.width

    """ setter for size """
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """ str magical function """
    def __str__(self):
        return "[{}]({}) {}/{} - {}\
".format(type(self).__name__, self.id, self.x, self.y, self.width)

    """ updates the value of the attributes """
    def update(self, *args, **kwargs):
        """ reseting attr with new values """
        length = len(args)

        if args is not None and length > 0:
            if length == 1:
                self.id = args[0]
            elif length == 2:
                self.id, self.size = args
            elif length == 3:
                self.id, self.size, self.x = args
            elif length == 4:
                self.id, self.size, self.x, self.y = args
        else:
            for key in kwargs:
                if key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'id':
                    self.id = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    """ returns the attr of the square obj as a dict """
    def to_dictionary(self):
        """ creating dictionary """
        """ returns the rectangle attributes in dictionary form """
    def to_dictionary(self):
        """ creating dictionary """

        new_dict = dict()
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
