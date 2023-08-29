#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """This function prints x elements of a list."""
    try:
        lists = 0

        for item in my_list:
            if lists < x:
                print(num, end=" ")
                lists += 1

    except IndexError:
        print("Invalid Index")
