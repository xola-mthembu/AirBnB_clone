#!/usr/bin/python3
"""
Defines FileStorage class to serialize and deserialize JSON files.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    # Updated class dictionary mapping to include new classes
    class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self, cls=None):
        """Returns the dictionary __objects, possibly filtered by class."""
        if cls:
            filtered_objects = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    filtered_objects[key] = value
            return filtered_objects
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                cls = self.class_dict.get(cls_name)
                if cls:
                    self.new(cls(**obj))
        except FileNotFoundError:
            pass
