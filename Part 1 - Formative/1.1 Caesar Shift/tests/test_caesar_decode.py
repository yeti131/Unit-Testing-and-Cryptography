import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode
class TestCaesarDecode(unittest.TestCase):
        def test_caesar_decode_shifted_two(self):
            self.assertEqual(caesar_decode("JGNNQYQTNF", 2), "HELLOWORLD")

        def test_caesar_decode_shifted_zero(self):
            self.assertEqual(caesar_decode("JGNNQYQTNF", 0), "JGNNQYQTNF")

        def test_caesar_decode_shifted_negative_one(self):
            self.assertEqual(caesar_decode("GDKKNVNQKC", -1), "HELLOWORLD")

        def test_caesar_decode_empty_string(self):
            self.assertEqual(caesar_decode("", 2), "")

        def test_caesar_decode_whitespace(self):
            self.assertEqual(caesar_decode(" ", 2), " ")

        def test_caesar_decode_numbers(self):
            self.assertEqual(caesar_decode("12", 2), "12")

        def test_caesar_decode_lower_case(self):
            self.assertEqual(caesar_decode("jgnnqyqtnf", 2), "helloworld")

        def test_caesar_decode_punctuation(self):
            self.assertEqual(caesar_decode("JGNNQYQTNF!", 2), "HELLOWORLD!")

        def test_caesar_decode_empty_string_shift(self):
            self.assertEqual(caesar_decode("JGNNQYQTNF", ""), "JGNNQYQTNF")

        def test_caesar_decode_string_number_shift(self):
            self.assertEqual(caesar_decode("JGNNQYQTNF", "2"), "HELLOWORLD")