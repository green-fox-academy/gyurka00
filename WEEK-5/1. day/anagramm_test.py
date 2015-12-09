import unittest
from anagramm import is_anagramm

class Test_is_anagramm(unittest.TestCase):
    def test_anagramma(self):
        self.assertEqual(is_anagramm('',''),True)
        self.assertEqual(is_anagramm('a',''),False)
        self.assertEqual(is_anagramm('ab','ba'),True)
        self.assertEqual(is_anagramm('abc','bac'),True)
        self.assertEqual(is_anagramm('asdfgh','fghasd'),True)

unittest.main()


'''
def test_assert(actual, expected):
    if actual == expected:
        print('Check')
    else:
        print('FAILED')

test_assert(is_anagramm('',''),True)
test_assert(is_anagramm('a',''),False)
test_assert(is_anagramm('ab','ba'),True)
test_assert(is_anagramm('abc','bac'),True)
test_assert(is_anagramm('asdfgh','fghasd'),True)
'''
