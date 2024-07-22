#!/usr/bin/python3
""" BaseModel from another one by using a dictionary representation"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        obj_clsname = obj.__class__.__name__
        key = "{}.{}".format(obj_clsname, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """ serializes __objects to the JSON file"""
        objects = FileStorage.__objects
        objects_dict = {}
        for obj in objects.keys():
            objects_dict = objects[obj].to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file(__file_path)exists ; otherwise, do nothing)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    objects_dict = json.load(f)
                    for key, value in objects_dict.items():
                        class_name, obj_id = key.split('.')
                        new_class = eval(class_name)
                        new_instance = new_class(**values)
                        FileStorage.__objects[key] = new_instance
                except Exception:
                    pass
