#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    "test for max_integer function"
    def test_max(self):
        self.assertEqual(max_integer([6, 7, 9]), 9)
        self.assertEqual(max_integer("hello"), 'o')
