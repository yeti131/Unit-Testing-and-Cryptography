from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import split_string


class Test(TestCase):
    def test_split_string_one_word_even(self):
        self.assertEqual(split_string("word"), "rdwo")

    def test_split_string_one_word_odd(self):
        self.assertEqual(split_string("hello"), "llohe")

    def test_split_string_empty_string(self):
        self.assertEqual(split_string(""), "")

    def test_split_string_full_sentence(self):
        self.assertEqual(split_string("Fortnite is not dead!"), "s not dead!Fortnite i")
