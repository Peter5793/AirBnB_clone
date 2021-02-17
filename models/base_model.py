#!/usr/bin/python3
"""Base class """
from uuid import uuid4
from datetime import datetime
#import models

class BaseModel:
    """Public instance attributes intialization"""
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """
        updates the public instance attribute with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictioanry containing all  keys/valu of __dict__
        """
        l_dict = self.__dict__
        dict_str = {}
        for key, value in l_dict.items():
            if isinstance(value, datetime):
                dict_str[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict_str[key] = value
        dict_str["__class__"] = self.__class__.__name__
        return dict_str
