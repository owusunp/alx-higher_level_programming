#!/usr/bin/python3


""" LIL DESCRIPTION ABOUT THE CLASS DOWN HERE """


class Base:
    """
    The Base class represents a base object.

    Attributes:
        __nb_objects (int): The total number of Base objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The identifier for the object. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

