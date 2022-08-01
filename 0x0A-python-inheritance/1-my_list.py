#!/usr/bin/python3

""" creating class MyList """


class MyList(list):
    """ creating a function that sorts the list using bubble sort"""
    def print_sorted(self):
        sorted_list = list(map(lambda x: x, self))
        i, j = 0, 0
        check, tmp = 0, 0

        while (i < len(self)):
            check = 0
            while j < len(self) - 1:
                if sorted_list[j] > sorted_list[j + 1]:
                    tmp = sorted_list[j + 1]
                    sorted_list[j + 1] = sorted_list[j]
                    sorted_list[j] = tmp
                    check = 1
                j += 1
            if check == 0:
                break
            i += 1
        print(list(sorted_list))
