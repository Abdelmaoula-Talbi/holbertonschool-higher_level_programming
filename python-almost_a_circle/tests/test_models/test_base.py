#!/usr/bin/python3
import unittest
from models.base import Base

class TestClassBase(unittest.TestCase):

    def test_class_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(25)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 25)
        self.assertEqual(b4.id, 3)

    def test_class_type(self):
        b = Base()
        self.assertTrue(b, '<class base.Base>')

    def test_instance(self):
        b = Base()
        self.assertIsInstance(b, Base)
