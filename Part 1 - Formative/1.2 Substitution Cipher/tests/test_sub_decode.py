import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode


class TestSubEncode(unittest.TestCase):
    def test_sub_encode_basic(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD")

    def test_sub_encode_lower_case_text_upper_codebet(self):
        self.assertEqual(sub_decode("mxtthahotu", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "helloworld")

    def test_sub_encode_lower_case_text_lower_codebet(self):
        self.assertEqual(sub_decode("mxtthahotu", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "helloworld")

    def test_sub_encode_upper_case_text_lower_codebet(self):
        self.assertEqual(sub_decode("MXTTHAHOTU", "wjkuxvbmiydtplhzgoncrsaefq"), "HELLOWORLD")

    def test_sub_encode_punctuation(self):
        self.assertEqual(sub_decode("MXTTHAHOTU!", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLOWORLD!")

    def test_sub_encode_space(self):
        self.assertEqual(sub_decode("MXTTH AHOTU", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLO WORLD")

    def test_sub_encode_numbers(self):
        self.assertEqual(sub_decode("MXTTH123", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLO123")
