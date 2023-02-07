#!/usr/bin/python3
"""Console for HBnB Project"""
"""Adding A Comment So I Can Commit & Push"""
import cmd
from models.base_model import *


class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing when an empty line and "enter" is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
