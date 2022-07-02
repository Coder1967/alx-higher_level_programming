#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
            print("{}".format(columns), end=" ")
        print()
