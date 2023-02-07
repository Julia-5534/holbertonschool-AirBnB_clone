#!/usr/bin/python3
"""Base Model for AirBnB Clone"""

<<<<<<< HEAD
from typing import Self
=======
>>>>>>> main
import uuid
import datetime
import models


class BaseModel:
    """Base Model Stuff"""
<<<<<<< HEAD
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
=======
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        booboo = self.__class__.__name__
        return "[{}] ({}) {}".format(booboo, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save(self)
>>>>>>> main

    def to_dict(self):
        dict_base = self.__dict__.copy()
        dict_base["__class__"] = self.__class__.__name__
        dict_base["created_at"] = self.created_at.isoformat()
        dict_base["updated_at"] = self.updated_at.isoformat()
        return dict_base
