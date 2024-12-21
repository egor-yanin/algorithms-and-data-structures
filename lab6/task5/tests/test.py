from lab6.utils import write_vars, read_lines
from lab6.task5.src.main import count_votes
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab6Task5TestCase(unittest.TestCase):
    def test_should_count_votes(self):
        # given
        data = ['Ivanov 101', 'Batikov 987', 'Tsar 657', 'Ivanov 54', 'Petr 70', 'Batikov 11']
        expected_result = {'Ivanov': 155, 'Batikov': 998, 'Tsar': 657, 'Petr': 70}

        # when
        result = count_votes(data)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
