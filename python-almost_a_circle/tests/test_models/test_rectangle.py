#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestClassRectangle(unittest.TestCase):

    def test_class_attributes(self):
        r1 = Rectangle(89, 90)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 89)
        r2 = Rectangle(27, 14)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.height, 14)
        self.assertEqual(r2.x, 0)
        r3 = Rectangle(21, 398, 2, 8, 64)
        self.assertEqual(r3.id, 64)

    def test_class_instance(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    def test_missing_required_arguments(self):
        self.assertRaises(TypeError, Rectangle, (5))
        self.assertRaises(TypeError, Rectangle, ())
        self.assertRaises(TypeError, Rectangle, (2, 8, 5, 0, 45, 7))
