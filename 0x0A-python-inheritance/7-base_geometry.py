#!/usr/bin/python3
"""Define a class base geometry"""


class BaseGeometry:
    """Reprsent a base geometry"""

    def area(self):
        """Area of the base geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integr validator
        Args:
            name: string input
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
