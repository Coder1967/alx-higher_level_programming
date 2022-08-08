#!/usr/bin/python3
""" definition of class to run unnitest """
from unittest import TestCase
from models.base import Base


class Base_tests(TestCase):
    """ test for id"""
    def test_id(self):
        """ tests the id"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)
        self.assertEqual(base2.id, base1.id + 1)
        base3 = Base(45)
        self.assertEqual(base3.id, 45)
    """ tests the object type """
    def test_class(self):
        """ tests the name of the class """
        base3 = Base()
        self.assertEqual(type(base3).__name__, "Base")

    """ for if too many arguments is passed """
    def test_tooMuch_args(self):
        """ tests for too much arguments"""
        with self.assertRaises(TypeError):
            b = Base(5, 4, 5)

    """ test for if an empty list is passed to to_json_string function """
    def test_empty_json_string(self):
        """ beginning test """
        b = Base()
        mdic = {}
        json_dict = Base.to_json_string([mdic])
        self.assertEqual(json_dict, '[]')
        self.assertEqual(type(json_dict).__name__, 'str')

    """ test for if a non empty list is passed to to_json_string function """
    def test_empty_json_string(self):
        """ beginning test """
        b = Base(5)
        mdic = {"id": 5}
        json_dict = Base.to_json_string([mdic])
        self.assertEqual(json_dict, "[{'id': 5}]")
        self.assertEqual(type(json_dict).__name__, 'str')
