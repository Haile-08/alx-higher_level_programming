#!/usr/bin/python3
"""Define a function that to find instance of an object"""


def is_same_class(obj, a_class):
    """is same class
    Args:
        obj: object input
        a_class: class input
    Returns:
        True if the object is exactly an instance of the specified
        class else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
