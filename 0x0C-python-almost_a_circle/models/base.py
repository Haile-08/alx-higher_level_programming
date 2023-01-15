#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """Reprsent the base of all class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of the class
        Args:
            id: id attribute of classes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
