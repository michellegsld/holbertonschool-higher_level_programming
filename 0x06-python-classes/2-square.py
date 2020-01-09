#!/usr/bin/python3
class Square:
    """Represents a square with a size."""
    def __init__(self, size=0):
        """Initializes the size."""
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
