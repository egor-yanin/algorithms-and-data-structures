from lab6.task6.src.main import is_fibonacci
from lab6.utils import read_lines, write_vars
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab6Task6TestCase(unittest.TestCase):
    def test_should_is_fibonacci(self):
        # given
        numbers = [4181, 5967]
        expected_result = [True, False]

        # when
        result = [is_fibonacci(x) for x in numbers]

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
