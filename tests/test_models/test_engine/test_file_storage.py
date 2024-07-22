import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstantiation(unittest.TestCase):
    """
    this function is to test filestorage instantiation.
    """
    def test_no_args(self):
        """ test with no args. """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_with_args(self):
        """ test with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_instance(self):
        """ test to check for instance. """
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """
    this class tests the class filestorage.
    """
    def setup(self):
        """ a temp file. """
        self.test_file = "test_file.json"

    def teardown(self):
        """ remove temp file"""
        if os.path.exists(self.test_file):
            os_remove(self.test_file)

    def test_all_to_dict(self):
        """ test if all method returns dictionary """
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """ test the new() method. """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id),models.storage.all())

    def test_new_with_args(self):
        """ test the new method with args"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """ test new() with None"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_reload(self):
        """ test to save obj and reload them"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save
        new_storage = FileStorage()
        new_storage.reload()
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save_to_file(self):
        """ test to save object to file"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_file(self):
        """ Test to check relaod file"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.relaod()

if __name__ == "__main__":
    unittest.main()
