#!/usr/bin/python3
"""
Module for the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Method called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
