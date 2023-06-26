#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: int(x)*int(x), row)) for row in matrix]
