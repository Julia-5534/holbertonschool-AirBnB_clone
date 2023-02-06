#!/usr/bin/python3
"""command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_emptyline(self):
        """do nothing when an empty line and "enter" is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
