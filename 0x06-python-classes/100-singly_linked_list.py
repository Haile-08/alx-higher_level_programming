#!/usr/bin/python3
"""Define a class node"""


class Node:
    """Represent a Likned list node"""

    def __init__(self, data, next_node=None):
        """initalize the data
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
        """Initialize the data"""
        self.__head = None

    def sorted_insert(self, value):
        """Method to sorted insert
        args:
            value: the input data
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node
    def __str__(self):
        """Define the print() representaion of a linked list"""
        value = []
        temp = self.__head
        while temp is not None:
            value.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(value))
