#!/usr/bin/python3
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import storage

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def destroy_all(cls):
        """DEEESTROYER OF ALLLLLL"""
        cls.__objects = {}
    
    def get(self, key):
        return FileStorage.__objects.get(key)
    
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
