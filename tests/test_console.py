#!/usr/bin/python3
"""Unittest for the console"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
import models
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test the console"""

    def setUp(self):
        """Set up test environment"""
        self.mock_stdin = StringIO()
        self.mock_stdout = StringIO()
        sys.stdin = self.mock_stdin
        sys.stdout = self.mock_stdout
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue().strip()
            self.assertTrue("Documented commands" in output)

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output.split()) == 1)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertTrue(model_id in output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {model_id}")
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {model_id} name 'Test'")
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertTrue("'name': 'Test'" in output)

    def test_update_dict(self):
        """Test update command with dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            model_id = f.getvalue().strip()
            update_dict = "{'name': 'Test', 'age': 25}"
            self.console.onecmd(f"update BaseModel {model_id} {update_dict}")
            self.console.onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
            self.assertTrue("'name': 'Test'" in output)
            self.assertTrue("'age': 25" in output)

    def test_classes(self):
        """Test command execution for all classes"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"create {cls}")
                model_id = f.getvalue().strip()
                self.console.onecmd(f"show {cls} {model_id}")
                output = f.getvalue().strip()
                self.assertTrue(model_id in output)
                self.console.onecmd(f"destroy {cls} {model_id}")
                self.console.onecmd(f"show {cls} {model_id}")
                output = f.getvalue().strip()
                self.assertTrue("** no instance found **" in output)


if __name__ == '__main__':
    unittest.main()
