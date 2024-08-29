from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import reverse_string

class TestReverseString(TestCase):
    def test_reverse_string_one_word_lowercase(self):
        self.assertEqual(reverse_string("apple"), "elppa")

    def test_reverse_string_two_word_lowercase(self):
        self.assertEqual(reverse_string("apple orange"), "egnaro elppa")

    def test_reverse_string_one_word_uppercase(self):
        self.assertEqual(reverse_string("APPLE"), "ELPPA")

    def test_reverse_string_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_nonsense(self):
        self.assertEqual(reverse_string("K3,5:=+oP "), " Po+=:5,3K")
