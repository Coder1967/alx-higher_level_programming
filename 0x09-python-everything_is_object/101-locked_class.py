#!/usr/bin/python3
""" creation of a class """


class LockedClass:
    """ saving space by assigning memory for only 'first_name
    using '__slots__'"""
    __slots__ = ["first_name"]
