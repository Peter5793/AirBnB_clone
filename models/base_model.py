#!/usr/bin/python3
"""Base class """
from uuid import uuid4
from datetime import datetime
#import models

class BaseModel:
    """Public instance attributes intialization"""
    def __init__(self, *args, **kwargs):
       self.id = str(uuid4())
       self.created_at = datetime.now()
       self.updated_at = datetime.now()
       if len(kwargs) > 0:
            convert = ["created_at", "updated_at"]
            for key, value in kwargs.items():
                if key in convert:
                    setattr(self, key, 
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

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