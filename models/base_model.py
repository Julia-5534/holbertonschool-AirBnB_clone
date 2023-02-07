#!/usr/bin/python3
"""Base Model for AirBnB Clone"""

import uuid
import datetime
import models


class BaseModel:
    """Base Model Stuff"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for ky, vl in kwargs.items():
                if ky != '__class__':
                    setattr(self, ky, vl)
                    if ky in ('created_at', 'updated_at'):
                        setattr(self, ky, datetime.datetime.
                                strptime(vl, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        booboo = self.__class__.__name__
        return "[{}] ({}) {}".format(booboo, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        dict_base = self.__dict__.copy()
        dict_base["__class__"] = self.__class__.__name__
        dict_base["created_at"] = self.created_at.isoformat()
        dict_base["updated_at"] = self.updated_at.isoformat()
        return dict_base
