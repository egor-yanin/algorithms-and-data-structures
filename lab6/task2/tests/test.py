from lab6.utils import write_vars, read_lines
from lab6.task2.src.main import execute
import unittest
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_INPUT = os.path.join(CURRENT_DIR, '../txtf/input.txt')
FILE_SAMPLE = os.path.join(CURRENT_DIR, '../txtf/sample.txt')


class Lab6Task2TestCase(unittest.TestCase):
    def test_should_execute(self):
        # given
        command_list = ['add 911 police', 'add 342689 Michael', 'add 749120 Tommy Vans', 'del 342689',
                        'find 749120', 'find 342689']
        expected_result = ['Tommy Vans', 'not found']

        # when
        result = execute(command_list)

        # then
        self.assertEqual(result, expected_result)

    @classmethod
    def tearDownClass(cls):
        write_vars(FILE_INPUT, *read_lines(FILE_SAMPLE))
