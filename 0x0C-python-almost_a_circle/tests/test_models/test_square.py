#!/usr/bin/python3
""" tests for the square module """
from unittest import TestCase
from models.square import Square
from models.base import Base


class test_square(TestCase):
    """ test for Square class """
    def test_attribute_set(self):
        s1 = Square(5, 10, 8, 78)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.id, 78)
        s1.size = 65
        s1.x = 5
        s1.y = 54
        self.assertEqual(s1.size, 65)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 54)

    """ tests for if the class was properly inherited"""
    def test_subclass(self):
        """ test if it Square object is a subclass of Rectangle """
        s1 = Square(8, 7)
        self.assertTrue(issubclass(type(s1), Square))

    """ testing for type and value Errors of size"""
    def test_size_error(self):
        """ for if the wrong value is passed """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-4, 8, 7, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True, 98, 6, 5)
            s = Square({8, 9, 87}, 98, 6, 5)
            s = Square(None, 98, 6, 5)

    """ testing str representation """
    def test_str(self):
        """ testing the str format """
        s = Square(4, 5, 1, 2)
        result = "[{}]({}) {}/{} - {}".format("Square\
", s.id, s.x, s.y, s.size)
        self.assertEqual(str(s), result)
        s = Square(4, 6, 8, 54)
        result = "[{}]({}) {}/{} - {}".format("Square\
", s.id, s.x, s.y, s.width, s.height)
        self.assertEqual(str(s), result)

    """ testing area"""
    def test_area(self):
        """ testing area of square """
        s = Square(5)
        self.assertEqual(s.area(), 25)

    """ testing the update function on id using args"""
    def test_updateId(self):
        """ creating class instance """
        s = Square(5, 4, 3, 2)
        self.assertEqual(s.id, 2)
        s.update(23)
        self.assertEqual(s.id, 23)

    """ testing the update function on x using args"""
    def test_x(self):
        """ creating class instance """
        s = Square(4, 5, 7)
        self.assertEqual(s.x, 5)
        s.update(4, 6, 11)
        self.assertEqual(s.x, 11)

    """ testing the update function on y using args"""
    def test_y(self):
        """ creating class instance """
        s = Square(3, 5, 7, 5)
        self.assertEqual(s.y, 7)
        s.update(4, 6, 1, 3)
        self.assertEqual(s.y, 3)

    """ testing the update function on size using args """
    def test_size(self):
        """ creating class instance """
        s = Square(4, 8, 7)
        self.assertEqual(s.size, 4)
        s.update(4, 11)
        self.assertEqual(s.size, 11)

    """ testing the update function on id using kwargs"""
    def test_updateId2(self):
        """ creating class instance """
        s = Square(5, 4, 3, 2)
        self.assertEqual(s.id, 2)
        s.update(id=23)
        self.assertEqual(s.id, 23)

    """ testing the update function on x using kwargs"""
    def test_x2(self):
        """ creating class instance """
        s = Square(4, 5, 7)
        self.assertEqual(s.x, 5)
        s.update(x=11)
        self.assertEqual(s.x, 11)

    """ testing the update function on y using kwargs"""
    def test_y2(self):
        """ creating class instance """
        s = Square(3, 5, 7, 5)
        self.assertEqual(s.y, 7)
        s.update(y=3)
        self.assertEqual(s.y, 3)

    """ testing the update function on size using kwargs """
    def test_size2(self):
        """ creating class instance """
        s = Square(4, 8, 7)
        self.assertEqual(s.size, 4)
        s.update(size=11)
        self.assertEqual(s.size, 11)

    """ testing the to_dictionary function """
    def test_dictionary(self):
        """ starting test """
        s1 = Square(10, 2, 1, 5)
        self.assertEqual(s1.to_dictionary(), {'id\
': 5, 'x': 2, 'size': 10, 'y': 1})

    """ test for a non empty string to to_json_string function """
    def test_json(self):
        """ starting test """
        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dict = s1.to_json_string([dictionary])
        self.assertEqual(json_dict, "[{'id': 8, 'size': 10, 'x': 7, 'y': 2}]")

    """ test for an empty string to to_json_string function """
    def test_empty_string(self):
        """ startin test"""
        dictionary = {}
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, '[]')

    """ testing for if the right type was returned """
    def test_type(self):
        """ starting test """
        s1 = Square(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        json_dict = s1.to_json_string([dictionary])
        self.assertEqual(type(json_dict), str)

    """ test for if none is passed to the 'save_to_file' function"""
    def test_save_to_file_None(self):
        """ beginning test """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            files = f.read()
        self.assertEqual(files, '[]')

    """ test for if 2 instances are passed to the 'save_to_file' function"""
    def test_save_to_file_obj(self):
        """ beginning test """
        files = ""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 0, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            files = f.read()
        self.assertEqual(files, "[{'id': 8, 'size': 10,\
 'x': 7, 'y': 2}, {'id': 2, 'size': 2, 'x': 4, 'y': 0}]")

    """ test for if 1 instance are passed to the 'save_to_file' function"""
    def test_save_to_file_object(self):
        """ beginning test """
        files = ""
        s = Square(2, 4, 0, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            files = f.read()
        self.assertEqual(files, "[{'id': 1, 'size': 2,\
 'x': 4, 'y': 0}]")

    """ testing the 'from_json_string' when None is passed """
    def test_from_json_None(self):
        """ beginning test """
        out = Square.from_json_string(None)
        self.assertEqual(out, [])

    """ testing the 'from_json_string' when empty list is passed """
    def test_from_json_empty(self):
        """ beginning test """
        out = Square.from_json_string([])
        self.assertEqual(out, [])

    """ testing the 'from_json_string' when json_string is passed """
    def test_from_json_str(self):
        list_input = [
                {'id': 89, 'size': 10},
                {'id': 7, 'size': 1}
                ]
        json_list_input = Square.to_json_string(list_input)
        out = Square.from_json_string(json_list_input)
        self.assertEqual(out,  [{'id': 89, 'size': 10}, {'\
id': 7, 'size': 1}])

    """ testing the create function """
    def test_create(self):
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))

    """ test for 'load_from_file' function for existing file"""
    def test_load_file(self):
        """ starting test """
        files = ""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 0, 0)
        Square.save_to_file([s1, s2])
        new_list = Square.load_from_file()
        self.assertEqual(str(s1), str(new_list[0]))
        self.assertEqual(str(s2), str(new_list[1]))

    """test for 'save_to_file_csv' function """
    def test_save_to_file_csv(self):
        """ beginning test """
        s1 = Square(7, 2, 8)
        s2 = Square(2, 4)
        list_square_input = [s1, s2]
        Square.save_to_file_csv(list_square_input)
        new_list = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(new_list[0]))
        self.assertEqual(str(s2), str(new_list[1]))
