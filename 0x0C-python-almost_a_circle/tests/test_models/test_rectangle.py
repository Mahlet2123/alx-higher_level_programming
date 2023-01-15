#!/usr/bin/python3
""" Module for Rectangle unit tests."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ tests for Rectangle class"""

    def setUp(self):
        """Imports module, instantiates class """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test_method. """
        pass

    def test_for_class(self):
       """ Test for class """
       r = Rectangle(10, 2)
       self.assertTrue(type(r) == Rectangle)

    def test_for_subclass(self):
        """ check for the base class """
        r = Rectangle(10, 2)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_for_validator(self):
        """ test for validator method """
        self.assertEqual(type(Rectangle.__dict__['validator']), function)

