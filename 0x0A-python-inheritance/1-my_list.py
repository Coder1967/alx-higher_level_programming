#!/usr/bin/python3

""" creating class MyList """


class MyList(list):
    """ creating a function that sorts the list using bubble sort"""
    def print_sorted(self):
        i, j = 0, 0
        check, tmp = 0, 0

        while (i < len(self)):
            check = 0
            while j < len(self) - 1:
                if self[j] > self[j + 1]:
                    tmp = self[j + 1]
                    self[j + 1] = self[j]
                    self[j] = tmp
                    check = 1
                j += 1
            if check == 0:
                break
            i += 1
        print(list(self))
