#!/usr/bin/python3
"""Define a function that retrun json object"""
import json


def to_json_string(my_obj):
    """Change to json object
    Args:
        my_obj: object input
    """
    return json.dumps(my_obj)
