#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num_printed = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return num_printed
