#!/usr/bin/python3
"""Unittest module for the State class."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""
    
    def setUp(self):
        """Set up test methods."""
        self.state = State()

    def test_instantiation(self):
        """Test instantiation of State class."""
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

if __name__ == "__main__":
    unittest.main()
