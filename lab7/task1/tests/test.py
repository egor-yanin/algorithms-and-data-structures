from lab7.task1.src.main import change_money
from lab7.utils import read_lines, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab7Task1TestCase(unittest.TestCase):
    def test_should_change_money(self):
        # given
        coins = [1, 3, 4]
        money = 34
        expected_result = 9

        # when
        result = change_money(money, coins)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
