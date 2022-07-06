#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_list = list(set(my_list))
    total = 0
    for item in my_list:
        total += item

    return total
