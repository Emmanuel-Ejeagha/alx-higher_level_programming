#!/bin/usr/python3
"""This script contains JSON"""


import json


def save_to_json_file(my_obj, filename):
    """
    this function writes an Object to a text file,
    using a JSON representation:
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
