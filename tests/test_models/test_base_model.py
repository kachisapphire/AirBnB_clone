#!/usr/bin/python3
""" Unittest for base_models.py """
import unittest
from models.base_model import BaseModel


class TestBaseModelpy(unittest.TestCase):
    """ Test case for BaseModel class. """
    def test_init_py(self):
        """ test case to check for public instance attributes. """
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_updated(self):
        """ test to check the time changes each time it is accessed"""
        base_model = BaseModel()
        self.assertNotEqual(base_model.updated_at, base_model.save())

    def test_dict(self):
        """ test to check function returns a dictionary """
        base_model = BaseModel()
        self.assertIsInstance(base_model.to_dict(), dict)
        self.assertEqual(base_model.to_dict()["__class__"], 'BaseModel')
        self.assertEqual(base_model.to_dict()['id'], base_model.id)
        self.assertEqual(base_model.to_dict()['created_at'], base_model.created_at.isoformat())
        self.assertEqual(base_model.to_dict()['updated_at'], base_model.updated_at.isoformat())

    def test_str(self):
        """ test to return string representation of BaseModel """
        base_model = BaseModel()
        self.assertTrue(str(base_model).startswith('[BaseModel]'))
        self.assertIn(base_model.id, str(base_model))
        self.assertIn(str(base_model.__dict__), str(base_model))

if __name__ == "__main__":
    unittest.main()
