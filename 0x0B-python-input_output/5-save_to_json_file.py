#!/usr/bin/python3
"""Define a funciton that write a object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """save to a json file
    Args:
        my_obj: object input
        filename: string input
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
