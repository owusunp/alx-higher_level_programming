#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            k = len(i)
            if j == i[k -1]:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print()
