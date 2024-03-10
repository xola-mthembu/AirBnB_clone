#!/usr/bin/python3
"""
Module for BaseModel class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the instance's updated_at attribute to the current datetime
        and saves the object to the storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dict containing all keys/values of the instance's __dict__
        and adds the class name in __class__ key.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
