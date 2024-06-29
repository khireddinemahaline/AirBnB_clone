#!/usr/bin/python3
"""storage file"""


import json
import os
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage Class : manipulate dictionary save and reload"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_object = {}
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """deserializes __objects to the JSON file (path: __file_path)"""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "State": State,
            "Place": Place,
            "Review": Review
        }
        try:
            with open(self.__file_path, 'r', encoding="utf8") as f:
                obj_dict = json.load(f)
            for obj_item in obj_dict.values():
                class_name = obj_item["__class__"]
                del obj_item["__class__"]
                self.new(eval(class_name)(**obj_item))
        except FileNotFoundError:
            pass