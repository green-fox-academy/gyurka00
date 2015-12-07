import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_wrong_sum(self):
        test_input = [1, 9, 3, 4, 5, 6, 7, 8, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "Wrong sum.")

    def test_is_complete_sum(self):
        test_input = [1, 9, 3, 4, 5, 6, 7, 8, 2]
        expected = True
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "Wrong numbers.")

    def test_is_complete_sum_ok_numbers_wrong(self):
        test_input = [1, 9, 4, 4, 5, 5, 7, 8, 2]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "Sum ok wrong numbers.")

unittest.main()
