import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode
class TestVigEncode(unittest.TestCase):
    def test_vig_encode_basic(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED", "TEST"), "LLWIMMUCUVFOFJFPBYDHXH")

    def test_vig_encode_lower_text(self):
        self.assertEqual(vig_encode("thequickbrownfoxjumped", "TEST"), "llwimmucuvfofjfpbydhxh")

    def test_vig_encode_lower_both(self):
        self.assertEqual(vig_encode("thequickbrownfoxjumped", "test"), "llwimmucuvfofjfpbydhxh")

    def test_vig_encode_lower_key(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED", "test"), "LLWIMMUCUVFOFJFPBYDHXH")

    def test_vig_encode_text_space(self):
        self.assertEqual(vig_encode("THE QUICK BROWN FOX JUMPED", "TEST"),"LLWSIY VCDTJG ESYSOSBYDHXH")

    def test_vig_encode_key_space(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED", "TE ST"), "LLDHMAGJTJG MXGPNTDHXH")

    def test_vig_encode_text_punctuation(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED!", "TEST"), "LLWIMMUCUVFOFJFPBYDHXH!")

    def test_vig_encode_key_punctuation(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED", "TE$T"), "LLXIYAVOUJSOFJGPNMETXW")

    def test_vig_encode_text_number(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED11234", "TEST"), "LLWIMMUCUVFOFJFPBYDHXH11234")

    def test_vig_encode_key_number(self):
        self.assertEqual(vig_encode("THEQUICKBROWNFOXJUMPED", "TE5T"), "LLXIYAVOUJSOFJGPNMETXW")

    def test_vig_encode_all(self):
        self.assertEqual(vig_encode("AbCdEfG1! ", "T E5T$"), "TaGwXeK1!S")

