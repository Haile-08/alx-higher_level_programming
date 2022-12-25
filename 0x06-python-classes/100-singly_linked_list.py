#!/usr/bin/python3
"""Define a class node"""


class Node:
    """Represent a Likned list node"""

    def __init__(self, data, next_node=None):
        """initalize the node class
        args:
            data: the data input
            next_node: the next node input
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """a getter method for data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """a setter method for data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """a getter method for next node value"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """a setter method for the next node value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""Define a class SinglyLinkedList"""


class SinglyLinkedList:
    """Represent a singly Linked list"""

    def __init__(self):

