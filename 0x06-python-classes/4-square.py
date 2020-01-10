#!/usr/bin/python3
class Square:
    """Represents a square with a size."""
    def __init__(self, size=0):
        """Initializes private instance attribute: size."""
        try:
            if type(size) is not int:
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer", end='')
            raise
        except ValueError:
            print("size must be >= 0", end='')
            raise

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
        try:
            if type(value) is not int:
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__size = value
        except TypeError:
            print("size must be an integer", end='')
            raise
        except ValueError:
            print("size must be >= 0", end='')
            raise
