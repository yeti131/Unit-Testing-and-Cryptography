from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import *

class Test(TestCase):
    def test_reverse_string_one_word_lowercase(self):
        self.assertEqual(reverse_string("apple"), "elppa")
