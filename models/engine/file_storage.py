#!/usr/bin/python3
"""
Defines FileStorage class to serialize and deserialize JSON files.
"""
import json


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        # Add other model imports here if necessary, e.g.:
        # from models.user import User
        # from models.review import Review
        # etc.

        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                cls = globals()[cls_name]
                self.new(cls(**obj))
        except FileNotFoundError:
            pass
