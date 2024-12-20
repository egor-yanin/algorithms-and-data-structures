from lab2.task6.src.main import task6, find_max_subarray
from lab2.utils import read_stocks, write_vars, read_lines
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_OUTPUT = os.path.join(CURRENT_DIR, '../txtf/output.txt')
FILE_AEROFLOT = os.path.join(CURRENT_DIR, '../txtf/aeroflot.txt')
FIlE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab2Task6TestCase(unittest.TestCase):
    def test_should_find_max_subarray(self):
        # given
        data = read_stocks(FILE_AEROFLOT)
        expected_result = 0, 14, 10.25

        # when
        result = find_max_subarray(data)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FIlE_SAMPLE))
