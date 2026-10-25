#!/usr/bin/env python3
"""Module for reading UTF-8 text files."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 text file."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
