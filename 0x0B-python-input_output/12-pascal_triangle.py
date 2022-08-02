#!/usr/bin/python3
"""
returns a list of list of pascal's triangle
"""


def pascal_triangle(n):
    if n == 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        mini_tri = triangles[-1]
        tmp = [1]
        for i in range(len(mini_tri) - 1):
            tmp.append(mini_tri[i] + mini_tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
