#!/usr/bin/python3
"""
This script writes a text
"""

def write_file(filename="", text=""):
    """returns the number of file written
    """
    with open(filename="", 'w', encoding="utf-8") as f:
        return f.write(text)
