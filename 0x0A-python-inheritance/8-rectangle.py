#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define a class Rectangle"""


class Rectangle(BaseGeometry):
    """Reprsent a Rectangle"""

    def __init__(self, width, height):
        """constructor
        Args:
            width: integer input
            height: integer input
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
