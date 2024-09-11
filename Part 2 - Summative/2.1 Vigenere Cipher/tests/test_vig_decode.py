import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode
class TestVigEncode(unittest.TestCase):
    def test_vig_decode_basic(self):
        self.assertEqual(vig_decode("LLWIMMUCUVFOFJFPBYDHXH", "TEST"), "THEQUICKBROWNFOXJUMPED")

    def test_vig_decode_lower_text(self):
        self.assertEqual(vig_decode("llwimmucuvfofjfpbydhxh", "TEST"), "thequickbrownfoxjumped")

    def test_vig_decode_lower_both(self):
        self.assertEqual(vig_decode("llwimmucuvfofjfpbydhxh", "test"), "thequickbrownfoxjumped")

    def test_vig_decode_lower_key(self):
        self.assertEqual(vig_decode("LLWIMMUCUVFOFJFPBYDHXH", "test"), "THEQUICKBROWNFOXJUMPED")

    def test_vig_decode_text_space(self):
        self.assertEqual(vig_decode("LLWSIY VCDTJG ESYSOSBYDHXH", "TEST"),"THE QUICK BROWN FOX JUMPED")

    def test_vig_decode_key_space(self):
        self.assertEqual(vig_decode("LLDHMAGJTJG MXGPNTDHXH", "TE ST"), "THEQUICKBROWNFOXJUMPED")

    def test_vig_decode_text_punctuation(self):
        self.assertEqual(vig_decode("LLWIMMUCUVFOFJFPBYDHXH!", "TEST"), "THEQUICKBROWNFOXJUMPED!")

    def test_vig_decode_key_punctuation(self):
        self.assertEqual(vig_decode("LLXIYAVOUJSOFJGPNMETXW", "TE$T"), "THEQUICKBROWNFOXJUMPED")

    def test_vig_decode_text_number(self):
        self.assertEqual(vig_decode("LLWIMMUCUVFOFJFPBYDHXH11234", "TEST"), "THEQUICKBROWNFOXJUMPED11234")

    def test_vig_decode_key_number(self):
        self.assertEqual(vig_decode("LLXIYAVOUJSOFJGPNMETXW", "TE5T"), "THEQUICKBROWNFOXJUMPED")

    def test_vig_decode_all(self):
        self.assertEqual(vig_decode("TaGwXeK1!Z", "T E5T$"), "AbCdEfG1! ")

