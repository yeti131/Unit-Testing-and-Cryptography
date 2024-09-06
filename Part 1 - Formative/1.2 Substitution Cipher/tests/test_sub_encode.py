import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestSubEncode(unittest.TestCase):
    def test_sub_encode_basic(self):
        self.assertEqual(sub_encode("HELLOWORLD", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTHAHOTU")

    def test_sub_encode_lower_case_text_upper_codebet(self):
        self.assertEqual(sub_encode("helloworld", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtthahotu")

    def test_sub_encode_lower_case_text_lower_codebet(self):
        self.assertEqual(sub_encode("helloworld", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtthahotu")

    def test_sub_encode_upper_case_text_lower_codebet(self):
        self.assertEqual(sub_encode("HELLOWORLD", "wjkuxvbmiydtplhzgoncrsaefq"), "MXTTHAHOTU")

    def test_sub_encode_small_codebet(self):
        self.assertEqual(sub_encode("HELLOWORLD", "wjkuxvbmiydtplhzgoncrs"), "HELLOWORLD") #idk about this

