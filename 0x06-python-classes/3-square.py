#!/usr/bin/python3
""" on square classs """

class Square:
    """
    class Square that defines a squar

    """

    def __init__(self, size = 0):
        """
        args:
        size must be an integer

        """

        self.__size = size
        
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    def area(self):
        
        """ the square of an area """
        return self.__size*self.__size

