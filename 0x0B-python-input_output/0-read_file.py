#!/usr/bin/python3
"""
    This function reads a file
"""

def read_file(filename=""):
    """
    Reads a file and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as my_file:
        print(my_file.read(), end="")
