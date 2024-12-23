from lab7.task6.src.main import longest_increasing_subsequence
from lab7.utils import read_lines, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab7Task6TestCase(unittest.TestCase):
    def test_should_longest_increasing_subsequence(self):
        # given
        sequence = [3, 29, 5, 5, 28, 6]
        expected_result = [3, 5, 28]

        # when
        result = longest_increasing_subsequence(sequence)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
