#!/usr/bin/python3
"""Unittest module for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
    
    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def test_instantiation(self):
        """Test instantiation of BaseModel class."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_save(self):
        """Test save method of BaseModel class."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel class."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(type(model_dict["created_at"]), str)
        self.assertEqual(type(model_dict["updated_at"]), str)

    def test_str(self):
        """Test __str__ method of BaseModel class."""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

if __name__ == "__main__":
    unittest.main()
