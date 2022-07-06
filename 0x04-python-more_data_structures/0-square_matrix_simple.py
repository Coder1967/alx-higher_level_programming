#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    length = len(matrix)
    my_list = [[] * i for i in range(length)]
    i = 0

    while i < length:
        my_list[i] = list(map((lambda x: x * x), matrix[i]))
        i += 1
    return my_list
