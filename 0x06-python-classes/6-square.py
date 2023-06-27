#!/usr/bin/python3
""" on square classs """

class Square:
    """
    class Square that defines a squar

    """

    def __init__(self, size = 0, position=(0, 0)):
        """
        args:
        size must be an integer

        """

        self.__size = size
        self.__position = position

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
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if isinstance(value, tuple):
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
   


    def area(self):
        
        """ the square of an area """
        return self.__size*self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
