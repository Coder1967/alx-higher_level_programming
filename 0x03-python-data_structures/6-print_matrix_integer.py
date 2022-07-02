#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
             print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
