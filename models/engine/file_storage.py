#!/usr/bin/python3
"""FILE STORAGE MODULE"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """STORE NEW FILES"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """RETURN ALL FILES"""
        return self.__objects

    def new(self, obj):
        """NEW OBJECT"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """SAVE FILES"""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def save(self):
        """Serializes __objects to the Jason :P file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            banan = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(banan, f)

    def reload(self):
        """RELOAD FILES"""
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                BANANAPANTS = json.load(f)
                for key, value in BANANAPANTS.items():
                    obj = eval(value['__class__'])(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
