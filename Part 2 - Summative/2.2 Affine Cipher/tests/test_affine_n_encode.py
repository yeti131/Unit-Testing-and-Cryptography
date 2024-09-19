import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_encode
class TestAffineEncode(unittest.TestCase):
    def test_affine_n_encode_basic(self):
        self.assertEqual(affine_n_encode("COOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_short_string(self):
        self.assertEqual(affine_n_encode("COOL", 3, 3, 121), "XURYWT")

    def test_affine_n_encode_space_on_n(self):
        self.assertEqual(affine_n_encode("CO OL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_space_off_n(self):
        self.assertEqual(affine_n_encode("C OOL", 2, 3, 121), "XUHN")

    def test_affine_n_encode_special_chars(self):
        self.assertEqual(affine_n_encode("COOL$", 2, 3, 121), "XUHN")

    def test_affine_n_encode_lower_case(self):
        self.assertEqual(affine_n_encode("cool", 2, 3, 121), "XUHN")
