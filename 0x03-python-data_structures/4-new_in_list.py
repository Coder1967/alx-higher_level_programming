#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    neo_list = []
    i = 0
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return my_list
    while i <= length:
        neo_list.append(my_list[i])
        i += 1
    neo_list[idx] = element
    return neo_list
