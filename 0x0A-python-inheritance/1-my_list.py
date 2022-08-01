#!/usr/bin/python3

""" creating class MyList """


class MyList(list):
    """ creating a function that sorts the list using bubble sort"""
    def __init__(self):
        """initializing class"""
        super().__init__()
    def print_sorted(self):
        print(sorted(self))
