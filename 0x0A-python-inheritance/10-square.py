#!/usr/bin/python3

""" LETS DO THIS INHERITANCE """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        __size (int): The size (side length) of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance.
        area(self): Calculates and returns the area of the square.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size (side length) of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        # Call the parent class's __init__ method

        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string in the format "[Square] size/size".
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

