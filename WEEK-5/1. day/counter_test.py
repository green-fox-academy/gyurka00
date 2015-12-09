import unittest
from counter import count_letters

class LetterCounterTes(unittest.TestCase):
    def test_if_exist(self):
        self.assertEqual(count_letters(''),{})
    def test_same_letter(self):
        self.assertEqual(count_letters('a'),{'a':1})
        self.assertEqual(count_letters('aa'),{'a':2})
    def test_different_letter(self):
        self.assertEqual(count_letters('b'),{'b':1})
    def test_distinct_letters(self):
        self.assertEqual(count_letters('ab'),{'a':1,'b':1})
        self.assertEqual(count_letters('kecske'),{'k':2,'e':2, 'c':1, 's':1})

unittest.main()
