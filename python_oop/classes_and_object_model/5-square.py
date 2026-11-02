#!/usr/bin/env python3
"""Defines a Square class that can print its shape."""


class Square:
    """Represents a square with a private size."""

    def __init__(self, size=0):
        """Initialize the square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the square size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        for i in range(self.__size):
            print("#" * self.__size)
