#!/usr/bin/python3
"""test for the rectangle module """
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class Test_rectangle(TestCase):
    """tests for Rectangle class """
    def test_attribute_set(self):
        rec1 = Rectangle(5, 10, 7, 8, 78)
        self.assertEqual(rec1.width, 5)
        self.assertEqual(rec1.height, 10)
        self.assertEqual(rec1.x, 7)
        self.assertEqual(rec1.y, 8)
        self.assertEqual(rec1.id, 78)
        rec1.width = 65
        rec1.height = 45
        rec1.x = 5
        rec1.y = 54
        self.assertEqual(rec1.width, 65)
        self.assertEqual(rec1.height, 45)
        self.assertEqual(rec1.x, 5)
        self.assertEqual(rec1.y, 54)

    """ tests for if the class was properly inherited"""
    def test_subclass(self):
        """ test if it Rectangle object is a subclass of Base """
        rec1 = Rectangle(8, 7)
        self.assertTrue(issubclass(type(rec1), Base))

    """ testing for type and value Errors of width"""
    def test_width_error(self):
        """ for if the wrong value is passed """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-4, 8, 7, 9)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 98, 6, 5)
            r = Rectangle({8, 9, 87}, 98, 6, 5)
            r = Rectangle(None, 98, 6, 5)
    """ tests for value and type error of height """
    def test_height_error(self):
        """ test for if the wrong value for height is passed """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(4, -8, 7, 9)
            r = Rectangle(10, 0, 8, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(67, True, 6, 5)
            r = Rectangle(5, {8, 9, 87}, 6, 5)
            r = Rectangle(98, None, 6, 5)

    """ tests for value and type error for x """
    def test_x_errors(self):
        """ tests for if invalid value is passed to for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(2, 3, -1, 6)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(98, 6, True, 5)
            r = Rectangle(98, 6, [8, 6, 5], 5)
            r = Rectangle(98, 6, None, 5)

    def test_y_errors(self):
        """tests for if invalid value is passed for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(2, 3, 1, -6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(98, 6, 5, True)
            r = Rectangle(98, 6, 5, [8, 6, 5])
            r = Rectangle(98, 6, 5, None)

    """ test for the area of the rectangle """
    def test_area(self):
        """ checks area of rectangle """
        r = Rectangle(12, 10)
        self.assertEqual(r.area(), 120)
        r = Rectangle(5, 8)
        self.assertEqual(r.area(), 40)

    """ test for printing out the rectangle to stdout """
    def test_display(self):
        """ checking if displayed properly"""
        r = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n##\n")

    """ test for the str of the instance"""
    def test_str(self):
        """ testing the str format """
        r = Rectangle(4, 5, 1, 2, 3)
        result = "[{}]({}) {}/{} - {}/{}".format("Rectangle\
", r.id, r.x, r.y, r.width, r.height)
        self.assertEqual(str(r), result)
        r = Rectangle(4, 6, 8, 54, 3)
        result = "[{}]({}) {}/{} - {}/{}".format("Rectangle\
", r.id, r.x, r.y, r.width, r.height)
        self.assertEqual(str(r), result)

    """ testing the update function on id using args"""
    def test_updateId(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.id, 9)
        r.update(5)
        self.assertEqual(r.id, 5)

    """ testing the update function on width using args"""
    def test_updateWidth(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.width, 3)
        r.update(4, 6)
        self.assertEqual(r.width, 6)

    """ testing the update function on height using args"""
    def test_updateHeight(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.height, 5)
        r.update(4, 6, 1)
        self.assertEqual(r.height, 1)

    """ testing the update function on x using args"""
    def test_x(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.x, 7)
        r.update(4, 6, 1, 11)
        self.assertEqual(r.x, 11)

    """ testing the update function on y using args"""
    def test_y(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.y, 5)
        r.update(4, 6, 1, 11, 3)
        self.assertEqual(r.y, 3)

    """ testing the update function on id using kwargs"""
    def test_updateId2(self):
        """ creating class instances """
        r = Rectangle(5, 3, 4, 21, 5)
        self.assertEqual(r.id, 5)
        r.update(id=6)
        self.assertEqual(r.id, 6)

    """ testing the update function on width using kwargs"""
    def test_updateWidth2(self):
        """ creating class instance """
        r = Rectangle(4, 6)
        self.assertEqual(r.width, 4)
        r.update(width=6)
        self.assertEqual(r.width, 6)

    """ testing the update function on height using kwargs"""
    def test_updateHeight2(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.height, 5)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    """ testing the update function on x using kwargs"""
    def test_x2(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.x, 7)
        r.update(x=11)
        self.assertEqual(r.x, 11)

    """ testing the update function on y using kwargs"""
    def test_y2(self):
        """ creating class instance """
        r = Rectangle(3, 5, 7, 5, 9)
        self.assertEqual(r.y, 5)
        r.update(y=3)
        self.assertEqual(r.y, 3)

    """ testing the to_dictionary function """
    def test_to_dictionary(self):
        """ beginning test """
        r = Rectangle(10, 2, 1, 9, 3)
        self.assertEqual(r.to_dictionary(), {'x': 1, 'y': 9, 'id': 3, '\
height': 2, 'width': 10})

    """ test for a non empty string to to_json_string function """
    def test_json(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, "[{'id': 1, 'width': 10, 'height': 7, '\
x': 2, 'y': 8}]")

    """ test for an empty string to to_json_string function """
    def test_empty_string(self):
        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, '[]')

    """ test for if none is passed to the 'save_to_file' function"""
    def test_save_to_file_None(self):
        """ beginning test """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            files = f.read()
        self.assertEqual(files, '[]')

    """ test for if 2 instances are passed to the 'save_to_file' function"""
    def test_save_to_file_obj(self):
        """ beginning test """
        files = ""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            files = f.read()
        self.assertEqual(files, "[{'id': 1, 'width': 10, 'height': 7\
, 'x': 2, 'y': 8}, {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}]")

    """ test for if 1 instance are passed to the 'save_to_file' function"""
    def test_save_to_file_object(self):
        """ beginning test """
        files = ""
        r = Rectangle(2, 4, 0, 0, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            files = f.read()
        self.assertEqual(files, "[{'id': 1, 'width': 2,\
 'height': 4, 'x': 0, 'y': 0}]")

    """ testing the 'from_json_string' when None is passed """
    def test_from_json_None(self):
        """ beginning test """
        out = Rectangle.from_json_string(None)
        self.assertEqual(out, [])

    """ testing the 'from_json_string' when empty list is passed """
    def test_from_json_empty(self):
        """ beginning test """
        out = Rectangle.from_json_string([])
        self.assertEqual(out, [])

    """ testing the 'from_json_string' when json_string is passed """
    def test_from_json_str(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        out = Rectangle.from_json_string(json_list_input)
        self.assertEqual(out,  [{'id': 89, 'width': 10, 'height': 4}, {'\
id': 7, 'width': 1, 'height': 7}])

    """ testing the create function """
    def test_create(self):
        """ beginning test """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    """ test for 'load_from_file' function"""
    def test_load_file(self):
        """ starting test """
        files = ""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        new_list = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(new_list[0]))
        self.assertEqual(str(r2), str(new_list[1]))

    """test for 'save_to_file_csv' function """
    def test_save_to_file_csv(self):
        """ beginning test """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        new_list = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(new_list[0]))
        self.assertEqual(str(r2), str(new_list[1]))
