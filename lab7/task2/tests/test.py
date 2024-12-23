from lab7.task2.src.main import calculate
from lab7.utils import read_lines, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab7Task2TestCase(unittest.TestCase):
    def test_should_calculate(self):
        # given
        number = 43
        expected_result = 6

        # when
        result = len(calculate(number)) - 1

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
