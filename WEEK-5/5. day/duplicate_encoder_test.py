import unittest
import duplicate_encoder

class TestIntro(unittest.TestCase):
    def setUp(self):
        self.first = duplicate_encoder.CodeWars('Zeno')
        self.second = duplicate_encoder.CodeWars('Sanyika')



    def test_without_repeat_letters(self):
        self.assertEqual(self.first.lists_names(),'((((')



unittest.main()
