#!/usr/bin/python3
"""Define a fucniton that checks class is inherited"""


def inherits_from(obj, a_class):
    """inherits from
    Args:
        obj: the object input
        a_class: the class input
    Returns:
        True if class is inherited
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
