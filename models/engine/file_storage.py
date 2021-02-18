#!/usr/bin/python3
"""
serialization instances to a JSON
deserializes JSON to instnace
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """ class File storage """
    """ private class attributes"""
    __file_path = 'file.json'
    __objects = {}
    
    """public intance methods"""
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects and the obj with key"""
        key = obj.__class__.__name__ + '.' + str(obj.id)
        FileStorage.objects[key] = obj

    def save(self):
        """serializes the JSON file to __objects"""
        dict_to_parse = {}
        for key, value in FileStorage.__objects.items():
            dict_to_parse[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding= 'utf-8') as file:
            file.write(json.dumps(dict_to_parse))

    def reload(self):
        """deserialize the JSON file to __objects"""
        dict_to_obj = {}
        for key, value in dict_to_obj.items():
            cls_to_ins = cls_arr.get(value['__class__'])
            obj = cls_to_ins(**value)
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
            FileStorage.__objects[key] = obj
