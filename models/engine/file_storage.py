#!/usr/bin/python3
"""
Defines FileStorage class to serialize and deserialize JSON files.
"""
import json
from models.base_model import BaseModel
from models.user import User  # Import User class


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    # Updated class dictionary mapping to include the User class
    class_dict = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                cls = FileStorage.class_dict.get(cls_name)
                if cls:
                    self.new(cls(**obj))
        except FileNotFoundError:
            pass
