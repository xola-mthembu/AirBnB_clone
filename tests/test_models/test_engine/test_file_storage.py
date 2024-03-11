#!/usr/bin/python3
"""
Unit Test for FileStorage Class
"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unit test for the class FileStorage"""

    def setUp(self):
        """Standard setup for all tests"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up tasks"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new adds an object to the storage dictionary"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save properly saves objects to file.json"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test that reload correctly loads objects from file.json"""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        key = f"BaseModel.{obj_id}"
        self.assertIn(key, objects)
        self.assertIsInstance(objects[key], BaseModel)

if __name__ == "__main__":
    unittest.main()
