import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode
class TestCaesarEncode(unittest.TestCase):
    def test_caesar_encode_shifted_two(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 2), "JGNNQYQTNF")  # add assertion here

    def test_caesar_encode_shifted_zero(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 0), "HELLOWORLD")

    def test_caesar_encode_shifted_negative_one(self):
        self.assertEqual(caesar_encode("HELLOWORLD", -1), "GDKKNVNQKC")

    def test_caesar_encode_empty_string(self):
        self.assertEqual(caesar_encode("", 1), "")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(caesar_encode("  ", 1), "  ")

    def test_caesar_encode_numbers(self):
        self.assertEqual(caesar_encode("12", 2), "12")

    def test_caesar_lower_case(self):
        self.assertEqual(caesar_encode("helloworld", 2), "jgnnqyqtnf")

    def test_caesar_punctuation(self):
        self.assertEqual(caesar_encode("HELLOWORLD!", 2), "JGNNQYQTNF!")

    def test_caesar_empty_string_shift(self):
        self.assertEqual(caesar_encode("HELLOWORLD", " "), "HELLOWORLD")

    def test_caesar_string_number_shift(self):
        self.assertEqual(caesar_encode("HELLOWORLD", "2"), "JGNNQYQTNF")