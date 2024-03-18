#!/usr/bin/python3
"""Unittest module for the Amenity class."""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""
    
    def setUp(self):
        """Set up test methods."""
        self.amenity = Amenity()

    def test_instantiation(self):
        """Test instantiation of Amenity class."""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

if __name__ == "__main__":
    unittest.main()
