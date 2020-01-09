#!/usr/bin/python3
class Square:
    """Represents a square with a size."""
    def __init__(self, size=None):
        """Initializes the size."""
        if size is not None:
            self._size = size
