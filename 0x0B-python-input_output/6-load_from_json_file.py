#!/usr/bin/python3
"""This script contains JSON"""


import json


def load_from_json_file(filename):
    """this function that creates an Object from a “JSON file”:"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
