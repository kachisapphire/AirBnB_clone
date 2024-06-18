#!/usr/bin/python3
""" This module contains the base class which others will inherit from. """
import uuid
from datetime import datetime


class BaseModel:
    """ this class defines all common attributes/methods for other classes.
    Parameters: id: a uuid string when an instance is created.
                created_at: date and time an instance is created.
                updated_at: date and time an instance is updated.
    """

    def __init__(self):
        """ instantiation for id, created_at, updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """
        inst_attr = self.__dict__.copy()
        inst_attr["__class__"] = self.__class__.__name__
        inst_attr["created_at"] = self.created_at.isoformat()
        inst_attr["updated_at"] = self.updated_at.isoformat()
        return (inst_attr)

    def __str__(self):
        """ return string representation of basemodel. """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
