#!/usr/bin/python3
"""Define a funciton that create object"""
import json


def load_from_json_file(filename):
    """Load json from a file
    Args:
        filename: string input
    """
    with open(filename) as f:
        return json.load(f)
