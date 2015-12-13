import unittest
import intro

class TestIntro(unittest.TestCase):
    def setUp(self):
        self.names = [{ 'id': 1, 'name': 'John'}, { 'id': 2, 'name': 'Molly'}, { 'id': 3, 'name': 'Jane'}]
        self.first = intro.MyMagic()
        self.second = intro.MyMagic(self.names)



    def test_return_names(self):
        self.assertEqual(self.first.lists_names(), [])
        self.assertEqual(self.second.lists_names(), ['John', 'Molly', 'Jane'])

    def test_return_names_with_J(self):
        self.assertEqual(self.second.names_start_with_j(), ['John', 'Jane'])


unittest.main()
