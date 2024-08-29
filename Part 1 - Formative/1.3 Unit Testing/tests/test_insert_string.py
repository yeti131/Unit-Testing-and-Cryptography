from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import insert_string

class TestInsertString(TestCase):
    def test_insert_string_two_words_lowercase(self):
        self.assertEqual(insert_string("apple", "orange"), "aporangeple")

    def test_insert_string_two_words_with_uppercase(self):
        self.assertEqual(insert_string("apple", "ORANGE"), "apORANGEple")

    def test_insert_string_empty_insert(self):
        self.assertEqual(insert_string("apple", ""), "apple")

    def test_insert_string_empty_text(self):
        self.assertEqual(insert_string("", "orange"), "orange")

    def test_insert_string_whitespace(self):
        self.assertEqual(insert_string("  ", "orange"), " orange ")
