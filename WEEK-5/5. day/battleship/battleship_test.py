import unittest
import battleship

class TestIntro(unittest.TestCase):
    def setUp(self):
        self.table = battleship.Table()



    def test_table_ready(self):
        self.assertEqual(self.table.ready(),True)

    def test_attack(self):
        self.assertEqual(self.table.attack(0,0),True)
        self.assertEqual(self.table.attack(1,0),False)

    def test_is_win(self):
        self.assertEqual(self.table.is_win(),False)
        self.table.lives = 0
        self.assertEqual(self.table.is_win(),True)


unittest.main()
