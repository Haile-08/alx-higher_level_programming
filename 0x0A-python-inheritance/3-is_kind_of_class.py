#!/usr/bin/python3
"""Define a funciton to find the instance of the object"""


def is_kind_of_class(obj, a_class):
    """is kind of class
    Args:
        obj: the object input
        a_class: the class input
    Returns:
        True if the object is an instance of
        else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
