import unittest
import game
import menu

class TestIntro(unittest.TestCase):
    def setUp(self):
        self.main_menu = menu.Menu(game.par)

    # def test_main_menu_ready(self):
    #     self.assertEqual(self.main_menu.menu_list(),"1. New game\n2. Load Game\n3. Exit\n")

    def test_main_menu_choose(self):
        print(self.main_menu.menu_list())
        self.assertEqual(self.main_menu.choose_list_item(),1)








unittest.main()
