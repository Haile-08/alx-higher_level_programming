#!/usr/bin/python3
"""Define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprsent a Rectangle"""

    def __init__(self, width, height):
        """constructor
        Args:
            width: integer input
            height: integer input
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
