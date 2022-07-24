#!/usr/bin/python3
" function divides a matrix of integer "


def matrix_divided(matrix, div):
    new_matrix = [[] * i for i in range(len(matrix))]
    i, j = 0, 0
    matrix_len = len(matrix)
    each_len = 0

    " ensuring the right arguments were passed"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    elif type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    each_len = len(matrix[0])

    while i < matrix_len:
        j = 0
        if len(matrix[i]) != each_len:
            raise TypeError("Each row of the matrix must have the same size")
        while j < each_len:
            if type(matrix[i][j]) != float and type(matrix[i][j]) != int:
                raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")

            new_matrix[i].append(round(matrix[i][j] / div, 2))
            j += 1
        i += 1

    return new_matrix
