import unittest
import os
from lab6.task1.src.main import execute
from lab6.utils import write_vars, read_lines


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab6Task1TestCase(unittest.TestCase):

    def test_should_execute(self):
        # given
        command_list = ['A 2', 'A 2', 'A 3', 'D 2', 'D 4', '? 2', '? 3', '? 4']
        expected_result = ['N', 'Y', 'N']

        # when
        result = execute(command_list)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
