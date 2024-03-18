#!/usr/bin/python3
"""Unittest module for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""
    
    def setUp(self):
        """Set up test methods."""
        self.user = User()

    def test_instantiation(self):
        """Test instantiation of User class."""
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()
