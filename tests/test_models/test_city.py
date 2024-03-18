#!/usr/bin/python3
"""Unittest module for the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""
    
    def setUp(self):
        """Set up test methods."""
        self.city = City()

    def test_instantiation(self):
        """Test instantiation of City class."""
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

if __name__ == "__main__":
    unittest.main()
