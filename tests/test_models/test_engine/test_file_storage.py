#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects.clear()
        self.storage._FileStorage__file_path = "test_file.json"

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass
        self.storage._FileStorage__objects.clear()

    def test_all(self):
        """Test the all method."""
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)
        self.assertEqual(len(objs), 0)

        model = BaseModel()
        self.storage.new(model)
        objs = self.storage.all()
        self.assertEqual(len(objs), 1)
        self.assertIn("{}.{}".format(model.__class__.__name__, model.id), objs)

    def test_new(self):
        """Test the new method."""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], model)

    def test_save(self):
        """Test the save method."""
        self.storage.save()
        self.assertTrue(os.path.exists("test_file.json"))

        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        with open("test_file.json", "r") as file:
            content = json.load(file)
        self.assertIn("{}.{}".format(model.__class__.__name__, model.id), content)

    def test_reload(self):
        """Test the reload method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(str(self.storage._FileStorage__objects[key]), str(model))

    def test_valid_classes(self):
        """Test valid classes."""
        classes = self.storage.classes()
        self.assertIn("BaseModel", classes)
        self.assertIn("User", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Place", classes)
        self.assertIn("Review", classes)

        model = BaseModel()
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        self.assertIsInstance(model, classes["BaseModel"])
        self.assertIsInstance(user, classes["User"])
        self.assertIsInstance(state, classes["State"])
        self.assertIsInstance(city, classes["City"])
        self.assertIsInstance(amenity, classes["Amenity"])
        self.assertIsInstance(place, classes["Place"])
        self.assertIsInstance(review, classes["Review"])

if __name__ == "__main__":
    unittest.main()
