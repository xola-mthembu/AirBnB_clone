#!/usr/bin/python3
"""FileStorage class"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serialize and deserialize instances to and from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_data in obj_dict.values():
                    cls_name = obj_data['__class__']
                    del obj_data['__class__']
                    self.new(eval(cls_name)(**obj_data))

    def classes(self):
        """Return a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
