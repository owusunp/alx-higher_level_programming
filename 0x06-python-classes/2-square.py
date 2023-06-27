#!/usr/bin/python3
""" we stil on square """
class Square:
    """ we still on square """
    def __init__(self, size=0):
        """
        arg:
        size which is provate

        """
        self.__size = size

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        


