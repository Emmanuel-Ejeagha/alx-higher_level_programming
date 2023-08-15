#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        k = 1
        for j in x:
            print("{:d}".format(j), end="")
            if len(x) > k:
                print(end=" ")
            k += 1
        print(end="\n")
