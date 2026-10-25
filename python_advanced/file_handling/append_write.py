#!/usr/bin/env python3
"""Module for appending text to UTF-8 files."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
