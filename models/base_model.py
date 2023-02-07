#!/usr/bin/python3
"""Base Model for AirBnB Clone"""

from typing import Self
import uuid
import datetime
from models.engine.file_storage import FileStorage

class BaseModel:
    """Base Model Stuff"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_base = self.__dict__.copy()
        dict_base["__class__"] = self.__class__.__name__
        dict_base["created_at"] = self.created_at.isoformat()
        dict_base["updated_at"] = self.updated_at.isoformat()
        return dict_base
