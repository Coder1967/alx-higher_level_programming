#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num_printed = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]))
            num_printed += 1
        except (ValueError, TypeError, IndexError):
            pass
        i += 1
    return num_printed
