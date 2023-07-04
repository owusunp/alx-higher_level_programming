#!/usr/bin/python3


""" this is my list class """
class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Methods:
        print_sorted(): Prints the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

