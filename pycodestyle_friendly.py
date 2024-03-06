#!/usr/bin/python3
"""
This module demonstrates adherence to Pycodestyle standards.
The module provides a simple example class and associated methods,
all formatted according to Pycodestyle guidelines.
"""


class StyleConscious:
    """A class that adheres to Pycodestyle standards."""

    def __init__(self, message):
        """Initialize the class with a message."""
        self.message = message

    def display_message(self):
        """Print the message to standard output."""
        print(self.message)


def run_example():
    """Create an instance of StyleConscious and call the display method."""
    example = StyleConscious("Hello, Pycodestyle!")
    example.display_message()


if __name__ == "__main__":
    run_example()
