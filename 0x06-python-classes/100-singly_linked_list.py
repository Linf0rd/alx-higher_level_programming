#!/usr/bin/python3
"""
Class Node that defines a node of a singly linked list.
"""


class Node:
    """
    Class Node that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The data value of the node.
            position (Node): The next node in the linked list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node.

        Returns:
            int: The data value of the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Args:
            value (int): The data value of the node..

        Raises:
            TypeError: If data is not an integer

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If next_node is not a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Class SinglyLinkedList that defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList instance.

        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the corrected sorted position in the list
        (increasing order).

        Args:
            value (int): The data value of the new Node.

        """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.

        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
