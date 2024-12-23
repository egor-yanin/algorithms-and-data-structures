from lab7.task5.src.main import common_subsequence_len
from lab7.utils import read_lines, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab7Task5TestCase(unittest.TestCase):
    def test_should_common_subsequence_len(self):
        # given
        subsequences = [[8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]]
        expected_result = 3

        # when
        result = common_subsequence_len(*subsequences)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
