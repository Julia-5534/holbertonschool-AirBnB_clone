#!/usr/bin/python3
"""Base Model for AirBnB Clone
class BaseModel: def init(self, *args, **kwargs):
self.id = uuid.uuid4().hex self.createdat = datetime.datetime.now() self.updatedat = datetime.datetime.now()
if kwargs: for key, value in kwargs.items():
if key != 'class': setattr(self, key, value) if key == 'createdat' or key == 'updatedat':
setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))

def __str__(self):
    return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

def save(self):
    self.updated_at = datetime.datetime.now()

def to_dict(self):
    dict_base = dict(self.__dict__)
    dict_base['__class__'] = self.__class__.__name__
    dict_base['created_at'] = self.created_at.isoformat()
    dict_base['updated_at'] = self.updated_at.isoformat()
    return dict_base
"""


import uuid
from datetime import datetime

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
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
