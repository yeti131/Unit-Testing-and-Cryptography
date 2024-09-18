import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode


class TestAffineDecode(unittest.TestCase):
    def test_affine_decode_basic(self):
        self.assertEqual(affine_decode("VY", 3, 0), "HI")

    def test_affine_decode_caesar_basic(self):
        self.assertEqual(affine_decode("EVQQZ", 3, 9), "HELLO")

    def test_affine_decode_lower_case(self):
        self.assertEqual(affine_decode("evqqz", 3, 9), "HELLO")

    def test_affine_decode_special_chars(self):
        self.assertEqual(affine_decode("EVQQZ!", 3, 9), "HELLO")

    def test_affine_decode_space(self):
        self.assertEqual(affine_decode("EV QQZ", 3, 9), "HELLO")

