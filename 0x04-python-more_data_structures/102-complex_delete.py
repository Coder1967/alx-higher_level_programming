#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    li = []
    if value not in a_dictionary.values():
        return a_dictionary
    for i in a_dictionary:
        if a_dictionary[i] == value:
            li.append(i)
    for i in li:
        del a_dictionary[i]
    return a_dictionary
