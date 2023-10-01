#!/usr/bin/python3
"""
Contains a function that appends a string
"""


def append_write(filename="", text=""):
    """
    function that appends a string and returns the num of char
    """
    with open("filename", 'a', encoding="utf-8") as f:
        return f.write(text)
