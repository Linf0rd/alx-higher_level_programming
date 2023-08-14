#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x, num in enumerate(row):
            if x != len(row) - 1:
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num))
