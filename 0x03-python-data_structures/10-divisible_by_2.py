#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = my_list.copy()
    for i in range(len(my_list)):
        if (n_list[i] % 2 == 0):
            n_list[i] = True
        else:
            n_list[i] = False
    return (n_list)
