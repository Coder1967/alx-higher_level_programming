#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    worse_case = (0, 0)
    "concatenating zeros to the tuples in case one or\
    two digits are missing"
    tuple_a += worse_case
    tuple_b += worse_case
    neo_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return neo_tuple
