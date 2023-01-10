#!/usr/bin/python3
"""Define a funciton retrun object"""
import json


def from_json_string(my_str):
    """From json to string
    Args:
        my_str: string input
    """
    return json.loads(my_str)
