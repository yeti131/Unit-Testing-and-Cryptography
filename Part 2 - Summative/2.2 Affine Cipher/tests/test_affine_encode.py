import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode
class TestAffineEncode(unittest.TestCase):
    def test_affine_encode_basic(self):
        self.assertEqual(affine_encode("HI", 3, 0), "VY")

    def test_affine_encode_caesar_basic(self):
        self.assertEqual(affine_encode("HELLO", 3, 9), "EVQQZ")

    def test_affine_encode_lower_case(self):
        self.assertEqual(affine_encode("hello", 3, 9), "EVQQZ")

    def test_affine_encode_special_chars(self):
        self.assertEqual(affine_encode("HELLO!", 3, 9), "EVQQZ")

    def test_affine_encode_space(self):
        self.assertEqual(affine_encode("HE LLO", 3, 9), "EVQQZ")

