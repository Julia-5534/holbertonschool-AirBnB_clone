#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """do nothing when an empty line and "enter" is entered"""


import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True
    
    def help_quit(self):
        """Prints the usage of quit command"""
        print("Quit the application.")
    
    def help_EOF(self):
        """Prints the usage of EOF command"""
        print("Quit the application using EOF signal.")

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        main
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
