#!/usr/bin/python3
"""Unittest module for the console."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up test environment."""
        self.cli = HBNBCommand()

    def tearDown(self):
        """Tear down test environment."""
        storage.all().clear()

    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands", output)

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cli.onecmd("EOF"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.assertIn("BaseModel." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create User")
            obj_id = f.getvalue().strip()
            self.assertIn("User." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create State")
            obj_id = f.getvalue().strip()
            self.assertIn("State." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create City")
            obj_id = f.getvalue().strip()
            self.assertIn("City." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create Amenity")
            obj_id = f.getvalue().strip()
            self.assertIn("Amenity." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create Place")
            obj_id = f.getvalue().strip()
            self.assertIn("Place." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create Review")
            obj_id = f.getvalue().strip()
            self.assertIn("Review." + obj_id, storage.all())

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel " + obj_id)
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("show BaseModel invalid_id")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy BaseModel " + obj_id)
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn("BaseModel." + obj_id, storage.all())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("destroy BaseModel invalid_id")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all")
            output = f.getvalue().strip()
            self.assertEqual(output, "[]")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.cli.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("all InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        """Test the update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {obj_id} name 'New Name'")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            obj = storage.all()["BaseModel." + obj_id]
            self.assertEqual(obj.name, "New Name")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {obj_id} age 25")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            obj = storage.all()["BaseModel." + obj_id]
            self.assertEqual(obj.age, 25)

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"update BaseModel {obj_id} status")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("update BaseModel invalid_id name 'New Name'")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

if __name__ == "__main__":
    unittest.main()
