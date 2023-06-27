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

    @property
    def size(self):
        """ returns the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ it is a setter """
        self.__size = value
        if isinstance(value, int):
            
            if value < 0:
                raise ValueError("size must be >= 0")
                
        else:
            raise TypeError("size must be an integer")


    def area(self):
        
        """ the square of an area """
        return self.__size*self.__size

    def my_print(self):
        """ prints some #"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

