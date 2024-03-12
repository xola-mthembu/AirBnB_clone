#!/usr/bin/python3
"""
Defines FileStorage class to serialize and deserialize JSON files.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    # Class dictionary mapping to ensure the correct class is called.
    class_dict = {
        'BaseModel': BaseModel,
        # Include other model classes here as needed
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {
            obj: self.__objects[obj].to_dict() for obj in self.__objects
        }
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                cls = self.class_dict[cls_name]
                self.new(cls(**obj))
        except FileNotFoundError:
            pass
