#!/usr/bin/python3
class Square:
    """Represents a square with a size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes private instance attribute: size."""
        if type(size) is not int:
            raise TypeError("size must be an integer", end='')
        elif size < 0:
            raise ValueError("size must be >= 0", end='')
        else:
            self.__size = size
        if type(position) is not tuple or len(position) is not 2:
            raise TypeError("position must be a tuple \
            of 2 positive integers", end='')
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple \
            of 2 positive integers", end='')
        elif type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple \
            of 2 positive integers", end='')
        else:
            self.__position = position

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrives the private instance attribute: size."""
        return self.__size

    @size.setter
    def size(self, value):
        """A property setter to set size."""
        if type(value) is not int:
            raise TypeError("size must be an integer", end='')
        elif value < 0:
            raise ValueError("size must be >= 0", end='')
        else:
            self.__size = value

    @property
    def position(self):
        """Retrives the private instance attribute: position."""
        return self.__position

    @position.setter
    def position(self, value):
        """A property setter to set position."""
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple \
            of 2 positive integers", end='')
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple \
            of 2 positive integers", end='')
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple \
            of 2 positive integers", end='')
        else:
            self.__position = value

    def my_print(self):
        """Prints in stdout the square."""
        if self.__size is 0:
            print()
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
