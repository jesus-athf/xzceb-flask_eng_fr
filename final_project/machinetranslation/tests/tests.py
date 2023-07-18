import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertNotEqual(english_to_french("welcome"), "bonjour")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertNotEqual(french_to_english("bienvenue"), "hello")
unittest.main()
