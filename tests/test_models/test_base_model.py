#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        mo1 = BaseModel()
        mo2 = BaseModel()
        self.assertNotEqual(mo1.id, mo2.id)

    def test_two_models_different_created_at(self):
        mo1 = BaseModel()
        sleep(0.05)
        mo2 = BaseModel()
        self.assertLess(mo1.created_at, mo2.created_at)

    def test_two_models_different_updated_at(self):
        mo1 = BaseModel()
        sleep(0.05)
        mo2 = BaseModel()
        self.assertLess(mo1.updated_at, mo2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        mo = BaseModel()
        mo.id = "123456"
        mo.created_at = mo.updated_at = dt
        mostr = mo.__str__()
        self.assertIn("[BaseModel] (123456)", mostr)
        self.assertIn("'id': '123456'", mostr)
        self.assertIn("'created_at': " + dt_repr, mostr)
        self.assertIn("'updated_at': " + dt_repr, mostr)

    def test_args_unused(self):
        mo = BaseModel(None)
        self.assertNotIn(None, mo.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        mo = BaseModel(id="567", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(mo.id, "567")
        self.assertEqual(mo.created_at, dt)
        self.assertEqual(mo.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
