#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    highest = 0
    name = ""
    for i in a_dictionary:
        if a_dictionary[i] > highest:
            highest = a_dictionary[i]
            name = i
    return name
