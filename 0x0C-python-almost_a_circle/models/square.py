#!/usr/bin/python3
"""Define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initilize a class
        Args:
            
