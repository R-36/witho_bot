import unittest
from utils import find_vowel, find_consonant
from config import vowel, consonant


class TestFindMethods(unittest.TestCase):
    def test_find_vowel(self):
        self.assertEqual(find_vowel(vowel, vowel), 10)

    def test_find_consonant(self):
        self.assertEqual(find_consonant(consonant, consonant), 23)
