import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('Merlin',100,10,20)

    def test_inheritance(self):
        wizard = Wizard('Merlin',100,10,20)
        self.assertEqual(wizard.hp,100)

    def test_manna(self):
        wizard = Wizard('Merlin',100,10,20)
        self.assertEqual(wizard.manna,20)

    def test_strike(self):
        wizard = Wizard('Merlin',100,10,20)
        opponent = Wizard('Gandalf',100,10,20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna,15)
        self.assertEqual(opponent.hp,70)

    def test_strike_no_manna(self):
        wizard = Wizard('Merlin',100,10,0)
        opponent = Wizard('Gandalf',100,10,20)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna,0)
        self.assertEqual(opponent.hp,97)


unittest.main()
