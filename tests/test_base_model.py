#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""
import unittest
from models import storage
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel Class """
    def test_class(self):
        """tests inatnce of class"""
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))
