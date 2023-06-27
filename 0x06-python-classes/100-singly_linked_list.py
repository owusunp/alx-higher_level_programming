""""""""


I WILL CONTINUE THIS WORK LATER


""""""""



#!/usr/bin/python3
""" Singly Linked List """
class Node:
    def __init__(self, data, next_node=None):
        """
        args:
           data:
           next_node

        """
        self.__data = data 
        self.__next_node = next_node

    @property
    def data(self):
        """ returns data """
        return self.__data

    @data.setter
    def data(self, value):
        """ it settes the data """
        self.__data = value
        if isinstance(value, int):
            pass
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ returns next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ it sets the next node """
        self.__next_node = value
        if value is None:
            raise TypeError("next_node must be a Node object")
        
""" singly linke list class """
class SinglyLinkedList:
    def __init__(self, head = 0):
        """ initialize the head """
        self.__head = head

    
    def sorted_insert(self, value):
        """ printd out next """
        
        self.__head = value

        if self.__head is None:
            self.__head = value

        

        
        









