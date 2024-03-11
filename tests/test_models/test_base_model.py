#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_id_creation(self):
        """Test if id is created correctly."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))

    def test_datetime_creation(self):
        """Test if created_at and updated_at are created correctly."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_str_method(self):
        """Test the __str__ method."""
        instance = BaseModel()
        expected_str = "[{}] ({}) {}".format(
            instance.__class__.__name__, instance.id, instance.__dict__)
        self.assertEqual(expected_str, str(instance))

    def test_save_method(self):
        """Test the save method."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual('BaseModel', instance_dict['__class__'])
        self.assertEqual(instance.id, instance_dict['id'])


if __name__ == "__main__":
    unittest.main()
