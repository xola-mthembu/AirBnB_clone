#!/usr/bin/python3
"""Unittest module for the Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""
    
    def setUp(self):
        """Set up test methods."""
        self.review = Review()

    def test_instantiation(self):
        """Test instantiation of Review class."""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

if __name__ == "__main__":
    unittest.main()
