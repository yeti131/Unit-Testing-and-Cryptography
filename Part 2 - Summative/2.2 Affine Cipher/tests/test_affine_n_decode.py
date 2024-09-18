import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode


class TestAffineDecode(unittest.TestCase):
    def test_affine_n_decode_basic(self):
        self.assertEqual(affine_n_decode("XUHN", 2, 3, 121), "COOL")

    def test_affine_n_decode_short_string(self):
        self.assertEqual(affine_n_decode("XURYWT", 3, 3, 121), "COOLXX")

    def test_affine_n_encode_space_on_n(self):
        self.assertEqual(affine_n_decode("XU HN", 2, 3, 121), "COOL")

    def test_affine_n_encode_space_off_n(self):
        self.assertEqual(affine_n_decode("X UHN", 23, 3, 121), "COOL")

    def test_affine_n_encode_special_chars(self):
        self.assertEqual(affine_n_decode("XUHN$", 2, 3, 121), "COOL")

    def test_affine_n_encode_lower_case(self):
        self.assertEqual(affine_n_decode("xuhn", 2, 3, 121), "COOL")
