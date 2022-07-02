#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    checker = []
    length = len(my_list)
    i = 0

    while i < length:
        if my_list[i] % 2 == 0:
            checker.append(1)
        else:
            checker.append(0)
        i += 1
    return checker
