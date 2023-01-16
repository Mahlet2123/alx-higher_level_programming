#!/usr/bin/python3
""" Module for Base unit tests."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ class test base"""
    def test_for_class(self):
        """ Test for class """
        b = Base()
        self.assertTrue(type(b) == Base)

    def test_nb(self):
        """ test private class attribute __nb_objects """
        b = Base()
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_base(self):
        """ tests for base.py """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
