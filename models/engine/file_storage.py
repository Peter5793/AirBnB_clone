#!/usr/bin/python3
"""
Serialization & deserialization of JSON file
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    class that serializes JSON file 
    private class atributes 
    """
    __file_path = 'file.json'
    __objects = {} 

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        key = obj.__class__.__name__+ '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the JSON file to __objects"""
        dict_to_parse = {}
        for key, value in FileStorage.__objects.items():
            dict_to_parse[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding= 'utf-8') as file:
            file.write(json.dumps(dict_to_parse))

    def reload(self):
        """
        deserialize the Json file to __objects
        """
        dict_to_obj = {}
        try:
            cls_arr = {"BaseModel": BaseModel}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                dict_to_obj = json.load(file)
                for key, value in dict_to_obj.items():
                    cls_to_ins =cls_arr.get(value['__class__'])
                    obj = cls_to_ins(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
