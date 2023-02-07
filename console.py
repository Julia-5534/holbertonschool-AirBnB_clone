#!/usr/bin/python3
"""Console for HBnB Project"""
"""Poop"""
import cmd
from models.base_model import *
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class for HBNB command interpreter"""

    prompt = '(hbnb) '
    cls_lst = ["Review", "Place", "State",
               "User", "BaseModel", "City", "Amenity"]

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing when an empty line and "enter" is entered"""
        pass

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        m = self.classes[class_name]()
        m.save()
        print(m.id)

    def do_show(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = self.classes[class_name].all()
        found = False
        for obj in objs:
            if obj.id == obj_id:
                print(obj)
                found = True
                break
        if not found:
            print("** no instance found **")

    def do_destroy(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = self.classes[class_name].all()
        found = False
        for obj in objs:
            if obj.id == obj_id:
                obj.delete()
                found = True
                break
        if not found:
            print("** no instance found **")

    def do_all(self, args):
        if len(args) == 0:
            for obj in BaseModel.all():
                print(obj)
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            for obj in self.classes[class_name].all():
                print(obj)

    def do_update(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        objs = self.classes[class_name].all()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
