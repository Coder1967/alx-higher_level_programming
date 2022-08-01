#!/usr/bin/python3

""" creating class MyList """


class MyList(list):
    """ creating a function that sorts the list using bubble sort"""
    def print_sorted(self):
        print(sorted(self))


