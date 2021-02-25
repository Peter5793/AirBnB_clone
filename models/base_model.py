#!/usr/bin/python3
"""
Base model
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    defines the common attributes
    """
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                    self.__dict__))
    def save(self):
        """
        Updates te public instance attibute updated_at
        """
        self.updated_at = datetime.now()
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        l_dict = self.__dict__
        dict_str  = {}
        for k, v in l_dict.items():
            if isinstance(v, datetime):
                dict_str[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict_str[k] = v
        dict_str["__class__"] = self.__class__.__name__
        return dict_str
